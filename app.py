import itertools

def brute_force_password(password):
    # Define the characters to be used for brute forcing
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    # Generate all possible combinations
    for length in range(1, len(password) + 1):
        for combination in itertools.product(characters, repeat=length):
            attempt = ''.join(combination)
            if attempt == password:
                return attempt

    return None

target_password = 'secretpassword'
result = brute_force_password(target_password)
print("Brute Force Result:", result)
