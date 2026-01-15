#!/bin/bash

# Список библиотек
LIBS="pygame colorama uuid nextcord twilio tk pyautogui flask"

# Определяем pip
if command -v pip3 &> /dev/null; then
    PIP="pip3"
elif command -v pip &> /dev/null; then
    PIP="pip"
else
    echo "Ошибка: pip не найден! | Error: pip not found!"
    exit 1
fi

echo "Используется: | Is used: $($PIP --version)"
echo "Установка библиотек... | Installing libraries..."

# Установка всех библиотек одной командой
$PIP install $LIBS

if [ $? -eq 0 ]; then
    echo "Установка завершена успешно! | The installation has been completed successfully!"
else
    echo "Во время установки возникли ошибки | Errors occurred during installation"
    exit 1
fi
