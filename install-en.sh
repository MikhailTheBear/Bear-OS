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

echo "Do you want install Bear-OS? (y/N)"
read answer

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    echo -e "${YELLOW}Downloading Bear-OS...${NC}"
    git clone --branch master --single-branch https://github.com/MikhailTheBear/Bear-OS.git
    cd Bear-OS
    echo -e "${YELLOW}The project is installed, press Enter to install the necessary py-libraries...${NC}"
    read answer
    echo -e "${YELLOW}Do you use pip3? (y/N), if not then just pip${NC}"
    read answer
    if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
        pip3 install pygame colorama uuid nextcord twilio tk pyautogui
    else
        pip install pygame colorama uuid nextcord twilio tk pyautogui
    echo -e "${GREEN}Done! Enjoy :)${NC}"
    echo "Press Enter to start..."
    read answer
    echo "from_email = 'youremail@example.com' " >> config.py
    echo "password = 'your password' " >> config.py
    echo "phone_account_sid = 'your account_sid' " >> config.py
    echo "phone_auth_token = 'your auth_token' " >> config.py
    echo "my_phone_number = 'your phone_number' " >> config.py
    echo "Please, setup SMTP [ok]"
    read answer
    nano config.py
    python3 MSDOS.py
    echo "Press Enter to exit..."
    read answer
    echo "Goodbye!"
else
    echo -e "${RED}Canceled!${NC}"
    exit 1
fi

