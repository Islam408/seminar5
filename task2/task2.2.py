# a) Добавьте игру против бота

from random import *


#приветсвие
weltext = ('ПРИВЕТСТВУЮ ИГРОКИ!, Добро пожаловать в игру КОНФЕТКИ!'
                'ДИСКЛЭЙМЕР! '
                'Не рекомендуется лицам с сахарным диабетом')
print(weltext)

message = ['твоя очередь', 'твой шанс', 'бери больше', 'ну же',
           'бери быстрее', 'ты справишься','прощяй диета']
winmessage =['мои поздваления', 'ты настоящий мастер игры','не проигравший сегодня'
              ,'да здравтвует диабет'
              ,'мог проиграть но выиграл','ты честно выиграл эту игру',]
import random

random_index = random.randrange(len(winmessage))


def player_vs_bot():
    candies_total = 100
    max_take = 28
    
    player1 = input('Имя игрока: ')
    player2 = 'Bot'
    players = [player1,player2]

    
    x = randint(1,2)
    
    if x == 1:
        lucky = player1
        loser = player2
    else:
        lucky = player2
        loser = player1
    print(f'Поздравляю {lucky} ты ходишь первым !')
    lucky = randint(1, 2)
# ход игры
    while candies_total > 0:
        lucky += 1
        if players[lucky % 2]== 'Bot':
            print(f'\n Ходит {players[lucky % 2]} \n Осталось {candies_total}.конфет. {choice(message)}: ')

            if candies_total > 0:
                step = candies_total
            
            while step > max_take:
                step = randint(1,28)
            print(step)

        else:
            step = int(input(f'\nХодит,  {players[lucky%2]} \n Осталось {candies_total} конфет. {choice(message)}: '))
            while step > max_take or step > candies_total:
                step = int (input(f'\nМожно взять только {max_take} конфет {loser}, играй по правилам: '))
        candies_total = candies_total - step

    print(f'Осталось {candies_total} конфет.')
    print(f'{winmessage[random_index]} Победитель {players[lucky%2]} ')



player_vs_bot()
                