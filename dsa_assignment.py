# # Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def getPairsCount(arr, n, sum):
    count = 0 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
# print("Count of pairs is", getPairsCount(arr, n, sum))

# # Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
# print(A)

# # Q3. Write a program to check if two strings are a rotation of each other?

def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    if size1 != size2:
        return 0
    temp = string1 + string1
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
string1 = "AACD"
string2 = "ACDA"
  
if areRotations(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")

  
# # Q4. Write a program to print the first non-repeated character from a string?

NO_OF_CHARS = 256
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
 
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
    return index
string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is" , string[index])


# # Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.  

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')  

# # Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# # Prefix: An expression is called the prefix expression if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2). 
# # Example : *+AB-CD (Infix : (A+B) * (C-D) )

# # Postfix: An expression is called the postfix expression if the operator appears in the expression after the operands. Simply of the form (operand1 operand2 operator). 
# # Example : AB+CD-* (Infix : (A+B * (C-D) )

def isOperator(x):
    if x == "+":
        return True
    if x == "-":
        return True
    if x == "/":
        return True
    if x == "*":
        return True
    return False 
def postToPre(post_exp):
 
    s = []
    length = len(post_exp)
    for i in range(length):   
        if (isOperator(post_exp[i])):
 
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
 
            s.append(temp)
 
        else:
            s.append(post_exp[i])   
    ans = ""
    for i in s:
        ans += i
    return ans
if __name__ == "__main__":
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))


# # Q7. Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
    stack = []

    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):

            stack.append(prefix[i])
            i -= 1
        else:
           
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))


# # Q8. Write a program to check if all the brackets are closed in a given code snippet.    

def areBracketsBalanced(expr):
    stack = []
 
 
    for char in expr:
        if char in ["(", "{", "["]:
 
            stack.append(char)
        else:
 
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# Q9. Write a program to reverse a stack.

# class Stack:

#     def __init__(self):
#         self.Elements = []
          
 
#     def push(self, value):
#         self.Elements.append(value)
        

#     def pop(self):
#         return self.Elements.pop()
      
  
#     def empty(self):
#         return self.Elements == []
  
#     def show(self):
#         for value in reversed(self.Elements):
#             print(value)
  
# def BottomInsert(s, value):
    

#     if s.empty(): 
          

#         s.push(value)
          

#     else:
#         popped = s.pop()
#         BottomInsert(s, value)
#         s.push(popped)
  

# def Reverse(s):
#     if s.empty():
#         pass
#     else:
#         popped = s.pop()
#         Reverse(s)
#         BottomInsert(s, popped)
# stk = Stack()
  
# stk.push(1)
# stk.push(2)
# stk.push(3)
# stk.push(4)
# stk.push(5)
  
# print("Original Stack")
# stk.show()
  
# print("\nStack after Reversing")
# Reverse(stk)
# stk.show()


# Q10. Write a program to find the smallest number using a stack.

# arr = [111, 13, 25, 9, 34, 1]
# n = len(arr)
# arr.sort()
# print("smallest element is "+str(arr[0]))