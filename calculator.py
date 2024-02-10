# this is  a simple calculator that does addition, multiplication,
#subtraction, division. this calculator is only capable of calculating two numbers
class calculator:
    def add(self,num1,num2):
        num1_num2=num1 + num2
        return f"{num1} + {num2} = {num1_num2}"
    
    def subtract(self,num1,num2):
        num1_num2=num1-num2
        return f"{num1} - {num2} = {num1_num2}"
    
    def multiply(self,num1,num2):
        num1_num2=num1 * num2
        return f"{num1} * {num2} = {num1_num2}"
    
    def divide(self,num1,num2):
        assert num2!=0, f"invalid in put --> {num2} "
        num1_num2=num1 / num2
        return f"{num1} / {num2} = {num1_num2}"
    
