from my_sort import MyEval
j = MyEval()
m = j.Evaluate(j.post_fix(j.tokens('(12+58)*3')))
# print(j.Evaluate(m))
print(type(m[0]),'hehe')