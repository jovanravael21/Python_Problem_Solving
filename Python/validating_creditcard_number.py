# A valid credit card from ABCD Bank has the following characteristics:
"""
► It must start with a 4,5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
"""
import re

credit_card_pattern = r'^[456]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}'

number_input = int(input())
for i in range(number_input):
    credit_card_input = str(input())
    credit_card_number = ""

    for number in credit_card_input:
        if number.isdigit():
            credit_card_number += number

    answer = "Valid"
    if re.match(credit_card_pattern,credit_card_input) and len(credit_card_number)==16:
        if re.search(r'(\d)\1{3,}',credit_card_number):
            answer = "Invalid"
        else:
            answer = "Valid"
    else:
        answer = "Invalid"

    print(answer)