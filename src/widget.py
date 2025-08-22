from masks import get_mask_account, get_mask_card_number


def mask_account_card(string_input: str) -> str:
    """Функция обрабатывает строку, содержащую тип и номер карты или счета"""
    parts = string_input.split(" ")  # Разделяем строку по пробелам
    parts_type = ""
    if len(parts) == 2:
        parts_type = " ".join(parts[:1])
    elif len(parts) > 2:
        parts_type = " ".join(parts[:2])
    part_digit = ""
    mask_number = 0
    for i in parts:
        if i.isdigit():
            part_digit += i
    if len(part_digit) == 16:
        mask_number = get_mask_card_number(part_digit)
    if len(part_digit) == 20:
        mask_number = get_mask_account(part_digit)
    mask_input_string = str(parts_type) + " " + str(mask_number)
    return mask_input_string


def get_date(user_input: str) -> str:
    """Функция преобразует дату в формат ДД.ММ.ГГГГ"""
    day = user_input[8:10]
    month = user_input[5:7]
    year = user_input[0:4]
    return day + "." + month + "." + year


# Функция проверки работы кода
if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
