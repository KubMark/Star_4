# Каждый четвертый символ в строке содержит сообщение Задание 3

message = "Рооз наа фмдиц а ывч ыва оо ивкр ьке пвшпрце уенпвта"
# mess = message.split(' ')

print(''.join([message[i] for i in range(3, len(message), 4)]))