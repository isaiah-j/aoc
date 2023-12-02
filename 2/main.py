totalRed = 12
totalGreen = 13
totalBlue = 14


# String -> {red: Natural, green: Natural, blue: Natural}
# count the number of red, green and blue dice in a single game

def get_count(game):
    count = {"red": 0, "green": 0, "blue": 0}

    game_array = game.split(' ')

    for i, el in enumerate(game_array):
        if 'red' in el:
            count['red'] += int(game_array[i - 1])

        if 'green' in el:
            count['green'] += int(game_array[i - 1])

        if 'blue' in el:
            count['blue'] += int(game_array[i - 1])

    return count

assert get_count('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == {"red": 5, "green": 4, "blue": 9}


# String  -> Boolean
# produce true if a game is playable (red, green and blue dice do not surpass their total count)
def is_playable(game):
    count = get_count(game)

    return count['red'] <= totalRed and count['green'] <= totalGreen and count['blue'] <= totalBlue


assert is_playable('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') is True
assert is_playable('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') is True
assert is_playable('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') is False
assert is_playable('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red') is False
assert is_playable('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green') is True


# String -> Natural
# return the id of the game
def get_game_id(game):
    id = game.split(' ')[1].split(':')[0]

    return int(id)


assert get_game_id('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == 1
assert get_game_id('Game 50: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == 50
assert get_game_id('Game 100: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == 100


# Natural Natural Natural -> Natural
# add the ids of the games that can be played given the red, green and blue dice count

def sum_playable_games(filePath):
    total = 0

    with open(filePath, 'r') as games:
        # Read the file line by line
        for game in games:

            if is_playable(game):
                total += get_game_id(game)

    return total


assert sum_playable_games('test_data.txt') == 8

if __name__ == '__main__':
    print(sum_playable_games('data.txt'))
