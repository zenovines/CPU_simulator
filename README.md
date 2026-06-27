# CPU Simulator 🖥️

A software simulation of a simple CPU built in Python. This project simulates how a real CPU works internally — with memory, registers, an instruction set, and a fetch-execute cycle.

Built from scratch as a learning project to understand computer architecture from the ground up.

---

 What It Simulates

| Component | What it does |
|---|---|
| **Memory** | A block of 256 addressable storage slots |
| **Registers** | 5 named high-speed storage slots (R0–R4) |
| **Instruction Set** | 5 commands the CPU understands |
| **Fetch-Execute Loop** | The heartbeat of the CPU — fetches and runs instructions sequentially |

---

 Instruction Set

| Instruction | Syntax | Description |
|---|---|---|
| `LOAD` | `LOAD Rx, value` | Load a value into a register |
| `ADD` | `ADD Rx, Ry` | Add two registers, store result in Rx |
| `SUB` | `SUB Rx, Ry` | Subtract Ry from Rx, store result in Rx |
| `STORE` | `STORE Rx, address` | Store register value into memory |
| `HALT` | `HALT` | Stop the CPU |

---

 Example Program

```python
program = [
    ("LOAD", "R0", 5),      # R0 = 5
    ("LOAD", "R1", 3),      # R1 = 3
    ("ADD",  "R0", "R1"),   # R0 = R0 + R1 = 8
    ("STORE", "R0", 50),    # memory[50] = 8
    ("HALT",),              # stop
]

cpu = CPU()
cpu.run(program)

print(cpu.register.read("R0"))  # 8
print(cpu.memory.read(50))      # 8
```

---

 How to Run

No dependencies. Just Python 3.

```bash
python simulator.py
```

---

## Project Structure

```
cpu-simulator/
│
├── simulator.py   # all source code
└── README.md
```

---

## Concepts Learned

- How RAM works as an array of addressable slots
- Why registers exist and how they differ from memory
- How a CPU instruction set defines what a processor can do
- How the fetch-decode-execute cycle drives every program ever run
