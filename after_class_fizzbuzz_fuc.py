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

def check_3(num):
    return (num % 3 == 0)
def check_5(num):
    return (num % 5 == 0)
def check_15(num):
    return (num % 15 == 0)

while True:
    user = str(input('Do you want to keep play FizzBuzz? y or exit ').lower().strip())
    if user == 'exit':
        print('See you next time.')
        break
    user_num = int(input('Enter number you want to play till: '))
    count_num = 1
    while user_num >= count_num:
        if check_15(count_num):
            print('FizzBuzz')
        elif check_5(count_num):
            print('Buzz')
        elif check_3(count_num):
            print('Fizz')

        else:
            print(count_num)
        count_num = count_num + 1
