# Profile Card: Create a formatted profile card using f-strings with name, age, and occupation. Example: "Name: Alice | Age: 28 | Job: Engineer"

name = input("Enter yoyr name: ")
age = input("Enter your age: ")
job = input("Enter your job: ")
Profile_card = f'Name: {name} | Age: {age} | Job: {job}'
print(Profile_card)

# Case Converter: Convert a sentence to title case, uppercase, and lowercase. Show all three versions.

s = "Kamal is A Good Student"
print("original sentence: ",s)
print("In title case: ",s.title())
print("In uppercase: ",s.upper())
print("In lower case: ",s.lower())

# String Statistics: For any input string, display: length, number of spaces, number of digits, and number of alphabetic characters.

s = "Kamal Kumar 123"
length = len(s)
spaces = s.count(" ")
alphabets = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print(f"length of string is {length}")
print(f"no of spaces in the string is {spaces}")
print(f"no of alphabets in the string is {alphabets}")
print(f"No of digits in the string is {digits}")

# Palindrome Detector: Check if a word or phrase is a palindrome (ignoring spaces and case). Examples: "racecar", "A man a plan a canal Panama"

s = input("Enter a string: ")
cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
if cleaned == cleaned[::-1]:
    print("Its a palindrome")
else:
    print("its not a palindrome")

# Email Validator: Extract and validate email parts. Split into username and domain, check for @ symbol and valid domain extension.

email = input("Enter a email id: ")
if "@" in email and "." in email.split("@")[-1]:
    user_name,domain = email.split("@")
   
    print(f"username is {user_name}")
    print(f"domain is {domain}")
else:
    print("Invalid email ")

# Word Frequency Counter: Count occurrences of each word in a sentence (case-insensitive). Display as a formatted list.



# Text Censor: Replace specified words in text with asterisks of the same length. Preserve the original word lengths.

# Name Formatter: Convert names between formats: "First Last" ↔ "Last, First" ↔ "Last, F."

# URL Slug Generator: Convert titles to URL-friendly slugs: lowercase, spaces to hyphens, remove special characters.

# Password Strength Checker: Evaluate password strength based on: length (8+), uppercase, lowercase, digits, special characters.

# Text Wrapper: Wrap long text to specified line width, breaking at word boundaries. Add line numbers.

# CSV Parser: Parse a CSV string into a list of dictionaries using the first row as headers.