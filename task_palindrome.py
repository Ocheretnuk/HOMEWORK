def  is_palindrome(s):
    s=s.replace(' ', '')
    s=s.lower()
    if s == s[::-1]: 
        return True
    else:
        return False
