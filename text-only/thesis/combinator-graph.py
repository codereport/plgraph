import graphviz as gv

EQ = 0 # EQUALITY
ID = 1 # IDENTITY
BOTH = 2

e_combinators = { 
    'ε' : ['Ê'],
    'E' : ['Ê'],
    'Φ₁' : ['Ê'],
}

d2_combinators = { 
    #'D₂' : ['Ê'],
    'D'  : [('D₂', ID)], #'E'],
    '∆' : [('D₂', ID)], # 'ε'],
    'Σ' : [('∆', EQ), ('Φ', ID), ('Ψ', ID)], # 'ε'],
    'Φ'  : [('D₂', EQ)], #'E\''],
    'S'  : [('Φ', ID), ('D', EQ), ('Ψ', ID)],
    'Ψ'  : [('D₂', EQ)],
    'W'  : [('S',ID) , ('Σ', ID)], # 'Σ'
}

d2bqn_combinators = { 
    '⟜₂'  : [('⊸⟜', ID)], #'E'],
    '⊸₂' : [('⊸⟜', ID)], # 'ε'],
    '⊸₁' : [('⊸₂', EQ), ('3T', ID), ('○', ID)], # 'ε'],
    '3T'  : [('⊸⟜', EQ)], #'E\''],
    '⟜₁'  : [('3T', ID), ('⟜₂', EQ), ('○', ID)],
    '○'  : [('⊸⟜', EQ)],
    '˜'  : [('⟜₁',ID) , ('⊸₁', ID)], # 'Σ'
}

combinators = d2_combinators

dot = gv.Digraph('combinator-graph', format = 'png')
dot.attr(size='7,7!')

for combinator in combinators.keys():
    l = combinator.replace('₁', '')
    l = l.replace('₂', '')
    if combinator in ['S', 'W', 'Φ', 'Σ', '3T', '˜', '⊸₁', '⟜₁']:
        dot.node(combinator, style='filled', fillcolor = 'gray', label=l)
    else: 
        dot.node(combinator, label=l)

for combinator, deps in combinators.items():
    for (dep, t) in deps:
        if t == EQ:   s = 'dashed'
        if t == ID:   s = 'solid'
        if t == BOTH: s = 'dashed,bold'
        dot.edge(dep, combinator, style=s)

dot.render(directory='.').replace('\\', '/')
