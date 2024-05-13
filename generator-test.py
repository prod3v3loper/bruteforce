#########################################################
# BRUTEFORCE TEST
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

def generate_combinations(max_length=3):

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

# Example of testing the generator
for pwd in generate_combinations(3):

    # delay between attempts
    # time.sleep(0.1)

    print(pwd)

    # Limit output
    if len(pwd) > 3:
        break
