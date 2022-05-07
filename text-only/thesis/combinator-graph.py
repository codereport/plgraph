import graphviz as gv

EQ = 0 # EQUALITY
ID = 1 # IDENTITY
BOTH = 2

e_combinators = { 
    # 'ε' : ['Ê'],
    'E' : [('Ê', ID)],
    'Φ₁' : [('Ê', EQ)],
}

d2_combinators = { 
    #'D₂' : ['Ê'],
    'D'  : [('D₂', ID)], #'E'],
    '∆' : [('D₂', ID)], # 'ε'],
    'Σ' : [('∆', EQ), ('Φ', ID), ], # 'ε'],
    'H₂' : [('Ψ', EQ),('Φ', EQ)],
    'Φ'  : [('D₂', EQ)], #'E\''],
    'S'  : [('Φ', ID), ('D', EQ),],
    'Ψ'  : [('D₂', EQ)],
    'W'  : [('S',ID), ('Σ', ID), ('H₂', ID)],
    # 'W'  : [('Ψ', BOTH), ('S',ID),]
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

combinators = {**d2_combinators} #, **d2bqn_combinators}

dot = gv.Digraph('combinator-graph', format = 'png')
dot.attr(size='7,7!')

for combinator in combinators.keys():
    if '⊸' in combinator or '⟜' in combinator:
        l = combinator.replace('₁', '')
        l = l.replace('₂', '')
    else:
        l = combinator
    if combinator in ['S', 'W', 'Φ', 'Σ', '3T', '˜', '⊸₁', '⟜₁', 'H₂', ' ']:
        dot.node(combinator, style='filled', fillcolor = 'lightgray', label=l)
    else: 
        dot.node(combinator, label=l)

for combinator, deps in combinators.items():
    for (dep, t) in deps:
        if t == EQ:   s = 'dashed'
        if t == ID:   s = 'solid'
        if t == BOTH: s = 'dashed,bold'
        dot.edge(dep, combinator, style=s)

dot.render(directory='.').replace('\\', '/')
