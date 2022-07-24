#               Задание 5
free_mailbox = ['yandex.ru', 'mail.ru', 'gmail.com', 'yahoo.com', 'rambler.ru']
user_mail = input('Вводим почту ')

user_mailbox = user_mail.split('@')[1]

if '@' not in user_mail and '.' not in user_mailbox:
    print('Это вообще не почта ')
elif user_mailbox in free_mailbox:
    print('Это почта, она на бесплатном домене')
else:
    print('Это почта, она на корпоратином домене')

