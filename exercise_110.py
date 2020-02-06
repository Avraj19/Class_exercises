# The game Fizz AND Buzz!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiples of 3 and 5 are FizzBuzz
# as a user I should be ask for a number,
# so that I can play the game with my input
# As a player, I should see the game counting up to my number and
# substituting the multiples of 3 and 5 with the appropriate values,
# So that I can see if it is working
## EXTRA TASK!
# As a player, I should be able to exit the game using a key word,
# so that I can stop playing

while True:
    user = str(input('Do you want to keep play FizzBuzz? y or exit ').lower().strip())
    if user == 'exit':
        print('See you next time.')
        break
    user_num = int(input('Enter number you want to play till: '))
    count_num = 1
    while user_num >= count_num:
        if count_num % 3 == 0 and count_num % 5 == 0:
            print('FizzBuzz')
        elif count_num % 3 == 0:
            print('Fizz')
        elif count_num % 5 == 0:
            print('Buzz')
        else:
            print(count_num)
        count_num = count_num + 1

# Make a weather/clothing game ## project
# IF statements
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'
# Make it so you keep playing until we say: 'No more Magic'
#
# while true
# weather = input("Enter what is the weather like,\n"
#                 "options are: stormy and rainy, stormy, rainy, sunny ")
# if ('stormy' in weather) and ('rainy' in weather):
#     print('Stay home')
# elif weather == 'stormy':
#     print('Take rain coat')
# elif weather == 'rainy':
#     print('Take umbrella')
# elif weather == 'sunny':
#     print('Take your shorts!')
# else:
#     print('sorry, i didn't quite catch that')
