class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_dict = {")":"(", "]":"[", "}":"{"}
        order_stack = []

        for bracket in s:
            if bracket in bracket_dict:
                if order_stack and order_stack[-1] == bracket_dict[bracket]:
                    order_stack.pop()
                else: 
                    return False
            else: 
                order_stack.append(bracket)

        return True if not order_stack else False    
