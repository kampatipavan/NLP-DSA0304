# ============================================================
# CO1 AT-3
# Python Programs using DFA and Regular Expressions
# ============================================================
# QUESTION 1: DFA SIMULATOR
# QUESTION 2: REGULAR EXPRESSION TEXT SEARCH ENGINE
# QUESTION 3: EMAIL, PASSWORD AND MOBILE VALIDATION
# ============================================================

import re


# ============================================================
# QUESTION 1
# PYTHON-BASED DETERMINISTIC FINITE AUTOMATA (DFA) SIMULATOR
# ============================================================

def dfa_simulator():
    print("\n" + "=" * 65)
    print("QUESTION 1 - DFA SIMULATOR")
    print("=" * 65)

    print("\nExample DFA: Strings ending with 'ab'")
    print("States: q0, q1, q2")
    print("Alphabet: a, b")

    # DFA transition table for strings ending with "ab"
    transitions = {
        "q0": {"a": "q1", "b": "q0"},
        "q1": {"a": "q1", "b": "q2"},
        "q2": {"a": "q1", "b": "q0"}
    }

    initial_state = "q0"
    final_states = {"q2"}

    n = int(input("\nEnter number of input strings: "))

    for i in range(n):
        string = input(f"Enter string {i + 1}: ")

        current_state = initial_state
        path = [current_state]
        valid_input = True

        for symbol in string:
            if symbol in transitions[current_state]:
                current_state = transitions[current_state][symbol]
                path.append(current_state)
            else:
                valid_input = False
                break

        print("\nInput String:", string)
        print("Transition Path:")
        print(" -> ".join(path))

        if valid_input and current_state in final_states:
            print("Accepted")
        else:
            print("Rejected")


# ============================================================
# QUESTION 2
# REGULAR EXPRESSION TEXT SEARCH ENGINE
# ============================================================

def text_search_engine():
    print("\n" + "=" * 65)
    print("QUESTION 2 - REGULAR EXPRESSION TEXT SEARCH ENGINE")
    print("=" * 65)

    text = """Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing"""

    print("\nText to Search:")
    print(text)

    while True:
        print("\n----- SEARCH MENU -----")
        print("1. Search Date")
        print("2. Search Phone Number")
        print("3. Search Hashtag")
        print("4. Search Mention")
        print("5. Search Prefix")
        print("6. Search Suffix")
        print("7. Search Word")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            # Date format: DD/MM/YYYY
            matches = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
            print("\nMatching Dates:", matches)

        elif choice == "2":
            # 10-digit phone number
            matches = re.findall(r"\b[6-9]\d{9}\b", text)
            print("\nMatching Phone Numbers:", matches)

        elif choice == "3":
            # Hashtag
            matches = re.findall(r"#[A-Za-z0-9_]+", text)
            print("\nMatching Hashtags:", matches)

        elif choice == "4":
            # @username
            matches = re.findall(r"@[A-Za-z0-9_]+", text)
            print("\nMatching Mentions:", matches)

        elif choice == "5":
            keyword = input("Enter prefix: ")
            words = re.findall(r"\b[A-Za-z]+\b", text)
            matches = [word for word in words
                       if word.lower().startswith(keyword.lower())]
            print("\nPrefix Matches:", matches)

        elif choice == "6":
            keyword = input("Enter suffix: ")
            words = re.findall(r"\b[A-Za-z]+\b", text)
            matches = [word for word in words
                       if word.lower().endswith(keyword.lower())]
            print("\nSuffix Matches:", matches)

        elif choice == "7":
            keyword = input("Enter word to search: ")
            matches = re.findall(
                r"\b" + re.escape(keyword) + r"\b",
                text,
                re.IGNORECASE
            )
            print("\nWord Matches:", matches)

        elif choice == "8":
            print("Exiting Text Search Engine...")
            break

        else:
            print("Invalid choice. Please select 1-8.")


# ============================================================
# QUESTION 3
# EMAIL, PASSWORD AND MOBILE NUMBER VALIDATION
# ============================================================

def credential_validation():
    print("\n" + "=" * 65)
    print("QUESTION 3 - USER CREDENTIAL VALIDATION")
    print("=" * 65)

    email = input("\nEnter Email Address: ")
    password = input("Enter Password: ")
    mobile = input("Enter Mobile Number: ")

    # --------------------------------------------------------
    # Email Validation
    # Rule:
    # - Must start with an alphabet
    # - Before @: letters, digits, . and _
    # - Domain: alphabets only
    # - Extensions: com, org, edu, net, in
    # --------------------------------------------------------
    email_pattern = (
        r"^[A-Za-z][A-Za-z0-9._]*@"
        r"[A-Za-z]+\.(com|org|edu|net|in)$"
    )

    # --------------------------------------------------------
    # Password Validation
    # - Minimum 8 characters
    # - Uppercase
    # - Lowercase
    # - Digit
    # - Special character from @ # $ % & !
    # --------------------------------------------------------
    password_pattern = (
        r"^(?=.*[A-Z])"
        r"(?=.*[a-z])"
        r"(?=.*\d)"
        r"(?=.*[@#$%&!])"
        r".{8,}$"
    )

    # --------------------------------------------------------
    # Mobile Validation
    # - Exactly 10 digits
    # - First digit 6-9
    # --------------------------------------------------------
    mobile_pattern = r"^[6-9]\d{9}$"

    valid_email = bool(re.fullmatch(email_pattern, email))
    strong_password = bool(re.fullmatch(password_pattern, password))
    valid_mobile = bool(re.fullmatch(mobile_pattern, mobile))

    print("\n----- VALIDATION RESULT -----")

    if valid_email:
        print("Valid Email")
    else:
        print("Invalid Email")

    if strong_password:
        print("Strong Password")
    else:
        print("Weak Password")

    if valid_mobile:
        print("Valid Mobile Number")
    else:
        print("Invalid Mobile Number")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        print("\n" + "#" * 65)
        print("CO1 AT-3 - PYTHON APPLICATIONS")
        print("#" * 65)

        print("\n1. DFA Simulator")
        print("2. Regular Expression Text Search Engine")
        print("3. Email, Password and Mobile Validation")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            dfa_simulator()

        elif choice == "2":
            text_search_engine()

        elif choice == "3":
            credential_validation()

        elif choice == "4":
            print("\nProgram completed successfully.")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()


# ============================================================
# SAMPLE OUTPUTS
# ============================================================
#
# QUESTION 1:
# Enter number of input strings: 1
# Enter string 1: abaab
#
# Input String: abaab
# Transition Path:
# q0 -> q1 -> q2 -> q1 -> q1 -> q2
# Accepted
#
# QUESTION 2:
# Choice: 1
# Matching Dates: ['12/09/2026']
#
# Choice: 2
# Matching Phone Numbers: ['9876543210']
#
# Choice: 3
# Matching Hashtags: ['#NLP']
#
# Choice: 4
# Matching Mentions: ['@OpenAI']
#
# QUESTION 3:
# Email: pavan123@university.edu
# Password: Pavan@123
# Mobile: 9876543210
#
# Valid Email
# Strong Password
# Valid Mobile Number
# ============================================================
