import random
x = random.randint(1, 101)
valid_inp = False
count = 0
guess = 0
errors = 0
while not (valid_inp and guess == x):
    try:
        guess = int(input("enter a number between 1 and 100 : "))
        valid_inp = True
        count += 1
        if guess > x:
            print("too high guess")
        if guess < x:
            print("too low guess")
    except:
        print("wrong input")
        errors += 1
        made_error = True

if guess == x and not made_error:
    print(f"you got the answer in {count} trials")
else:
    print(
        f"you got the answer in {count} trials while making {errors} invalid inputs "
    )
