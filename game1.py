EMPTY_CEIL = 1
def init_field(size: int=3, ) -> list:
    empty_ceil = '-'
    return  [
        [EMPTY_CEIL for _ in range(size)]
        for _ in range(size)
    ]


def is_empty_ceil(field: list, x: int, y: int) -> bool:
    # current_ceil = field[x][y]
    # if current_ceil == EMPTY_CEIL:
    #     return True
    # else:
    #     return False
    return True if current_ceil == EMPTY_CEIL else False

def player_step(x: int, y: int, symbol: str, field: list):
    # field_copy = field.copy()
    field[x][y] = symbol


def enemy_step(x: int, y: int, symbol: str, field: list):
    player_step(x, y, symbol, field)

def is_win(field) -> bool:
    win_combination =



if __name__ == '__main__':
    main_field = init_field()
