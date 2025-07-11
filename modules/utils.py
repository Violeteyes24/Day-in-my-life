"""
Utility functions for input handling and validation.
"""

def get_continue_input():
    """Get and validate the 'w' continue input"""
    continueTerminal = input('Press w and enter to continue: ')
    while continueTerminal != 'w':
        continueTerminal = input('Press w and enter to continue: ')
    return ''

def get_sleep_time():
    """Get and validate sleep time input"""
    print('Pick a number between 9 to 12 (Represents PM/AM, basically the time you slept.)')
    print('8PM-9PM')
    print('10PM-11PM')
    print('12AM')
    print()
    
    time_slept = int(input("What time did you sleep last night?: "))
    while time_slept < 9 or time_slept > 12:
        time_slept = int(input("Please enter a valid time between 9 and 12: "))
    
    return time_slept

def get_morning_choice():
    """Get and validate morning activity choice"""
    print('[1] Exercise [2] Scroll')
    choice = int(input('You woke up. What do you do?: '))
    
    while choice != 1 and choice != 2:
        choice = int(input('Please enter 1 or 2: '))
    
    return choice

def calculate_sleep_hours(time_slept):
    """Calculate hours slept based on sleep time"""
    # Original sleep calculation logic here
    # This would include the logic for calculating hours slept based on the input time
    return 8  # Placeholder return
