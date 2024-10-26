import random
import functions_for_hang_man


words =["elephant","puzzle","mountain","oxygen","adventure","galaxy","pyramid","chocolate","butterfly","rainbow",
        "bicycle","diamond","volcano","giraffe","astronaut","cucumber","mystery","tornado","parachute","whisper",]
#choosing a random word form the words list
random_word = random.choice(words)
#word_len is the length of the word stored ,also used for length of the dashes
word_len = len(random_word)
#it store amount of dashes according to count of the word_length
num1  = 0
dashes = ""
while num1 < word_len:
    dashes += "_"*1
    num1+=1
# making both string in to a list of charaters
list_of_random_word = list(random_word)
list_of_dashes =list(dashes)
functions_for_hang_man.show_joined(list_of_dashes)
# print(list_of_random_word)

#function to ask for user input
def word_input():
    letter_enterd = input("Guess the word : ").lower() # it convert upper case input to lower
    return letter_enterd

# ask for input as per life
life = 6
while life >=1:
    letter = word_input()
    """if the below condition is ture the "correct_ gueess" will be assigned to True,when the input make changes to
    the list_of_dashes"""
    correct_guess = False
    # check the list of letters for similer as guessed word
    for i in range(word_len):
        # if the guessed letter is similer, the dash is replaced with that letter at that same index as letter.
        if letter == list_of_random_word[i]:
            list_of_dashes[i] = list_of_random_word[i]
            correct_guess = True
    if correct_guess == False:
        life -=1

    if list_of_dashes == list_of_random_word:
        print("You guessed the word !")
        break
    #to show the dashes as a string without converting to string using join in anoter file(it is copy)
    functions_for_hang_man.show_joined(list_of_dashes)
    print(f"Life left : {life}")
#to show the final word after life is finished or winning
print(f"The word is -> "),functions_for_hang_man.show_joined(list_of_random_word)
#win or lost based on difference of two list
if list_of_dashes == list_of_random_word :
    print("You Win :)\n")
else:
    print("You Lost :( \n")


