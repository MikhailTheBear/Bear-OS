#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo "██████╗░███████╗░█████╗░██████╗░░░░░░░░█████╗░░██████╗"
echo "██╔══██╗██╔════╝██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔════╝"
echo "██████╦╝█████╗░░███████║██████╔╝█████╗██║░░██║╚█████╗░"
echo "██╔══██╗██╔══╝░░██╔══██║██╔══██╗╚════╝██║░░██║░╚═══██╗"
echo "██████╦╝███████╗██║░░██║██║░░██║░░░░░░╚█████╔╝██████╔╝"
echo "╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░"

echo ""

echo "Добро пожаловать в установщик Bear-OS!"
echo ""

echo "Хотите установить Bear-OS? (y/n)"
read answer

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    echo -e "${YELLOW}Загрузка Bear-OS...${NC}"
    git clone --branch master --single-branch https://github.com/MikhailTheBear/Bear-OS.git
    cd Bear-OS
    echo -e "${YELLOW}Проект установлен, нажмите Enter для установки необходимых py-библиотек...${NC}"
    read answer
    pip install pygame colorama uuid nextcord twilio tk pyautogui
    echo -e "${GREEN}Готово! Наслаждайтесь :)${NC}"
    echo "Нажмите Enter, чтобы запустить..."
    read answer
    echo "from_email = 'youremail@example.com' " >> config.py
    echo "password = 'your password' " >> config.py
    echo "phone_account_sid = 'your account_sid' " >> config.py
    echo "phone_auth_token = 'your auth_token' " >> config.py
    echo "my_phone_number = 'your phone_number' " >> config.py
    echo "Пожалуйста, настройте SMTP [ok]"
    read answer
    nano config.py
    python3 MSDOS.py
    echo "Нажмите Enter, чтобы выйти..."
    read answer
    echo "Пока!"
else
    echo -e "${RED}Отменено!${NC}"
    exit 1
fi
