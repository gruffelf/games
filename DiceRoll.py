import random 

print("-----Dice Rolling Simulator-----")

roll = input("Roll a Dice? (y/n) ")
val = int(input("Enter Maximum Value: "))

if roll == "y":
    
    while True:
        
        print(random.randint(1,val))
        ans = input("Roll Again? (y/n) ")        
        if ans == "n":            
            break
        
quit()
