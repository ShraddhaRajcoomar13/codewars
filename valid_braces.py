def valid_braces(string):
    def is_matching_pair(opening, closing):
        pairs = {"(": ")", "{": "}", "[": "]"}
        return pairs.get(opening) == closing
    if not string:
        return True
    for i in range(len(string) - 1):
        if is_matching_pair(string[i], string[i + 1]):
            return valid_braces(string[:i] + string[i + 2:])
    return False
