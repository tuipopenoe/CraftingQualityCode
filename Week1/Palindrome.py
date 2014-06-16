# Tui Popenoe
# Palindrom: Algorithm 1

def is_palindrome_v1(s):
    """ (str) -> bool

    Return True if and only if s is a is_palindrome
    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('dented')
    False
    """
    return reverse(s) == s

def is_palindrome_v2(s):
    """ (str) -> bool

    Return True if and only if s is a is_palindrome
    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('dented')
    False
    """
    n = len(s)

    return s[:n/2] == reverse(s[n-n/2:])

def is_palindrome_v3(s):
    """ (str) -> bool

    Return True if and only if s is a is_palindrome
    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('dented')
    False
    """
    i = 0
    j = len(s)-1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j -1

    return j <= i

def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''
    for ch in s:
        rev = ch + rev

    return rev
