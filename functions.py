import random
def bubble_sorting(list):
    '''
    sorts from the lowest to the bigest
    :param list:
    :return: list sorted
    '''
    for j in range(0, len(list)):
        previous = list[0]
        position = 0
        for i in list:
            if i >= previous:
                previous = i
            else:
                number_to_move = list.pop(position)
                list.insert(position - 1, number_to_move)
            position += 1
    return list


def binary_to_decimal(a):
    '''
    function converts number from binary to decimal
    :param a:binary number
    :return:int (decimal number)
    '''
    list_of_bytes = []
    dec_number = 0
    position = 0
    for byte in str(a):
        list_of_bytes.append(byte)
    list_of_bytes.reverse()
    for i in list_of_bytes:
        dec_number += int(i) * (2 ** position)
        position += 1
    return dec_number


def odd_or_even(a):
    '''
    function tells whether given number is odd or even
    :param a: int
    :return: boolean value. True if a is even False if it is odd
    '''
    if int(a)%2 == 0:
        is_even = True
    else:
        is_even = False
    return is_even    
        

def word_count(sentence):
    '''
    functions takes one argument (string) and returns information about number of words in it
    :param sentence: string
    :return: int
    '''
    num_of_spaces = str(sentence).count(" ")
    if (len(sentence) == 0) or (len(sentence) == num_of_spaces) or (sentence[-1] == " "):
        words = 0
    else:
        words = 1
    previous = sentence[0]  #used to compare if one space comes after anothers
    for i in sentence:
        if i == " " and i != previous:
            words += 1
        else:
            pass
        previous = i
    return words


def guess_game_0_10(low_range, high_range, guess):
    error = False
    victory = False
    low_range = int(low_range)
    high_range = int(high_range)
    guess = int(guess)
    random_number = random.randint(low_range, high_range)
    if low_range >= high_range:
        print('lower limit range number should be lower than high range number')
        error = True    #variable to help count games played
    elif guess < low_range or guess > high_range:
        print('your guess is out of range')
        error = True
    elif random_number == guess:
        print('congrats your guess was correct')
        victory = True
    elif random_number != guess:
        print('try one more time')
        victory = False
    return victory, error


def guess_game_interface():
    play_again = True
    games_played = 1
    while play_again:
        victory, error = guess_game_0_10(input('give lover limit'), input('give upper limit'), input('what is your guess'))
        if victory:
            print(f'it took you {games_played} games to win')
            play_again = False
        elif not victory and error:
            play_again = not(input('Do you want to try one more time? press enter if yes'))
        else:
            games_played += 1
            play_again = not(input('Do you want to try one more time? press enter if yes'))


def give_word_to_list():
    '''
    function takes from user as many words as he wants and writes them to a list
    :return: list
    '''
    i = 0
    num_of_words = int(input('how many words would you like to give?'))
    list_of_words = []
    while i < num_of_words:
        word = input(f'give me a word ({num_of_words-i} left)\n')
        list_of_words.append(word)
        i += 1
    return list_of_words


def palindrome_chceck():
    '''
    function takes a list of words and checks if any of them is a palindrome
    :param list:
    :return:
    '''
    list_of_words = give_word_to_list()     #another function (takes input from user)
    list_of_palindromes = []
    palindrome_count = 0
    for word in list_of_words:
        i = 0
        same_pair = 0                       #counts how many pairs of the same sign are in word
        while i < (len(word)/2).__ceil__(): #half of word length, rounded up (if 5 words it checks 3 times)
            if word[i] == word[-i-1]:       #check first position and last one, then second and one before last
                same_pair += 1              #if signs are the same store information about that
            else:
                pass
            i += 1                          #next position in word
        if same_pair == (len(word)/2).__ceil__():       #num   of pairs = ammount of pairs checked (one sign in the middle is also a pair)
            list_of_palindromes.append(word)
            palindrome_count += 1
    print(f'there are {palindrome_count} palindromes, which are {list_of_palindromes}')

