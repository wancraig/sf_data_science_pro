"Game Guess a Number V2: Computer generates number and guesses it itself"

import numpy as np

def random_predict (number:int = np.random.randint(1,101)) -> int:
    """Random guessing of prediction number

    Args:
        number (int, optional): number to be guessed. Defaults to 1.

    Returns:
        int: amount of guesses
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101) # generated number
        if number == predict_number:
            break # function exit if guessed right
    return(count)
    


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для хранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size = (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score= int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return (score)


if __name__ == "__main__":
#RUN
score_game(random_predict)