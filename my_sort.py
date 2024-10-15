"""123"""
import re
from enum import Enum
class TOKEN_TYPE(Enum):
    """enum"""
    NUMBER = 0
    OPERATOR = 1
    BRACKET = 2
class MyEval():
    """moy eval"""
    def __init__(self):
        self._ops = {'+':1, '-':1, '/':2, '*':2}
        self._digits = "0123456789"
        self._brackets = "()"
        self.state = TOKEN_TYPE.NUMBER
    class Token():
        """123"""
        def __init__(self, data,typ3):
            self.data = data
            self.type = typ3
    def tokens(self, s:str) -> list:
        """разбираем строку на токены"""
        ls = []
        def is_number(n: str) -> bool:
            a = re.compile(r'^-?\d+\.?\d*$')
            return a.match(n)  
        def is_token(pattern: str) -> bool:
            """ Это токен или нет """
            t_list=['+', '-', '*', '/', '**', 'sqrt','']
            if pattern in ['(',')']:
                self.state = TOKEN_TYPE.BRACKET
                return True
            if pattern in t_list:
                self.state = TOKEN_TYPE.OPERATOR
                return True
            if is_number(pattern):
                if pattern[0] == '-' and len(ls)>0:
                    return None   
                self.state = TOKEN_TYPE.NUMBER
                return True
            return None
        start_pos = 0
        end_pos = 0
        while end_pos < len(s):
            while is_token(s[start_pos:end_pos]):
                end_pos +=1
                if end_pos > len(s):
                    break
            end_pos -= 1
            ls.append(self.Token(s[start_pos:end_pos], self.state))
            start_pos = end_pos
        return ls
    
    def post_fix(self, s):
        """123"""
        stack = []
        output = []
        i = 0
        for i in s:
            if i.type == TOKEN_TYPE.NUMBER:
                output.append(i)
                continue
            if i.type == TOKEN_TYPE.OPERATOR:
                try:
                    while self._ops[i.data] <= self._ops[stack[-1]]:
                        output.append(stack.pop())
                except IndexError:
                    print('stek pustoi')
                except KeyError:
                    print('v steke ne operazia')
                stack.append(i)
            if i.type == TOKEN_TYPE.BRACKET:
                if i.data == "(":
                    stack.append(i)
                    continue
                if i.data == ")":
                    while stack[-1] != "(":
                        output += stack.pop()
                    stack.pop()
                    continue
        while len(stack) >= 0:
            try:
                output.append(stack.pop())
            except IndexError:
                break
        return output
    def Evaluate(self,value):
        """" вычисляем """
        stack = []
        for i in value:
            if i.type == TOKEN_TYPE.NUMBER:
                stack.append(i.data)
            if i.type == TOKEN_TYPE.OPERATOR:
                result = stack.pop(-2) + i.data + stack.pop(-1)
                print(result)
                stack.append(str(eval(result)))
        return stack

if __name__== "__main__":
    j = MyEval()
    m = j.post_fix(j.tokens('12+58'))
    print(j.Evaluate(m))

        
