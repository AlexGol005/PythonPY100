from game1 import (init_field, set_ceil, is_win,
is_win, player_step, enemy_step, is_avalible_ceil
)

def main():
    field = init_field()
    print_field(field)

    first_player, second_player = 'X', '0'

    is_wined = False
    while  not is_wined:
        x, y  = get_step(first_player)
        set_ceil(field, x, y, first_player)
        print_field(field)

        if is_win(field, first_player):
            print(f"Победил игрок {first_player}")
            break


        if not is_avalible_ceil:
            print('ничья')
            break
    print('конец игры')

    x, y = get_step(second_player)
    enemy_step(x, y, second_player, field)
    print_field(field)



def get_step(player_symbol: str) -> tuple[int, int]:
    while True:
        step = input(f"Игрок {player_symbol} "
                     f"введите 2 координаты через пробел: ")

        coords = step.split()
        if len(coords) > 2:
            print("введено слишком много координат")
        if len(coords) < 2:
            print("введено слишком мало координат")
            continue

        x_str: str
        y_str: str
        x, y = coords

        if not x_str.isdigit():
            print('координата x не число')
        if not y_str.isdigit():
            print('координата y не число')
            continue
        x, y = int(x_str), int(y_str)
        if not 0 < x < 3 + 1:
            print('неверная икс')
            continue
        if not 0 < y < 3 + 1:
            print('неверная икс')
            continue



def print_field(field) -> None:
    for row in field:
        for ceil in row:
            print(ceil, end="")
        print()

if __name__ == '__main__':
    main()