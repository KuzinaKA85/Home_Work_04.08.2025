from masks import get_mask_account, get_mask_card_number

user_input_string = input("Введите номер карты или счета")


def mask_account_card(user_input_string: str) -> str:
    """Функция обрабатывает строку, содержащую тип и номер карты или счета"""
    parts = user_input_string.split(" ")  # Разделяем строку по пробелам
    parts_type = None
    if len(parts) == 2:
        parts_type = " ".join(parts[:1])
    elif len(parts) > 2:
        parts_type = " ".join(parts[:2])
    part_digit = ""
    mask_number = None
    for i in parts:
        if i.isdigit():
            part_digit += i
    if len(part_digit) == 16:
        mask_number = get_mask_card_number(part_digit)
    if len(part_digit) == 20:
        mask_number = get_mask_account(part_digit)
    mask_input_string = parts_type + " " + mask_number
    return mask_input_string


print(mask_account_card(user_input_string))
