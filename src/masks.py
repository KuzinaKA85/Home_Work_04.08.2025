number_card = int(input("Введите номер карты"))


def get_mask_card_number(number_card: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    number_card_str = str(number_card)
    form_str_1 = number_card_str[:6]
    form_str_2 = "******"
    form_str_3 = number_card_str[12:]
    total_form_str = form_str_1 + form_str_2 + form_str_3
    new_str = [total_form_str[i:i+4] for i in range(0, len(total_form_str), 4)]
    return " ".join(new_str)


print(get_mask_card_number(number_card))


mask_account = int(input("Введите номер счета"))


def get_mask_account(mask_account: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    mask_account_str = str(mask_account)
    formated_account_str_2 = "**"
    formated_account_str_3 = mask_account_str[-4:]
    return formated_account_str_2 + formated_account_str_3


print(get_mask_account(mask_account))
