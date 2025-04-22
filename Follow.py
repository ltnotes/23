EPS = "#"
def parse(txt):
    G = {}
    for line in txt.splitlines():
        if "->" not in line: continue
        lhs, rhs = map(str.strip, line.split("->"))
        G.setdefault(lhs, []).extend([alt.split() for alt in rhs.split("|")])
    return G
def first_sym(x, FIRST):
    if x == EPS or x not in FIRST:
        return {x}
    return FIRST[x]
def compute_follow(G, FIRST):
    FOLLOW = {A: set() for A in G}
    FOLLOW[next(iter(G))].add('$')  # Start symbol gets the end symbol
    changed = True
    while changed:
        changed = False
        for A, prods in G.items():
            for p in prods:
                for i, X in enumerate(p):
                    if X not in G: continue  # Skip terminals
                    if i + 1 < len(p):
                        # Add FIRST of the next symbol (exclude ε)
                        follow_add = first_sym(p[i + 1], FIRST) - {EPS}
                        if not follow_add.issubset(FOLLOW[X]):
                            FOLLOW[X] |= follow_add
                            changed = True
                    else:  # If end of production, add FOLLOW(A)
                        if not FOLLOW[A].issubset(FOLLOW[X]):
                            FOLLOW[X] |= FOLLOW[A]
                            changed = True
    return FOLLOW
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
                    if EPS not in fx: break
                    if i == len(p) - 1:
                        FIRST[A].add(EPS)
                    changed |= len(FIRST[A]) != before
    return FIRST
grammar = """E -> T E'
E' -> + T E' | #
T -> F T'
T' -> * F T' | #
F -> ( E ) | id"""
G = parse(grammar)
FIRST = first_sets(G)
FOLLOW = compute_follow(G, FIRST)

for nt, f in FOLLOW.items():
    print(f"FOLLOW({nt}) = {sorted(f)}")
