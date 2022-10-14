#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""


from random import *
import os

#приветсвие
weltext = ('ПРИВЕТСТВУЮ ИГРОКИ!, Добро пожаловать в игру КОНФЕТКИ!\n'
                'ДИСКЛЭЙМЕР! \n'
                'Не рекомендуется лицам с сахарным диабетом')
print(weltext)

message = ['твоя очередь', 'твой шанс', 'бери больше', 'ну же\n',
           'бери быстрее', 'ты справишься','прощяй диета']
winmessage =['мои поздваления', 'ты настоящий мастер игры','не проигравший сегодня\n'
              ,'да здравтвует диабет\n'
              ,'мог проиграть но выиграл','ты честно выиграл эту игру',]
import random

random_index = random.randrange(len(winmessage))
#имена играков
def player_vs_player():
    candies_total = 10
    max_take = 28
    count = 0
    player_1 = input('Имя первого игрока: ')
    player_2 = input('Имя второго игрока: ')

    #определяем кто ходит первым

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю {lucky} ты ходишь первым !')
#ход игры
    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет {lucky}, играй по правилам: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось {candies_total} конфет ')
            count = 1
        else:
            print('КОНЕЦ ИГРЫ!')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nМожно взять только {max_take} конфет {loser}, играй по правилам: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось {candies_total} конфет ')
            count = 0
        else:
            print('КОНЕЦ ИГРЫ!')
#победитель
    if count == 1:
        print(winmessage[random_index])
        print(f'ПОБЕДИТЕЛЬ {loser}' )
    if count == 0:
        print(winmessage[random_index])
        print(f'ПОБЕДИТЕЛЬ {lucky} ')

player_vs_player()







def player_vs_bot():
    candies_total = 10
    max_take = 28
    count = 0
    player_1 = input('Имя первого игрока: ')
    player_2 = 'Bot'
    players =[player_1,player_2]

    #определяем кто ходит первым

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    #print(f'Поздравляю {lucky} ты ходишь первым !')
    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nХод,  {players[lucky%2]} \n {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(
                    f'\nМожно взять только {max_take} конфет {loser}, играй по правилам: '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

player_vs_bot()


