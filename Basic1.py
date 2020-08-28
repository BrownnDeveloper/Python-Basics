################################################################################################################

#BASIC ** STARTING WITH PYTHON **
number = 3  #Numeric Declaration
print(number)
number =5
print(number)
number = 6
c = number+number
print(c)

number = "It is a string" #String Declaration
print(number+' '+number)   #String Concatenation

################################################################################################################
#LIST DECLARATION
Shopping_list = []  #List declaration
Shopping_list.append(10)  #Appending element into list
Shopping_list.append(number)
print(Shopping_list) #printing a list
print(Shopping_list[1]) #printing a value defined at some index

################################################################################################################
#Taking Input from the user

name = input("Enter your name: ") #Input String
print("hello",name)

numb = int(input("Enter number")) #Input Number
print(numb)

flo = float(input("Float Number")) #Input a float number
print(format(flo,'.2f'))           #Round off a float number

################################################################################################################
#IF - Elif Statement in Python
#Finding maximum in 3 numbers

a= int(input("First Number"))
b= int(input("Second Number"))
c= int(input("Third Number"))
if a>=b and a>=c:
	print("Max :",a)
elif b>=a and b>=c:	
	print("max :",b)
else:
	print("max :",c)	

#Finding Max and Min between 3 numbers
a= int(input("First Number"))
b= int(input("Second Number"))
c= int(input("Third Number"))

max = 0
min = 0

if a>=b and a>=c:
	max = a
	if b>=c:
		min = c	
	else:
		min = b	
elif b>=a and b>=c: 
 	max = b
 	if a>=c:
 		min =c
 	else:
 		min = a
else:
	max = c
	if a>=b:
		min = b
	else:
		min = a

print("maximum in 3#s",max)
print("minimum in 3#s",min)

################################################################################################################
#Defining a function in Python

def fac(n):
	if n==0:
		return 1
	else:
		f = n*fac(n-1)	
	return f

def main():   #Main function to call the factorial of a number
	a = int(input("Integer number to find factorial"))	
	output = fac(a)  #Calling factorial function
	print(output)
 
if __name__ == '__main__': #To know python about "main" Function
		main()		

################################################################################################################

#USE OF FOR LOOP
#Implementing Linear Search in list operation

def search(element_list,element_to_search):
	if len(element_list) <= 0:
		print("Inappropriate list limit")
	else :
		for i in range(len(element_list)):
			if element_list[i] == element_to_search:
				return True

	return False

def main():
	element_list = []
	size_of_list = int(input("Please define number of elements in list"))
	print("#########################################")
	for i in range(size_of_list):
		e = int(input())
		element_list.append(e)
	print("#########################################")	
	element_to_search = int(input("**Element to search :"))	
	output = search(element_list,element_to_search)
	if output == True:
		print("\nElement Available :O")
	else:
		print("\nElement Not Available ;(")		
if __name__ == '__main__':
			main()		

################################################################################################################			

if __name__ == '__main__':
		main()	