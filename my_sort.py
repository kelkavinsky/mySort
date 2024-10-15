
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
        # Здесь надо определить, что есть токен.

        ls = []
        def is_number(n: str) -> bool:
            a = re.compile(r'^-?\d+\.?\d*$')
            return a.match(n)
        
             
        def is_token(pattern: str) -> bool:
            """ Это токен или нет """
            t_list=['+', '-', '*', '/', '**', 'sqrt']
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
        end_pos = 1
        while (end_pos< len(s)+1):
            if is_token(s[start_pos:end_pos]):
                print(s[start_pos:end_pos-1], 'token')
                end_pos += 1
            else:
                print(s[start_pos:end_pos-1], "добавляем в вывод", self.state)
                ls.append(self.Token(s[start_pos:end_pos-1], self.state))
                print(s[end_pos-1], "след токен")
                # ls.append(s[start_pos:end_pos-1])
                start_pos = end_pos-1

        if is_token(s[start_pos:end_pos]):
            print(s[start_pos:end_pos-1], "добавляем в вывод", self.state)
            ls.append(self.Token(s[start_pos:end_pos-1], self.state))
            
        print(ls)
        k = 0
        while k != len(ls):
            print(ls[k].data, ls[k].type)
            k += 1  
        
        return ls
    
    def post_fix(self, s):
        """123"""
        print('postfix')
        stack = []
        output = []
        i = 0
        for i in s:
            if i.type == TOKEN_TYPE.NUMBER:
                output.append(i.data)
                print(i.data, 'число, запихиваем его в стек')
                continue
            if i.type == TOKEN_TYPE.OPERATOR:
                print(i.data,'operator', stack,'stack')
                try:
                    while self._ops[i.data] <= self._ops[stack[-1]]:
                        output.append(stack.pop())
                        print(stack)
                        print('выпуливаем все операторы')
                except IndexError:
                    print('stek pustoi')
                except KeyError:
                    print('v steke ne operazia')
                stack.append(i.data)
            if i.type == TOKEN_TYPE.BRACKET:
                print(i.data,'skobka')
                if i.data == "(":
                    stack.append(i.data)
                    continue
                if i.data == ")":
                    while stack[-1] != "(":
                        output += stack.pop()
                    stack.pop()
                    continue
     
        return output
        
        
    # def post_fix(self, s):
    #     """aboba"""
        
    #     stack = []
    #     out = []
    #     for i in s: 
    #         print(f"Токен={i}, Стек={stack}")
    #         if :
    #             print (i, "число - добавляем в строку")
    #             out.append(i)
    #             print("строка =", out)
    #             continue
    #         if i in self._ops:
    #             try:
    #                 while self._ops[i] <= self._ops[stack[-1]]:  
    #                     print( i , "меньше или равно", stack[-1], "добавляем в обратном порядке к строке")      
    #                     out.append(stack.pop())
    #             except IndexError:
    #                 print("Стек пустой")
    #             except KeyError:
    #                 print("В стеке не операция")
    #             stack.append(i)
    #             continue
    #         if i == "(":
    #             stack.append(i)
    #             continue
    #         if i == ")":
    #             while stack[-1] != "(":
    #                 out += stack.pop()
    #             stack.pop()
    #             continue

        # for i in range(len(stack)):
        #     out += stack.pop()
        #     #print(out,stack,brackets)
        # print(stack)
        # print(out)
        # return out
    
    def Evaluate(self,value):
        """" вычисляем """
        stack = []
        for i in value:
            # print(i)
            if i.lstrip("-").isdigit():
                stack.append(i)
            if i in self._ops:
                print(stack)
                result = stack.pop(len(stack)- 2) + i + stack.pop(len(stack)-1)
                print(result)
                stack.append(str(eval(result)))
        
        print(stack)
        return stack
                
             

j = MyEval()
expression = j.tokens('(1+5.1)*3-')
m = j.post_fix(expression)
print(m)
    
    
