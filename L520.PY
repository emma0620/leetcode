def detectCapitalUse(word):
    return word.isupper() or word.islower() or word.istitle()


print(detectCapitalUse("USA"))
print(detectCapitalUse("leetcode"))
print(detectCapitalUse("lEETcode"))
print(detectCapitalUse("Leetcode"))
