class Solution:
    def isValid(self, s: str) -> bool:
        
        def valid_bracket(bracket, bracket_type, order_stack):
            if bracket == bracket_type[1] and order_stack[-1] == bracket_type[0]:
                    order_stack.pop()
            else:
                order_stack.append(bracket)
            return order_stack

        type_1 = "()"
        type_2 = "[]"
        type_3 = "{}"

        order_stack = []

        for bracket in s:

            if len(order_stack) == 0:
                order_stack.append(bracket)
            
            else:
                if bracket in type_1:
                    order_stack = valid_bracket(bracket, type_1, order_stack)

                elif bracket in type_2:
                    order_stack = valid_bracket(bracket, type_2, order_stack)

                elif bracket in type_3:
                    order_stack = valid_bracket(bracket, type_3, order_stack)
            
        return True if len(order_stack)==0 else False
            
        