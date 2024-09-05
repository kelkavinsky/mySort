class myEval():
    def __init__(self):
        self._ops = {'+':1, '-':1, '/':2, '*':2}
        self._digits = "0123456789"
    
    def tokens(self, s:str) -> list:
        # Здесь разобрать строку на токены
        return list(s)

    def postfix(self, s:str) -> list:
        stack = []
        out = []
        
        for i in s: 
            print(f"Токен={i}, Стек={stack}")
            if i in self._digits:
                print (i, "число - добавляем в строку")
                out += i
                continue
            if i in self._ops.keys():
                try:
                    while self._ops[i] <= self._ops[stack[-1]]:  
                        print( i , "меньше или равно", stack[-1], "добавляем в обратном порядке к строке")      
                        out += stack.pop()
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
    
    def Evaluate(input):
        digits = "0123456789"
        stack = []
        for i in input:
            if i in digits:
                stack.append(i)
            else:
                b = (stack[-2] + i + stack[-1])
                #print(b,"boba")
                #print(type(b))
                m = str(eval(b))
                stack.pop()
                stack.pop()
                stack.append(m)
        print(stack) 

j = myEval()
data = j.postfix(j.tokens(input("Ну чо? ")))
print(data)
#j.Evaluate(data)
    
    
