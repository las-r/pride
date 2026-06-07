import sys

# pride interpreter
# by las-r

# parse filename
if len(sys.argv) < 2:
    print("usage: python pride.py file_to_run.rid")
    sys.exit(1)
with open(sys.argv[1]) as f:
    code = f.read()

# env
stk = [False]

# exec code
i = 0
while i < len(code):
    cmd = code[i]
    
    # basic logic
    if cmd == "*": stk.append(stk[-1])
    if cmd == "@": stk.append(stk.pop(-2))
    if cmd == "#": stk.append(stk.pop(-4))
    if cmd == "$": stk.append(stk.pop(-8))
    if cmd == "-": 
        stk.pop()
        if len(stk) < 1:
            stk = [False]
    
    # operators
    if cmd == "!": stk.append(not stk.pop())
    if cmd == "&": stk.append(stk.pop() and stk.pop())
    if cmd == "|": stk.append(stk.pop() or stk.pop())
    if cmd == "^": stk.append(stk.pop() ^ stk.pop())
    
    # control flow
    if cmd == "[":
        if stk[-1]:
            while code[i] != "]":
                i += 1
    if cmd == "]":
        if not stk[-1]:
            while code[i] != "[":
                i -= 1
    
    # io
    if cmd == ",": print(int(stk[-1]), end="")
    if cmd == ".": 
        print(chr(int("".join(["1" if b else "0" for b in reversed(stk[-8:])]), 2)), end="")
    if cmd == "/": print()
    if cmd == "?":
        stk.extend([bit == "1" for char in input() for bit in f"{ord(char):08b}"])
    
    # increment inst pointer
    i += 1