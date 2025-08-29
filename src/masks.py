def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(number_card) == 16:
        form_str_1 = number_card[:6]
        form_str_2 = "******"
        form_str_3 = number_card[12:]
        total_form_str = form_str_1 + form_str_2 + form_str_3
        new_str = [total_form_str[i:i + 4] for i in range(0, len(total_form_str), 4)]
        return " ".join(new_str)
    elif len(number_card) != 16:
        raise ValueError("Неправильная длина номера карты")
    else:
        return "Номер карты не введен"


def get_mask_account(mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(mask_account) == 20:
        formated_account_str_2 = "**"
        formated_account_str_3 = mask_account[-4:]
        return formated_account_str_2 + formated_account_str_3
    elif len(mask_account) != 20:
        raise ValueError("Неправильная длина номера счета")
    else:
        return "Некорректный ввод номера счета"


# Функция проверки работы кода
if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
