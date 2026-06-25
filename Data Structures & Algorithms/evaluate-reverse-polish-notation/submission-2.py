class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        result=0
        stack = []

        for i in tokens:
            print("1",i)
            if i == "+":
                num1=int(stack.pop())
                num2=int(stack.pop())
                stack.append(num1 + num2)
                print("2",stack)
            elif i == "-":
                num1=int(stack.pop())
                num2=int(stack.pop())
                stack.append(num2 - num1)
                print("3",stack)
            elif i == "*":
                num1=int(stack.pop())
                num2=int(stack.pop())
                stack.append(num1 * num2)
                print("4",stack)
            elif i == "/":
                num1=int(stack.pop())
                num2=int(stack.pop())
                stack.append(int(num2 / num1))
                print("5",stack)
            else:
                stack.append(int(i))
                print("6",stack)

        return stack.pop()