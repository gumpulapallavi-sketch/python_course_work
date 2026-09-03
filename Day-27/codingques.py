#1. Reverse a Number
# Write a Python program to reverse the digits of a given integer.
'''
num = int(input("Enter an integer: "))
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)
'''
# 2. Check Palindrome Number
# Write a Python program to check whether a given number is a palindrome.
'''
num = int(input("Enter an integer: "))
original = num
reverse = 0

while num> 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
 

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
    '''

#3. Check Prime Number
# Write a Python program to check whether a given number is prime.
'''
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
    '''
#4. Print Prime Numbers in a Range
# Write a Python program to print all prime numbers between two given numbers.
'''
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num)
        '''

#5. Find Factorial
# Write a Python program to find the factorial of a given number.
'''
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)
'''

#6. Generate Fibonacci Series
# Write a Python program to generate the first n Fibonacci numbers.
'''
n = int(input("Enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
    '''
#7. Check Armstrong Number
# Write a Python program to check whether a number is an Armstrong number.
'''
num = int(input("Enter a number: "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    '''

#8. Find GCD of Two Numbers
# Write a Python program to find the greatest common divisor of two integers.
'''
import math

# Program to find GCD of two numbers

# Input two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD
gcd = math.gcd(num1, num2)

# Display result
print(f"The GCD of {num1} and {num2} is {gcd}")
'''

#9. Find LCM of Two Numbers
# Write a Python program to find the least common multiple of two integers.
'''
import math

# Program to find LCM of two numbers

# Input two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate LCM using formula: LCM(a, b) = |a * b| / GCD(a, b)
lcm = abs(num1 * num2) // math.gcd(num1, num2)

# Display result
print(f"The LCM of {num1} and {num2} is {lcm}")
'''

#10. Count Digits in a Number
# Write a Python program to count the number of digits in a given integer.

# Program to count digits in a number

# Input an integer
'''
num = int(input("Enter a number: "))

# Convert number to string and count length
count = len(str(abs(num)))   # abs() handles negative numbers

# Display result
print(f"The number {num} has {count} digits")
'''
# Section 2 - Strings

#11. Reverse a String
# Write a Python program to reverse a string without using the built-in reverse() method.

# Program to reverse a string

# Input a string
'''
text = input("Enter a string: ")

# Reverse using slicing
reversed_text = text[::-1]

# Display result
print(f"The reverse of '{text}' is '{reversed_text}'")
'''

#12. Check String Palindrome
# Write a Python program to check whether a given string is a palindrome.

# Program to check if a string is a palindrome

# Input a string
'''
text = input("Enter a string: ")

# Convert to lowercase for case-insensitive check
text_lower = text.lower()

# Reverse the string using slicing
if text_lower == text_lower[::-1]:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
    '''

#13. Count Vowels and Consonants
# Write a Python program to count the number of vowels and consonants in a string.
# Program to count vowels and consonants in a string

# Input a string
'''
text = input("Enter a string: ")

# Convert to lowercase for easy checking
text_lower = text.lower()

# Define vowels
vowels = "aeiou"

# Initialize counters
vowel_count = 0
consonant_count = 0

# Loop through each character
for char in text_lower:
    if char.isalpha():   # Only check letters
        if char in vowels:    #This avoids counting spaces, numbers, or punctuation.
            vowel_count += 1
        else:
            consonant_count += 1

# Display result
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
'''

#14. Count Character Frequency
# Write a Python program to count the frequency of every character in a string.

# Program to count character frequency in a string

# Input a string
'''
text = input("Enter a string: ")

# Create an empty dictionary to store frequencies
freq = {}

# Loop through each character in the string
for char in text:
    if char in freq:
        freq[char] += 1   # If character already exists, increment count
    else:
        freq[char] = 1    # If character not in dictionary, add it with count 1

# Display result
print("Character frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")
    

                #(or)


from collections import Counter

text = input("Enter a string: ")
freq = Counter(text)

print("Character frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")
    '''

#15. Find First Non-Repeating Character
# Write a Python program to find the first character that occurs only once in a string.

# Program to find the first non-repeating character in a string

# Input a string
'''
text = input("Enter a string: ")

# Loop through each character
for char in text:
    # Check if this character occurs only once
    if text.count(char) == 1:
        print(f"The first non-repeating character is '{char}'")
        break
else:
    print("No non-repeating character found")

                    # (or)

'''   
#16. Remove Duplicate Characters
#Write a Python program to remove duplicate characters from a string while preserving their first occurrence.

# Program to remove duplicate characters from a string

# Input a string
'''
text = input("Enter a string: ")

# Initialize an empty string to store result
result = ""

# Loop through each character
for char in text:
    if char not in result:   # Only add if not already present
        result += char

# Display result
print(f"String after removing duplicates: {result}")

          #(or)

text = input("Enter a string: ")
result = "".join(dict.fromkeys(text))
print(f"String after removing duplicates: {result}")
'''

#17. Check Anagram
# Write a Python program to check whether two strings are anagrams of each other.
# Program to check if two strings are anagrams

# Input two strings
'''
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Convert both strings to lowercase and remove spaces
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if sorted characters are the same
if sorted(str1) == sorted(str2):
    print(f"'{str1}' and '{str2}' are anagrams")
else:
    print(f"'{str1}' and '{str2}' are not anagrams")
                 #(or)

from collections import Counter

str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()

if Counter(str1) == Counter(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
    '''

#18. Find Duplicate Characters
# Write a Python program to find all characters that occur more than once in a string.
# Program to find duplicate characters in a string

# Input a string
'''
text = input("Enter a string: ")

# Create a dictionary to store character frequencies
freq = {}

# Count occurrences of each character
for char in text:
    freq[char] = freq.get(char, 0) + 1

# Display duplicate characters
print("Duplicate characters:")
for char, count in freq.items():
    if count > 1:
        print(f"'{char}' occurs {count} times")

                  # (or)

from collections import Counter

text = input("Enter a string: ")
freq = Counter(text)

print("Duplicate characters:")
for char, count in freq.items():
    if count > 1:
        print(f"'{char}' occurs {count} times")
'''
#19. Count Words in a Sentence
# Write a Python program to count the number of words in a sentence.
# Program to count words in a sentence

# Input a sentence
'''
sentence = input("Enter a sentence: ")

# Split the sentence into words using split()
words = sentence.split()

# Count the number of words
word_count = len(words)

# Display result
print(f"The sentence has {word_count} words")
'''
#20. Find Longest Word
# Write a Python program to find the longest word in a given sentence.

# Program to find the longest word in a sentence

# Input a sentence
'''
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word using max() with key=len
longest_word = max(words, key=len)

# Display result
print(f"The longest word is '{longest_word}' with length {len(longest_word)}")
'''
#21. Reverse Words in a Sentence
# Write a Python program to reverse the order of words in a sentence.

# Program to reverse words in a sentence

# Input a sentence
'''
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join them back into a sentence
reversed_sentence = " ".join(reversed_words)

# Display result
print(f"Reversed sentence: {reversed_sentence}")

              # (or)

sentence = input("Enter a sentence: ")
reversed_sentence = " ".join(reversed(sentence.split()))
print(f"Reversed sentence: {reversed_sentence}")
'''
#22. Reverse Each Word
#Write a Python program to reverse every word in a sentence while keeping the word order unchanged.

# Program to reverse each word in a sentence

# Input a sentence
'''
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Reverse each word individually
reversed_words = [word[::-1] for word in words]

# Join them back into a sentence
reversed_sentence = " ".join(reversed_words)

# Display result
print(f"Reversed words sentence: {reversed_sentence}")
            (or)

# Alternative (using a loop instead of list comprehension):
sentence = input("Enter a sentence: ")
words = sentence.split()

reversed_words = []
for word in words:
    reversed_words.append(word[::-1])

reversed_sentence = " ".join(reversed_words)
print(f"Reversed words sentence: {reversed_sentence}")
'''
#23. Find the Most Frequent Character
# Write a Python program to find the character with the highest frequency in a string.
# Program to find the most frequent character in a string

# Input a string
'''
text = input("Enter a string: ")

# Create a dictionary to store character frequencies
freq = {}

# Count occurrences of each character
for char in text:
    freq[char] = freq.get(char, 0) + 1

# Find the character with maximum frequency
most_frequent = max(freq, key=freq.get)

# Display result
print(f"The most frequent character is '{most_frequent}' occurring {freq[most_frequent]} times")

                        #(or)
from collections import Counter

text = input("Enter a string: ")
freq = Counter(text)

most_frequent = freq.most_common(1)[0]
print(f"The most frequent character is '{most_frequent[0]}' occurring {most_frequent[1]} times")
'''
#24. Remove All Spaces
# Write a Python program to remove all spaces from a string.
# Program to remove all spaces from a string

# Input a string
'''
text = input("Enter a string: ")

# Replace spaces with empty string
no_spaces = text.replace(" ", "")

# Display result
print(f"String without spaces: {no_spaces}")
             #(or)

text = input("Enter a string: ")
no_spaces = "".join(text.split())
print(f"String without spaces: {no_spaces}")
'''

#25. Check if One String Is a Rotation of Another
# Write a Python program to check whether one string is a rotation of another string.

# Program to check if one string is a rotation of another

# Input two strings
'''
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if lengths are equal
if len(str1) != len(str2):
    print("Strings are not rotations (different lengths)")
else:
    # Concatenate str1 with itself
    temp = str1 + str1
    
    # If str2 is a substring of temp, then it's a rotation
    if str2 in temp:
        print(f"'{str2}' is a rotation of '{str1}'")
    else:
        print(f"'{str2}' is not a rotation of '{str1}'")
'''
#26. Longest Common Prefix
# Write a Python program to find the longest common prefix among a list of strings.
# Program to find the longest common prefix among strings
'''
def longest_common_prefix(strings):
    if not strings:
        return ""

    # Start with the first string as the prefix
    prefix = strings[0]

    # Compare with each string in the list
    for s in strings[1:]:
        # Reduce prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # shorten prefix by one character
            if not prefix:
                return ""  # no common prefix

    return prefix


# Example usage
words = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(words))

                    #(or)

def longest_common_prefix(strings):
    prefix = ""
    for chars in zip(*strings):
        if len(set(chars)) == 1:  # all characters same
            prefix += chars[0]
        else:
            break
    return prefix

words = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(words))
'''

#27. Compress a String
# Write a Python program to compress consecutive repeated characters.

# Program to compress consecutive repeated characters

def compress_string(text):
    if not text:
        return ""

    compressed = ""
    count = 1

    # Loop through the string
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1  # increase count if same character repeats
        else:
            compressed += text[i - 1] + str(count)  # add char + count
            count = 1  # reset count

    # Add the last character and its count
    compressed += text[-1] + str(count)

    return compressed


# Example usage
s = input("Enter a string: ")
print("Compressed string:", compress_string(s))

                #(or)

def compress_string(text):
    if not text:
        return ""

    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + (str(count) if count > 1 else "")
            count = 1

    compressed += text[-1] + (str(count) if count > 1 else "")
    return compressed

