# при помощи команды input добавляем возможность вносить информацию
name = input("Введите ваше имя: ")
title = input("Введите заголовок заметки: ")
content = input('Описание заметки: ')
status = input('Какой статус заметки? - ')
created_date = input("Дата создания заметки в формате 20-12-2024: ")
issue_date = input("Дата дедлайна в формате 20-12-2024:" )
temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

print('Имя пользователя:', name)
print( 'Заголовок:' , title)
print( 'Описание заметки: ', content)
print( 'Статус заметки: ', status)
print( 'Дата создания: ', temp_created_date)
print('Дата дедлайна:', temp_issue_date)
