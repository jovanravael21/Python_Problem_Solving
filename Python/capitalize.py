def solve(s):
    words = s.split(" ")
    capitalized = []
    for word in words:
        if word:
            capitalized.append(word.capitalize())
        else:
            capitalized.append("")
    return " ".join(capitalized)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
