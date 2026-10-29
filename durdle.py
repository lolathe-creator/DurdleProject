# DurdleProject
def durdle_match(guess, target):
    new_string = ''
    for i in range(len(guess)):
        if guess[i] == target[i]:
            new_string += 'G'
        elif guess[i] in target:
            new_string += 'Y'
        else:
            new_string += 'B'         
    return new_string
    
def durdle_game(target):
    let_targ = len(target)
    print("Welcome to Durdle! The target word has", let_targ, "Letters.")
    tries = 0
    guess = input("Enter a guess: ")
    while guess != target:
        if guess.isalpha() == True and guess.islower() == True and len(guess) == let_targ:
            durdle_match(guess,target)
            tries += 1
            result = durdle_match(guess,target)
            print("              ",result)
            if guess != target:
                guess = input("Enter a guess: ")
            
        else:
            print("Invalid guess.")
            guess = input("Enter a guess: ")
    
    if guess == target:
        durdle_match(guess,target)
        tries += 1
        result = durdle_match(guess,target)
        print("              ",result)
        return tries
    
if __name__ == '__main__':
    from wonderwords import RandomWord
    random = RandomWord()
    word = random.word(word_min_length = 1, word_max_length = 10)
    tries = durdle_game(word)
    print(f'Number of guesses: {tries}')

