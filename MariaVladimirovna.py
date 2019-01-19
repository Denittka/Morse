def encode_to_morse(text):
    # переводим в верхний регистр и разбиваем текст по символам пустого пространства
    text = text.upper().split()
    code_morse = []  # пустой список закодированных слов
    for word in text:  # перебираем слова исходноо текста
        string = ''  # каждое слово кодируем отдельно
        for char in word:  # перебираем символы слова
            if char in MorseCode:
                string += MorseCode[char]  # кодируем
        code_morse.append(string)  # добавляем закодированное слово в список
    return code_morse  # или ' '.join(code_morse)
