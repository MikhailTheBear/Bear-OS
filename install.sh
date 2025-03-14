#!/bin/bash
echo "██████╗░███████╗░█████╗░██████╗░░░░░░░░█████╗░░██████╗"
echo "██╔══██╗██╔════╝██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔════╝"
echo "██████╦╝█████╗░░███████║██████╔╝█████╗██║░░██║╚█████╗░"
echo "██╔══██╗██╔══╝░░██╔══██║██╔══██╗╚════╝██║░░██║░╚═══██╗"
echo "██████╦╝███████╗██║░░██║██║░░██║░░░░░░╚█████╔╝██████╔╝"
echo "╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░"

echo ""

echo "Welcome to Bear-OS installer!"


echo "Do you want install Bear-OS? (y/n)"
read answer

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    echo "Downloading Bear-OS..."
    git clone --branch master --single-branch https://github.com/MikhailTheBear/Bear-OS.git
    cd Bear-OS
    echo "The project is installed, press Enter to install the necessary py-libraries..."
    read answer
    pip install pygame colorama uuid nextcord twilio tk pyautogui
    echo "Done! Enjoy :)"
    echo "Press Enter to exit..."
    read answer
    echo "Goodbye!"
else
    echo "Canceled!"
    exit 1
fi

