
playing = True
print("Welcome to the Green Glass Door! Would you like to play?")
line = 'Y/N: '
correct = False
user_input = input(line)
if user_input == 'n':
    playing = False
else:
    while playing == True:
        correct = False
        print("-------------------------------------")
        print("Enter a word to see if can go through the Green Glass Door: ")
        answer = input()
        i = 0
        while i < len(answer) - 1:
            if answer[i] == answer[i+1]:
                correct = True
            i+=1
        if correct:            
            print("Yes, " + answer + " can go through the Green Glass Door.")        
        else:
            print("Sorry, " + answer + " cannot go through the Green Glass Door.")
        print("Do you now know the requirements to go through the Green Glass Door?")
        answer = input(line)
        if answer.lower() == 'y':
            print("What does one need to go through the Green Glass Door?")
            user_input = input()
            if user_input.lower() == 'double letters':
                print("Correct!")
            else:
                print("Nope, not quite.")
        print("Would you like to try to send something else through the Green Glass Door?")
        user_input = input(line)
        if user_input.lower() == 'n':
            playing = False

print("Goodbye!")
