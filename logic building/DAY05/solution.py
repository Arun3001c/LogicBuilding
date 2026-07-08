#first solution
def sum_of_digits():
    try:
        number = int(input("Enter a number: "))
        if number<0:
            print("Please enter a non-negative integer.")
            return
        total = 0
        while number>0:
            total+=number%10
            number//=10
        print("The sum of digits is:", total)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
sum_of_digits()

#second solution
def is_vowel():
    vowels="aeiouAEIOU"
    char=input("enter a character: ")
    if len(char)!=1:
        print("Please enter a single character.")
        return
    else:
        if char in vowels:
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is not a vowel.")
is_vowel()

#3rd solution
char=input("enter a character:")
print("ASCII value of", char, "is", ord(char))

# ASCII (American Standard Code for Information Interchange)
# - ASCII is a character encoding standard.
# - It contains 128 characters (values 0 to 127).
# - It includes English letters, digits, punctuation, and control characters.
# - Examples:
#     'A' = 65
#     'a' = 97
#     '0' = 48
#
# Unicode
# - Unicode is a universal character encoding standard.
# - It includes ASCII as its first 128 characters.
# - It supports characters from almost all languages, symbols, and emojis.
# - Every character has a unique Unicode code point.
#
# Python
# - Python uses Unicode for characters.
# - ord(character) returns the Unicode code point.
# - For ASCII characters, the Unicode code point is the same as the ASCII value.
# - chr(number) converts a Unicode code point back to its character.
# ============================================================
# Difference Between ASCII and Unicode
# ------------------------------------------------------------
# ASCII:
# • Contains only 128 characters.
# • Mainly supports English characters.
# • Values range from 0 to 127.
#
# Unicode:
# • Contains over 149,000 characters.
# • Supports almost all languages and symbols.
# • Includes ASCII as its first 128 characters.
#
# For the first 128 characters:
# ASCII value == Unicode code point
#
# Example:
#     'A' -> ASCII = 65, Unicode = 65
#
# ============================================================
# Unicode Code Point
# ------------------------------------------------------------
# • Every character in Unicode has a unique number called
#   a Unicode code point.
# • It uniquely identifies that character.
# • Code points are usually written in hexadecimal using
#   the format U+XXXX.
#
# Examples:
#     'A'  -> U+0041 (decimal 65)
#     'a'  -> U+0061 (decimal 97)
#     '😊' -> U+1F60A (decimal 128522)
#
# ============================================================
# ord() Function
# ------------------------------------------------------------
# Syntax:
#     ord(character)
#
# Purpose:
# • Returns the Unicode code point (integer) of a character.
#
# Examples:
#     ord('A')   -> 65
#     ord('a')   -> 97
#     ord('0')   -> 48
#     ord('😊')  -> 128522
#
# ============================================================
# chr() Function
# ------------------------------------------------------------
# Syntax:
#     chr(integer)
#
# Purpose:
# • Converts a Unicode code point (integer) into its
#   corresponding character.
#
# Examples:
#     chr(65)      -> 'A'
#     chr(97)      -> 'a'
#     chr(48)      -> '0'
#     chr(128522)  -> '😊'
#
# ord() and chr() are opposite operations:
#
#     Character --ord()--> Unicode code point
#     Code point --chr()--> Character
#
# Example:
#     ord('A') = 65
#     chr(65) = 'A'
#
# ============================================================