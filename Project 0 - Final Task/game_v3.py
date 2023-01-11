"Game Guess a Number V3: Computer generates number and guesses itself"
"Additional task - find solution to generate min number of guesses (<20)"

import numpy as np

def random_predict (number: int = np.random.randint(1, 101)) -> int:
    """Random guessing of prediction number

    Args:
        number (int, optional): number to be guessed. Defaults to 1.

    Returns:
        int: amount of guesses
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        while count < 20:
            count += 1
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 1
        break
    return count
    


def score_game(random_predict) -> int:
    """Average amount from 1000 tries our algo guessess the number

    Args:
        random_predict (_type_): main function 

    Returns:
        int: average amount of tries
    """
    count_ls = [] # list where we store tries
    #np.random.seed(1) # seed fix
    random_array = np.random.randint(1,101, size = (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score= int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return (score)

#RUN
score_game(random_predict)