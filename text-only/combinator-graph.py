import graphviz as gv

combinators = { 
    # 'ε' : ['Ê'],
    # 'E' : ['Ê'],
    #'D₂' : ['Ê'],
    'D' : ['D₂',], #'E'],
    # '∆' : ['D₂',], # 'ε'],
    'S\'' : ['D₂',], #'E\''],
    'S' : ['S\'', 'D'],
    # 'Σ' : ['∆' ,'S\''],
    'Ψ' : ['D₂'],
    'W' : ['S','Ψ'], # 'Σ'
    # 'E\'' : ['Ê'],
}

monadic = ['S\'', 'S', 'W', 'Σ']

dot = gv.Digraph('combinator-graph', format = 'png')

for combinator in combinators.keys():
    if combinator in monadic:
        dot.node(combinator, style='filled', fillcolor = 'gray')
    else: 
        dot.node(combinator)

for combinator, deps in combinators.items():
    for dep in deps:
        dot.edge(dep, combinator)

dot.render(directory='.').replace('\\', '/')
