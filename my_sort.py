"""" //// """
class MyEval():
    """moy eval"""
    def __init__(self):
        self._ops = {'+':1, '-':1, '/':2, '*':2}
        self._digits = "0123456789"
        self._brackets = "()"
    def tokens(self, s:str) -> list:
        """разбираем строку на токены"""
        ls = []
        token = ""
        state = "digits"
        for i in s:
            match state:
                case "digits":
                    if i in self._digits:
                        token += i
                    if i in self._ops:
                        if len(token) > 0:
                            ls.append(token)
                        token = ""
                        state = "ops"
                        token += i
                    if i in self._brackets:
                        if len(token) > 0:
                            ls.append(token)
                        token = ""
                        state = "brackets"
                        token +=i
                case "ops":
                    if i in self._digits:
                        ls.append(token)
                        token = ""
                        state = "digits"
                        token += i
                    if i in self._ops:
                        continue
                    if i in self._brackets:
                        ls.append(i)

                case "brackets":
                    if i in self._digits:
                        ls.append(token)
                        token = ""
                        state = "digits"
                        token += i
                    if i in self._ops:
                        if len(token) > 0:
                            ls.append(token)
                        token = ""
                        state = "ops"
                        token += i
                    if i in self._brackets:
                        if len(token) > 0:
                            ls.append(token)
                        token = ""
                        state = "ops"
                        token += i

        ls.append(token)
        token = ""

        return ls
               
    def post_fix(self, s):
        """aboba"""
        stack = []
        out = []
        print(s,"s ravno")
        for i in s: 
            print(f"Токен={i}, Стек={stack}")
            if i.isdigit():
                print (i, "число - добавляем в строку")
                out.append(i)
                print("строка =", out)
                continue
            if i in self._ops.keys():
                try:
                    while self._ops[i] <= self._ops[stack[-1]]:  
                        print( i , "меньше или равно", stack[-1], "добавляем в обратном порядке к строке")      
                        out.append(stack.pop())
                except IndexError:
                    print("Стек пустой")
                except KeyError:
                    print("В стеке не операция")
                stack.append(i)
                continue
            if i in "()":
                if i == "(":
                    stack.append(i)
                    continue
                else:
                    while stack[-1] != "(":
                        out += stack.pop()
                    stack.pop()
                continue

        for i in range(len(stack)):
            out += stack.pop()
            #print(out,stack,brackets)
        return out
    
    # def Evaluate(self,input):
    #     """" вычисляем """
    #     digits = "0123456789"
    #     stack = []
    #     for i in input:
    #         if i in digits:
    #             stack.append(i)
    #         else:
    #             b = (stack[-2] + i + stack[-1])
    #             #print(b,"boba")
    #             #print(type(b))
    #             m = str(eval(b))
    #             stack.pop()
    #             stack.pop()
    #             stack.append(m)
    #     print(stack) 

j = MyEval()
print(j.tokens("51+1"))
# data = j.postfix(j.tokens("12+43*52"))
# print(data)
#j.Evaluate(data)
    
    
