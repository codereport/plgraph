import graphviz as gv

pages = { 
    'Overview': ['BQN Docs'],
    'References': ['BQN Docs'],
    'Concepts': ['BQN Docs'],
    'Syntax' : ['Overview'],
    'Types' : ['Overview'],
    'Primitives' : ['Overview'],
    'Paradigms' : ['Overview'],
    'Glossary' : ['References'],
    'BQN-Dyalog dictionary' : ['References'],
    'BQN-J dictionary' : ['References'],
    'BQN as combinatory logic' : ['References'],
    
    # missing a bunch
    'Blocks' : ['Concepts', '#Blocks'],
    'Expression Syntax' : ['Concepts', '#Expressions'],

    'Tutorials' : ['BQN Docs'],
    'Variables' : ['Tutorials'],
    'Expressions' : ['Tutorials'],
    
    'Combinators' : ['Tutorials'],
    'List Manipulation' : ['Tutorials'],
    '#Expressions' : ['Syntax'],
    '#List Notation' : ['Syntax'],
    '#Blocks' : ['Syntax'],
    '#Expressions' : ['Syntax'],
}

dot = gv.Digraph('bqn-doc-graph', format = 'png')
dot.attr(rankdir="LR")

for page in pages.keys():
    dot.node(page)

for page, deps in pages.items():
    for dep in deps:
        dot.edge(dep, page)

dot.render(directory='.').replace('\\', '/')
