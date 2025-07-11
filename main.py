from modules.stats import GameStats
from modules.tests import run_test_1, run_test_2, run_test_3, run_test_4
from modules.battle import BattleSystem
from modules.utils import get_continue_input, get_sleep_time, get_morning_choice, calculate_sleep_hours

def main():
    # Initialize game stats
    game_stats = GameStats()

    print('Welcome to my personal sleeping journey where I gamified my own experiences when it comes to my day to day life.')
    get_continue_input()
    print()
    
    print('The goal is to be able to get good stats for energy, focus, distraction, happiness, and sadness.')
    get_continue_input()
    print()
    
    print('The stats will be updated based on the choices you make and the time you sleep.')
    get_continue_input()
    print()
    
    print('A bad choice can decrease stats and could lead to a set of bad choices that will diminish your stats.')
    get_continue_input()
    print()
    print()

    # Get sleep time and calculate hours
    time_slept = get_sleep_time()
    hours_slept = calculate_sleep_hours(time_slept)
    pmORam = 'AM' if time_slept == 12 else 'PM'

    print(f'Time check: it is 7 am in the morning, you slept around {time_slept} {pmORam}, and slept {hours_slept} hours')
    game_stats.display_stats()
    print()

    # Morning choice
    morning_choice = get_morning_choice()
    if morning_choice == 1:
        print('Good choice! You exercised and got your blood flowing. Bonus: Added stats')
        game_stats.update_stats(energy=25, focus=25, distraction=-25, happiness=25, sadness=-25)
    else:
        print('Oh no, you have wasted time to be honest. Penalty: Minus stats')
        game_stats.update_stats(energy=-25, focus=-25, distraction=25, happiness=-25, sadness=25)
    
    game_stats.display_stats()
    
    # Continue with morning routine
    get_continue_input()
    print()

    print('After your recent activity, you showered, brushed teeth and ate breakfast...')
    get_continue_input()
    print()

    # Programming tests section
    print('Now is the crucial part for your career...')
    get_continue_input()
    print()

    game_stats.update_stats(happiness=run_test_1())
    game_stats.update_stats(happiness=run_test_2())
    
    print('Its afternoon already...')
    get_continue_input()
    print()
    
    print('After all of that, you begin programming again...')
    get_continue_input()
    print()
    
    game_stats.update_stats(happiness=run_test_3())
    game_stats.update_stats(happiness=run_test_4())

    # Evening battle section
    print('Its dinner time...')
    get_continue_input()
    print()
    
    battle = BattleSystem()
    battle_result = battle.run_battle()

if __name__ == "__main__":
    main()

# Original comments preserved:
# this is where the RPG will take over. I might need to enclose the whole code with a while loop, so that it will go back to the very start and 
# you can input what time you slept.

# also validations / control statements for input, should help users if they input wrong, they can try to input again and not exit the terminal.

# morning good chain of events (Wake up -> Exercise -> Shower, Brush Teeth, Eat Breakfast -> Programming)
# afternoon good chain of events (Lunch -> Talk to your Family -> Programming -> Exercise)
# evening good chain of events (Dinner -> Talk to your Friends -> Fight if you still want to play more with your friends(won game) -> Reflection -> Sleep )

# morning bad chain of events (Wake up -> Scroll -> Shower, Brush Teeth, Eat Breakfast -> Programming)
# afternoon bad chain of events (Lunch -> Scroll -> Programming -> Scroll)
# evening good chain of events (Dinner -> Talk to your Friends -> Fight if you still want to play more with your friends(lose game) -> Scroll -> Sleep )

# to do:
# 1. programming tests - done
# 2. rpg - done
# 3. validations - to do in near future.

# My legendary code that I will never delete, because it is the only custom code I have ever written that works for decrementing a value from an incrementing for loop.

# for i in range(9,13):
#     time_slept = 19 - i --> the only code for decrementing a value from an incrementing for loop ***
#     print(f'value of i: {i} value of time slept: {time_slept}') 
#     time_calculation = 21-7
#     print(f'first calculation {time_calculation}')
#     time_calculation = 24 - time_calculation
#     print(f'second calculation {time_calculation}')
#     time_calculation = time_calculation - 1
#     print(f'Decrement time calculation to also decrement time slept {time_calculation}')
#     time_slept = time_calculation
#     print(f'Value of time slept per i {time_slept}')
#     print(f'i is {i} and time slept is: {time_slept}')
#     print(time_slept)

# time_slept = time_slept 
# print(f'You slept for {time_slept} hours')