"""
Module containing all programming tests.
"""
import random
from modules.utils import get_continue_input

def run_test_1():
    """Run programming test #1: If/Elif/Else & Input Functions"""
    print("=== PROGRAMMING TEST #1: If/Elif/Else & Input Functions ===")
    print("Answer 10 questions correctly to pass!")
    print()
    
    correct = 0
    while correct != 10:
        # Generate random question
        question_num = random.randint(1, 12)
        
        if question_num == 1:
            print("1. What is the correct way to write an if statement in Python?")
            print("   1) if x == 5:   2) if (x == 5)   3) if x = 5:   4) if x == 5 then")
            q1 = int(input('Your answer: '))
            if q1 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The answer is if x == 5:')
        
        elif question_num == 2:
            print("2. How do you write an else if statement in Python?")
            print("   1) else if   2) elif   3) elseif   4) else_if")
            q2 = int(input('Your answer: '))
            if q2 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The answer is elif')
        
        elif question_num == 3:
            print("3. What is the output of the following code?")
            print("   x = 5")
            print("   if x == 5:")
            print("       print('Hello')")
            print("   1) Hello   2) Nothing   3) Error   4) 5")
            q3 = int(input('Your answer: '))
            if q3 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The code prints Hello')
        
        elif question_num == 4:
            print("4. Which of the following is a correct syntax for a while loop?")
            print("   1) while x > 5:   2) while (x > 5)   3) while x > 5 do   4) while x > 5")
            q4 = int(input('Your answer: '))
            if q4 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct syntax is while x > 5:')
        
        elif question_num == 5:
            print("5. How can you generate a random number between 1 and 10 in Python?")
            print("   1) random(1, 10)   2) rand(1, 10)   3) random.randint(1, 10)   4) randint(1, 10)")
            q5 = int(input('Your answer: '))
            if q5 == 3:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct function is random.randint(1, 10)')
        
        elif question_num == 6:
            print("6. What will be the output of the following code?")
            print("   for i in range(3):")
            print("       print(i)")
            print("   1) 0 1 2   2) 1 2 3   3) 0 1 2 3   4) 1 2")
            q6 = int(input('Your answer: '))
            if q6 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The output will be 0 1 2')
        
        elif question_num == 7:
            print("7. Which of the following is the correct way to start a for loop in Python?")
            print("   1) for i in [1, 2, 3]:   2) for (i = 0; i < 3; i++):")
            print("   3) for i = 1 to 3:   4) for i in range(3)")
            q7 = int(input('Your answer: '))
            if q7 == 1 or q7 == 4:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct ways are for i in [1, 2, 3]: or for i in range(3):')
        
        elif question_num == 8:
            print("8. What is the output of print(2 ** 3)?")
            print("   1) 6   2) 8   3) 9   4) Error")
            q8 = int(input('Your answer: '))
            if q8 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! 2 ** 3 equals 8')
        
        elif question_num == 9:
            print("9. How do you create a function in Python?")
            print("   1) function myFunc()   2) def myFunc()")
            print("   3) create myFunc()   4) myFunc() = function")
            q9 = int(input('Your answer: '))
            if q9 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct syntax is def myFunc():')
        
        elif question_num == 10:
            print("10. What is the purpose of the return statement in a function?")
            print("   1) To return to the previous menu   2) To exit the function")
            print("   3) To send a value back to the caller   4) To print a value")
            q10 = int(input('Your answer: '))
            if q10 == 3:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The return statement sends a value back to the caller')
        
        print(f"Score: {correct}/10")
        print()

    print("Congratulations! You passed Test #1!")
    print()
    return 30  # Return happiness increase

def run_test_2():
    """Run programming test #2: For Loops & While Loops"""
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
            print("2. How many times will the following loop run?")
            print("   for i in range(5):")
            print("       print(i)")
            print("   1) 4 times   2) 5 times   3) 6 times   4) Infinite")
            q2 = int(input('Your answer: '))
            if q2 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The loop runs 5 times')
        
        elif question_num == 3:
            print("3. What is the output of the following code?")
            print("   x = 0")
            print("   while x < 3:")
            print("       print(x)")
            print("       x += 1")
            print("   1) 0 1 2   2) 1 2 3   3) 0 1 2 3   4) 1 2")
            q3 = int(input('Your answer: '))
            if q3 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The output will be 0 1 2')
        
        elif question_num == 4:
            print("4. Which of the following is the correct syntax for a while loop?")
            print("   1) while x > 5:   2) while (x > 5)   3) while x > 5 do   4) while x > 5")
            q4 = int(input('Your answer: '))
            if q4 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct syntax is while x > 5:')
        
        elif question_num == 5:
            print("5. How can you generate a random number between 1 and 10 in Python?")
            print("   1) random(1, 10)   2) rand(1, 10)   3) random.randint(1, 10)   4) randint(1, 10)")
            q5 = int(input('Your answer: '))
            if q5 == 3:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct function is random.randint(1, 10)')
        
        elif question_num == 6:
            print("6. What will be the output of the following code?")
            print("   for i in range(3):")
            print("       print(i)")
            print("   1) 0 1 2   2) 1 2 3   3) 0 1 2 3   4) 1 2")
            q6 = int(input('Your answer: '))
            if q6 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The output will be 0 1 2')
        
        elif question_num == 7:
            print("7. Which of the following is the correct way to start a for loop in Python?")
            print("   1) for i in [1, 2, 3]:   2) for (i = 0; i < 3; i++):")
            print("   3) for i = 1 to 3:   4) for i in range(3)")
            q7 = int(input('Your answer: '))
            if q7 == 1 or q7 == 4:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct ways are for i in [1, 2, 3]: or for i in range(3):')
        
        elif question_num == 8:
            print("8. What is the output of print(2 ** 3)?")
            print("   1) 6   2) 8   3) 9   4) Error")
            q8 = int(input('Your answer: '))
            if q8 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! 2 ** 3 equals 8')
        
        elif question_num == 9:
            print("9. How do you create a function in Python?")
            print("   1) function myFunc()   2) def myFunc()")
            print("   3) create myFunc()   4) myFunc() = function")
            q9 = int(input('Your answer: '))
            if q9 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct syntax is def myFunc():')
        
        elif question_num == 10:
            print("10. What is the purpose of the return statement in a function?")
            print("   1) To return to the previous menu   2) To exit the function")
            print("   3) To send a value back to the caller   4) To print a value")
            q10 = int(input('Your answer: '))
            if q10 == 3:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The return statement sends a value back to the caller')
        
        print(f"Score: {correct}/10")
        print()

    print("Congratulations! You passed Test #2!")
    print("You have completed both programming tests!")
    return 30  # Return happiness increase

def run_test_3():
    """Run programming test #3: Debugging"""
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
            print("2. What will be the output of the following code?")
            print("   x = 5")
            print("   if x == 5:")
            print("       print('Hello')")
            print("   1) Hello   2) Nothing   3) Error   4) 5")
            q2 = int(input('Your answer: '))
            if q2 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The code prints Hello')
        
        elif question_num == 3:
            print("3. What is the correct way to write an if statement in Python?")
            print("   1) if x == 5:   2) if (x == 5)   3) if x = 5:   4) if x == 5 then")
            q3 = int(input('Your answer: '))
            if q3 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The answer is if x == 5:')
        
        elif question_num == 4:
            print("4. How do you write an else if statement in Python?")
            print("   1) else if   2) elif   3) elseif   4) else_if")
            q4 = int(input('Your answer: '))
            if q4 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The answer is elif')
        
        elif question_num == 5:
            print("5. What is the output of the following code?")
            print("   for i in range(3):")
            print("       print(i)")
            print("   1) 0 1 2   2) 1 2 3   3) 0 1 2 3   4) 1 2")
            q5 = int(input('Your answer: '))
            if q5 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The output will be 0 1 2')
        
        elif question_num == 6:
            print("6. How can you generate a random number between 1 and 10 in Python?")
            print("   1) random(1, 10)   2) rand(1, 10)   3) random.randint(1, 10)   4) randint(1, 10)")
            q6 = int(input('Your answer: '))
            if q6 == 3:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct function is random.randint(1, 10)')
        
        elif question_num == 7:
            print("7. What is the correct syntax for a while loop?")
            print("   1) while x > 5:   2) while (x > 5)   3) while x > 5 do   4) while x > 5")
            q7 = int(input('Your answer: '))
            if q7 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct syntax is while x > 5:')
        
        elif question_num == 8:
            print("8. What is the output of print(2 ** 3)?")
            print("   1) 6   2) 8   3) 9   4) Error")
            q8 = int(input('Your answer: '))
            if q8 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! 2 ** 3 equals 8')
        
        elif question_num == 9:
            print("9. How do you create a function in Python?")
            print("   1) function myFunc()   2) def myFunc()")
            print("   3) create myFunc()   4) myFunc() = function")
            q9 = int(input('Your answer: '))
            if q9 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The correct syntax is def myFunc():')
        
        elif question_num == 10:
            print("10. What is the purpose of the return statement in a function?")
            print("   1) To return to the previous menu   2) To exit the function")
            print("   3) To send a value back to the caller   4) To print a value")
            q10 = int(input('Your answer: '))
            if q10 == 3:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! The return statement sends a value back to the caller')
        
        print(f"Score: {correct}/10")
        print()

    print("Congratulations! You passed Test #3!")
    print()
    return 30  # Return happiness increase

def run_test_4():
    """Run programming test #4: Decision Making - When to Seek Help"""
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
            print("2. You don't understand a concept after reading the documentation. What do you do?")
            print("   1) Keep reading the documentation until you understand")
            print("   2) Search for a tutorial or example code")
            print("   3) Ask a friend for help   4) Give up")
            q2 = int(input('Your answer: '))
            if q2 == 2:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! It\'s often helpful to see an example')
        
        elif question_num == 3:
            print("3. You're getting an unexpected output from your code. What should you do first?")
            print("   1) Print debug information to understand the issue")
            print("   2) Check if there's a typo in your code")
            print("   3) Assume it's a Python bug and reinstall Python")
            print("   4) Ask AI what went wrong")
            q3 = int(input('Your answer: '))
            if q3 == 1:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! Printing debug information is a good first step')
        
        elif question_num == 4:
            print("4. How do you feel about asking for help on programming forums?")
            print("   1) It's a great way to get help and learn from others")
            print("   2) I prefer not to, I can solve it myself")
            print("   3) Only if I'm really stuck   4) It's embarrassing to ask for help")
            q4 = int(input('Your answer: '))
            if q4 == 1 or q4 == 3:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! Asking for help is a valuable part of the learning process')
        
        elif question_num == 5:
            print("5. You've solved a tough problem. What should you do next?")
            print("   1) Move on to the next problem")
            print("   2) Take a break and relax")
            print("   3) Write a blog post about the solution")
            print("   4) Help others who are stuck on the same problem")
            q5 = int(input('Your answer: '))
            if q5 == 2 or q5 == 4:
                correct += 1
                print('You got that right!')
            else:
                print('Wrong! Taking breaks and helping others are both great options')
        
        print(f"Score: {correct}/5")
        print()

    print("Congratulations! You passed Test #4!")
    print("You have completed all programming tests!")
    return 30  # Return happiness increase
