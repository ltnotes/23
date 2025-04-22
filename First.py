EPS = "#"
def parse(txt):
    G = {}
    for line in txt.splitlines():
        if "->" not in line: continue
        lhs, rhs = map(str.strip, line.split("->"))
        G.setdefault(lhs, []).extend([alt.split() for alt in rhs.split("|")])
    return G
def first_sym(x, FIRST):
    if x == EPS or x not in FIRST:     # terminal if not a non‑terminal
        return {x}
    return FIRST[x]
def first_sets(G):
    FIRST, changed = {A: set() for A in G}, True
    while changed:
        changed = False
        for A, prods in G.items():
            for p in prods:
                for i, X in enumerate(p):
                    before = len(FIRST[A])
                    fx = first_sym(X, FIRST)
                    FIRST[A] |= fx - {EPS}
                    if EPS not in fx:
                        break
                    if i == len(p) - 1:
                        FIRST[A].add(EPS)
                    changed |= len(FIRST[A]) != before
    return FIRST
grammar = """E -> T E'
E' -> + T E' | #
T -> F T'
T' -> * F T' | #
F -> ( E ) | id"""

for nt, s in first_sets(parse(grammar)).items():
    print(f"FIRST({nt}) = {sorted(s)}")
