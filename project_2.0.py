import random
import time
import os
import os.path

scoresDict = {}

# clears the screen after 5 seconds
def fiveSecond_timer():
    print("\nMemorize the characters in ", end="")
    counter = "54321"
    for num in counter:
        print(f"{num}...", end=" ",flush=True) # https://stackoverflow.com/questions/56896710/does-time-sleep-not-work-inside-a-for-loop-with-a-print-function-using-the
        time.sleep(0.5)
    os.system("cls")

# prints random characters on screen and stores the character to a list
def print_random_char(character_count, list_of_chars):
    pattern = []
    for j in range(character_count):
        randomChar = random.choice(list_of_chars)
        print(randomChar, end=" ")
        pattern.append(randomChar)
    return pattern

# stores each character on a string to a list
def store_chars_to_list(string):
    charList= []
    for char in string:
        if not char == " ":
            charList.append(char)
    return charList

# takes all elements of a list and turns it into a string
def list_to_string(list):
    pattern_as_string = ""
    for char in list:
        pattern_as_string += char
        pattern_as_string += ' '
    return pattern_as_string

# assigns rank to a user and saves their score to the dictionary
def save_score(score,lastpattern):
    user_name = input("Enter your name: ")
    if user_name in scoresDict:
        while True:
            update_prompt = input("Do you want to update your high score (y/n): ")
            if update_prompt == 'y':
                break
            elif update_prompt == 'n':
                viewScores()
                exit()

    scoresDict[user_name] = {
    'score': score,
    'last_pattern': lastpattern,
    'rank': 0
    }

    # assign user's rank
    if len(scoresDict) == 1:
        scoresDict[user_name]['rank'] = 1
    else:
        score_list = []

        # populate score list
        for player in scoresDict:
            if not scoresDict[player]['score'] in score_list:
                score_list.append(scoresDict[player]['score'])

        # assign rank to each score
        # https://scipython.com/book/chapter-2-the-core-python-language-i/questions/ranking-a-list/
        score_list.sort(reverse=True)
        ranks = []
        for player_score in score_list:
            ranks.append(score_list.index(player_score) + 1)

        # assigns rank to each player via the rank of their score
        for k in range(len(score_list)):
            for user in scoresDict:
                if scoresDict[user]['score'] == score_list[k]:
                    scoresDict[user]['rank'] = ranks[k]


# displays score on screen
def viewScores():
    # https://stackoverflow.com/questions/9989334/create-nice-column-output-in-python
    if len(scoresDict) > 0:
        table_data = [
            ['Rank','Name','Score','Last Pattern']
        ]

        # check max rank in the scores dictionary
        rank_list = []
        for i in scoresDict:
            rank_list.append(int(scoresDict[i]['rank']))
        max_rank = max(rank_list)

        # stores stat of each user in a list, then adds the list to the table data
        for rank in range(1,max_rank + 1):
            for player in scoresDict:

                # stores user rank in order
                if scoresDict[player]['rank'] == rank:
                    user_stat = []
                    user_stat.append(scoresDict[player]['rank'])
                    user_stat.append(player)
                    user_stat.append(scoresDict[player]['score'])
                    user_stat.append(scoresDict[player]['last_pattern'])

                    table_data.append(user_stat)

        # prints scores in a table
        print("High scores:")
        for row in table_data:
            print("{: <20} {: <20} {: <20} {: <20}".format(*row))

    else:
        print("No high scores yet.")


# loads user score from a file
def load_score_from_file():
    if os.path.exists("scores.csv"):
        with open("scores.csv", "r") as scoreFile:
            for row in scoreFile:
                userStat = row[:-1].split(",")
                scoresDict[userStat[0]] = {
                'score': int(userStat[1]),
                'last_pattern': userStat[2],
                'rank': int(userStat[3])
                }


# saves user stats to a file
def save_scores_to_file():
    with open("scores.csv", "w") as scoreFile:
        # name score lastpatt rank
        for player in scoresDict:
            scoreFile.write(f"{player},{scoresDict[player]['score']},{scoresDict[player]['last_pattern']},{scoresDict[player]['rank']}\n")


# game in easy mode
def easy():
    level = 1
    score = 0
    lives = 2
    print("Lives: 2")

    while lives <= 2:
        charCount = level + 2

        alphabet = []
        for i in range(97, 123): # populate the alphabet list
            alphabet.append(chr(i))

        # shows how many lives the user has

        pattern = print_random_char(charCount,alphabet)
        fiveSecond_timer();

        userAnswer = input("\nType the pattern: ")
        user_list = store_chars_to_list(userAnswer)

        # if user's answer is correct
        if user_list == pattern:
            print("Correct!")

            # updates user score and level
            score += level*10
            level += 1

        # if user has incorrect answer
        else:
            lives -= 1
            # if user has no more life left
            if lives < 0:
                # converts the contents of the printed pattern list to string
                pattern_as_string = list_to_string(pattern)

                print(f"Game over. Final score: {score}")
                save_score(score,pattern_as_string)
                save_scores_to_file()
                viewScores()
                menu()
            print("Incorrect.")
            print(f"Lives: {lives}")


def medium():
    level = 1
    score = 0

    lives = 2
    print("Lives: 2")

    while True:
        charCount = level + 4

        alphaNum = ['0','1','2','3','4','5','6','7','8','9']

        # stores alphabet letters to the list
        for i in range(97, 123): # populate the alphabet list
            alphaNum.append(chr(i))

        pattern = print_random_char(charCount,alphaNum)
        fiveSecond_timer()

        userAnswer = input("\nType the pattern: ")
        user_list = store_chars_to_list(userAnswer)

        # if user's answer is correct
        if user_list == pattern:
            print("Correct!")

            # updates user score and level
            score += level*20
            level += 1

        # if user has incorrect answer
        else:
            lives -= 1
            # if user has no more life left; game over
            if lives < 0:
                # converts the contents of the printed pattern list to string
                pattern_as_string = list_to_string(pattern)

                print(f"Game over. Final score: {score}")
                save_score(score,pattern_as_string)
                save_scores_to_file()
                viewScores()
                menu()
            print("Incorrect.")
            print(f"Lives: {lives}")


def hard():
    level = 1
    score = 0

    lives = 2
    print("Lives: 2")

    while True:
        charCount = level + 4

        alphaNum_symbols = ['0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','*','&']

        # stores alphabet letters to the list
        for i in range(97, 123): # populate the alphabet list
            alphaNum_symbols.append(chr(i))

        pattern = print_random_char(charCount,alphaNum_symbols)
        fiveSecond_timer()

        userAnswer = input("\nType the pattern: ")
        user_list = store_chars_to_list(userAnswer)

        # if user's answer is correct
        if user_list == pattern:
            print("Correct!")

            # updates user score and level
            score += level*30
            level += 1


        # if user has incorrect answer
        else:
            lives -= 1

            # if user has no more life left; game over
            if lives < 0:
                # converts the contents of the printed pattern list to string
                pattern_as_string = list_to_string(pattern)

                print(f"Incorrect. Final score: {score}")
                save_score(score,pattern_as_string)
                save_scores_to_file()
                viewScores()
                menu()
            print("Incorrect.")
            print(f"Lives: {lives}")


# displays game difficulties
def play():
    print("""\n[1] Easy
[2] Medium
[3] Hard
        """)
    while True:
        gameMode = int(input("Select game mode (1-3): "))
        if gameMode in range(1,4):
            if gameMode == 1:
                easy()
            elif gameMode == 2:
                medium()
            elif gameMode == 3:
                hard()

def menu():
    while True:
        # displays game menu
        print("\nMenu:")
        print("""[1] Play Game
[2] View Scores
[3] Exit""")
        userInput = int(input("What do you want to do (1-3): "))

        if userInput in range(1,4):
            if userInput == 1:
                play()
            elif userInput == 2:
                viewScores()
            else:
                exit()
        else:
            print("Program only accepts 1-3.")


# main program
def main():
    # loads score from file
    load_score_from_file()

    print("=== TYPE THE PATTERN ===")
    menu()

main()