# import bot, user_input
import user_input

# from bot import program_name, generate_computer_response
from bot import program_name as BotProgram, generate_computer_response  # can use 'as' to change names when imported, in case of conflicts, etc.
# from user_input import *

print('Welcome to ' + BotProgram)

print('Type "STOP" to end.')

user_input.ask_question('How was your day?')

while True:
    bot_response = generate_computer_response()
    response = user_input.ask_question(bot_response)
    if response.upper() == 'STOP':
        break

print('Thanks for the interesting conversation!')