import re

# ============================================================
# CO1 AT1 - REGULAR EXPRESSION PROGRAMS
# ============================================================


# QUESTION 1: RESUME INFORMATION EXTRACTION SYSTEM
def resume_information_extraction():
    print("\n" + "=" * 60)
    print("QUESTION 1 - RESUME INFORMATION EXTRACTION")
    print("=" * 60)

    resume = """
    Name: Rahul Kumar
    Email: rahul.kumar@gmail.com
    Mobile: 9876543210
    Skills: Python, Java, SQL, Machine Learning
    Experience: 3 years
    """

    name_match = re.search(r"Name:\s*(.*)", resume, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else "Not Found"

    email_match = re.search(r"[\w.-]+@[\w.-]+\.\w+", resume)
    email = email_match.group() if email_match else "Not Found"

    mobile_match = re.search(r"\b\d{10}\b", resume)
    mobile = mobile_match.group() if mobile_match else "Not Found"

    skill_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
    skills = []

    for skill in skill_list:
        if re.search(r"\b" + re.escape(skill) + r"\b",
                     resume, re.IGNORECASE):
            skills.append(skill)

    experience_match = re.search(
        r"(\d+)\s*(?:years?|yrs?)", resume, re.IGNORECASE
    )
    experience = int(experience_match.group(1)) if experience_match else 0

    print("\n----- CANDIDATE PROFILE -----")
    print("Name       :", name)
    print("Email      :", email)
    print("Mobile     :", mobile)
    print("Skills     :", ", ".join(skills) if skills else "None")
    print("Experience :", experience, "years")

    if experience >= 2 and "Python" in skills:
        print("Eligibility: Eligible")
    else:
        print("Eligibility: Not Eligible")


# QUESTION 2: E-COMMERCE PRODUCT SEARCH SYSTEM
def product_search_system():
    print("\n" + "=" * 60)
    print("QUESTION 2 - E-COMMERCE PRODUCT SEARCH")
    print("=" * 60)

    products = [
        "Apple iPhone 15",
        "Samsung Galaxy S24",
        "OnePlus 12",
        "Apple MacBook Air",
        "Dell Laptop",
        "HP Laptop",
        "Samsung Smart TV",
        "Apple AirPods",
        "OnePlus Earbuds"
    ]

    keyword = input("\nEnter product search keyword: ").strip()

    exact = [
        p for p in products
        if re.search(r"\b" + re.escape(keyword) + r"\b",
                     p, re.IGNORECASE)
    ]

    prefix = [
        p for p in products
        if re.search(r"\b" + re.escape(keyword), p, re.IGNORECASE)
    ]

    suffix = [
        p for p in products
        if re.search(re.escape(keyword) + r"\b", p, re.IGNORECASE)
    ]

    partial = [
        p for p in products
        if re.search(re.escape(keyword), p, re.IGNORECASE)
    ]

    print("\n----- PRODUCT SEARCH REPORT -----")

    for title, matches in [
        ("Exact Keyword Matches", exact),
        ("Prefix Matches", prefix),
        ("Suffix Matches", suffix),
        ("Partial Keyword Matches", partial)
    ]:
        print("\n" + title + ":")
        if matches:
            for p in matches:
                print("-", p)
        else:
            print("No matches found")
        print("Total:", len(matches))


# QUESTION 3: STUDENT REGISTRATION VALIDATION SYSTEM
def registration_validation():
    print("\n" + "=" * 60)
    print("QUESTION 3 - STUDENT REGISTRATION VALIDATION")
    print("=" * 60)

    register_no = input("Student Register Number: ").strip()
    email = input("Institutional Email: ").strip()
    course_code = input("Course Code: ").strip()
    semester = input("Semester: ").strip()
    mobile = input("Mobile Number: ").strip()

    # Example register number: 23AI1234
    register_pattern = r"^\d{2}[A-Za-z]{2,4}\d{4}$"

    # Example institutional email: student@university.edu
    email_pattern = r"^[A-Za-z0-9._%+-]+@university\.edu$"

    # Example course codes: CS101, AI205, DS301
    course_pattern = r"^[A-Za-z]{2,4}\d{3}$"

    # Accepts: 1, 2, ... 8 or Semester 1, Semester 2, ... Semester 8
    semester_pattern = r"^(?:[1-8]|Semester\s*[1-8])$"

    # Indian 10-digit mobile number
    mobile_pattern = r"^[6-9]\d{9}$"

    register_valid = bool(re.fullmatch(register_pattern, register_no))
    email_valid = bool(re.fullmatch(email_pattern, email))
    course_valid = bool(re.fullmatch(course_pattern, course_code))
    semester_valid = bool(
        re.fullmatch(semester_pattern, semester, re.IGNORECASE)
    )
    mobile_valid = bool(re.fullmatch(mobile_pattern, mobile))

    print("\n----- VALIDATION RESULTS -----")
    print("Register Number:",
          "Valid" if register_valid else "Invalid")
    print("Institutional Email:",
          "Valid" if email_valid else "Invalid")
    print("Course Code:",
          "Valid" if course_valid else "Invalid")
    print("Semester:",
          "Valid" if semester_valid else "Invalid")
    print("Mobile Number:",
          "Valid" if mobile_valid else "Invalid")

    all_valid = (
        register_valid and email_valid and course_valid
        and semester_valid and mobile_valid
    )

    print("\n----- FINAL REGISTRATION STATUS -----")
    if all_valid:
        print("Registration Status: SUCCESSFUL")
        print("All student information is valid.")
    else:
        print("Registration Status: FAILED")
        print("Please correct the invalid fields.")


# MAIN PROGRAM
print("\n" + "#" * 60)
print("CO1 AT1 - REGULAR EXPRESSION APPLICATIONS")
print("#" * 60)

resume_information_extraction()
product_search_system()
registration_validation()

print("\n" + "#" * 60)
print("ALL THREE PROGRAMS COMPLETED")
print("#" * 60)
