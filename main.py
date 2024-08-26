from game_data import data
import random

print("Welcome to Higher lower game")
score = 0
A = random.choice(data)
game_continue = True


def check_answer():
    if (B['follower_count']>C['follower_count'] and guess == 'b') or (B['follower_count']<C['follower_count'] and guess == 'a'):
        return True
    elif (B['follower_count']>C['follower_count'] and guess == 'a') or (B['follower_count']<C['follower_count'] and guess == 'b'):
        return False


while game_continue:
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    C = A
    data.remove(A)
    B = random.choice(data)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    A = B
    guess = input("Who has more followers ").lower()
    is_correct = check_answer()
    if is_correct:
        score += 1
        print("Correct")
        print(f"Score: {score}")
    else:
        print("Wrong, game over")
        print(f"Total score: {score}")
        game_continue = False

