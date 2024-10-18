
def a(sentence): # функция
    glasnie = "ауоиэыяюеёАУОИЭЫЯЮЕЁ"  # список гласных букв
    b = 0  # счетчик гласных
    for char in sentence: # проходит по каждому символу
        if char in glasnie: # если есть гласная, то увеливает b
            b += 1
    return b

user_input = input("Введите строку: ") # ввод
print("Количество гласных букв:", a(user_input)) # вывод