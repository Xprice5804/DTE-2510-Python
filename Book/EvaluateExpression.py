import Stack

def main():
    expression = input("Enter an expression: ").strip()
    try:
        print(expression, "=", evaluateExpression(expression))
    except:
        print("Wrong expression: ", expression)

# Evaluate an expression 
def evaluateExpression(expression):
    # Create operandStack to store operands
    operandStack = Stack.Stack()
  
    # Create operatorStack to store operators
    operatorStack = Stack.Stack()
  
    # Insert blanks around (, ), +, -, /, and *
    expression = insertBlanks(expression)

    # Extract operands and operators
    tokens = expression.split()

    # Phase 1: Scan tokens
    for token in tokens:
        if len(token) == 0: # Blank space
            continue # Back to the while loop to extract the next token
        elif token[0] == '+' or token[0] == '-':
            # Process all +, -, *, / in the top of the operator stack 
            while not operatorStack.isEmpty() and \
                (operatorStack.peek() == '+' or 
                 operatorStack.peek() == '-' or
                 operatorStack.peek() == '*' or
                 operatorStack.peek() == '/'):
                processAnOperator(operandStack, operatorStack)
    
            # Push the + or - operator into the operator stack
            operatorStack.push(token[0])
        elif token[0] == '*' or token[0] == '/':
            # Process all *, / in the top of the operator stack 
            while not operatorStack.isEmpty() and \
                (operatorStack.peek() == '*' or
                 operatorStack.peek() == '/'):
                processAnOperator(operandStack, operatorStack)

            # Push the * or / operator into the operator stack
            operatorStack.push(token[0])
        elif token.strip()[0] == '(':
            operatorStack.push('(') # Push '(' to stack
        elif token.strip()[0] == ')':
            # Process all the operators in the stack until seeing '('
            while operatorStack.peek() != '(':
                processAnOperator(operandStack, operatorStack)
        
            operatorStack.pop() # Pop the '(' symbol from the stack
        else: # An operand scanned
            # Push an operand to the stack
            operandStack.push(float(token))

    # Phase 2: process all the remaining operators in the stack 
    while not operatorStack.isEmpty():
        processAnOperator(operandStack, operatorStack)

    # Return the result
    return operandStack.pop()

# Process one operator: Take an operator from operatorStack and
#  apply it on the operands in the operandStack 
def processAnOperator(operandStack, operatorStack):
    op = operatorStack.pop()
    op1 = operandStack.pop()
    op2 = operandStack.pop()
    if op == '+': 
        operandStack.push(op2 + op1)
    elif op == '-':
        operandStack.push(op2 - op1)
    elif op == '*': 
        operandStack.push(op2 * op1)
    elif op == '/':
        operandStack.push(op2 / op1)

def insertBlanks(s):
    result = ""

    for ch in s:
        if ch == '(' or ch == ')' or ch == '+' or ch == '-' or \
           ch == '*' or ch == '/':
            result += " " + ch + " "
        else:
            result += ch
    
    return result

main()