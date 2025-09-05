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
echo -e "${RED}Внимание! ${YELLOW}На данный момент проект доступен только на русском языке, автор постарается добавить английский в версии ${GREEN}1.9.${NC}"

echo "Вы хотите установить Bear-OS? (y/N)"
read -r answer

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    echo -e "${YELLOW}Скачиваем Bear-OS...${NC}"
    git clone --branch master --single-branch https://github.com/MikhailTheBear/Bear-OS.git
    cd Bear-OS || exit

    echo -e "${YELLOW}Проект установлен, нажмите Enter для установки необходимых библиотек Python...${NC}"
    read -r

    echo -e "${YELLOW}Вы используете pip3? (y/N), если нет — будет использоваться pip${NC}"
    read -r answer

    if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
        pip3 install pygame colorama uuid nextcord twilio tk pyautogui
    else
        pip install pygame colorama uuid nextcord twilio tk pyautogui
    fi

    echo -e "${GREEN}Готово! Наслаждайтесь :)${NC}"
    echo "Нажмите Enter для продолжения..."
    read -r

    # Настройка config.py
    cat <<EOL >> config.py
from_email = 'youremail@example.com'
password = 'your password'
phone_account_sid = 'your account_sid'
phone_auth_token = 'your auth_token'
my_phone_number = 'your phone_number'
EOL

    echo "Пожалуйста, настройте SMTP [ok]"
    read -r
    nano config.py

    python3 bearOS.py

    echo "Нажмите Enter для выхода..."
    read -r
    echo "До свидания!"

else
    echo -e "${RED}Отменено!${NC}"
    exit 1
fi
