
import random
# The members to pick from are in the list, and all begin with a capital letter i.e capitalize()
Nas_members = ["Azeez", "Pami", "Deji", "Tolani", "Glory"]
secret_member = random.choice(Nas_members)
print(secret_member)
print("GUESS THE NAS MEMBER")
guess = ""
guesses_made = []
count = 0
# Informing player of tries left and counting tries made
while count < 3:
    print("tries left: " + str(3 - count))
    guess = input("Enter Which member you think it is: ")
    count += 1

    # WIN
    if guess.capitalize() == secret_member:
        print("Congratulations, You won!!!")
        break

    # If a non-NAS member is inputted, player doesn't lose try and the possible options are listed out
    elif guess.capitalize() not in Nas_members:
        print("INVALID INPUT! ... Input one of " + ", ".join(k for k in Nas_members if k not in guesses_made))
        count -= 1

    # If the new guess has been made before, try again but doesnt miss turn:
    elif guess.capitalize() in guesses_made:
        print("Guess already made, try another NAS member")
        count -= 1

    # WRONG ANSWER
    elif guess.capitalize() != secret_member and count < 3:
        guesses_made.append(guess.capitalize())
        print("You are wrong, Try again!")

    # TRIES EXHAUSTED
    elif count == 3:
        print(f"You lose, {secret_member.upper()} was the answer, GAME OVER!!!")
