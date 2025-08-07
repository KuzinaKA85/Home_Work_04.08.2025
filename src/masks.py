number_card = input("Введите номер карты")
count_symbol = 16
while len(number_card) != count_symbol:
    number_card = input("Ввод некорректный. Повторите ввод")
    if len(number_card) == count_symbol:
        break


def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    form_str_1 = number_card[:6]
    form_str_2 = "******"
    form_str_3 = number_card[12:]
    total_form_str = form_str_1 + form_str_2 + form_str_3
    new_str = [total_form_str[i:i + 4] for i in range(0, len(total_form_str), 4)]
    return " ".join(new_str)


print(get_mask_card_number(number_card))

mask_account = input("Введите номер счета")
count_mask = 20

while len(mask_account) != count_mask:
    mask_account = input("Ввод некорректный. Повторите ввод")
    if len(mask_account) == count_mask:
        break


def get_mask_account(mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    formated_account_str_2 = "**"
    formated_account_str_3 = mask_account[-4:]
    return formated_account_str_2 + formated_account_str_3


print(get_mask_account(mask_account))
