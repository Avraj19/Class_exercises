# mr Miyagi trainee ##projct
# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'

# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

while True:
    user_input = input('Ask question to Mr. Miyagi')

    if user_input == True:
        print('questions are wise, but for now. Wax on, and Wax off!')


#
#     print('You are smart, but not wise - address me as Sensei please')
#
#     print('Remeber, best block, not to be there..')
#
#     print('do not lose focus. Wax on. Wax off.')
# else:
#
#     print('Sometimes, what heart know, head forget')