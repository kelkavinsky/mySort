class myEval():
	
	def postfix():
		ops = {'+':1, '-':1, '/':2, '*':2,"(":0,")":0}
		INPUT = "1+3*2"
		stack = []
		OUTPUT = ""
		a = ""
		brackets = 0
		x = 0
		digits = "0123456789"
		
		for i in INPUT:
			if i in digits:
				print (i, "число - добавляем в строку")
				OUTPUT += i
			
			elif i in ops:
				#if i in "()":
					#if i == "(":
						#stack.append(i)
						#continue
					#else:
						#while stack[-1]!= "(":
							#OUTPUT += stack.pop()

				if len(stack) < 1:
					print("добавляем в стэк", i)
					stack.append(i)
					
			

				
				elif ops[i] <= ops[stack[-1]]:  
					print( i , "меньше или равно", stack[-1], "добавляем в обратном порядке к строке")      
					for j in range(len(stack)):
						OUTPUT += stack.pop()		
					stack.append(i)					
				elif ops[i] > ops[stack[-1]]:			#
					#result = eval(OUTPUT[-2] + stack.pop() + OUTPUT[-1])
					#OUTPUT = OUTPUT[0:-2]
					#OUTPUT += str(result)
					stack.append(i)
					print("добавляем в стэк", i )

		for i in range(len(stack)):
			OUTPUT += stack.pop()
	
			
					


					

		#print(OUTPUT,stack,brackets)
		return OUTPUT
	


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

		


j = myEval
data = j.postfix()
print(data)
#j.Evaluate(data)
    
	