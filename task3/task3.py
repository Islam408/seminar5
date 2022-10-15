# Создайте программу для игры в ""Крестики-нолики"".
# Это было сложно
from itertools import count


print('*'*100)
print('XO'*5, 'КРЕСТИКИ НОЛИКИ!', 'XO'*5)
print('Добро пожаловать игроки!')


field = list(range(1,10))

def init_field(field):
    print('-' * 13)
    for i in range(3):
        print('|', field[0+i*3],'|', field[1+i*3],'|', field[2+i*3], '|')
        print('-'*13)

def take_input(player_token):
    valid = False
    while not valid:
        player_input = input("Куда поставим " + player_token+"? ")
        try:
            player_input = int(player_input)
        except:
            print ("Некорректный ввод. Введите число")
            continue
        if player_input >= 1 and player_input <= 9:
            if (str(field[player_input-1]) not in "XO"):
                field[player_input-1] = player_token
                valid = True
            else:
                print ("Занятая клетка")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
def chek_win(field):
    vektor = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for each in vektor:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False

def mein(fiald):
    count = 0
    win = False
    while not win:
        init_field(field)
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        count += 1

        if count > 4:
            temp  = chek_win(field)
            if temp:
                print(temp, 'Победитель')
                win = True
                break
            if count == 9:
                print("ничья")
                break
    init_field(field)
mein(field)

    







    


