note = {"Имя пользователя: ": input ("Введите ваше имя:"),
        "Описание заметки: ": input ("Введите описание заметки: "),
         "Дата создания:":input ("Введите дату создания заметки в формате день-месяц-год: "),
         "Дата дедлайна: ":input ("Введите дату дедлайна в формате день-месяц-год: "),
        "Заголовки: ": [] }
for i in range(3):
    titles = input(f'Введите заголовки: {i + 1}: ')
    note["Заголовки: "].append(titles)
print('\nИнформация по заметке')
for key, value in note.items():
    print(f'{key.capitalize()}: {value }')


