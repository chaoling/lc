from typing import List, Tuple


def calculate2(s: str) -> int:
        '''
        ()+- , ignore white space
        the other stores the oprand aka numbers 1,2, 12,42 etc.
        '''
        def helper(it):
            stack = []
            num = 0
            sign = 1  # 1 means positive, -1 means negative

            while True:
                try:
                    ch = next(it)
                except StopIteration:
                    break

                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch in '+-':
                    stack.append(sign * num)
                    num = 0
                    sign = 1 if ch == '+' else -1
                elif ch == '(':
                    num = helper(it)
                elif ch == ')':
                    stack.append(sign * num)
                    return sum(stack)
                elif ch == ' ':
                    continue

            stack.append(sign * num)
            return sum(stack)

        return helper(iter(s))

def calculate(s: str) -> int:
    '''
    also consider +-*/
    '''
    from collections import deque
    def helper(chars: deque[str]) -> int:
        stk = []
        operand = 0
        sign = '+' #assume first number is always positive

        while len(chars) > 0:
            c = chars.popleft()
            print(f"now processing... {c=}")
            if c.isdigit():
                operand = operand * 10 + int(c)

            if c == '(':
                operand = helper(chars)

            if  not c.isdigit() and c != ' ' or len(chars) == 0:
                if sign == '+':
                    stk.append(operand)
                elif sign == '-':
                    stk.append(-operand)
                elif sign == '*':
                    stk[-1] = stk[-1] * operand
                elif sign == '/':
                    stk[-1] = int(stk[-1] / operand)

                sign = c 
                operand = 0
            
            if c == ')':
                break
        print(f"{stk=}")
        return sum(stk)
    
    return helper(deque(s))
       



print(calculate('2147483647'))
print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1 + 1)"))
print(calculate("(1+(4+5+2)-3)+(6+8)"))