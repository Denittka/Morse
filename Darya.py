def decode_from_morse(code):
    new_MorseCode = {}
    for codes, letters in MorseCode.items():
        new_MorseCode[letters] = codes
    # меняем местами ключи и значения(разворачиваем словарь)
    code = code.split()  # создаем список закодированных символов
    spisok = []  # пустой список для расшифрованных символов
    for symb in code:  # перебираем зашифрованные символы
        if symb in new_MorseCode:
            spisok.append(new_MorseCode[symb]) # декодируем
    return spisok