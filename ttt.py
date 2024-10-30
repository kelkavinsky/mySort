#!/usr/bin/env python3 

import re
from enum import Enum

class TOKEN_TYPE(Enum):
    """
    Класс типа токена.
    """
    NUMBER = 0
    OPERATOR = 1
    BRACKET = 2


class Token():
    """
    Класс для токена.
    Атрибуты
    --------
    data : str
    type : TOKEN_TYPE
    """
    
    operators = [ 
        {'+': 0}, 
        '-', 
        {'*': 1}, 
        '/', 
        '**' 
        ]

    def __new__(self, data):
        """
        Создаёт новый экземпляр класса из строки.
        """
        rc = super(Token, self).__new__(self)
        rc.data = data
        rc.type = None
        if rc.is_token(data):
            return rc
            # if rc.type == TOKEN_TYPE.OPERATOR
            #     rc.data = operators   
            # return rc
        return None

    def __repr__(self):
        return(f"('{self.data}', {self.type})")

    def find_op(self, op: str) -> Operator:
        for x in :
            if x == op:
                return

    def is_number(self, n: str) -> bool:
        return re.match(r'^-?\d+\.?\d*$', n)

    def is_token(self, pattern: str) -> bool:
        """ Это токен или нет """
        if len(pattern) == 0:
            return True
        t_list=['+', '-', '*', '/', '**' ]
        if pattern in ['(',')']:
            self.type = TOKEN_TYPE.BRACKET
            return True
        if pattern in t_list:
        #if pattern in [ z.data for z in t_list ]:
            self.type = TOKEN_TYPE.OPERATOR
            return True
        if self.is_number(pattern):
            self.type = TOKEN_TYPE.NUMBER
            return True
        return None


class MyEval():
    def __init__(self, s=None):
        self.last_token = None
        self.compiled = None
        if s is not None:
            self.compiled = self.tokens(s)

    def __repr__(self):
        return(f"self.compiled = {self.compiled}")

    def tokens(self, s:str) -> list:
        """разбираем строку на токены"""
        ls = list()
        start_pos = 0
        end_pos = 0
        while end_pos < len(s):
            while token := Token(s[start_pos:end_pos]):
                self.last_token = token
                end_pos +=1
                if end_pos > len(s):
                    break
            end_pos -= 1
            ls.append(self.last_token)
            start_pos = end_pos
        return ls

class Sortir():
    def __init__(self, s):
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
                    try:
                        while stack[-1] != "(":
                            output.append(stack.pop())
                        stack.pop()
                    except IndexError:
                        continue
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
                stack.append(str(eval(result)))
        return stack

if __name__== "__main__":
    j = MyEval('(25+5)*3')
    print(j)
    j = MyEval()
    print(j)
    t = j.tokens('(25+5)*3')
    print(t)
    m = j.post_fix(t)
    print(m)
    print(j.Evaluate(m))

        
