
def longest_substring(input):

    substring = []
    result = 0

    for letter in input:
        if letter in substring:
            if len(substring) > result:
                result = len(substring)
            substring = [letter]
            continue
        substring.append(letter)

    return result
