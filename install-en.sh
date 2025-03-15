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

echo "Do you want install Bear-OS? (y/n)"
read answer

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    echo -e "${YELLOW}Downloading Bear-OS...${NC}"
    git clone --branch master --single-branch https://github.com/MikhailTheBear/Bear-OS.git
    cd Bear-OS
    echo -e "${YELLOW}The project is installed, press Enter to install the necessary py-libraries...${NC}"
    read answer
    pip install pygame colorama uuid nextcord twilio tk pyautogui
    echo -e "${GREEN}Done! Enjoy :)${NC}"
    echo "Press Enter to exit..."
    read answer
    echo "Goodbye!"
else
    echo -e "${RED}Canceled!${NC}"
    exit 1
fi

