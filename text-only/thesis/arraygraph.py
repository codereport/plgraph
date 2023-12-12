import graphviz as gv

langs = { 
     'BQN'   : ['J', 'K', 'I', 'DyAPL 18.0'],
     'DyAPL 1.0' : ['APL'],
     'DyAPL 14.0' : ['J', 'DyAPL 1.0'],
     'DyAPL 18.0' : ['DyAPL 14.0'],
    #  'FL'    : ['FP'],
    #  'FP'    : ['APL'],
     'I'     : ['K', 'J'],
     'J'     : ['Sharp APL'], #, 'FP'],
     'Sharp APL': ['APL'],
     'Jelly' : ['J'],
     'Jellyfish' : ['Jelly', 'Uiua', 'BQN', 'Q'],
     'K'     : ['APL'],
     'Q'     : ['K'],
     'Uiua'  : ['BQN'],
     'Kap'   : ['DyAPL 18.0', 'BQN'],
     'Kap++' : ['Kap']
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
