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
    
reg1 = Register()
reg1.write("R4", 11)
print(reg1.read("R4"))
