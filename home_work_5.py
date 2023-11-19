from random import randint

def casino(money):
    
    while money > 0:
        number = int(input())
        some_money = int(input())
        if number == 0 or some_money > money:
            if some_money > money:
                print("You don't have enough money on your balance")
            else:
                print("Game over")
            break
        elif number == randint(1, 30):
            money += some_money
            print(f"You have won {some_money} som")
        else:
            money -= some_money
            print(f"You have lost {some_money} som")
        print(f"Balance: {money}") 
        


