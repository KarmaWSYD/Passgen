# Simple password generator that creates a random password of a given length (default 28) with characters from a-z, A-Z, 0-9, and special characters !@#$%/.;:-_*=+?
# Using python's secrets module https://docs.python.org/3/library/secrets.html#module-secrets instead of random module for better security

import secrets


def passgen(length = 28):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%/.;:-_*=+?"
    password = ""
    for i in range(length):
        password += secrets.choice(alphabet)
    return password

if __name__ == "__main__":
    print(passgen())
    
