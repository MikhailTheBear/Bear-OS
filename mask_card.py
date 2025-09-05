def mask_card_number(card_number: str) -> str:
    """Преобразует номер карты в формат **** **** **** 1234"""
    parts = card_number.strip().split()
    if len(parts) != 4:
        return "Invalid card format"

    return "**** **** **** " + parts[3]


# Пример использования:
if __name__ == "__main__":
    full_card = "1234 5678 9012 3456"
    masked = mask_card_number(full_card)
    print("Masked card:", masked)  # 👉 **** **** **** 3456