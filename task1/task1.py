# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'текстабв дляабв проверкиабв заданияабв одинабв'

words = text.split(' ')


newtext = []
for word in words:
    if not 'абв' in word:
        newtext.append(word)

answer = " ".join(word)
print(newtext)
