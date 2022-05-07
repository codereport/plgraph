import graphviz as gv

langs = { 
     'BQN'   : ['J', 'K', 'I', 'Dyalog APL'],
     'Dyalog APL' : ['APL', 'J'],
    #  'FL'    : ['FP'],
    #  'FP'    : ['APL'],
     'I'     : ['K', 'J'],
     'J'     : ['APL'], #, 'FP'],
     'K'     : ['APL'],
     'Q'     : ['K'],
 #  'SHAKTI' : ['K'],
}

dot = gv.Digraph('arraylang-graph', format = 'png')
dot.attr(size='10,10!')

for lang in langs.keys():
    dot.node(lang)

for lang, deps in langs.items():
    for dep in deps:
        dot.edge(dep, lang)

dot.render(directory='.').replace('\\', '/')
