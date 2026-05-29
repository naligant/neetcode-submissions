class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1, list2 = list(s), list(t)
        list1.sort()
        list2.sort()
        list1, list2 =  "".join(list1), "".join(list2)
        
        if list1 != list2:
            return False
        else:
            return True