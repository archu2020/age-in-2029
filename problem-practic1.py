# The task is “Your Age In 2029”.
# This task without using any type of modules like DateTime or date utils

print("Do you want to know your age at 2029?")
while(True):
    inp = input("Enter your current age or Birth of year\n")
    if inp.isnumeric():
        inp1=int(inp)
    else:
        print("Invald input try again!!")
        continue
    if inp1>1800 and inp1<2020:
        print("You entered your Birth of year!")
        print(f"Your age at 2029 will be {2029-inp1} years")
        break
    elif inp1>2020:
        print("You are not yet born")
        break
    elif inp1<100:
        print("you entered your age!")
        print(f"Your age at 2029 will be {2029-(2020-inp1)} years")
        break
    elif inp1>100 and inp1<160:
        print("you seem to be the oldest person alive")
        print(f"Your age at 2029 will be {2029-(2020-inp1)} years")
        break
    elif inp1==2020:
        print("you seem new born")
        print(f"Your age at 2029 will be {2029-inp1} years")
        break
    else:
        print("Invalid Try again!!")

