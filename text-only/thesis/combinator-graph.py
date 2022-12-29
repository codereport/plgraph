import graphviz as gv

EQ = 0 # EQUALITY
ID = 1 # IDENTITY
FK = 2 # FUNCTION + K
BOTH = 3

e_combinators = { 
    'E' : [('Ê', ID)],
    'Φ₁' : [('Ê', EQ)],
    'ε' : [('Ê', ID)],
}

d2_combinators = { 
    'D₂' : [('Ê', FK)],
    'D'  : [('D₂', ID), ('E', FK)], #'E'],
    '∆' : [('D₂', ID), ('ε', FK)],
    'Σ' : [('∆', EQ), ('Φ', ID), ], # 'ε'],
    'Π' : [('Ψ', EQ), ('Φ', EQ)],
    'Φ'  : [('D₂', EQ), ('Φ₁', FK)],
    'S'  : [('Φ', ID), ('D', EQ),],
    'Ψ'  : [('D₂', EQ)],
    'W'  : [('S',ID), ('Σ', ID), ('Π', ID)],
    # 'W'  : [('Ψ', BOTH), ('S',ID),]
}

b_combinators = {
    'B₁' : [('D', FK), ('∆', FK)],
    'B'  : [('B₁', FK), ('B₀.₅', FK)],
    'B₀.₅'  : [('B₁', EQ)],
}

solo_combinators = {
    'I' : [],
    'K' : [],
    'C' : [],
}

d2bqn_combinators = { 
    '⟜₂' : [('⊸⟜', ID)], #'E'],
    '⊸₂' : [('⊸⟜', ID)], # 'ε'],
    '⊸₁' : [('⊸₂', EQ), ('3T', ID)], # 'ε'],
    ' '  : [('○', EQ),('3T', EQ)],
    '3T' : [('⊸⟜', EQ)], #'E\''],
    '⟜₁' : [('3T', ID), ('⟜₂', EQ)],
    '○'  : [('⊸⟜', EQ)],
    '˜'  : [('⟜₁',ID) , ('⊸₁', ID), (' ', ID)], # 'Σ'
}

combinators = {**d2_combinators, **e_combinators, **b_combinators}# , **solo_combinators} # , **d2bqn_combinators}

dot = gv.Digraph('combinator-graph', format = 'png')
dot.attr(size='7,7!')

for combinator in combinators.keys():
    if '⊸' in combinator or '⟜' in combinator:
        l = combinator.replace('₁', '')
        l = l.replace('₂', '')
    else:
        l = combinator
    if combinator in ['S', 'W', 'Φ', 'Σ', '3T', '˜', '⊸₁', '⟜₁', 'H₂', ' ', 'B', 'Π', 'B₀.₅']:
        dot.node(combinator, style='filled', fillcolor = 'lightgray', label=l)
    else: 
        dot.node(combinator, label=l)

for combinator, deps in combinators.items():
    for (dep, t) in deps:
        if t == EQ:   s = 'dashed'
        if t == ID:   s = 'solid'
        if t == FK:   s = 'dotted'
        if t == BOTH: s = 'dashed,bold'
        dot.edge(dep, combinator, style=s)

dot.render(directory='.').replace('\\', '/')
