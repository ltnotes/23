class AssemblerPass1:
    def __init__(self):
        self.symtab = {}          # {symbol: address}
        self.littab = {}          # {literal: address or None}
        self.pooltab = [0]        # index where each literal pool starts
        self.ic = []              # intermediate‑code lines
        self.lc = 0               # location counter
        self.next_lit_no = 1      # literal sequence number for IC refs
    def add_ic(self, *parts):
        """Join parts into one IC line."""
        self.ic.append(' '.join(parts))
    def dump_literals(self):
        """Assign addresses to current pool and emit DL lines."""
        for lit, addr in self.littab.items():
            if addr is None:                  
                self.littab[lit] = self.lc
                self.add_ic("(DL,02)", f"(C,{lit})")
                self.lc += 1
        self.pooltab.append(len(self.littab))
    def process_line(self, label, opcode, operand):
        if opcode == "START":
            self.lc = int(operand)
            self.add_ic("(AD,01)", f"(C,{operand})")
        elif opcode == "END":
            self.dump_literals()             
            self.add_ic("(AD,02)")
        elif opcode == "LTORG":
            self.dump_literals()
            self.add_ic("(AD,05)")  
        elif opcode == "DS":
            self.symtab[label] = self.lc
            self.add_ic("(DL,01)", f"(C,{operand})")
            self.lc += int(operand)
        else:
            if label:
                self.symtab[label] = self.lc
            if "=" in operand:
                lit = operand.split("'")[1]   # extracts 3 from ='3'
                if lit not in self.littab:
                    self.littab[lit] = None   # reserve
                operand = f"(L,{self.next_lit_no})"
                self.next_lit_no += 1
            self.add_ic("(IS,xx)", operand)   # xx = op‑code number
            self.lc += 1
    def display_results(self):
        print("SYMBOL TABLE:", self.symtab)
        print("LITERAL TABLE:", self.littab)
        print("POOL TABLE:", self.pooltab)
        print("\nINTERMEDIATE CODE:")
        for line in self.ic:
            print(line)
assembly_code = [
    ("JOHN", "START", "200"),
    ("",     "MOVER", "R1, ='3'"),
    ("",     "MOVEM", "R1, X"),
    ("L1",   "MOVER", "R2, ='2'"),
    ("",     "LTORG", ""),
    ("X",    "DS",    "1"),
    ("",     "END",   "")
]
asm = AssemblerPass1()
for lbl, opc, opr in assembly_code:
    asm.process_line(lbl, opc, opr)
asm.display_results()
