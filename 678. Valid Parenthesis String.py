class Solution:
    def checkValidString(self, s: str) -> bool:
        "((**" #Valid
        "))**"#Not valid
        "**(("#Not valid
        "**)"
        "(()"
        open = closed = stars = 0
        for c in s:
            match c:
                case '(':   open += 1
                case ')':   closed += 1
                case '*':   stars += 1
            
            if closed > open and open + stars >= closed:
                stars -= 1
                closed -= 1
            elif closed > open and open + stars < closed:
                return False
        open = closed = stars = 0
        for c in s[::-1]:
            match c:
                case '(':   open += 1
                case ')':   closed += 1
                case '*':   stars += 1
            
            if closed < open and closed + stars >= open:
                stars -= 1
                open -= 1
            elif closed < open and closed + stars < open:
                return False
        return True
