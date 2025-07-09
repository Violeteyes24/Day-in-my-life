from doctest import testsource
import random

energy = 0
focus =0
distraction = 0
happiness = 0
sadness = 0

print('Welcome to my personal sleeping journey where I gamified my own experiences when it comes to my day to day life.')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()
print('The goal is to be able to get good stats for energy, focus, distraction, happiness, and sadness.')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()
print('The stats will be updated based on the choices you make and the time you sleep.')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()
print('A bad choice can decrease stats and could lead to a set of bad choices that will diminish your stats.')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()
print()
print('Pick a number between 9 to 12 (Represents PM/AM, basically the time you slept.)')
# I use 24-hour format for time and present it in 12-hour format. But I will limit the input until 12 (12AM).
print('8PM-9PM')
print('10PM-11PM')
print('12AM')
print()
time_slept = int(input("What time did you sleep last night?: "))
hours_slept = 0
while time_slept < 9 or time_slept > 12:
    print('Invalid time')
    time_slept = int(input("What time did you sleep last night?: "))
# assuming we wake up always at 7am

if time_slept == 9:
    hours_slept = 10
    energy += 100
    focus += 100
    distraction -= 0
    happiness += 80
    sadness -= 0
elif time_slept == 10:
    hours_slept = 9
    energy += 75
    focus += 75
    distraction += 0
    happiness += 60
    sadness -= 0
elif time_slept == 11:
    hours_slept = 8 
    energy += 50
    focus += 50
    distraction += 0
    happiness += 40
    sadness += 0
else:  # time_slept == 12
    hours_slept = 7
    energy += 25
    focus += 25
    distraction += 25
    happiness += 20
    sadness += 25
pmORam = ''
if time_slept == 12:
    pmORam = 'AM'
else:
    pmORam = 'PM'

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

print(f'Time check: it is 7 am in the morning, you slept around {time_slept} {pmORam}, and slept {hours_slept} hours')
print(f'Energy: {energy}')
print(f'Focus: {focus}')
print(f'Distraction: {distraction}')
print(f'Happiness: {happiness}')
print(f'Sadness: {sadness}')
print()

print('[1] Exercise [2] Scroll')
morningChoice1 = int(input('You woke up. What do you do?: '))

while morningChoice1 != 1 and morningChoice1 != 2:
    print()
    print('[1] Exercise [2] Scroll')
    morningChoice1 = int(input('You woke up. What do you do?: '))

if morningChoice1 == 1:
    energy += 25
    happiness += 25
    print('Great exercise, points have been added to stats.')
    print(f'Happiness: {happiness}, Energy: {energy}')
elif morningChoice1 ==2:
    print('Oh no, you have wasted time to be honest. Penalty: Minus stats')
    energy -=25
    focus -=25
    distraction +=25
    happiness -= 25
    sadness += 25
    print(f'Energy: {energy}')
    print(f'Focus: {focus}')
    print(f'Distraction: {distraction}')
    print(f'Happiness: {happiness}')
    print(f'Sadness: {sadness}')
    print()

else:
    print('invalid choice')

continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()

print('After your recent activity, you showered, brushed teach and ate breakfast...')

continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()

print('Now is the crucial part for your career, this needs to be everyday since there are a lot of smart people and you cannot fall behind.')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()

print('A fun fact about me is that I am continuously learning and improving, this is due to the fact that in my early childhood / teen days, I did not do anything remarkable and its paying off, since I have been slapped by reality that I need to try and push myself harder.')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()

print('You begin Programming... turn on pomodoro timer and force yourself in the zone.')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()

print("=== PROGRAMMING TEST #1: If/Elif/Else & Input Functions ===")
print("Answer 10 questions correctly to pass!")
print()

correct = 0

while correct != 10:
    # Generate random question
    question_num = random.randint(1, 12)
    
    if question_num == 1:
        print("1. What will this code output?")
        print("   x = 5")
        print("   if x > 3:")
        print("       print('A')")
        print("   else:")
        print("       print('B')")
        print("   1) A   2) B   3) Error   4) Nothing")
        q1 = int(input('Your answer: '))
        if q1 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is A')
    
    elif question_num == 2:
        print("2. What does input() function return in Python 3?")
        print("   1) string   2) integer   3) float   4) boolean")
        q2 = int(input('Your answer: '))
        if q2 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is string')
    
    elif question_num == 3:
        print("3. What will this code output?")
        print("   score = 85")
        print("   if score >= 90:")
        print("       print('A')")
        print("   elif score >= 80:")
        print("       print('B')")
        print("   else:")
        print("       print('C')")
        print("   1) A   2) B   3) C   4) Error")
        q3 = int(input('Your answer: '))
        if q3 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is B')
    
    elif question_num == 4:
        print("4. How do you convert input() to an integer?")
        print("   1) int(input())   2) input(int)   3) integer(input())   4) input().int()")
        q4 = int(input('Your answer: '))
        if q4 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is int(input())')
    
    elif question_num == 5:
        print("5. What will this code output?")
        print("   age = 17")
        print("   if age >= 18:")
        print("       print('Adult')")
        print("   else:")
        print("       print('Minor')")
        print("   1) Adult   2) Minor   3) Error   4) Nothing")
        q5 = int(input('Your answer: '))
        if q5 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is Minor')
    
    elif question_num == 6:
        print("6. Which operator is used for 'not equal to' in Python?")
        print("   1) !=   2) <>   3) =/=   4) not=")
        q6 = int(input('Your answer: '))
        if q6 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is !=')
    
    elif question_num == 7:
        print("7. What will this code output?")
        print("   x = 10")
        print("   y = 20")
        print("   if x < y:")
        print("       print('Yes')")
        print("   elif x > y:")
        print("       print('No')")
        print("   else:")
        print("       print('Equal')")
        print("   1) Yes   2) No   3) Equal   4) Error")
        q7 = int(input('Your answer: '))
        if q7 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is Yes')
    
    elif question_num == 8:
        print("8. What is the correct syntax for an if statement?")
        print("   1) if condition:   2) if (condition)   3) if condition then:   4) if condition {}")
        q8 = int(input('Your answer: '))
        if q8 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is if condition:')
    
    elif question_num == 9:
        print("9. What will this code output if user enters 7?")
        print("   num = int(input('Enter a number: '))")
        print("   if num % 2 == 0:")
        print("       print('Even')")
        print("   else:")
        print("       print('Odd')")
        print("   1) Even   2) Odd   3) Error   4) 7")
        q9 = int(input('Your answer: '))
        if q9 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is Odd')
    
    elif question_num == 10:
        print("10. Which of these is correct for multiple conditions?")
        print("    1) if x > 0 and y < 10:   2) if x > 0 & y < 10:")
        print("    3) if x > 0 AND y < 10:   4) if (x > 0) && (y < 10):")
        q10 = int(input('Your answer: '))
        if q10 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is if x > 0 and y < 10:')
    
    elif question_num == 11:
        print("11. What will this code output?")
        print("    grade = 'B'")
        print("    if grade == 'A':")
        print("        print('Excellent')")
        print("    elif grade == 'B':")
        print("        print('Good')")
        print("    elif grade == 'C':")
        print("        print('Average')")
        print("    else:")
        print("        print('Poor')")
        print("    1) Excellent   2) Good   3) Average   4) Poor")
        q11 = int(input('Your answer: '))
        if q11 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is Good')
    
    elif question_num == 12:
        print("12. How do you check if a string is empty using input()?")
        print("    1) if input() == '':   2) if input() == None:")
        print("    3) if input() == 0:    4) if len(input()) == False:")
        q12 = int(input('Your answer: '))
        if q12 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is if input() == \'\':')
    
    print(f"Score: {correct}/10")
    print()

print("Congratulations! You passed Test #1!")
print()

# Test #2: For Loops & While Loops
print("=== PROGRAMMING TEST #2: For Loops & While Loops ===")
print("Answer 10 questions correctly to pass!")
print()

correct = 0

while correct != 10:
    # Generate random question
    question_num = random.randint(1, 12)
    
    if question_num == 1:
        print("1. What will this code output?")
        print("   for i in range(3):")
        print("       print(i)")
        print("   1) 0 1 2   2) 1 2 3   3) 0 1 2 3   4) 1 2")
        q1 = int(input('Your answer: '))
        if q1 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is 0 1 2')
    
    elif question_num == 2:
        print("2. How many times will this loop run?")
        print("   i = 0")
        print("   while i < 5:")
        print("       print(i)")
        print("       i += 1")
        print("   1) 4   2) 5   3) 6   4) Infinite")
        q2 = int(input('Your answer: '))
        if q2 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is 5')
    
    elif question_num == 3:
        print("3. What does range(1, 6) produce?")
        print("   1) 1, 2, 3, 4, 5   2) 1, 2, 3, 4, 5, 6")
        print("   3) 0, 1, 2, 3, 4, 5   4) 2, 3, 4, 5, 6")
        q3 = int(input('Your answer: '))
        if q3 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is 1, 2, 3, 4, 5')
    
    elif question_num == 4:
        print("4. What will this code output?")
        print("   for i in range(2, 8, 2):")
        print("       print(i)")
        print("   1) 2 4 6   2) 2 4 6 8   3) 2 3 4 5 6 7   4) 4 6 8")
        q4 = int(input('Your answer: '))
        if q4 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is 2 4 6')
    
    elif question_num == 5:
        print("5. What happens if you forget to increment in a while loop?")
        print("   1) Infinite loop   2) Error   3) Loop runs once   4) Loop doesn't run")
        q5 = int(input('Your answer: '))
        if q5 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is Infinite loop')
    
    elif question_num == 6:
        print("6. What will this code output?")
        print("   count = 0")
        print("   while count < 3:")
        print("       print(count)")
        print("       count += 1")
        print("   1) 0 1 2   2) 1 2 3   3) 0 1 2 3   4) Error")
        q6 = int(input('Your answer: '))
        if q6 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is 0 1 2')
    
    elif question_num == 7:
        print("7. How do you loop through a list called 'items'?")
        print("   1) for item in items:   2) for item of items:")
        print("   3) for items in item:   4) while item in items:")
        q7 = int(input('Your answer: '))
        if q7 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is for item in items:')
    
    elif question_num == 8:
        print("8. What does the 'break' statement do in a loop?")
        print("   1) Exits the loop   2) Skips current iteration")
        print("   3) Pauses the loop   4) Restarts the loop")
        q8 = int(input('Your answer: '))
        if q8 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is Exits the loop')
    
    elif question_num == 9:
        print("9. What will this code output?")
        print("   for i in range(5):")
        print("       if i == 3:")
        print("           break")
        print("       print(i)")
        print("   1) 0 1 2   2) 0 1 2 3   3) 0 1 2 3 4   4) 3 4")
        q9 = int(input('Your answer: '))
        if q9 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is 0 1 2')
    
    elif question_num == 10:
        print("10. What does the 'continue' statement do?")
        print("    1) Skips to next iteration   2) Exits the loop")
        print("    3) Restarts the loop   4) Pauses the loop")
        q10 = int(input('Your answer: '))
        if q10 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is Skips to next iteration')
    
    elif question_num == 11:
        print("11. What will this code output?")
        print("    for i in range(4):")
        print("        if i == 2:")
        print("            continue")
        print("        print(i)")
        print("    1) 0 1 3   2) 0 1 2 3   3) 2   4) 0 1 2")
        q11 = int(input('Your answer: '))
        if q11 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is 0 1 3')
    
    elif question_num == 12:
        print("12. How do you create a while loop that runs forever?")
        print("    1) while True:   2) while 1:   3) while Forever:   4) while Always:")
        q12 = int(input('Your answer: '))
        if q12 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! The answer is while True:')
    
    print(f"Score: {correct}/10")
    print()

print("Congratulations! You passed Test #2!")
print("You have completed both programming tests!")
happiness += 30
print(f'Due to productivity, happiness has increased: {happiness}')
# programming test #1 should be about if, elif and else statements, as well as input functions (10)
# programming test #2 should be about for loops and while loops (10)
print('Its afternoon already, you ate lunch and talked to your family. You also do chores or buy food/things outside that is needed in the house')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()
print('After all of that, you begin programming again...')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()

# Test #3: Debugging
print("=== PROGRAMMING TEST #3: Debugging ===")
print("Answer 10 questions correctly to pass!")
print()

correct = 0

while correct != 10:
    # Generate random question
    question_num = random.randint(1, 12)
    
    if question_num == 1:
        print("1. What's wrong with this code?")
        print("   if x = 5:")
        print("       print('Hello')")
        print("   1) Should use == instead of =   2) Missing quotes")
        print("   3) Wrong indentation   4) Nothing wrong")
        q1 = int(input('Your answer: '))
        if q1 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Should use == for comparison, = is for assignment')
    
    elif question_num == 2:
        print("2. What will cause an error in this code?")
        print("   age = input('Enter age: ')")
        print("   if age > 18:")
        print("       print('Adult')")
        print("   1) input() returns string, can't compare with int")
        print("   2) Missing colon   3) Wrong variable name   4) Nothing wrong")
        q2 = int(input('Your answer: '))
        if q2 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! input() returns string, need int(input()) to compare with numbers')
    
    elif question_num == 3:
        print("3. What's the error in this code?")
        print("   for i in range(5)")
        print("       print(i)")
        print("   1) Missing colon after range(5)   2) Wrong indentation")
        print("   3) Should be while loop   4) range is wrong")
        q3 = int(input('Your answer: '))
        if q3 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Missing colon (:) after for statement')
    
    elif question_num == 4:
        print("4. What will happen when this code runs?")
        print("   count = 0")
        print("   while count < 5:")
        print("       print(count)")
        print("   1) Infinite loop   2) Prints 0-4   3) Error   4) Prints 1-5")
        q4 = int(input('Your answer: '))
        if q4 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Missing count += 1, so it runs forever')
    
    elif question_num == 5:
        print("5. What's wrong with this indentation?")
        print("   if x > 0:")
        print("   print('Positive')")
        print("   else:")
        print("   print('Not positive')")
        print("   1) Print statements not indented   2) Missing colons")
        print("   3) Wrong variable   4) Nothing wrong")
        q5 = int(input('Your answer: '))
        if q5 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Print statements must be indented after if/else')
    
    elif question_num == 6:
        print("6. What error will this code produce?")
        print("   num = int(input('Enter number: '))")
        print("   # User enters 'hello'")
        print("   print(num)")
        print("   1) ValueError   2) TypeError   3) SyntaxError   4) No error")
        q6 = int(input('Your answer: '))
        if q6 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! ValueError occurs when int() can\'t convert string to number')
    
    elif question_num == 7:
        print("7. What's the problem with this code?")
        print("   for i in range(3):")
        print("       print(i)")
        print("   print(i)")
        print("   1) Variable i not defined outside loop")
        print("   2) Wrong range   3) Missing colon   4) Nothing wrong")
        q7 = int(input('Your answer: '))
        if q7 == 4:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! This code is actually correct - i retains its last value')
    
    elif question_num == 8:
        print("8. What will cause this code to crash?")
        print("   numbers = [1, 2, 3]")
        print("   print(numbers[3])")
        print("   1) IndexError   2) ValueError   3) TypeError   4) No error")
        q8 = int(input('Your answer: '))
        if q8 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! IndexError - list has indices 0,1,2 but trying to access 3')
    
    elif question_num == 9:
        print("9. What's wrong with this elif statement?")
        print("   if score >= 90:")
        print("       print('A')")
        print("   elif score >= 80")
        print("       print('B')")
        print("   1) Missing colon after elif condition   2) Wrong operator")
        print("   3) Wrong indentation   4) Nothing wrong")
        q9 = int(input('Your answer: '))
        if q9 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Missing colon (:) after elif condition')
    
    elif question_num == 10:
        print("10. What debugging technique helps find logical errors?")
        print("    1) Adding print statements   2) Reading error messages")
        print("    3) Checking syntax   4) Restarting computer")
        q10 = int(input('Your answer: '))
        if q10 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Adding print statements helps trace program flow')
    
    elif question_num == 11:
        print("11. What's the issue with this code?")
        print("    x = 10")
        print("    if x > 5")
        print("        print('Greater')")
        print("    else:")
        print("        print('Less')")
        print("    1) Missing colon after if condition   2) Wrong comparison")
        print("    3) Wrong indentation   4) Missing quotes")
        q11 = int(input('Your answer: '))
        if q11 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Missing colon (:) after if condition')
    
    elif question_num == 12:
        print("12. What error type is this?")
        print("    print('Hello World'")
        print("    1) SyntaxError   2) ValueError   3) TypeError   4) IndexError")
        q12 = int(input('Your answer: '))
        if q12 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! SyntaxError - missing closing parenthesis')
    
    print(f"Score: {correct}/10")
    print()

print("Congratulations! You passed Test #3!")
print()

# Test #4: Decision Making - When to Seek Help
print("=== PROGRAMMING TEST #4: Decision Making - When to Seek Help ===")
print("Answer 5 questions correctly to pass!")
print()

correct = 0

while correct != 5:
    # Generate random question
    question_num = random.randint(1, 7)
    
    if question_num == 1:
        print("1. You've been stuck on a syntax error for 5 minutes. What should you do?")
        print("   1) Keep trying for another hour")
        print("   2) Read the error message carefully and try to fix it")
        print("   3) Ask AI immediately   4) Give up")
        q1 = int(input('Your answer: '))
        if q1 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Always read error messages first - they usually tell you what\'s wrong')
    
    elif question_num == 2:
        print("2. When is it appropriate to use AI for help?")
        print("   1) For every single problem immediately")
        print("   2) After trying for 15-20 minutes and researching")
        print("   3) Never   4) Only for advanced problems")
        q2 = int(input('Your answer: '))
        if q2 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Try solving it yourself first, then use AI after reasonable effort')
    
    elif question_num == 3:
        print("3. You get a 'NameError' in your code. What should you do first?")
        print("   1) Ask AI to fix it")
        print("   2) Check if variable names are spelled correctly")
        print("   3) Restart the program   4) Delete the variable")
        q3 = int(input('Your answer: '))
        if q3 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! NameError usually means misspelled or undefined variable')
    
    elif question_num == 4:
        print("4. What's the best approach when learning a new programming concept?")
        print("   1) Ask AI to write all the code")
        print("   2) Try examples yourself, then ask for help when stuck")
        print("   3) Only use textbooks   4) Memorize all syntax first")
        q4 = int(input('Your answer: '))
        if q4 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Practice first, then seek help - builds better understanding')
    
    elif question_num == 5:
        print("5. You're debugging code and can't find the error. What's most helpful?")
        print("   1) Add print statements to trace the program")
        print("   2) Delete everything and start over")
        print("   3) Ask someone else to write it   4) Keep guessing randomly")
        q5 = int(input('Your answer: '))
        if q5 == 1:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Print statements help you see what\'s happening in your code')
    
    elif question_num == 6:
        print("6. When should you try to solve a problem on your own?")
        print("   1) Never - always ask for help")
        print("   2) For simple errors and concept review")
        print("   3) Only for advanced problems   4) When you have unlimited time")
        q6 = int(input('Your answer: '))
        if q6 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Try simple problems yourself to build problem-solving skills')
    
    elif question_num == 7:
        print("7. What's the benefit of struggling with a problem before asking for help?")
        print("   1) It wastes time   2) It builds problem-solving skills")
        print("   3) It makes you frustrated   4) No benefit")
        q7 = int(input('Your answer: '))
        if q7 == 2:
            correct += 1
            print('You got that right!')
        else:
            print('Wrong! Struggling builds critical thinking and problem-solving skills')
    
    print(f"Score: {correct}/5")
    print()

print("Congratulations! You passed Test #4!")
print("You have completed all programming tests!")

happiness += 30
print(f'Due to productivity, happiness has increased: {happiness}')
# programming test #3 should be about debugging (10)
# programming test #4 should be about decision making scenarios if you are stuck on a problem, the context is where do you seek help with AI or try to find it on your own.(5 questions)

print('Its dinner time, you ate, then talked to your family again, then lastly, talked and played with your friends.')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()
print('For some reason, you lost track of time...')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()
print('This is where you would fight your inner self to not fall into the temptation of sleeping very late...')
continueTerminal = input('Press w and enter to continue: ')
while continueTerminal != 'w':
    continueTerminal = input('Press w and enter to continue: ')
continueTerminal = ''
print()

hp = 100
atk = 10
mana = 100
speed = 50
skill1damage = 20
skill2damage = speed - 50  # This is 0, so it's a stun
ultdamage = 50

# Enemy stats
enemy_hp = 100
enemy_atk = 10
enemy_mana = 100
enemy_speed = 55
enemy_skill = 20
enemy_ultdamage = 40

# Game state variables
player_stunned = False
enemy_stunned = False
turn = 1

print("=" * 50)
print("          TURN-BASED RPG BATTLE")
print("=" * 50)
print(f"Player: HP={hp}, ATK={atk}, MANA={mana}, SPEED={speed}")
print(f"Enemy:  HP={enemy_hp}, ATK={enemy_atk}, MANA={enemy_mana}, SPEED={enemy_speed}")
print("=" * 50)

# Main game loop
while hp > 0 and enemy_hp > 0:
    print(f"\n--- TURN {turn} ---")
    
    # Determine who goes first based on speed
    if speed >= enemy_speed:
        player_first = True
    else:
        player_first = False
    
    # Player turn (if going first or enemy is stunned)
    if player_first or enemy_stunned:
        if not player_stunned:
            print(f"\nPlayer's turn!")
            print(f"Player: HP={hp}, MANA={mana}")
            print(f"Enemy:  HP={enemy_hp}, MANA={enemy_mana}")
            
            print("\nChoose your action:")
            print("1. Normal Attack (ATK damage)")
            print("2. Skill 1 (20 damage, -20 mana)")
            print("3. Skill 2 (Stun enemy, -30 mana)")
            print("4. Ultimate (50 damage, -50 mana)")
            
            # Player input
            while True:
                try:
                    action = int(input("Enter your choice (1-4): "))
                    if action >= 1 and action <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number.")
            
            # Execute player action
            if action == 1:
                print(f"Player attacks for {atk} damage!")
                enemy_hp = enemy_hp - atk
            elif action == 2:
                if mana >= 20:
                    print(f"Player uses Skill 1 for {skill1damage} damage!")
                    enemy_hp = enemy_hp - skill1damage
                    mana = mana - 20
                else:
                    print("Not enough mana! Normal attack instead.")
                    enemy_hp = enemy_hp - atk
            elif action == 3:
                if mana >= 30:
                    print("Player uses Skill 2 - Enemy is stunned!")
                    enemy_stunned = True
                    mana = mana - 30
                else:
                    print("Not enough mana! Normal attack instead.")
                    enemy_hp = enemy_hp - atk
            elif action == 4:
                if mana >= 50:
                    print(f"Player uses Ultimate for {ultdamage} damage!")
                    enemy_hp = enemy_hp - ultdamage
                    mana = mana - 50
                else:
                    print("Not enough mana! Normal attack instead.")
                    enemy_hp = enemy_hp - atk
            
            # Pause after player action
            continueTerminal = input('Press w and enter to continue: ')
            while continueTerminal != 'w':
                continueTerminal = input('Press w and enter to continue: ')
            continueTerminal = ''
            print()
        else:
            print("Player is stunned and cannot act!")
            player_stunned = False
            continueTerminal = input('Press w and enter to continue: ')
            while continueTerminal != 'w':
                continueTerminal = input('Press w and enter to continue: ')
            continueTerminal = ''
            print()
    
    # Check if enemy is defeated
    if enemy_hp <= 0:
        break
    
    # Enemy turn (if going first or player is stunned)
    if not player_first or player_stunned:
        if not enemy_stunned:
            print(f"\nEnemy's turn!")
            print(f"Player: HP={hp}, MANA={mana}")
            print(f"Enemy:  HP={enemy_hp}, MANA={enemy_mana}")
            
            # Enemy AI - simple pattern
            if turn % 3 == 1:
                # Normal attack
                print(f"Enemy attacks for {enemy_atk} damage!")
                hp = hp - enemy_atk
            elif turn % 3 == 2:
                # Skill attack
                if enemy_mana >= 25:
                    print(f"Enemy uses skill for {enemy_skill} damage!")
                    hp = hp - enemy_skill
                    enemy_mana = enemy_mana - 25
                else:
                    print("Enemy is low on mana! Normal attack instead.")
                    hp = hp - enemy_atk
            else:
                # Ultimate attack
                if enemy_mana >= 40:
                    print(f"Enemy uses ultimate for {enemy_ultdamage} damage!")
                    hp = hp - enemy_ultdamage
                    enemy_mana = enemy_mana - 40
                else:
                    print("Enemy is low on mana! Normal attack instead.")
                    hp = hp - enemy_atk
            
            # Pause after enemy action
            continueTerminal = input('Press w and enter to continue: ')
            while continueTerminal != 'w':
                continueTerminal = input('Press w and enter to continue: ')
            continueTerminal = ''
            print()
        else:
            print("Enemy is stunned and cannot act!")
            enemy_stunned = False
            continueTerminal = input('Press w and enter to continue: ')
            while continueTerminal != 'w':
                continueTerminal = input('Press w and enter to continue: ')
            continueTerminal = ''
            print()
    
    # Check if player is defeated
    if hp <= 0:
        break
    
    # Second turn for the slower character
    if player_first and not enemy_stunned:
        if not enemy_stunned:
            print(f"\nEnemy's turn!")
            print(f"Player: HP={hp}, MANA={mana}")
            print(f"Enemy:  HP={enemy_hp}, MANA={enemy_mana}")
            
            # Enemy AI - simple pattern
            if turn % 3 == 1:
                # Normal attack
                print(f"Enemy attacks for {enemy_atk} damage!")
                hp = hp - enemy_atk
            elif turn % 3 == 2:
                # Skill attack
                if enemy_mana >= 25:
                    print(f"Enemy uses skill for {enemy_skill} damage!")
                    hp = hp - enemy_skill
                    enemy_mana = enemy_mana - 25
                else:
                    print("Enemy is low on mana! Normal attack instead.")
                    hp = hp - enemy_atk
            else:
                # Ultimate attack
                if enemy_mana >= 40:
                    print(f"Enemy uses ultimate for {enemy_ultdamage} damage!")
                    hp = hp - enemy_ultdamage
                    enemy_mana = enemy_mana - 40
                else:
                    print("Enemy is low on mana! Normal attack instead.")
                    hp = hp - enemy_atk
            
            # Pause after enemy action
            continueTerminal = input('Press w and enter to continue: ')
            while continueTerminal != 'w':
                continueTerminal = input('Press w and enter to continue: ')
            continueTerminal = ''
            print()
        else:
            print("Enemy is stunned and cannot act!")
            enemy_stunned = False
            continueTerminal = input('Press w and enter to continue: ')
            while continueTerminal != 'w':
                continueTerminal = input('Press w and enter to continue: ')
            continueTerminal = ''
            print()
    elif not player_first and not player_stunned:
        if not player_stunned:
            print(f"\nPlayer's turn!")
            print(f"Player: HP={hp}, MANA={mana}")
            print(f"Enemy:  HP={enemy_hp}, MANA={enemy_mana}")
            
            print("\nChoose your action:")
            print("1. Normal Attack (ATK damage)")
            print("2. Skill 1 (20 damage, -20 mana)")
            print("3. Skill 2 (Stun enemy, -30 mana)")
            print("4. Ultimate (50 damage, -50 mana)")
            
            # Player input
            while True:
                try:
                    action = int(input("Enter your choice (1-4): "))
                    if action >= 1 and action <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number.")
            
            # Execute player action
            if action == 1:
                print(f"Player attacks for {atk} damage!")
                enemy_hp = enemy_hp - atk
            elif action == 2:
                if mana >= 20:
                    print(f"Player uses Skill 1 for {skill1damage} damage!")
                    enemy_hp = enemy_hp - skill1damage
                    mana = mana - 20
                else:
                    print("Not enough mana! Normal attack instead.")
                    enemy_hp = enemy_hp - atk
            elif action == 3:
                if mana >= 30:
                    print("Player uses Skill 2 - Enemy is stunned!")
                    enemy_stunned = True
                    mana = mana - 30
                else:
                    print("Not enough mana! Normal attack instead.")
                    enemy_hp = enemy_hp - atk
            elif action == 4:
                if mana >= 50:
                    print(f"Player uses Ultimate for {ultdamage} damage!")
                    enemy_hp = enemy_hp - ultdamage
                    mana = mana - 50
                else:
                    print("Not enough mana! Normal attack instead.")
                    enemy_hp = enemy_hp - atk
            
            # Pause after player action
            continueTerminal = input('Press w and enter to continue: ')
            while continueTerminal != 'w':
                continueTerminal = input('Press w and enter to continue: ')
            continueTerminal = ''
            print()
        else:
            print("Player is stunned and cannot act!")
            player_stunned = False
            continueTerminal = input('Press w and enter to continue: ')
            while continueTerminal != 'w':
                continueTerminal = input('Press w and enter to continue: ')
            continueTerminal = ''
            print()
    
    # Mana regeneration
    if mana < 100:
        mana = mana + 10
        if mana > 100:
            mana = 100
    
    if enemy_mana < 100:
        enemy_mana = enemy_mana + 10
        if enemy_mana > 100:
            enemy_mana = 100
    
    # End of turn status
    print(f"\nEnd of turn {turn}:")
    print(f"Player: HP={hp}, MANA={mana}")
    print(f"Enemy:  HP={enemy_hp}, MANA={enemy_mana}")
    print("-" * 30)
    
    # Pause before next turn
    continueTerminal = input('Press w and enter to continue: ')
    while continueTerminal != 'w':
        continueTerminal = input('Press w and enter to continue: ')
    continueTerminal = ''
    print()
    
    turn = turn + 1
    
    # Prevent infinite loops
    if turn > 20:
        print("\nBattle timeout! It's a draw!")
        break

# Battle result
print("\n" + "=" * 50)
if hp <= 0:
    print("          DEFEAT!")
    print("        Enemy wins!")
    print("        In the end, you slept very late and highly likely you'll wake up feeling uncomfortable and this start might lead to a chain of bad events..")
elif enemy_hp <= 0:
    print("          VICTORY!")
    print("        Player wins!")
    print("        Completed a balanced and productive day! You sleep early and will wake up in a good mood.")

else:
    print("          DRAW!")
    print("      Battle ended!")
    print("      You still slept late, but not late enough to ruin your day tomorrow, just not as refreshed.")

print("=" * 50)


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