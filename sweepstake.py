import random

sweepstake_box =set()

while 1:
    print("MENU")
    print("1. Add a coupon sweepstake")
    print("2. Remove a coupon sweepstake")
    print("3. Sweepstake drawing")
    print("4. Exit")

    choice = int(input("Your choice is: "))

    if choice == 1:
        phone_num = input("Enter your phone number: ")
        sweepstake_box.add(phone_num)
    elif choice == 2:
        print(sweepstake_box)
        phone_num_remove = input("Enter your phone number you want to remove: ")
        sweepstake_box.discard(phone_num_remove)
    elif choice == 3:
        index = random.randrange(0, len(sweepstake_box) - 1)
        i = 0 
        for x in sweepstake_box:
            if i == index:
                break
            i = i + 1
        print("Congrat the phone number " + x + " hit the jack-pot")
        sweepstake_box.discard(x)    
    elif choice == 4:
        break
    