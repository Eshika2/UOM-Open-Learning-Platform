#Stack implementing
def push (stack, value):
    stack.append(value)

def pop (stack):
    return stack.pop()

my_stack = []
push(my_stack, 'a')
push(my_stack, 'b')
push(my_stack, 'c')

print (my_stack)

pop(my_stack)
print (my_stack)

#Queue implementation
def enqueue(queue, value):
    queue.append(value)

def dequeue(queue):
    return queue.pop(0) # index

my_queue = []
enqueue(my_queue, 'd')
enqueue(my_queue, 'e')
enqueue(my_queue, 'f')

print (my_queue)

dequeue(my_queue)
print (my_queue)