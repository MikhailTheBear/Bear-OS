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
echo "Welcome to Bear-OS installer!"
echo ""
echo -e "${RED}Attention! ${YELLOW}The project currently only has Russian language, the author will try to add English in version ${GREEN}1.9.${NC}"

echo "Do you want to install Bear-OS? (y/N)"
read -r answer

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    echo -e "${YELLOW}Downloading Bear-OS...${NC}"
    git clone --branch master --single-branch https://github.com/MikhailTheBear/Bear-OS.git
    cd Bear-OS || exit

    echo -e "${YELLOW}The project is installed, installing the necessary py-libraries...${NC}"
    

    echo -e "${YELLOW}Do you use pip3? (y/N), if not then just pip${NC}"
    read -r answer

    if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
        pip3 install pygame colorama uuid nextcord twilio tk pyautogui flask
    else
        pip install pygame colorama uuid nextcord twilio tk pyautogui flask
    fi

    # Настройка config.py
    cat <<EOL >> config.py
from_email = 'youremail@example.com'
password = 'your password'
phone_account_sid = 'your account_sid'
phone_auth_token = 'your auth_token'
my_phone_number = 'your phone_number'
EOL

    echo "Please, setup SMTP [ok]"
    read -r
    nano config.py

    echo -e "${GREEN}Done! Enjoy :)${NC}"
    echo "Press Enter to start..."
    read -r

    python3 bearOS.py

    echo "Press Enter to exit..."
    read -r
    echo "Goodbye!"

else
    echo -e "${RED}Canceled!${NC}"
    exit 1
fi
