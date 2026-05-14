from art import logo, vs
from game_data import data
import random
def formated_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"
def check_answer(user_guess, a_followers, b_followers ):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
print(logo)
score = 0
game_continue = True
account_B = random.choice(data)
while game_continue:
    account_A = account_B
    account_B = random.choice(data)
    if account_A == account_B:
        account_B = random.choice(data)
    print(f"Compare A:{formated_data(account_A)}")
    print(vs)
    print(f"Against B:{formated_data(account_B)}")
    guess = input("Who has more followers?, type A or B").lower()
    print("\n" *20)
    print(logo)
    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"Your are right, your current score is: {score}")
    else:
        print(f"Your are wrong, your final score is: {score}")
        game_continue = False

