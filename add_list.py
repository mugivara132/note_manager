name = input ("Введите ваше имя: ")
title1 = input( "Заголовок 1: ")
title2 = input( "Заголовок 2: ")
title3 = input( "Заголовок 3: ")
titles = [title1, title2, title3]
content = input ('Описание заметки: ')
status = input ('Какой статус заметки? - ')
created_date = input ("Дата создания заметки в формате 20-12-2024: ")
issue_date = input ("Дата дедлайна в формате 20-12-2024:" )
temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]
print ( 'Имя пользователя:', name)
print ( 'Заголовки:' , titles )
print ( 'Описание заметки: ', content)
print ( 'Статус заметки: ', status)
print ( 'Дата создания: ', temp_created_date)
print ( 'Дата дедлайна:', temp_issue_date)
