# You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

# TODO:
"""
Valid email addresses must follow these rules:
1. It must have the username@websitename.extension format type.
2. The username can only contain letters, digits, dashes and underscores.
    [a-z],[A-Z],[0-9],[_-]
3. The website name can only have letters and digits
4. The extension can only contain letters 
    [a-z],[A-Z]
5. The maximum length of the extension is 3
"""

"""
Concept
A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. 
A Lambda function can be used with filters.
A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. 
A Lambda function can be used with filters.
"""
import re
email_pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
# The pattern is explained as follows:
# ! ^[a-zA-Z0-9_-]+ : The username can only contain letters, digits, dashes and underscores.
# ! @ : The @ symbol is mandatory in the email address.
# ! [a-zA-Z0-9]+ : The website name can only have letters and digits.
# ! \. : The dot before the extension is mandatory.
# ! [a-zA-Z]{1,3}$ : The extension can only contain letters and its maximum length is 3.
# ! The $ symbol indicates the end of the string.

def fun(s):
    if re.match(email_pattern, s):
        return True
    else:
        return False
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)