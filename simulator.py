
class Memory:
    def __init__(self, size):
        self.data = [0] * size 

    def read(self,address):
        return self.data[address]
    
    def write(self, address, value):
        self.data[address] = value

class Register:
    def __init__(self):
        registers = {'R0': 0,
                     'R1': 0,
                     'R2': 0,
                     'R3': 0,
                     'R4': 0
                    }
        self.data = registers
    
    def read(self,name):
        return self.data[name]
    
    def write(self, name, value):
        self.data[name] = value

mem = Memory(100)
mem.write(10, 1)
print(mem.read(10))

reg = Register()
reg.write("R2", 99)
print(reg.read('R2'))

class CPU:
    def __init__(self):
        self.memory = Memory(256)
        self.register = Register()
        self.pc = 0
        self.running = False

    def execute(self, instruction):
        op = instruction[0] # first element is always instruction

        if op == 'LOAD':
            reg, value = instruction[1], instruction[2]
            self.register.write(reg, value)
        elif op == 'ADD':
            reg1, reg2 = instruction[1], instruction[2]
            a = self.register.read(reg1)
            b = self.register.read(reg2)
            self.register.write(reg1, a+b)
        elif op == 'SUB':
            reg1, reg2 = instruction[1], instruction[2]
            a = self.register.read(reg1)
            b = self.register.read(reg2)
            self.register.write(reg1, a - b)
        elif op == 'STORE':
            reg, address = instruction[1], instruction[2]
            value = self.register.read(reg)
            self.memory.write(address, value)
        elif op == 'HALT':
            self.running = False
        
    def run(self,program):
            self.running = True
            self.pc = 0

            while self.running:
                instruction = program[self.pc] # FETCH
                self.execute(instruction) # EXECUTE
                self.pc += 1 # ADVANCE
                print(f'Running: {instruction}')

def assembler(assembly_code):
    program = []
    with open('assembly_code', 'r') as f:
        for line in f:
            parts = line.strip().split()

            if not parts:
                continue

        op = parts[0]

        if op == 'LOAD':
            reg = parts[1].rstrip(',')
            value = int(parts[2])
            program.append(('LOAD', reg, value))

        elif op == 'ADD' or op == 'SUB':
            reg1 = parts[1].rstrip(',')
            reg2 = parts[2].rstrip(',')
            program.append((op, reg1, reg2))

        elif op == 'STORE':
            reg = parts[1].rstrip(',')
            address = int(parts[2])
            program.append(('STORE', reg, address))

        elif op == 'HALT':
            program.append(('HALT',))
    return program

cpu1 = CPU()

program1 = [("LOAD", 'R0', 5),
           ("LOAD", 'R1', 3),
           ("ADD", "R0", "R1"),
           ('STORE', 'R0', 50),
           ("HALT",)]
cpu1.run(program1)

print(cpu1.register.read('R0'))
print(cpu1.memory.read(50))

cpu2 = CPU()
program2 = [("LOAD", 'R2', 10),
            ("LOAD", 'R3', 20),
            ("ADD", 'R2', 'R3'),
            ('STORE', 'R2',60),
            ("SUB",'R2','R3'),
            ("STORE", 'R2', 10),
            ("HALT",)]

cpu2.run(program2) # R2 starts as 10, R3 as 20
                       # After ADD → R2 = 30
                      #  After SUB → R2 = 30 - 20 = 10
print(cpu2.memory.read(60))   # result of ADD
print(cpu2.memory.read(10))   # result of SUB 