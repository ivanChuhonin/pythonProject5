# Задание 1

myStack = []
myOutput = []
maxNumber = 10 ** 6


def stack():
    with open('input1.txt') as f:
        line = f.readline()
        qty = int(line) if line else 0
        i = 0
        while line and i < qty:
            i += 1
            line = f.readline()
            if line:
                x = line.split(" ")
                if x[0] == '+':
                    if len(myStack) < maxNumber:
                        myStack.append(x[1])
                else:
                    if len(myStack) != 0:
                        myOutput.append(myStack.pop())

    f = open("output1.txt", "w")
    for line in myOutput:
        f.write(line)
    f.close()


stack()


# Задание 3
def brackets():
    with open('input2.txt') as f:
        line = f.readline()
        qty = int(line) if line else 0
        i = 0
        while line and i < qty:
            i += 1
            line = f.readline()
            if line.strip() == '':
                myOutput.append('YES')
            else:
                state = ''
                for c in line:
                    if state == '' and c in [')', ']']:
                        state = 'NO'
                        break
                    elif c in ['(', '[']:
                        state += c
                    elif state != '' and c == ')' and state[-1] == '(':
                        state = state[:-1]
                    elif state != '' and c == ']' and state[-1] == '[':
                        state = state[:-1]
                if state == '':
                    myOutput.append('YES\n')
                else:
                    myOutput.append('NO\n')

    f = open("output2.txt", "w")
    f.writelines(myOutput)
    f.close()


myStack = []
myOutput = []
brackets()


# Задание 5
def maxStack():
    with open('input3.txt') as f:
        line = f.readline()
        qty = int(line) if line else 0
        i = 0
        while line and i < qty:
            i += 1
            line = f.readline()
            if line:
                x = line.split(" ")
                if x[0] == 'push':
                    myStack.append(int(x[1]))
                elif x[0] == 'pop':
                    myStack.pop()
                elif x[0].strip() == 'max':
                    myOutput.append(str(max(myStack)) + '\n')

    f = open("output3.txt", "w")
    f.writelines(myOutput)
    f.close()


myStack = []
myOutput = []
maxStack()


# Задание 7
def maxSubsequence():
    from collections import deque
    dq = deque()
    with open('input4.txt') as f:
        line = f.readline()
        n = int(line) if line else 0
        line = f.readline()
        lines = line.split(' ')
        result = [int(s) for s in lines]
        line = f.readline()
        m = int(line) if line else 0
    i = 0
    while i < n - m + 1:
        dq.append(str(max(result[i:m + i])))
        i += 1
    f = open("output4.txt", "w")
    f.writelines(' '.join(dq))
    f.close()
maxSubsequence()


import time

t_start = time.perf_counter()

# stack()
# brackets()
maxStack()
# maxSubsequence()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
