def checkPalindrome(s):
    return helper(s, 0, len(s) - 1, 1)

def helper(s, start, end, error):
    if start == end:
        return True

    if start == end - 1 and s[start] == s[end]:
        return True
    
    if s[start] == s[end]:
        return helper(s, start + 1, end - 1, error)
    elif error > 0:
        return helper(s, start + 1, end, error - 1) or helper(s, start, end - 1, error - 1)
    
    return False

print(checkPalindrome('abccbca'))
print(checkPalindrome('abbcbca'))