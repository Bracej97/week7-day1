import unittest

class TestPalindromeCheck(unittest.TestCase):
    def test_palindrome_check(self):
        self.assertTrue(palindrome_check("hannah"))
        self.assertFalse(palindrome_check("test"))

def palindrome_check(word):
    palindrome = True
    length = len(word)
    y = 1
    for x in word:
        if x == word[length - y]:
            y += 1
            continue
        else:
            palindrome = False
            y += 1
    return palindrome

class TestAlphabetCheck(unittest.TestCase):
    def test_alphabet_test(self):
        self.assertTrue(alphabet_check("hello"))
        self.assertFalse(alphabet_check("123"))

def alphabet_check(word):
    alphabet_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = True
    for y in word:
        if y in alphabet_letters:
            continue
        else:
            alphabet = False
    return alphabet


if __name__ == '__main__':
    unittest.main()
