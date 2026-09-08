def is_palindrome(s: str) -> bool:
    s = s.strip().lower()
    return s == s[::-1]
