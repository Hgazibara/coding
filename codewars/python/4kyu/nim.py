def choose_move(game_state):
    X = nim_sum(game_state)

    for index, heap_size in enumerate(game_state):
        x = nim_sum([heap_size, X])
        if x < heap_size:
            return index, heap_size - x


def nim_sum(numbers):
    return reduce(lambda x,y: x^y, numbers)
