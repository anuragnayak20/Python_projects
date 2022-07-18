import random 
#import time

options = {
    1 : "Rock",
    2 : "Paper",
    3 : "Scissors"
}

def user_play(choice):
    for i in options.keys():
        if i == choice:
            print(f"User : {options.get(i)}")
            return i
    

def computer_play():
    choice = random.randint(1,4) #3+1=4
    for i in options.keys():
        if i == choice:
            print(f"Computer : {options.get(i)}")
            return i

def choose_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
        return "t"
    elif user_choice == 1 and computer_choice == 3:
        print("User won!")
        return "u"
    elif user_choice == 2 and computer_choice == 1:
        print("User won!")
        return "u"
    elif user_choice == 3 and computer_choice == 2:
        print("User won!")
        return "u"
    else:
        print("Computer won")
        return "c"
    
if __name__ == "__main__":
    results=[]
    play_count = 1
    while play_count <= 6:
        choice = int(input("Enter your choice(1-R,2-P,3-S) : "))
        u = user_play(choice)
        c = computer_play()
        results.append(choose_winner(u,c))
        play_count+=1
    
    print(f" Results : {results}")
    user_win_perc = (results.count("u")/len(results))*100
    comp_win_perc = (results.count("c")/len(results))*100
    tie_perc = (results.count("t")/len(results))*100

    print(f"User win % :{user_win_perc} Computer win % : {comp_win_perc} Tie %:{tie_perc}")


    