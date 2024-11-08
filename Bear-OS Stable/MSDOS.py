from time import sleep
import config
from config import password, from_email
import json
import pygame
from random import randint
import os
import pyautogui as pt
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
pygame.mixer.init()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import uuid
import nextcord
from nextcord import *
from nextcord.ext import commands
import twilio
from twilio.rest import Client
import sys


"""
sinch_client = SinchClient(
    key_id=config.phone_key_id,
    key_secret=config.phone_key_secret,
    project_id=config.project_id
)
"""


client = Client(config.phone_account_sid, config.phone_auth_token)










def writepass(data,filenamepass):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filenamepass, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def readpass(filenamepass):
    with open(filenamepass, 'r', encoding='utf-8') as file: 
        return json.load(file)   


def writeuser(data2,filenameuser):
    data2 = json.dumps(data2)
    data2 = json.loads(str(data2))
    with open(filenameuser, 'w', encoding='utf-8') as file2:
        json.dump(data2, file2, indent=4)


def readuser(filenameuser):
    with open(filenameuser, 'r', encoding='utf-8') as file2: 
        return json.load(file2) 

def writelc(data3,filenamelc):
    data3 = json.dumps(data3)
    data3 = json.loads(str(data3))
    with open(filenamelc, 'w', encoding='utf-8') as file3:
        json.dump(data3, file3, indent=4)


def readlc(filenamelc):
    with open(filenamelc, 'r', encoding='utf-8') as file3: 
        return json.load(file3) 


#data["pass"].append("cat")

#writepass(data, 'data.json')

#print(readpass('data.json'))

#(data["pass"][0])
    
data3 = {
    "licensekey" : ""
}



def licensekeygen():
    licensekey = 1
    licensekey1 = ["10X7W","9XV11","7B88C","90X7W","0XV11","7B88B"]
    licensekey2 = ["10C7W","9ZV11","7B89C","10X7M","1XV11","7B78C"]
    licensekey3 = ["90X7W","9XV21","7V88C","10K7W","9XV20","7R88C"]
    licensekey4 = ["91X7W","9WV21","7V38C","18X7W","9XC11","7B88L"]

    licensekey = licensekey1[randint(0,5)] + "-" + licensekey2[randint(0,5)] + "-" + licensekey3[randint(0,5)] + "-" + licensekey4[randint(0,5)]
    return licensekey


def veriferygen():
    verifycodegeniration = randint(100000, 999999)
    return verifycodegeniration




def IDGen():
    BuyID = 1
    BuyID1 = ["10","9X","8C","7W","11","7B"]
    BuyID2 = ["10W","91","789C","107M","1","7BU4C"]
    BuyID3 = ["90XW","921","78C","W","9XV20","78C"]
    BuyID4 = ["X7W","921","8C","18W","91","7"]

    BuyID = BuyID1[randint(0,5)] + "-" + BuyID2[randint(0,5)] + "-" + BuyID3[randint(0,5)] + "-" + BuyID4[randint(0,5)]
    return BuyID




def MakeError():
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + ":(")
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + "На вашем ПК Возникла Ошибка!")
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + "Код Ошибки:")
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + "Проверьте правильность на сайте: ")
    print(Back.BLUE + Fore.WHITE + "https://sites.google.com/view/bear-os-official/")
    for i in range(3):
        print(Back.BLUE + Fore.WHITE + "")



data3["licensekey"] = licensekeygen()

writelc(data3, 'yourlicensekey.json')



logo = ("""
██████╗░███████╗░█████╗░██████╗░░░░░░░░█████╗░░██████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔════╝
██████╦╝█████╗░░███████║██████╔╝█████╗██║░░██║╚█████╗░
██╔══██╗██╔══╝░░██╔══██║██╔══██╗╚════╝██║░░██║░╚═══██╗
██████╦╝███████╗██║░░██║██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░
""")








#modeset = input()

#---------------
#properties:

forgormsdos = "Y" #forget BEAR-OS?
chekpass = "Y" #Check password?
passset = "" #default password
checkaccaunt = "Y" #check accaunt
activatebearos = "N" #Activate Bear-OS
BearOSVersion = "1.6" # Version Of Bear-OS
systemName = "Bear-OS" # Bear-OS System Name
to_mail = "" #default mail
defaultMail = "" #default mail
errorName = "" #default error name
defaultСurrency = "$" #default currency
currency = "" #default currency
product = "" #default product
cost = "0" #default cost
phone_number = ""
verify = False
SMTPPROTOCOL = "smtp.gmail.com"
SMTPPORT = 587
TOKEN = "123456789"
bot = commands.Bot(command_prefix="!")


#Computer Components
BIOS = "DolBOIS V1.0"
Processor = "Intel Pentium -1000 year"
RAM = "10KB"
Motherboard = "Mamont A1"


#---------------

if currency == "":
    currency = defaultСurrency
else:
    print(Fore.RED + "[" + systemName + "] " + "The currency is worth '" + currency + "'")



"""
try:
    send_batch_response = sinch_client.sms.batches.send(
        body="Bear-OS",
        to=[phone],
        from_=config.my_sinch_pnone,
        delivery_report="none"
        
    )
    print("Отправлено!")
except Exception as sincherr:
    print("Error! " + str(sincherr))
"""







@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно подключен!")





errors = ["Нельзя делить на ноль!","","","",""]


redeemcodes = ["SA3V-8X9B-C7JK-DZ87","3A7Z-F3MH-827A-21A3","HG5D-8D98-KJ6Q-RT3Q"]


try:
    with open("htmltemplate.html") as file:
        html = file.read()
except:
    print("ERROR!")





def send_mail(to_mail, subject, text):
    try:
        msg = MIMEMultipart()
        msg['From'] = config.from_email
        msg['To'] = to_mail
        msg['Subject'] = subject
        msg.attach(
            MIMEText(text, 'plain')
        )
        server = smtplib.SMTP(SMTPPROTOCOL, SMTPPORT)
        server.starttls()
        #server.ehlo(config.from_email)
        server.login(config.from_email, config.password)
        #server.auth_plain()
        server.send_message(msg)
        server.quit()
        print("Отправлено!")
    except smtplib.SMTPException as ex:
        MakeError()
        print(Fore.RED + Back.RED + "")
        print(Fore.RED + Back.RED + "")
        print(Fore.RED + Back.RESET + "Случилась внутрнния ошибка! Код ошибки: " + str(ex))
        print(Fore.RED + Back.RED + "")
        print(Fore.RED + Back.RED + "")
        print(Fore.RED + Back.RESET + "")




def send_html_mail(to_mail, subject):
    try:
        msg = MIMEMultipart()
        msg['From'] = config.from_email
        msg['To'] = to_mail
        msg['Subject'] = subject
        msg.attach(
            MIMEText(html, 'html')
        )
        server = smtplib.SMTP(SMTPPROTOCOL, SMTPPORT)
        server.starttls()
        #server.ehlo(config.from_email)
        server.login(config.from_email, config.password)
        #server.auth_plain()
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPException as ex:
        MakeError()
        print(Fore.RED + Back.RED + "")
        print(Fore.RED + Back.RED + "")
        print(Fore.RED + Back.RESET + "Случилась внутрнния ошибка! Код ошибки: " + str(ex))
        print(Fore.RED + Back.RED + "")
        print(Fore.RED + Back.RED + "")
        print(Fore.RED + Back.RESET + "")












data = {
    "pass" : passset
}


data2 = {
    "user" : []
}


if forgormsdos == "Y":
    msdosexist = "N"
else:
    msdosexist = "Y"
    name = "(Unknown)"
    Computer_name = "(Unknown)"
    chekpass = "N"
    print(Back.RED + Fore.YELLOW + "ВАШ КОМЬЮТЕР НЕ НАЗВАН!!!")
    pygame.mixer.music.load("error.mp3")
    pygame.mixer.music.play()
#YoN = pt.confirm("!", name, ("Да","Нет"))
#print(YoN)
#print(data["pass"])

print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")
print(Back.RESET + Fore.GREEN + "")




print(BIOS)
sleep(randint(1,2))
print("-----------------------------------")
print("Материнская Плата: " + Motherboard)
print("-----------------------------------")
sleep(randint(1,2))
print("Процессор: " + Processor)
print("-----------------------------------")
sleep(randint(1,2))
print("ОЗУ: " + RAM)
print("-----------------------------------")
sleep(randint(1,5))
input("Нажмите Enter для продолжения...")




while True:
    sleep(2)
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")
    print(Back.RESET + Fore.GREEN + "")


    while msdosexist == "N":
        print(Back.RESET + Fore.GREEN + logo)
        print(Back.RESET + Fore.GREEN + "Добро пожаловать в установщик " + systemName)
        name = input("Введите ваше имя: ")
        print("Здравствуйте, " + name)
        data2["user"].append(name)

        writeuser(data2, 'user.json')
        Computer_name = input("Введите имя компьютера: ")
        print(name + ", вы назвали компьютер: " + Computer_name)
        
            
        passset = input("Введите Пароль для аккаунта " + name + ": ")
        
        data["pass"] = passset

        writepass(data, 'data.json')

        phone_number = input("Ваш номер телефона: ")

        to_mail = input("Ваша почта: ")
        defaultMail = to_mail


        predupr = "Письмо было отправлено на вашу почту. Если его нет проверте                          вкладку 'Спам'! Лицензионный Ключ?" 
        print(name + ", Вы поставили пароль: " + (data["pass"]))
        licenseyes = pt.confirm("У вас есть Лицензионный Ключ?", "Bear-OS", ("Да","Нет"))
        if licenseyes == "Да":
            activatebearos = "Y"
            licensekeynow = licensekeygen()
            if to_mail != "":
                send_mail(to_mail, "License Key / Лицензионный Ключ", "Your key / Ваш ключ: " + licensekeynow)
            else:
                print("Ошибка, Письмо не может быть отправлено! Так как вы не указали почту!")
                to_mail = input("Ваша почта: ")
                while not to_mail != "":
                    if to_mail == "":
                        print("Ошибка, Письмо не может быть отправлено! Так как вы не указали почту!")
                        to_mail = input("Ваша почта: ")
                    else:
                        send_mail(to_mail, "License Key / Лицензионный Ключ", "Your key / Ваш ключ: " + licensekeynow)
                send_mail(to_mail, "License Key / Лицензионный Ключ", "Ваш ключ: " + licensekeynow)
            licensekeyQ = pt.prompt(predupr, name)
            if licensekeynow == licensekeyQ:
                pass
            else:
                pt.alert("Неправильный Лицензионный Ключ!", name)
                while licensekeynow != licensekeyQ:
                    licensekeyQ = pt.prompt("Лицензионный Ключ?", name)
                    if licensekeynow != licensekeyQ:
                        pt.alert("Неправильный Лицензионный Ключ!", name)
        else:
            activatebearos = "N"
                    


        print(name + "@" + Computer_name + " ~ % " + "Чтобы начать установку пропишите команду: " + Fore.YELLOW + "/start download: ")
        installsucses = "no"
        stdo = input()
        while installsucses == "no":
            if stdo == "/start download":
                print(Fore.GREEN + "Установка...")
                sleep(5)
                print("Готово!")
                installsucses = "yes"
                msdosexist = "Y"
            else:
                print(Fore.RED + "Неизвестная команда: " + stdo + " <-")
                pygame.mixer.music.load("error.mp3")
                pygame.mixer.music.play()
                installsucses = "no"
                stdo = input(Fore.GREEN + "Чтобы начать установку пропишите команду: " + Fore.YELLOW + "/start download: ")
    if checkaccaunt == "Y":
        pt.alert("Выбирите Акаунт", systemName, button=name)
    if chekpass == "Y":
        passwordsys = pt.password("Пароль", name)
        if passwordsys == (data["pass"]):
            pass
        else:
            pt.alert("Неправильный пароль!", name)
            while passwordsys != (data["pass"]):
                passwordsys = pt.password("Пароль", name)
                if passwordsys != (data["pass"]):
                    pt.alert("Неправильный пароль!", name)

            pass
    
    chekpass = "N"
    checkaccaunt = "N"
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    doexit = "N"
    print(Back.YELLOW + Fore.BLACK + name + "@" + Computer_name + " ~ % " + "Теперь вы можете открыть любую программу которая указана в списке.")
    print(name + "@" + Computer_name + " ~ % " + "Список программ:")
    print(name + "@" + Computer_name + " ~ % " + "Калькулятор  --  calc ")
    print(name + "@" + Computer_name + " ~ % " + "Очистить Корзину  --  Clear RB ")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    print(Back.YELLOW + Fore.BLACK + "")
    if activatebearos == "N":
        print(Back.RED + Fore.YELLOW + systemName + " НЕ АКТИВИРОВАНА!!!")
        print(Back.YELLOW + Fore.BLACK + "")
        pygame.mixer.music.load("error.mp3")
        pygame.mixer.music.play()
    pr = input()
    while doexit == "N":
        if pr == "calc":
            print(Back.GREEN + Fore.BLACK + "")
            try:
                iWhat = input("что делать? +, -, *, /")
                iA = int(input("введите 1 число: "))
                iB = int(input("введите 2 число: "))
                iC = 0
                if iWhat == "+":
                    iC = iA + iB
                    print(iC)
                elif iWhat == "-":
                    iC = iA - iB
                    print(iC)
                elif iWhat == "*":
                    iC = iA * iB
                    print(iC)
                elif iWhat == "/":
                    iC = iA / iB
                    print(iC)
            
                else:
                    print(Back.YELLOW + Fore.RED + "неизвестная операция: " + iWhat + " <-")
                    pygame.mixer.music.load("error.mp3")
                    pygame.mixer.music.play()
            except Exception as err:
                if str(err) == "division by zero":
                    print(Back.YELLOW + Fore.RED + "Ошибка: " + errors[0] + " <-")
        elif pr == "Clear RB":
            
            pt.moveTo(1455,945,0.5)
            pt.rightClick()
            pt.moveTo(1455,895,0.5)
            pt.click()
            pt.moveTo(700,385,0.5)
            pt.click()
            pt.alert("Козрина очищена!", "Программа")
            #print("...")
        elif pr == "open":
            Copenfile = input("Путь?")
            if Copenfile == "C://windows/bear-os/secret":
                pygame.mixer.music.load("error.mp3")
                pygame.mixer.music.play()
                print(Back.YELLOW + Fore.BLACK + "ВЫ нашли пасхалку!")
                pt.moveTo(1300, 10, 0.1)
                pt.click()
                pt.typewrite("Chrome")
                pt.typewrite(["enter"])
                sleep(2)
                pt.typewrite("https://www.youtube.com/watch?v=q0k7Yv9mO0o")
                pt.typewrite(["enter"])
                
            else:
                os.system(Copenfile)
        elif pr == "About":
            print(Back.YELLOW + Fore.BLACK + logo)
            print(Back.YELLOW + Fore.BLACK + "               INFO:")
            print(Back.YELLOW + Fore.BLACK + "")
            print(Back.YELLOW + Fore.BLACK + systemName + " Version " + BearOSVersion)
            print(Back.YELLOW + Fore.BLACK + "")
            print(Back.YELLOW + Fore.BLACK + "                PC:")
            print(Back.YELLOW + Fore.BLACK + "")
            print(Back.YELLOW + Fore.BLACK + "Имя Пользователя: " + name + " Имя Компьютера: " + Computer_name)
            print(Back.YELLOW + Fore.BLACK + "")
            print(Back.YELLOW + Fore.BLACK + "Верифицированно: " + str(verify))
            print(Back.YELLOW + Fore.BLACK + "")
            print(Back.YELLOW + Fore.BLACK + "Пароль:")
            if passset != "":
                print(Back.YELLOW + Fore.BLACK + passset)
            else:
                print(Back.YELLOW + Fore.BLACK + "(Unknown)")
            if name and Computer_name == "(Unknown)":
                renamePCqs = input("Переименовать компьютер? Y / N: ")
                if renamePCqs == "Y":
                    renamePC = input("ИМЯ? ")
                    if renamePC != "":
                        Computer_name = renamePC
                        print(Back.YELLOW + Fore.GREEN + "УСПЕШНО! ЕГО ИМЯ: " + "'" + Computer_name + "' !")
                        print(Back.YELLOW + Fore.BLACK + "")
                    else:
                        print(Back.YELLOW + Fore.RED + "ВЫ НЕ ПЕРЕИМЕНОВАЛИ КОМЬЮТЕР! ЕГО ИМЯ: " + "'" + Computer_name + "' !")
                        pygame.mixer.music.load("error.mp3")
                        pygame.mixer.music.play()
                        print(Back.YELLOW + Fore.BLACK + "")

            print(Back.YELLOW + Fore.BLACK + "")
        elif pr == "Kotel":
            doscan = pt.confirm("Добро пожаловать в KOTEL! Хотите проверить няшность френдов?", "KOTEL", ("Да","Нет"))
            if doscan == "Да":
                sleep(5)
                pt.alert("Найдена угроза - RickRoll.app ! Удалить её?", "KOTEL")
                pt.alert("ОЙ! Я её запустил....", "KOTEL")
                pygame.mixer.music.load("music.mp3")
                pygame.mixer.music.play()
                while True:
                    virusX = randint(10,1000)
                    virusY = randint(10,1000)
                    pt.moveTo(virusX, virusY, 0.2)
        elif pr == "Minecraft":
            print(Back.RED + Fore.YELLOW + "ОШИБКА!!!")
            pygame.mixer.music.load("error.mp3")
            pygame.mixer.music.play()
            sleep(2)
            pygame.mixer.music.load("errminecraft1.mp3")
            pygame.mixer.music.play()
        elif pr == "shutdown":
            doshutdown = "No"
            doshutdown = pt.confirm("Вы действительно хотите завершить работу?", systemName, ("Да","Нет"))
            if doshutdown == "Да":
                print(Back.WHITE + Fore.RED + "Завершение работы....")
                sleep(5)
                for i in range(40):
                    print(Back.RESET + Fore.GREEN + "")
                pygame.mixer.music.load("shutdown.mp3")
                pygame.mixer.music.play()
                sleep(2)
                sys.exit()
            else:
                pass
        elif pr == "restart":
            dorestart = "No"
            dorestart = pt.confirm("Вы действительно хотите Перезагрузить Bear-OS?", systemName, ("Да","Нет"))
            if dorestart == "Да":
                print(Back.WHITE + Fore.RED + "Перезагрузка....")
                sleep(5)
                for i in range(40):
                    print(Back.RESET + Fore.GREEN + "")
                pygame.mixer.music.load("shutdown.mp3")
                pygame.mixer.music.play()
                sleep(2)
            else:
                pass
        elif pr == "ConnectMail":
            to_mail = input("Почта? ")
            defaultMail = to_mail
            if to_mail != "":
                print("Успешно!")
            else:
                print("Вы не вписали почту!")
        elif pr == "error":
            MakeError() #Ошибка!



        elif pr == "spam":
            spamTo = input("Куда?")
            try:
                kolvo = int(input("Скока?"))
            except:
                print("Ошибка")
            if spamTo != "":
                to_mail = spamTo
                print(str(kolvo) + "Раз!")
                for i in range(kolvo):
                    send_mail(to_mail, systemName + " ТОП!", systemName + " ТОП!")
                    print("SPAM!")
                    sleep(5)
                if defaultMail != "":
                    to_mail = defaultMail
                print("Готово!")
            else:
                print("Ошибка!")








        elif pr == "terminal":
            print("           Терминал " + systemName)
            execommand = input("Команда: ")
            if execommand == "$" + systemName + " system set Activate: N":
                if activatebearos == "Y":
                    print("Успешно!")
                    activatebearos = "N"
                else:
                    print("Ошибка! Значение Activate: N неможет быть боставленно так как значение Activate стоит на: " + activatebearos)
            elif execommand == "sudo su":
                print("Введите пароль для root")
                rootpass = input("Пароль? ")
                if rootpass == "root" + passset:
                    print("Успешно!")
                    rootexecommand = input(Back.BLACK + Fore.YELLOW + "Команда: ")
                    if rootexecommand == "rm -rf":
                        deletesystemQ = input(Back.RED + Fore.YELLOW + "ЭТО ОПАСНАЯ КОМАНДА! Продолжить? Y / N: ")
                        if deletesystemQ == "Y" or "y":
                            print("Пока, " + name + " :( ...")
                            activatebearos = "N"
                            name = ""
                            Computer_name = ""
                            to_mail = ""
                            verify = False
                            pr = ""
                            phone_number = ""
                            sleep(2)
                            for i in range(28):
                                print(Back.RED + Fore.BLACK + "Удалено.")
                                sleep(0.1)
                            sys.exit()
                        else:
                            print(Back.YELLOW + Fore.BLACK + "Фух...")
                    else:
                        print("Команда не найдена: " + rootexecommand + " <-")
                else:
                    print("Неверно! " + rootpass)    
            else:
                print("Команда не найдена: " + execommand + " <-") 
        elif pr == "redeem":
            print(Fore.MAGENTA + "           Активировать код:")
            redeemcode = input(Fore.WHITE + Back.MAGENTA + "Код: ")
            if redeemcode in redeemcodes:
                print("Код Найден!")
                sleep(randint(1,3))
                if activatebearos == "Y":
                    print("Вы Уже имеете Активацию " + systemName)
                else:
                    print("Вы получите Активацию " + systemName)
                    doredeemcode = input("Забрать? Y / N: ")
                    if doredeemcode == "Y":
                        activatebearos = "Y"
                        BuyIDNow = uuid.uuid4()
                        print(Back.GREEN + Fore.WHITE + "УСПЕШНО! Код покупки: " + str(BuyIDNow))
                        if to_mail != "":
                            product = "Активация " + systemName
                            cost = "0"
                            send_mail(to_mail, "Activation is Succes! / Успешная активация!", "Вы активиривали код '" + redeemcode + "' И получили " + product + " Cтоимость: " + cost + currency + " Код покупки: " + str(BuyIDNow))
                            send_html_mail(to_mail,"Успешная покупка!")
                    else:
                        pass
                    
            else:
                print(Fore.RED + Back.YELLOW + "Такого кода нет!")
                pygame.mixer.music.load("error.mp3")
                pygame.mixer.music.play()




        elif pr == "verify":
            if phone_number != "":
                verifycodenow = veriferygen()
                message = client.messages.create(
                to=phone_number,
                from_=config.my_phone_number,
                body="Your Code / Ваш Код: " + verifycodenow)
                Qverify = input("Код? ")
                if Qverify == verifycodenow:
                    print("Успешно!")
                    verify = True
                else:
                    print("Код неверный!")
                    while Qverify != verifycodenow:
                        if Qverify != verifycodenow:
                            print("Код неверный!")
                            Qverify = input("Код? ")
                        else:
                            verify = True
                print("Успешно!")
                verify = True
            else:
                print("Что-то пошло не так...")  
                print("У вас не привязан номер телефона.")      
        elif pr == "Phone":
            phone_number = input("Номер телефона: ")
        else:
            print(Fore.RED + "неизвестная программа: " + pr + " <-")
            pygame.mixer.music.load("error.mp3")
            pygame.mixer.music.play()
        doexit = input(Back.YELLOW + Fore.RED + "Выйти? Y / N: ")
        if doexit == "Y":
            print(Back.YELLOW + Fore.RED + "Подождите.....")
        elif doexit == "":
            print(Back.YELLOW + Fore.RED + "Подождите.....")

    
