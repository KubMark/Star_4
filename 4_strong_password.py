#               Задание 2

login = input()
password = input()
is_digit_in_password = False

for num in password:
    if num.isdigit():
        is_digit_in_password = True

    if len(login) > 3 and len(password) > 8 and is_digit_in_password:
        print('Это хорошие пароль и логин!')
        break
    else:
        if len(password) < 8:
            print("Пароль должен содержать больше 8 символов.")
        if len(login) < 3:
            print('Логин должен содержать больше 3 символов.')

        if not is_digit_in_password:
            print("Пароль должен содержать хотя бы одну цифру.")
            break