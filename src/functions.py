import random
import sys
from data import characters


def desired_password_length() -> int:
    print('How long do you want you password to be?')
    desired_length = input()

    try:
        password_length = int(desired_length)
        return password_length
    except:
        print('Desired password length provided must be a number')
        sys.exit()


def generate_password(length: int) -> str:
    password = []

    for x in range(length):
        password.append(characters[random.randrange(0, len(characters))])

        shuffled_password = ''.join(random.sample(password, len(password)))

    return shuffled_password
