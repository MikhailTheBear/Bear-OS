#--------Greeting--------#

#Hello! This is Bear-OS, a simple OS written in Python!
#This OS is still in development, so there may be some bugs!
#License at the end of the file!

#ATENTION: The config.py file is required to run this OS and contains your email and password for sending emails!

#This OS in Russian Language! (EN version is in development!) because this is my native language! Please dont hate me :D

#Libraries like bearpay and mask_card wrotten by me!

#--------Приветствие--------#

#Привет! Это Bear-OS, простая ОС написанная на Python!
#ОС всё ещё в разработке, так что могут быть баги!
#Лицензия в конце файла!

#ВНИМАНИЕ: Файл config.py требуется для запуска этой ОС и содержит вашу почту и пароль для отправки писем!

#Библиотеки такие как bearpay и mask_card написаны мной!



#--------VERSION 1.8.7, What's new?--------#

#- Added currency system (RUB, $, EUR, HRY, GBP, BYN) etc.
#- BearPay - Added card masking function (mask_card)
#- Fixed some bugs, like: If you change currency, the balance is not changed (If i have 587 RUB and change to $ i will have 587$)
#- Added new redeem codes
#- BearPay now can work with Iphone (with flask server and Shortcuts POST request) INSTRUCTIONS HERE: https://placeholder.com
#- theme changer by theme.py


#--------ВЕРСИЯ 1.8.7, Что нового?--------#
#- Добавлена система валют (RUB, $, EUR, HRY, GBP, BYN) и т.д.
#- BearPay - Добавлена функция маскировки карт (mask_card)
#- Исправлены некоторые баги, например: Если вы меняете валюту, баланс не меняется (Если у меня 587 RUB и я меняю на $, у меня будет 587$)
#- Добавлены новые коды активации
#- BearPay теперь может работать с Iphone (с flask сервером и Shortcuts POST запросом) ИНСТРУКЦИИ ЗДЕСЬ: https://placeholder.com
#- смена темы через theme.py



#--------IMPORTS--------#
from time import sleep
import config
from config import password, from_email
import json
import pygame
from random import *
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
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
import bearpay
from mask_card import mask_card_number
import theme
from theme import *




sleep(1)


#--------READ/WRITE JSON--------#





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


def writeban(data4,filenameban):
    data3 = json.dumps(data3)
    data3 = json.loads(str(data3))
    with open(filenameban, 'w', encoding='utf-8') as file4:
        json.dump(data4, file4, indent=4)


def readban(filenameban):
    with open(filenameban, 'r', encoding='utf-8') as file4: 
        return json.load(file4)

#data["pass"].append("cat")

#writepass(data, 'data.json')

#print(readpass('data.json'))

#(data["pass"][0])
    
data3 = {
    "licensekey" : ""
}


#--------License Key Geniration--------#

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

#--------Error/Ban Function--------#


def MakeError():
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + ":(")
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + "На вашем ПК Возникла Ошибка!")
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + "Код Ошибки:")
    print(Back.BLUE + Fore.WHITE + "Читайте ниже")
    print(Back.BLUE + Fore.WHITE + "")
    print(Back.BLUE + Fore.WHITE + "Проверьте правильность на сайте: ")
    print(Back.BLUE + Fore.WHITE + "https://sites.google.com/view/bear-os-official/")
    for i in range(3):
        print(Back.BLUE + Fore.WHITE + "")

def MakeBan():
    print(Back.RED + Fore.WHITE + "")
    print(Back.RED + Fore.WHITE + ":(")
    print(Back.RED + Fore.WHITE + "")
    print(Back.RED + Fore.WHITE + "Вы были забанены!")
    print(Back.RED + Fore.WHITE + "")
    print(Back.RED + Fore.WHITE + "Код Ошибки:")
    print(Back.RED + Fore.WHITE + "You are been banned")
    print(Back.RED + Fore.WHITE + "")
    print(Back.RED + Fore.WHITE + "Проверьте правильность на сайте: ")
    print(Back.RED + Fore.WHITE + "https://sites.google.com/view/bear-os-official/документация/ошибки/you-are-been-banned")
    for i in range(3):
        print(Back.RED + Fore.WHITE + "")



data3["licensekey"] = licensekeygen()

writelc(data3, 'yourlicensekey.json')



#--------Logo--------#





logo = ("""
██████╗░███████╗░█████╗░██████╗░░░░░░░░█████╗░░██████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔════╝
██████╦╝█████╗░░███████║██████╔╝█████╗██║░░██║╚█████╗░
██╔══██╗██╔══╝░░██╔══██║██╔══██╗╚════╝██║░░██║░╚═══██╗
██████╦╝███████╗██║░░██║██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░
""")










#--------PROPERTIES--------#
forgorbearos = "N" #forget BEAR-OS?
checkpass = "Y" #Check password?
defaultName = "User" #default name
passset = "123" #default password
checkaccaunt = "Y" #check accaunt
activatebearos = "N" #Activate Bear-OS
BearOSVersion = "1.8.7" # Version Of Bear-OS
systemName = "Bear-OS" # Bear-OS System Name
to_mail = "" #default mail IMPORTANT: DONT CHANGE THIS!
defaultMail = "" #default mail
errorName = "" #default error name
defaultСurrency = "$" #default currency
currency = "₽" #set currency
product = "(Unknown)" #default product
cost = 0 #default cost
askLanguage = "Y"
defaultLanguage = "EN"
currencyrate = 1 #default rate
phone_number = "" #default number
balance = 0 #default balance
verify = False #default BOOLEAN

#--------SMTP--------#

SMTPPROTOCOL = "smtp.gmail.com"
SMTPPORT = 587 #SMTP MAIL PORT! 587 - For GMAIL 465 - For YANDEX

#--------COPYRIGHT FORMAT--------#

#-Russian-#
COPYRIGHT = Fore.RED + "© " + systemName + ", все права защещены." + Fore.RESET
#-English-#
COPYRIGHTEN = Fore.RED + "© " + systemName + ", all rights reserved." + Fore.RESET




#--------Computer Components--------#
BIOS = "BearBOIS V1.1.2"
Processor = "Intel Pentium 2000 BC"
RAM = "1KB"
Motherboard = "Dinoboard A0.1"


#--------SHOW PROPERTIES--------#


SHOWPROPERTIES = True

if SHOWPROPERTIES == True:
    print(logo + "\n----------------------------\n          PROPERTIES:\n----------------------------")

    print(f"VERSION: {BearOSVersion}")
    print("\n")
    print(f"Forgor Bear-OS: {forgorbearos}")
    print(f"System Name: {systemName}")
    print(f"Check Password: {checkpass}")
    print(f"Default Name: {defaultName}")
    print(f"Default Password: {passset}")
    print("\n")
    input("Press ENTER to continue...")





if currency == "":
    currency = defaultСurrency
else:
    print(Fore.RED + "[" + systemName + "] " + "The currency is worth '" + currency + "'")

#--------Functions--------#



def createCaptcha():
    captcha1 = [1,3,2,5,2,7]
    captcha2 = [6,1,2,9,0]
    captcha3 = ["x","y","a","g","z"]
    captcha4 = ["B","S","Q","K","J"]
    captcha5 = ["n","2","L","9","m"]
    captchagen = str(captcha1[randint(0,5)]) + str(captcha2[randint(0,4)]) + str(captcha3[randint(0,4)]) + str(captcha4[randint(0,4)]) + str(captcha5[randint(0,4)])
    return captchagen


def loading():
    sleep(randint(1,3))
    print("\n"*28)
    print(">...... [0%]")
    sleep(randint(1,3))
    print("\n"*28)
    print("=>..... [20%]")
    sleep(randint(1,3))
    print("\n"*28)
    print("==>.... [40%]")
    sleep(randint(1,3))
    print("\n"*28)
    print("===>... [60%]")
    sleep(randint(1,3))
    print("\n"*28)
    print("====>.. [80%]")
    sleep(randint(1,3))
    print("\n"*28)
    print("=====> [100%]")
    sleep(randint(1,3))
    print("\n"*28)

def setcurrencyrate(currency):
    if currency == "$": 
        currencyrate = 1
    elif currency == "":
        currencyrate = 1
    elif currency == "RUB" or currency == "₽":
        currencyrate = 80
    elif currency == "HRY":
        currencyrate = 41.50
    elif currency == "GBP":
        currencyrate = 0.75
    elif currency == "EUR":
        currencyrate = 0.89
    elif currency == "BYN":
        currencyrate = 3.28
    else:
        currencyrate = 9999999999
    return currencyrate


def makeSuspend(suspendreason):
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + "Ваш аккаунт был приостановлен!")
    print("Причина: " + suspendreason)
    print("ВАЖНО: Ваш аккаунт будет забанен если вы сделаете ошибку!")
    print("Для проверки: \n1: введите капчу; \n2: напишите код, который вам придёт на почту (Почта была сброшенна!)")
    input("Дальше")
    print(Fore.WHITE + Back.MAGENTA + "")
    captchanow = createCaptcha()
    suspendcode = veriferygen()
    print("Капча: " + captchanow)
    QascСaptcha = str(input("Введите капчу: "))
    if QascСaptcha == captchanow:
        to_mail = input("Почта: ")
        if to_mail != "":
            send_mail(to_mail, "Code / Код", str(suspendcode))
        
        else:
            to_mail = input("Почта: ")
            if to_mail != "":
                send_mail(to_mail, "Code / Код", str(suspendcode))

            else:
                return 0

        QascCode = int(input("Код: "))
        if QascCode == suspendcode:
            return 1
        else:
            return 0
    else:
        return 0
            
        
        










#--------Data--------#



cardnums = ["0000 0000 0000 0000", "1234 1234 1234 1234"]

carddates = ["09/28", "11/26"]

cardcvvs = ["222", "444"]

banwords = ["Nigger", "nigger", "Nigga", "nigga", "Nigg", "Nigg", "Nig", "nig", "AltDoors", "altdoors", "Gitler", "gitler", "g1tler", "G1tler"]


errors = ["Нельзя делить на ноль!","","","",""]

errorsen = ["You can't divide by zero!","","","",""]

errorInfo = [
    "ℹ️ Эта ошибка связана с ошибкой SMTP (У вас включен VPN, У вас нет Интернета и т.д. (Иногда может случится из-за бага " + systemName + ") Чаще всего у ошибки бывает код 502!)",
    "ℹ️ Неопределённая ошибка! Такое может случится когда сервис/библиотека не может нормально описать ошибку. Чаще всего это выглядит так: '{}'",
    "Кажись программа хотела другой тип данных (В этом случае целое число (int) )"
]


redeemcodes = [
    "SA3V-8X9B-C7JK-DZ87",
    "3A7Z-F3MH-827A-21A3",
    "HG5D-8D98-KJ6Q-RT3Q",
    "Q4Z7-KM9B-2P6D-XT3R",
    "N8H3-VR2F-1L9C-JW5S",
    "B2D6-ZT8K-5M4X-LQ1J",
    "F7G1-HK5N-3C8P-VR2M",
    "L9P4-XJ6B-2T8Q-WF3K",
    "C3R7-MF1V-8Z2N-YK5H",
    "V5K8-LT2Q-9H3D-PB7X",
    "J1M9-WC5F-4X7R-ZT2G",
    "T6N2-PH3K-7L8B-QV4S",
    "R8F4-DX1M-6K5J-NC9V"
]

redeemedcodes = []


SMTPPORTS = [587, 465, 25]
SMTPPROTOCOLS = ["smtp.gmail.com", "smtp.yandex.com", "smtp.yandex.ru"]


#--------CHECKS--------#


try:
    with open("htmltemplate.html") as file:
        html = file.read()
except:
    print(Back.RED + Fore.WHITE + "FATAL ERROR! The system cannot open the file 'htmltemplate.html'")
    pygame.mixer.music.load("error.mp3")
    pygame.mixer.music.play()
    sleep(2)
    sys.exit()


try:
    with open("htmltemplate2.html") as file:
        htmlerror = file.read()
except:
    print(Back.RED + Fore.WHITE + "FATAL ERROR! The system cannot open the file 'htmltemplate2.html'")
    pygame.mixer.music.load("error.mp3")
    pygame.mixer.music.play()
    sleep(2)
    sys.exit()


if SMTPPORT not in SMTPPORTS:
    print(Back.RED + Fore.WHITE + "FATAL ERROR! The system cannot find 'SMTPPORT'")
    pygame.mixer.music.load("error.mp3")
    pygame.mixer.music.play()
    sleep(2)
    sys.exit()

elif SMTPPROTOCOL not in SMTPPROTOCOLS:
    print(Back.RED + Fore.WHITE + "FATAL ERROR! The system cannot find 'SMTPROTOCOL'")
    pygame.mixer.music.load("error.mp3")
    pygame.mixer.music.play()
    sleep(2)
    sys.exit()


#--------MAIL FUNCTION--------#


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
        if "smtp" in str(ex):
            print(errorInfo[0])
        elif str(ex) == "":
            print(errorInfo[1])




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
        if "smtp" in str(ex):
            print(errorInfo[0])
        elif str(ex) == "":
            print(errorInfo[1])






def send_html_error(to_mail, subject):
    try:
        msg = MIMEMultipart()
        msg['From'] = config.from_email
        msg['To'] = to_mail
        msg['Subject'] = subject
        msg.attach(
            MIMEText(htmlerror, 'html')
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
        if "smtp" in str(ex):
            print(errorInfo[0])
        elif str(ex) == "":
            print(errorInfo[1])


def send_ban(to_mail, subject, text):
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
        if "smtp" in str(ex):
            print(errorInfo[0])
        elif str(ex) == "":
            print(errorInfo[1])


def send_data(to_mail, subject, text):
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
        if "smtp" in str(ex):
            print(errorInfo[0])
        elif str(ex) == "":
            print(errorInfo[1])
        



#--------CHECK WORDS--------#


#-Russian-#

def checkwords(to_mail, name, Computer_name, mailText, mailSubject):
    if name in banwords:
            if to_mail != "":
                send_ban(to_mail, "Вы были забанены!", systemName + "\n Здравствуйте, " + to_mail + " Вы были забанены! " + "\n Причина бана: Имя: " + name)
            return "ban"
    else:
        pass
    if Computer_name in banwords:
            if to_mail != "":
                send_ban(to_mail, "Вы были забанены!", systemName + "\n Здравствуйте, " + to_mail + " Вы были забанены! " + "\n Причина бана: Имя компьютера: " + Computer_name)
            return "ban"
    
    if mailText in banwords:
            if to_mail != "":
                send_ban(to_mail, "Вы были забанены!", systemName + "\n Здравствуйте, " + to_mail + " Вы были забанены! " + "\n Причина бана: Текст Сообщения: " + mailText)
            return "ban"
    else:
        pass

    if mailSubject in banwords:
            if to_mail != "":
                send_ban(to_mail, "Вы были забанены!", systemName + "\n Здравствуйте, " + to_mail + " Вы были забанены! " + "\n Причина бана: Текст Темы Сообщения: " + mailSubject)
            return "ban"
    
#-English-#

def checkwordsen(to_mail, name, Computer_name, mailText, mailSubject):
    if name in banwords:
            if to_mail != "":
                send_ban(to_mail, "You have been banned!", systemName + "\n Hello, " + to_mail + " You have been banned! " + "\n Reason for ban: Name: " + name)
            return "ban"
    else:
        pass
    if Computer_name in banwords:
            if to_mail != "":
                send_ban(to_mail, "You have been banned!", systemName + "\n Hello, " + to_mail + " You have been banned! " + "\n Reason for ban: Computer Name: " + Computer_name)
            return "ban"
    
    if mailText in banwords:
            if to_mail != "":
                send_ban(to_mail, "You have been banned!", systemName + "\n Hello, " + to_mail + " You have been banned! " + "\n Reason for ban: Message Text: " + mailText)
            return "ban"
    else:
        pass

    if mailSubject in banwords:
            if to_mail != "":
                send_ban(to_mail, "You have been banned!", systemName + "\n Hello, " + to_mail + " You have been banned! " + "\n Reason for ban: Message Subject Text: " + mailSubject)
            return "ban"


#--------DATA--------#



data = {
    "pass" : passset
}


data2 = {
    "user" : []
}




#--------START--------#


if forgorbearos == "Y":
    bearosexist = "N"
    
else:
    bearosexist = "Y"
    if defaultName == "":
        name = "(Unknown)"
    else:
        name = defaultName
    Computer_name = "(Unknown)"
    checkpass = "N"
    print(Back.RED + Fore.YELLOW + "No name!")
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



color = getattr(Fore, installer_color)

print(Back.RESET + color + "")



try:
    if askLanguage == "Y":
        print("-------------------------------")
        print("Select Language/Выберете язык:")
        print("1 -- RU - Русский")
        print("2 -- EN - English (BETA)")
        print("-------------------------------")
        Qlang = int(input(""))
        if Qlang == 1:
            selectedLang = "RU"
        else:
            selectedLang = "EN"

    else:
        selectedLang = defaultLanguage
except:
    for i in range(15):
        print("")
    print("Default language: English")
    selectedLang = defaultLanguage 
    
for i in range(4):
        print("")
if selectedLang == "RU":
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

else:
    print(BIOS)
    sleep(randint(1,2))
    print("-----------------------------------")
    print("Motherboard: " + Motherboard)
    print("-----------------------------------")
    sleep(randint(1,2))
    print("Processor: " + Processor)
    print("-----------------------------------")
    sleep(randint(1,2))
    print("RAM: " + RAM)
    print("-----------------------------------")
    sleep(randint(1,5))
    input("Press Enter to continue...")

 


if selectedLang == "RU":


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

        color = getattr(Fore, installer_color)

        print(Back.RESET + color + "")


        while bearosexist == "N":
            print(Back.RESET + Fore.GREEN + logo)
            print(Back.RESET + Fore.GREEN + "Добро пожаловать в установщик " + systemName)
            name = input("Введите ваше имя: ")
            if name == "":
                name = "(Unknown)"
            else:
                pass
            print("Здравствуйте, " + name)
            data2["user"].append(name)

            writeuser(data2, 'user.json')
            Computer_name = input("Введите имя компьютера: ")
            if Computer_name == "":
                Computer_name = "(Unknown)"
            else:
                pass
            print(name + ", вы назвали компьютер: " + Computer_name)
            
                
            passset = input("Введите Пароль для аккаунта " + name + ": ")
            if passset == "":
                passset = "(Unknown)"
                checkpass = "N"
            else:
                pass
            data["pass"] = passset

            writepass(data, 'data.json')

            phone_number = input("Ваш номер телефона: ")

            to_mail = input("Ваша почта: ")
            defaultMail = to_mail 
            if checkwords(to_mail, name, Computer_name, "", "") == "ban": # Проверяем слова, Баним если они плохие!
                MakeBan()
                pt.alert("Вы были забанены!", systemName)
                isbanned = True

                #data4["ban"] = isbanned

                #writepass(data4, 'ban.json')
                sys.exit()
            else:
                pass

            if to_mail != "":
                send_data(to_mail, "Вы успешно зарегестрированы на " + systemName, "\nИмя: " + name + "\nИмя компьютера: " + Computer_name + "\nПочта: " + to_mail + "\nСервис: " + systemName + "\nПочта отправителя: " + config.from_email + "\nС уважением, " + systemName + " Team" + "\n ⚠️ Если это не вы, то видимо кто-то использует вашу почту!")
            else:
                pass
            



            # print("Is Banned", data4["ban"])
            # if (data4["ban"]) == True:
            #     pt.alert("Вы были забанены в этой системе!", systemName)
            #     sys.exit()
            # else:
            #     pass

            predupr = "Письмо было отправлено на вашу почту. Если его нет проверте                          вкладку 'Спам'! Лицензионный Ключ?" 
            print(name + ", Вы поставили пароль: " + (data["pass"]))
            licenseyes = pt.confirm("У вас есть Лицензионный Ключ?", "Bear-OS", ("Да","Нет"))
            if licenseyes == "Да":
                activatebearos = "Y"
                licensekeynow = licensekeygen()
                if to_mail != "":
                    send_mail(to_mail, "License Key / Лицензионный Ключ", "Your key / Ваш ключ: " + licensekeynow)
                else:
                    #messagebox.showerror("Почта", "Ошибка в почте!")
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
            installsuccess = "no"
            stdo = input()
            while installsuccess == "no":
                if stdo == "/start download":
                    print(Fore.GREEN + "Установка...")
                    loading()
                    print("Готово!")
                    installsuccess = "yes"
                    bearosexist = "Y"
                else:
                    print(Fore.RED + "Неизвестная команда: " + stdo + " <-")
                    pygame.mixer.music.load("error.mp3")
                    pygame.mixer.music.play()
                    installsuccess = "no"
                    stdo = input(Fore.GREEN + "Чтобы начать установку пропишите команду: " + Fore.YELLOW + "/start download: ")
        if checkaccaunt == "Y":
            print("---------------------------- \n Войдите в аккаунт!\n----------------------------")
            pt.alert("Выбирите Акаунт", systemName, button=name)
        if checkpass == "Y":
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
        
        checkpass = "N"
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
        print(name + "@" + Computer_name + " ~ % " + "Terminal  --  terminal ")
        print(name + "@" + Computer_name + " ~ % " + "Выключить  --  shutdown ")
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
                pt.alert("Корзина очищена!", "Программа")
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
                print(Back.YELLOW + Fore.BLACK + "")
                print(Back.YELLOW + Fore.BLACK + COPYRIGHT)
                if Computer_name == "(Unknown)":
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
                        print("Ошибка! Значение Activate: N неможет быть поставленно так как значение Activate стоит на: " + activatebearos)
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
                if redeemcode in redeemcodes and redeemcode not in redeemedcodes:
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
                            redeemedcodes.append(redeemcode)
                            if to_mail != "":
                                product = "Активация " + systemName
                                cost = 0
                                send_mail(to_mail, "Activation is Success! / Успешная активация!", "Здравствуйте, " + name + "\nВы активиривали код '" + redeemcode + "' И получили " + product + "\nCтоимость: " + str(cost) + currency + "\nКод покупки: " + str(BuyIDNow))
                                send_html_mail(to_mail,"Успешная покупка!")
                        else:
                            pass

                elif redeemcode in redeemedcodes:
                    print(Fore.RED + Back.YELLOW + "Извините, но этот код уже был использован!")
                    pygame.mixer.music.load("error.mp3")
                    pygame.mixer.music.play()
            
                    
                else:
                    print(Fore.RED + Back.YELLOW + "Такого кода нет!")
                    pygame.mixer.music.load("error.mp3")
                    pygame.mixer.music.play()




            elif pr == "verify":
                try:
                    verifycode = veriferygen()
                    if to_mail != "":
                        send_mail(to_mail, "Code / Код", str(verifycode))
                        Qverify = int(input("Код: "))
                        if Qverify == verifycode:
                            print("Успешно!")
                            verify = True
                        else:
                            print("Неправильный код!")
                    else:
                        print("Почта не привязана! Используйте ConnectMail")
                except Exception as ex:
                    if "invalid literal for int()" in str(ex):
                        print("Случилась ошибка: " + errorInfo[2])
                



            elif pr == "mail":
                print("Почта")
                Qsend_mail = input("Отправить письмо? Y / N: ")
                if Qsend_mail == "Y" or "":
                    mailTo = input("Получатель: ")
                    mailSubject = input("Тема: ")
                    mailText = input("Текст: ")
                    if checkwords(to_mail, name, Computer_name, mailText, mailSubject) == "ban": # Проверяем слова, Баним если они плохие!
                        MakeBan()
                        pt.alert("Вы были забанены!", systemName)
                        isbanned = True

                        #data4["ban"] = isbanned

                        #writepass(data4, 'ban.json')
                        sys.exit()
                    else:
                        pass
                    send_mail(mailTo, str(mailSubject) + " - Отправлено через " + systemName, mailText)

            elif pr == "logout":
                checkaccaunt = "N"
                checkpass = "N"
                Qlogout = input(Back.YELLOW + Fore.RED + "Выйти? 1/2 Y / N: ")
                if Qlogout == "Y" or "":
                    checkaccaunt = "Y"
                    if passset != "":
                        checkpass = "Y"



            elif pr == "store":
                cost1 = 200 * setcurrencyrate(currency)
                product1 = "Ключ Активации " + systemName
                showbalance = balance * setcurrencyrate(currency)
                print("Баланс: " + str(showbalance) + currency)
                print("")
                print("1 -- Ключ Активации -- " + systemName + " -- " + str(cost1) + currency)
                print("")
                print("2 -- Скоро...")
                print("")

                Qitem = str(input("Выбор товара: "))
                if Qitem == "1":
                    cost = cost1
                    product = product1
                    print("Товар: "+ product + ". К оплате: " + str(cost) + currency)
                    Qbuy = input("Купить? Y / N: ")
                    if Qbuy == "Y":
                        if showbalance < cost:
                            print("Недостаточно средств! (" + str(showbalance) + " / " + str(cost) + currency + ")")
                            if to_mail != "":
                                send_html_error(to_mail, "Ошибка покупки: Недостаточно средств!")
                        else:
                            showbalance = showbalance - cost
                            balance = showbalance / setcurrencyrate(currency)
                            BuyIDNow = uuid.uuid4()
                            print(Back.GREEN + Fore.WHITE + "УСПЕШНО! Код покупки: " + str(BuyIDNow))
                            boughtcode = choice(redeemcodes)
                            print(Fore.WHITE + Back.MAGENTA + "Ваш ключ: " + boughtcode + ". Используете его в redeem")
                            if to_mail != "":
                                send_mail(to_mail, "Success puschare! / Успешная покупка!", "Здравствуйте, " + name + "\nВы купили товар '" + product + "' И получили " + product + "\nCтоимость: " + str(cost) + currency + "\nКод покупки: " + str(BuyIDNow) + "\nБаланс: " + str(showbalance) + currency + " (" + str(balance) + "$)" + "\nВаш код: " + boughtcode)
                                send_html_mail(to_mail,"Успешная покупка!")
                        
            elif pr == "addtobalance":
                
                try:
                    # -----------------------------
                    # Нормализация валюты, чтобы не было None
                    # -----------------------------
                    currency = str(currency or "₽").upper().strip()

                    # Ввод суммы пополнения
                    Qatb = float(input("Сумма пополнения (В " + currency + "): ")) 
                    Qatb2 = input("Сумма пополнения: " + str(Qatb) + currency + " Продолжить? Y / N: ")

                    if Qatb2.upper() == "Y":
                        # Оплата через BearPay
                        result = bearpay.pay_RU(Qatb, currency)  # True/False

                        if result:
                            # -----------------------------
                            # Маскируем карту только если она есть
                            # -----------------------------
                            if bearpay.last_card_number:
                                masked = mask_card_number(bearpay.last_card_number)
                                payment_method = "Карта "
                            else:
                                masked = ""
                                payment_method = "Телефон "

                            print("Успешно пополнено: " + str(Qatb) + currency)

                            # Расчет нового баланса
                            newbalance = Qatb / setcurrencyrate(currency)
                            balance = balance + newbalance
                            showbalance = balance * setcurrencyrate(currency)

                            BuyIDNow = uuid.uuid4()

                            # Отправка письма при необходимости
                            if to_mail != "":
                                send_mail(
                                    to_mail,
                                    "Успешная пополнение!",
                                    "Здравствуйте, " + name +
                                    "\nВы пополнили баланс." +
                                    "\nКод покупки: " + str(BuyIDNow) +
                                    "\nНовый баланс: " + str(showbalance) + currency + " (" + str(balance) + "$)" +
                                    "\nМетод оплаты: " + payment_method + masked
                                )
                        else:
                            print("Оплата не прошла. Неверная карта или недостаточно средств.")

                except Exception as ex:
                    print("An error has occurred: " + str(ex))
            

            elif pr == "settings":
                print("Настройки ⚙️")
                print("Изменить валюту - currency ($ / GBP / RUB / HRY)")
                print("Сменить пароль - changepassword")
                Qdosettings = input("Действие: ")
                if Qdosettings == "currency":
                    Qnewcurrency = input("Валюта: ")
                    currency = Qnewcurrency
                    print("Успешно!")
                if Qdosettings == "changepassword":
                    newpass = input("Новый пароль: ")
                    newpassconfirm = input("Подтвердите новый пароль: ")
                    if newpass == newpassconfirm:
                        if newpass != "":
                            passset = newpass
                            data["pass"] = passset
                            writepass(data, 'data.json')

                            print("Успешно! Новый пароль: " + (data["pass"]))
                        else:
                            print("Пароль не должен быть пустым!")
                    else:
                        print("Пароли не совпадают")        

                else:
                    print(Fore.RED + "неизвестное действие: " + Qdosettings + " <-")
                    print(Back.YELLOW + Fore.BLACK + "")
                    


            elif pr == "suspendtest":
                if makeSuspend("Это тест") == 1:
                    print(Fore.WHITE + Back.GREEN  + "Ваш аккаунт был разблокирован!")
                else:
                    MakeBan()
                    pt.alert("Вы были забанены!", systemName)
                    isbanned = True

                    #data4["ban"] = isbanned

                    #writepass(data4, 'ban.json')
                    sys.exit()



            
            else:
                print(Fore.RED + "неизвестная программа: " + pr + " <-")
                pygame.mixer.music.load("error.mp3")
                pygame.mixer.music.play()
            doexit = input(Back.YELLOW + Fore.RED + "Выйти? Y / N: ")
            if doexit == "Y":
                print(Back.YELLOW + Fore.RED + "Подождите.....")
            elif doexit == "":
                print(Back.YELLOW + Fore.RED + "Подождите.....")



#-----------------------EN--------------------------#




else:
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


        while bearosexist == "N":
            print(Back.RESET + Fore.GREEN + logo)
            print(Back.RESET + Fore.GREEN + "Welcome to the installer " + systemName)
            name = input("Enter your name: ")
            if name == "":
                name = "(Unknown)"
            else:
                pass
            print("Hello, " + name)
            data2["user"].append(name)

            writeuser(data2, 'user.json')
            Computer_name = input("Enter your computer name: ")
            if Computer_name == "":
                Computer_name = "(Unknown)"
            else:
                pass
            print(name + ", you named the computer: " + Computer_name)
            
                
            passset = input("Enter your "+ name +" account password: ")
            if passset == "":
                passset = "(Unknown)"
                checkpass = "N"
            else:
                pass
            data["pass"] = passset

            writepass(data, 'data.json')

            phone_number = input("Your phone number: ")

            to_mail = input("Your email: ")
            defaultMail = to_mail 
            if checkwordsen(to_mail, name, Computer_name, "", "") == "ban": # Проверяем слова, Баним если они плохие!
                MakeBan()
                pt.alert("You have been banned!", systemName)
                isbanned = True

                #data4["ban"] = isbanned

                #writepass(data4, 'ban.json')
                sys.exit()
            else:
                pass

            if to_mail != "":
                send_data(to_mail, "You have successfully registered on " + systemName, "\nName: " + name + "\nComputer Name: " + Computer_name + "\nEmail: " + to_mail + "\nService: " + systemName + "\nSender's email: " + config.from_email + "\nBest regards, " + systemName + " Team" + "\n ⚠️ If it's not you, then apparently someone is using your email!")
            else:
                pass
            



            # print("Is Banned", data4["ban"])
            # if (data4["ban"]) == True:
            #     pt.alert("Вы были забанены в этой системе!", systemName)
            #     sys.exit()
            # else:
            #     pass

            predupr = "The letter was sent to your email. If it is not there, check the 'Spam' tab! License Key?" 
            print(name + ", You have set a password: " + (data["pass"]))
            licenseyes = pt.confirm("Do you have a License Key?", "Bear-OS", ("Yes","No"))
            if licenseyes == "Yes":
                activatebearos = "Y"
                licensekeynow = licensekeygen()
                if to_mail != "":
                    send_mail(to_mail, "License Key / Лицензионный Ключ", "Your key / Ваш ключ: " + licensekeynow)
                else:
                    #messagebox.showerror("Почта", "Ошибка в почте!")
                    print("Error, The letter cannot be sent! Because you did not specify the email!")
                    to_mail = input("Your Email: ")
                    while not to_mail != "":
                        if to_mail == "":
                            print("Error, The letter cannot be sent! Because you did not specify the email!")
                            to_mail = input("Your Email: ")
                        else:
                            send_mail(to_mail, "License Key / Лицензионный Ключ", "Your key / Ваш ключ: " + licensekeynow)
                    send_mail(to_mail, "License Key / Лицензионный Ключ", "Ваш ключ: " + licensekeynow)
                licensekeyQ = pt.prompt(predupr, name)
                if licensekeynow == licensekeyQ:
                    pass
                else:
                    pt.alert("Incorrect license key!", name)
                    while licensekeynow != licensekeyQ:
                        licensekeyQ = pt.prompt("License key?", name)
                        if licensekeynow != licensekeyQ:
                            pt.alert("Incorrect license key!", name)
            else:
                activatebearos = "N"
                        


            print(name + "@" + Computer_name + " ~ % " + "To start the installation, enter the command: " + Fore.YELLOW + "/start download: ")
            installsuccess = "no"
            stdo = input()
            while installsuccess == "no":
                if stdo == "/start download":
                    print(Fore.GREEN + "Installation...")
                    loading()
                    print("Done!")
                    installsuccess = "yes"
                    bearosexist = "Y"
                else:
                    print(Fore.RED + "Unknown command: " + stdo + " <-")
                    pygame.mixer.music.load("error.mp3")
                    pygame.mixer.music.play()
                    installsuccess = "no"
                    stdo = input(Fore.GREEN + "To start the installation, enter the command: " + Fore.YELLOW + "/start download: ")
        if checkaccaunt == "Y":
            print("---------------------------- \n Login to your account!\n----------------------------")
            pt.alert("Select Account", systemName, button=name)
        if checkpass == "Y":
            passwordsys = pt.password("Password", name)
            if passwordsys == (data["pass"]):
                pass
            else:
                pt.alert("Incorrect password!", name)
                while passwordsys != (data["pass"]):
                    passwordsys = pt.password("Password", name)
                    if passwordsys != (data["pass"]):
                        pt.alert("Incorrect password!", name)

                pass
        
        checkpass = "N"
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
        print(Back.YELLOW + Fore.BLACK + name + "@" + Computer_name + " ~ % " + "Now you can open any program that is listed.")
        print(name + "@" + Computer_name + " ~ % " + "List of programs:")
        print(name + "@" + Computer_name + " ~ % " + "calc ")
        print(name + "@" + Computer_name + " ~ % " + "Clear RB ")
        print(name + "@" + Computer_name + " ~ % " + "terminal ")
        print(name + "@" + Computer_name + " ~ % " + "shutdown ")
        print(Back.YELLOW + Fore.BLACK + "")
        print(Back.YELLOW + Fore.BLACK + "")
        print(Back.YELLOW + Fore.BLACK + "")
        if activatebearos == "N":
            print(Back.RED + Fore.YELLOW + systemName + " NOT ACTIVATED!!!")
            print(Back.YELLOW + Fore.BLACK + "")
            pygame.mixer.music.load("error.mp3")
            pygame.mixer.music.play()
        pr = input()
        while doexit == "N":
            if pr == "calc":
                print(Back.GREEN + Fore.BLACK + "")
                try:
                    iWhat = input("what to do? +, -, *, /")
                    iA = int(input("enter 1 number: "))
                    iB = int(input("enter 2 number: "))
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
                        print(Back.YELLOW + Fore.RED + "unknown operation: " + iWhat + " <-")
                        pygame.mixer.music.load("error.mp3")
                        pygame.mixer.music.play()
                except Exception as err:
                    if str(err) == "division by zero":
                        print(Back.YELLOW + Fore.RED + "Error: " + errorsen[0] + " <-")
            elif pr == "Clear RB":
                
                pt.moveTo(1455,945,0.5)
                pt.rightClick()
                pt.moveTo(1455,895,0.5)
                pt.click()
                pt.moveTo(700,385,0.5)
                pt.click()
                pt.alert("Trash is empty!", "Program")
                #print("...")
            elif pr == "open":
                Copenfile = input("Path?")
                if Copenfile == "C://windows/bear-os/secret":
                    pygame.mixer.music.load("error.mp3")
                    pygame.mixer.music.play()
                    print(Back.YELLOW + Fore.BLACK + "YOU found an Easter egg!")
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
                print(Back.YELLOW + Fore.BLACK + "Username: " + name + " Computer Name: " + Computer_name)
                print(Back.YELLOW + Fore.BLACK + "")
                print(Back.YELLOW + Fore.BLACK + "Verified: " + str(verify))
                print(Back.YELLOW + Fore.BLACK + "")
                print(Back.YELLOW + Fore.BLACK + "Password:")
                if passset != "":
                    print(Back.YELLOW + Fore.BLACK + passset)
                else:
                    print(Back.YELLOW + Fore.BLACK + "(Unknown)")
                print(Back.YELLOW + Fore.BLACK + "")
                print(Back.YELLOW + Fore.BLACK + COPYRIGHTEN)
                if Computer_name == "(Unknown)":
                    renamePCqs = input("Rename computer? Y / N: ")
                    if renamePCqs == "Y":
                        renamePC = input("NAME? ")
                        if renamePC != "":
                            Computer_name = renamePC
                            print(Back.YELLOW + Fore.GREEN + "SUCCESS! ITS NAME: " + "'" + Computer_name + "' !")
                            print(Back.YELLOW + Fore.BLACK + "")
                        else:
                            print(Back.YELLOW + Fore.RED + "YOU DIDN'T RENAME THE COMPUTER! ITS NAME IS: " + "'" + Computer_name + "' !")
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
                print(Back.RED + Fore.YELLOW + "ERROR!!!")
                pygame.mixer.music.load("error.mp3")
                pygame.mixer.music.play()
                sleep(2)
                pygame.mixer.music.load("errminecraft1.mp3")
                pygame.mixer.music.play()
            elif pr == "shutdown":
                doshutdown = "No"
                doshutdown = pt.confirm("Are you sure you want to shutdown?", systemName, ("Yes","No"))
                if doshutdown == "Yes":
                    print(Back.WHITE + Fore.RED + "Shutdowning...")
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
                to_mail = input("Email? ")
                defaultMail = to_mail
                if to_mail != "":
                    print("Sucsess!")
                else:
                    print("You haven't entered your email!")

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
                        print("Ошибка! Значение Activate: N неможет быть поставленно так как значение Activate стоит на: " + activatebearos)
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
                print(Fore.MAGENTA + "           Activate code:")
                redeemcode = input(Fore.WHITE + Back.MAGENTA + "Code: ")
                if redeemcode in redeemcodes and redeemcode not in redeemedcodes:
                    print("Code Found!")
                    sleep(randint(1,3))
                    if activatebearos == "Y":
                        print("You Already Have Activation of " + systemName)
                    else:
                        print("You will receive Activation of " + systemName)
                        doredeemcode = input("Claim? Y / N: ")
                        if doredeemcode == "Y":
                            activatebearos = "Y"
                            BuyIDNow = uuid.uuid4()
                            print(Back.GREEN + Fore.WHITE + "SUCCESSFULLY! Purchase code: " + str(BuyIDNow))
                            redeemedcodes.append(redeemcode)
                            if to_mail != "":
                                product = "Activation of " + systemName
                                cost = 0
                                send_mail(to_mail, "Activation is Success! / Успешная активация!", "Hello, " + name + "\nYou activated the code '" + redeemcode + "' And you received the " + product + "\nPrice: " + str(cost) + currency + "\nPurchase code: " + str(BuyIDNow))
                                send_html_mail(to_mail,"Successful purchase!")
                        else:
                            pass

                elif redeemcode in redeemedcodes:
                    print(Fore.RED + Back.YELLOW + "Sorry, but this code has already been redeemed.")
                    pygame.mixer.music.load("error.mp3")
                    pygame.mixer.music.play()


                else:
                    print(Fore.RED + Back.YELLOW + "There is no such code!")
                    pygame.mixer.music.load("error.mp3")
                    pygame.mixer.music.play()




            elif pr == "verify":
                try:
                    verifycode = veriferygen()
                    if to_mail != "":
                        send_mail(to_mail, "Code / Код", str(verifycode))
                        Qverify = int(input("Code: "))
                        if Qverify == verifycode:
                            print("Successfully!")
                            verify = True
                        else:
                            print("Incorrect code!")
                    else:
                        print("Email is not linked! Use ConnectMail")
                except Exception as ex:
                    if "invalid literal for int()" in str(ex):
                        print("An error has occurred: " + errorInfo[2])
                



            elif pr == "mail":
                print("Почта")
                Qsend_mail = input("Send a email? Y / N: ")
                if Qsend_mail == "Y" or "":
                    mailTo = input("Recipient: ")
                    mailSubject = input("Subject: ")
                    mailText = input("Text: ")
                    if checkwordsen(to_mail, name, Computer_name, mailText, mailSubject) == "ban": # Проверяем слова, Баним если они плохие!
                        MakeBan()
                        pt.alert("You have been banned!", systemName)
                        isbanned = True

                        #data4["ban"] = isbanned

                        #writepass(data4, 'ban.json')
                        sys.exit()
                    else:
                        pass
                    send_mail(mailTo, mailSubject, mailText)

            elif pr == "logout":
                checkaccaunt = "N"
                checkpass = "N"
                Qlogout = input(Back.YELLOW + Fore.RED + "Logout? 1/2 Y / N: ")
                if Qlogout == "Y" or "":
                    checkaccaunt = "Y"
                    if passset != "":
                        checkpass = "Y"



            elif pr == "store":
                cost1 = 200 * setcurrencyrate(currency)
                product1 = "Activation Key of " + systemName
                showbalance = balance * setcurrencyrate(currency)
                print("Balance: " + str(showbalance) + currency)
                print("")
                print("1 -- Activation Key of -- " + systemName + " -- " + str(cost1) + currency)
                print("")
                print("2 -- Soon...")
                print("")

                Qitem = str(input("Product selection: "))
                if Qitem == "1":
                    cost = cost1
                    product = product1
                    print("Product: "+ product + ". To be paid: " + str(cost) + currency)
                    Qbuy = input("Buy? Y / N: ")
                    if Qbuy == "Y":
                        if showbalance < cost:
                            print("Not enough funds! (" + str(showbalance) + " / " + str(cost) + currency + ")")
                            if to_mail != "":
                                send_html_error(to_mail, "Purchase Error: Insufficient funds!")
                        else:
                            showbalance = showbalance - cost
                            balance = showbalance / setcurrencyrate(currency)
                            BuyIDNow = uuid.uuid4()
                            print(Back.GREEN + Fore.WHITE + "SUCCESSFULLY! Purchase code: " + str(BuyIDNow))
                            boughtcode = choice(redeemcodes)
                            print(Fore.WHITE + Back.MAGENTA + "Your key: " + boughtcode + ". Use it in redeem")
                            if to_mail != "":
                                send_mail(to_mail, "Success puschare! / Успешная покупка!", "Hello, " + name + "\nYou bought the product '" + product + "' And you got " + product + "\nCost: " + str(cost) + currency + "\nPurchase code: " + str(BuyIDNow) + "\nBalance: " + str(showbalance) + currency + " (" + str(balance) + "$)" + "\nYour code: " + boughtcode)
                                send_html_mail(to_mail,"Успешная покупка!")
                        

            elif pr == "addtobalance":
                try:
                    # -----------------------------
                    # Normalize currency
                    # -----------------------------
                    currency = str(currency or "$").upper().strip()

                    # Enter top-up amount
                    Qatb = float(input("Enter top-up amount (in " + currency + "): ")) 
                    Qatb2 = input("Top-up amount: " + str(Qatb) + currency + ". Continue? Y / N: ")

                    if Qatb2.upper() == "Y":
                        # Pay via BearPay
                        result = bearpay.pay_EN(Qatb, currency)  # True/False

                        if result:
                            # -----------------------------
                            # Mask card only if it exists
                            # -----------------------------
                            if bearpay.last_card_number:
                                masked = mask_card_number(bearpay.last_card_number)
                                payment_method = "Card "
                            else:
                                masked = ""
                                payment_method = "Phone "

                            print("Top-up successful: " + str(Qatb) + currency)

                            # Calculate new balance
                            newbalance = Qatb / setcurrencyrate(currency)
                            balance = balance + newbalance
                            showbalance = balance * setcurrencyrate(currency)

                            BuyIDNow = uuid.uuid4()

                            # Send email if needed
                            if to_mail != "":
                                send_mail(
                                    to_mail,
                                    "Top-up Successful!",
                                    "Hello " + name +
                                    "\nYou have topped up your balance." +
                                    "\nPurchase ID: " + str(BuyIDNow) +
                                    "\nNew balance: " + str(showbalance) + currency + " (" + str(balance) + "$)" +
                                    "\nPayment method: " + payment_method + masked
                                )
                        else:
                            print("Payment failed. Invalid card or insufficient funds.")

                except Exception as ex:
                    print("An error has occurred: " + str(ex))
            

            elif pr == "settings":
                print("Настройки ⚙️")
                print("Изменить валюту - currency ($ / GBP / RUB / HRY)")
                print("Сменить пароль - changepassword")
                Qdosettings = input("Действие: ")
                if Qdosettings == "currency":
                    Qnewcurrency = input("Валюта: ")
                    currency = Qnewcurrency
                    print("Успешно!")
                if Qdosettings == "changepassword":
                    newpass = input("Новый пароль: ")
                    newpassconfirm = input("Подтвердите новый пароль: ")
                    if newpass == newpassconfirm:
                        if newpass != "":
                            passset = newpass
                            data["pass"] = passset
                            writepass(data, 'data.json')

                            print("Успешно! Новый пароль: " + (data["pass"]))
                        else:
                            print("Пароль не должен быть пустым!")
                    else:
                        print("Пароли не совпадают")        

                else:
                    print(Fore.RED + "неизвестное действие: " + Qdosettings + " <-")
                    print(Back.YELLOW + Fore.BLACK + "")


            elif pr == "suspendtest":
                if makeSuspend("Это тест") == 1:
                    print(Fore.WHITE + Back.GREEN  + "Ваш аккаунт был разблокирован!")
                else:
                    MakeBan()
                    pt.alert("Вы были забанены!", systemName)
                    isbanned = True

                    #data4["ban"] = isbanned

                    #writepass(data4, 'ban.json')
                    sys.exit()



            
            else:
                print(Fore.RED + "unknown program: " + pr + " <-")
                pygame.mixer.music.load("error.mp3")
                pygame.mixer.music.play()
            doexit = input(Back.YELLOW + Fore.RED + "Quit? Y / N: ")
            if doexit == "Y":
                print(Back.YELLOW + Fore.RED + "Wait.....")
            elif doexit == "":
                print(Back.YELLOW + Fore.RED + "Wait.....")

#^----------------------------^#
#--------Code ends here--------#




#--------LICENSE--------#

#-English-#

#Copyright © 2023-2025 MikhailTheBear. All rights reserved.
#Please do not delete this lines.
#deleting or changing this lines is a violation of the license agreement.
#this project made with fun and love <3

# - MikhailTheBear Love from Russia! -

#-Russian-#

#copyright © 2023-2025 MikhailTheBear. Все права защищены.
#Пожалуйста, не удаляйте эти строки.
#Удаление или изменение этих строк является нарушением лицензионного соглашения.
#Этот проект сделан с удовольствием и любовью <3

# - MikhailTheBear с любовью из России! -



#--------END LICENSE--------#



#--------LINKS/ССЫЛКИ--------#

#YT: https://www.youtube.com/channel/UC8m8HuhyXGER_I98OxyExvA - (Videos in Russian Language)

#GitHub: https://github.com/MikhailTheBear

#Minecraft Server Site: https://tailsbear.ru - (For Russian Users)
