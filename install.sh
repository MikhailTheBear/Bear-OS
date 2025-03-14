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
    echo "Done!"

else
    echo "Canceled!"
    exit 1
fi

