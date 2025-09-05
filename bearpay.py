import tkinter as tk
from tkinter import messagebox
import json, os, threading
from flask import Flask, request, jsonify

# -------------------
# Глобальные переменные
# -------------------
last_card_number = None
last_card_date = None
last_card_cvv = None
waiting_phone = False
expected_amount = None
expected_currency = None
phone_result = None
lock = threading.Lock()
server_started = False

# -------------------
# Безопасный strip
# -------------------
def safe_str(val, default=""):
    if val is None:
        return default
    return str(val).strip()

# -------------------
# Flask сервер
# -------------------
app = Flask(__name__)

@app.route("/pay", methods=["POST"])
def pay():
    global waiting_phone, expected_amount, expected_currency, phone_result
    data = request.get_json(force=True)
    if not data or "amount" not in data or "currency" not in data:
        return jsonify({"success": False, "error": "Missing 'amount' or 'currency'"}), 400
    try:
        amount = float(data["amount"])
        currency = safe_str(str(data.get("currency", "")).upper())
    except ValueError:
        return jsonify({"success": False, "error": "Invalid amount"}), 400

    with lock:
        if not waiting_phone:
            return jsonify({"success": False, "error": "Not waiting for phone payment"}), 400
        if float(amount) == float(expected_amount) and currency == safe_str(str(expected_currency).upper()):
            phone_result = True
        else:
            phone_result = False
        waiting_phone = False

    print(f"[DEBUG] Flask received POST: amount={amount}, currency={currency}, result={phone_result}")
    return jsonify({"success": phone_result}), 200

def start_server():
    global server_started
    if server_started:
        return
    server_started = True
    threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=1212, debug=False, threaded=True),
        daemon=True
    ).start()

start_server()

# -------------------
# Функции BearPay
# -------------------
def _load_cards():
    if not os.path.exists("cards.json"): return []
    with open("cards.json","r") as f: return json.load(f)

def _save_cards(cards):
    with open("cards.json","w") as f: json.dump(cards,f,indent=4)

def _get_currency_rate(currency: str) -> float:
    currency = safe_str(currency).upper()
    rates = {"$":1,"":1,"RUB":80,"₽":80,"HRY":41.5,"GBP":0.75,"EUR":0.89,"BYN":3.28}
    return rates.get(currency,1e9)

def _detect_card_brand(number: str) -> str:
    number = safe_str(number).replace(" ","")
    if number.startswith("4"): return "Visa"
    if number[:2] in {"51","52","53","54","55"} or (number[:4].isdigit() and 2221<=int(number[:4])<=2720): return "Mastercard"
    return "BearCard"

def _open_window(language: str, amount: float, currency: str):
    global last_card_number, last_card_date, last_card_cvv
    global waiting_phone, expected_amount, expected_currency, phone_result

    waiting_phone = True
    expected_amount = amount
    expected_currency = safe_str(currency).upper()
    phone_result = None

    texts = {
        "EN":{"title":"Bear-Pay","cardnum":"Card Number","date":"Expiration Date (MM/YY)","cvv":"CVV","pay":"Pay","error":"Please fill in all fields.","failed":"Payment failed. Invalid card or insufficient balance.","success":"Payment successful!","phone":"Waiting for phone payment via POST..."},
        "RU":{"title":"Bear-Pay","cardnum":"Номер карты","date":"Срок действия (MM/ГГ)","cvv":"CVV","pay":"Оплатить","error":"Пожалуйста, заполните все поля.","failed":"Оплата не прошла. Неверная карта или недостаточно средств.","success":"Оплата прошла успешно!","phone":"Ожидание оплаты телефоном через POST..."}
    }
    t = texts[language]
    result = {"success": False}

    window = tk.Tk()
    window.title(t["title"])
    window.geometry("420x360")
    window.resizable(False, False)
    window.configure(bg="#f2f2f2")

    tk.Label(window,text=f"{t['title']} - {amount} {currency}", bg="#f2f2f2", fg="black", font=("Helvetica",14,"bold")).pack(pady=(10,5))
    card_brand_var = tk.StringVar(value="Brand: Unknown")
    tk.Label(window,textvariable=card_brand_var, bg="#f2f2f2", fg="black", font=("Helvetica",12,"italic")).pack(pady=(0,5))

    tk.Label(window,text=t["cardnum"], bg="#f2f2f2", fg="black", font=("Helvetica",13)).pack()
    entry_cardnum = tk.Entry(window,font=("Helvetica",13),justify="center",bg="white",fg="black",relief="groove")
    entry_cardnum.pack(ipady=5, ipadx=10, padx=40, fill="x")
    def format_cardnum(event):
        raw = ''.join(filter(str.isdigit, entry_cardnum.get()))[:16]
        spaced = ' '.join([raw[i:i+4] for i in range(0,len(raw),4)])
        entry_cardnum.delete(0,tk.END); entry_cardnum.insert(0,spaced)
        card_brand_var.set(f"Brand: {_detect_card_brand(raw)}")
    entry_cardnum.bind("<KeyRelease>", format_cardnum)

    tk.Label(window,text=t["date"], bg="#f2f2f2", fg="black", font=("Helvetica",13)).pack(pady=(10,0))
    entry_carddate = tk.Entry(window,font=("Helvetica",13),justify="center",bg="white",fg="black",relief="groove")
    entry_carddate.pack(ipady=5, ipadx=10, padx=40, fill="x")
    def format_carddate(event):
        raw = ''.join(filter(str.isdigit, entry_carddate.get()))[:4]
        formatted = raw[:2]+"/"+raw[2:] if len(raw)>2 else raw
        entry_carddate.delete(0,tk.END); entry_carddate.insert(0,formatted)
    entry_carddate.bind("<KeyRelease>", format_carddate)

    tk.Label(window,text=t["cvv"], bg="#f2f2f2", fg="black", font=("Helvetica",13)).pack(pady=(10,0))
    cvv_var = tk.StringVar()
    cvv_var.trace("w", lambda *args: cvv_var.set(cvv_var.get()[:3]))
    entry_cardcvv = tk.Entry(window,textvariable=cvv_var,font=("Helvetica",13),justify="center",bg="white",fg="black",show="*",relief="groove")
    entry_cardcvv.pack(ipady=5, ipadx=10, padx=40, fill="x")

    def submit_card():
        global last_card_number, last_card_date, last_card_cvv
        cardnum = safe_str(entry_cardnum.get())
        carddate = safe_str(entry_carddate.get())
        cardcvv = safe_str(cvv_var.get())
        if not cardnum or not carddate or not cardcvv:
            messagebox.showwarning(t["title"], t["error"])
            return
        last_card_number, last_card_date, last_card_cvv = cardnum, carddate, cardcvv
        cards = _load_cards(); rate=_get_currency_rate(currency); converted_amount=amount/rate
        for c in cards:
            if c["number"]==cardnum and c["date"]==carddate and c["cvv"]==cardcvv and c.get("balance",0)>=converted_amount:
                c["balance"]-=round(converted_amount,2); _save_cards(cards)
                messagebox.showinfo(t["title"], t["success"])
                result["success"]=True; window.destroy(); return
        messagebox.showerror(t["title"], t["failed"])

    tk.Button(window,text=t["pay"],font=("Helvetica",13),command=submit_card,relief="raised",bg="#e0e0e0").pack(pady=20)

    def check_post():
        global waiting_phone, phone_result
        with lock:
            if phone_result is not None:
                result["success"] = phone_result
                print(f"[DEBUG] Phone payment result received: {phone_result}")
                window.destroy()
                return
        window.after(100, check_post)

    def phone_button():
        messagebox.showinfo(t["title"], t["phone"])

    tk.Button(window,text=t["phone"], font=("Helvetica",13), command=phone_button, relief="raised", bg="#c0e0ff").pack(pady=10)

    window.after(100, check_post)
    window.mainloop()

    print(f"[DEBUG] _open_window returning: {result['success']}")
    return result["success"]

def pay_EN(amount: float, currency: str="$") -> bool:
    return _open_window("EN", amount, currency)

def pay_RU(amount: float, currency: str="₽") -> bool:
    return _open_window("RU", amount, currency)