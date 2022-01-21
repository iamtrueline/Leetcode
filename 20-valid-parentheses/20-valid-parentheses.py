class Solution(object):
    def isValid(self, s):
        li = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                li.append(s[i])
            else:
                if len(li) == 0 and (s[i] == ")" or s[i] == "}" or s[i] == "]"):
                    return False
                elif li[-1] == "(" and s[i] == ")":
                    li.pop()
                elif li[-1] == "{" and s[i] == "}":
                    li.pop()
                elif li[-1] == "[" and s[i] == "]":
                    li.pop()
                else:
                    return False
        if len(li) == 0:
            return True
        else:
            return False