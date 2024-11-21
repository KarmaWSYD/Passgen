import secrets

def passgen(length):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%/.;:-_*=+?"
    password = ""
    for i in range(length):
        password += secrets.choice(alphabet)
    return password

if __name__ == "__main__":
    print(passgen(28))
    
