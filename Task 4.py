def isPalindrome(word):
    # If the word has 0 or 1 characters, it is a palindrome
    if len(word) <= 1:
        return True
    # Check if the first and last characters are the same
    if word[0] != word[-1]:
        return False
    # Recursion, check the middle section of the word
    return isPalindrome(word[1:-1])

# examples
print(isPalindrome("apple"))      
print(isPalindrome("hannah"))    
print(isPalindrome("screen"))  
print(isPalindrome("madam")) 
