#########################################################
# BRUTEFORCE SIMPLE
#
# @author       prod3v3loper
# @copyright    (c) 2024, prod3v3loper
# @package      Brutforce
# @subpackage   Website
# @version      1.0
# @since        1.0
# @link         https://www.prod3v3loper.com
#
#########################################################
import string
import itertools
import time
from datetime import datetime

# ANSI color codes for the console
BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"

EMAIL = "email@localhost" # Set the email for login
MAX_PASS_LENGTH = 4

# Example login function
def login(username, password):
    # You replace this function with the actual login logic
    return username == "email@localhost" and password == "adm1#"

# Generator function to produce combinations of passwords
def generate_combinations(max_length=10):
    # Character sets: lowercase letters, uppercase letters, numbers, special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    length = 1
    # A set to ensure that each combination is only created once
    generated_combinations = set()

    while length <= max_length:
        # Systematic generation of all combinations for the current length
        all_combos = list(itertools.product(characters, repeat=length))
        for combo in all_combos:
            combo_string = ''.join(combo)
            # Generate all permutations for the current combination
            if combo_string not in generated_combinations:
                all_permutations = set(itertools.permutations(combo_string))
                for perm in all_permutations:
                    perm_string = ''.join(perm)
                    if perm_string not in generated_combinations:
                        yield perm_string
                        generated_combinations.add(perm_string)

        # Increase the length for the next round of combinations
        length += 1

# Brute force login feature
def brute_force_login(username):
    # Output header
    print(f"{BLUE}/*{'-' * 85}*/")
    print("/*{:^85}*/".format("BRUTEFORCE ATTACK"))
    print(f"/*{'-' * 85}*/")
    print("{}/*{:^85}*/".format(RED, "Don't use for illegal activities"))
    print(f"{RED}/*{'-' * 85}*/\n")
    print(f"{RESET}\n")

    # Record start time and initialize number of attempts
    start_time = datetime.now()
    tries = 0

    for guess_password in generate_combinations(MAX_PASS_LENGTH):
        tries += 1
        print(f"Test combination: {guess_password}")

        if login(username, guess_password):
            elapsed_time = datetime.now() - start_time
            elapsed_ms = elapsed_time.total_seconds() * 1000

            # Password found output
            print(f"{BLUE}\n/*{'-' * 85}*/")
            print("/*{:^85}*/".format("PASSWORD FOUND"))
            print(f"/*{'-' * 85}*/")
            print("/*{:^20}|{:^21}|{:^21}|{:^20}*/".format(
                "Time (ms)", "Tries", "Name", "Password"))
            print("/*{:^20}|{:^21}|{:^21}|{:^20}*/".format(
                f"{elapsed_ms:.3f}", tries, username, guess_password))
            print(f"/*{'-' * 85}*/{RESET}")

            return guess_password

        # Limit output
        if len(guess_password) > MAX_PASS_LENGTH:
            break

    print("No password found")
    return None

# Example call
brute_force_login(EMAIL)