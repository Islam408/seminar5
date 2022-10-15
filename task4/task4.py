# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('textforRLE.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст который нужно сжать: '))
with open('textforRLE.txt', 'r') as file:
    mytext = file.readline()
    text_compression = mytext.split()

print(mytext)

def rle_encode(text):
    encod = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                encod += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encod += str(count) + prev_char
        return encod


text_compression = rle_encode(mytext)

with open('textcompressRLE.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)




