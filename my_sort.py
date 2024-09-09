"""" //// """

class STATE(Enum):
    digits = 0
    ops = 1

class MyEval():
    """moy eval"""
    def __init__(self):
        self._ops = {'+':1, '-':1, '/':2, '*':2}
        self._digits = "0123456789"
        self._brackets = "()"
    def tokens(self, s:str) -> list:
        """разбираем строку на токены"""
        # Здесь надо определить, что есть токен.
        ls = []
        token = ""
        state = "digits"
        def is_number(n: str) -> bool:
            """ Истина, если строка есть число """
             
        def is_token(pattern: str) -> bool:
            """ Это токен или нет """
            t_list=['(', ')', '+', '-', '*', '/', is_number, '**', 'sqrt']

        first_t=next_t=0
        while (next_t < последний индекс s):
            while (is_token(s[first_t:next_t])):
                next_t++
            next_t--
            ls += [ s[first_t:next_t] ]
            first_t = next_t
        # как-то так

        def len_token(st: str):
            nonlocal token
            nonlocal state
            nonlocal ls
            if len(token) > 0:
                ls.append(token)
            token = ""
            state = st
            token += i
        for i in s:
            match state:
                case "digits":
                    if i in self._digits:
                        token += i
                    if i in self._ops:
                        if len(token) == 0 and i == "-":
                            token +=i
                            continue
                        len_token("ops")
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
                        ls.append(token)
                        token = ""
                        state = "brackets"
                        token += i

                case "brackets":
                    if i in self._digits:
                        ls.append(token)
                        token = ""
                        state = "digits"
                        token += i
                    if i in self._ops:
                        if token == "(" and i == "-":
                            ls.append(token)
                            token = ""
                            state = "digits"
                            token += i
                            continue
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
        for i in s: 
            print(f"Токен={i}, Стек={stack}")
            if i.lstrip("-").isdigit():
                print (i, "число - добавляем в строку")
                out.append(i)
                print("строка =", out)
                continue
            if i in self._ops:
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
            if i == "(":
                stack.append(i)
                continue
            if i == ")":
                while stack[-1] != "(":
                    out += stack.pop()
                stack.pop()
                continue

        for i in range(len(stack)):
            out += stack.pop()
            #print(out,stack,brackets)
        print(stack)

        return out
    
    def Evaluate(self,value: list):
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
                
             

j = MyEval()
print(j.tokens("12+5*3/4"))
data = j.post_fix(j.tokens("12+5*3/4"))
print(data, "result")
j.Evaluate(data)
    
    
