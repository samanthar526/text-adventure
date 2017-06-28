direction=False
word=False
choice=False
start = '''
You're in the woods, and have no idea why you're there. Find your way out.
'''


print(start)


print("You encounter two different trails. Do you choose to go left or right?")
user_input = input()
while not direction:
    if user_input == "left":
        print("You decide to go left and encounter a pack of wolves ")
        decision_1=input("Do you choose to fight or run away?")
        direction=True
        while not word:
            if decision_1=="fight":
                print("You die :(")
                word = True
            elif decision_1=="run away":
                print("You ran and got away from the pack of wolves. You found your way out of the woods")
                word = True
            else:
                decision_1=input("Do you choose to fight or run away?")

    elif user_input == "right":
        print("You choose to go right and encounter a river")
        decision_2=input("Swim across or find another way around?")
        direction=True
        while not choice:
            if decision_2=="swim across":
                print("You can't swim beacuse the current is too strong so you drown :(")
                choice=True
            elif decision_2=="find another way around":
                print("You find a way out")
                choice=True
            else:
                decision_2=input("Swim across or find another way around?")
    else:
        user_input=input("You encounter two different trails. Do you choose to go left or right?")
