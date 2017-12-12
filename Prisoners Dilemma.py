<<<<<<< HEAD
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Anthony'
strategy_name = 'Rando Calrissian'
strategy_description = 'Random Choice'
import random    
def move():
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    # This player colludes on even numbered rounds (first round is round #0).
    movement = random.randint(1,2)
    if movement == 1:
        return 'c'
    if movement == 2:
=======
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Anthony'
strategy_name = 'Rando Calrissian'
strategy_description = 'Random Choice'
import random    
def move():
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    # This player colludes on even numbered rounds (first round is round #0).
    movement = random.randint(1,2)
    if movement == 1:
        return 'c'
    if movement == 2:
>>>>>>> origin/master
        return 'b'