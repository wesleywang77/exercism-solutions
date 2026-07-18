def is_match(char_1,char_2):
    if char_1 == ']':
        return char_2 == '['
    if char_1 == '}':
        return char_2 == '{'
    if char_1 == ')':
        return char_2 == '('
    return False

def is_paired(input_string):
    stack = []
    for char in input_string:
        if char == '[' or char == '{' or char == '(':
            stack.append(char)
        elif char == '}' or char == ']' or char == ')':
            if len(stack) == 0:
                return False
            popped_char = stack.pop()
            if not is_match(char, popped_char):
                return False
    return len(stack) == 0
            
    
        
    