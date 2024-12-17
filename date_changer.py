from datetime import datetime as dt
created_date = '17-12-2024'
issue_date = '19-12-2024'
temp_created_date = dt.strptime(created_date, '%d-%m-%Y') # создание архива основной даты
temp_issue_date = dt.strptime(issue_date, '%d-%m-%Y') # создание архива даты дедлайна
created_date = temp_created_date.strftime('%d-%m')
issue_date=temp_issue_date.strftime('%d-%m')
print (created_date)
print (issue_date)




