class Memory:
    def __init__(self, size):
        self.data = [0] * size

    def read(self, address):
        return self.data[address]
    
    def write(self, address, value):
        self.data[address] = value

# Memory class is a simple implementation of a memory storage system. It initializes a 
# list of zeros with a specified size and provides methods to read from and write to specific 
# addresses in that list. The read method retrieves the value at a given address, while the write 
# method updates the value at a specified address.

m1 = Memory(10)
m1.write(0, 12)
print(m1.read(0))
m1.write(11, 33) # This will raise an IndexError since the address is out of bounds
print(m1.read(11)) # This will also raise an IndexError since the address is out of bounds