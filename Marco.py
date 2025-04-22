class MacroProcessor:
    def __init__(self):  # Fixed here
        self.macro_def = {}  # Store macro name and its body
        self.in_macro = False
        self.current_macro = ""
        self.macro_body = []

    def process_line(self, line):
        if line.strip() == "MACRO":
            self.in_macro = True
            self.macro_body = []
        elif self.in_macro:
            if line.strip() == "MEND":
                self.macro_def[self.current_macro] = self.macro_body[:]
                self.in_macro = False
            elif not self.macro_body:
                self.current_macro = line.strip()  # First line after MACRO is macro name
            else:
                self.macro_body.append(line)
        elif line.strip() in self.macro_def:
            # Expand macro
            for macro_line in self.macro_def[line.strip()]:
                print(f"{macro_line.strip()}")
        else:
            # Normal line, just print it
            print(f"{line.strip()}")

    def process(self, lines):
        for line in lines:
            self.process_line(line)

# Example input
code = [
    "MACRO",
    "INCR",
    "    MOVER AREG, NUM",
    "    ADD AREG, ONE",
    "    MOVEM AREG, NUM",
    "MEND",
    "START 100",
    "INCR",
    "STOP",
    "NUM DS 1",
    "ONE DC 1",
    "END"
]

mp = MacroProcessor()
mp.process(code)
