# Create a stack
def create_stack():
    stack=[]
    return stack

# Check if the stack is empty
def check_empty(stack):
    return len(stack) == 0

# Push new element into stack
def push(stack, item):
    stack.append(item)
    print(item, "is pushed")

# Pop an element from stack
def pop(stack):
    if check_empty(stack):
        print('Stack is empty')
    else:
        return stack.pop()

# Main
word=input("Enter any word to reverse:")
new_stack=create_stack()
for i in range(len(word)):
    push(new_stack,word[i])

print('The stack is:', new_stack)

new_word=[]
for i in range(len(word)):
    new_word.append(pop(new_stack))

print('The new word is ', end='')
for i in new_word:
    print(i,end='')
#New line is update in the code