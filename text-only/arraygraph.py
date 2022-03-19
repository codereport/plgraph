import graphviz as gv

langs = { 
     'BQN'   : ['J', 'APL', 'K', 'I', 'Dyalog APL'],
     'Dyalog APL' : ['APL', 'J'],
     'FL'    : ['FP'],
     'FP'    : ['APL'],
     'I'     : ['K', 'J'],
     'J'     : ['APL','FL'],
     'K'     : ['APL'],
     'Q'     : ['K'],
 #  'SHAKTI' : ['K'],
}

dot = gv.Digraph('arraylang-graph', format = 'png')

for lang in langs.keys():
    dot.node(lang)

for lang, deps in langs.items():
    for dep in deps:
        dot.edge(dep, lang)

dot.render(directory='.').replace('\\', '/')