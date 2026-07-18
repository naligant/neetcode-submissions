class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_text = ""
        for i in range(len(list(s))):
            if s[i].isalnum():
                cleaned_text += s[i]
        cleaned_text = list(cleaned_text)
        print(cleaned_text)
        print(cleaned_text[::-1])
        if cleaned_text == cleaned_text[::-1]:
            return True
        else:
            return False