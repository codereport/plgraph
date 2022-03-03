from PIL import Image
import graphviz as gv

langs = ['APL', 'SMALLTALK', 'LISP', 'SIMULA', 'SELF', 'RUBY', \
         'PERL', 'ELIXIR' , 'ERLANG', 'CLOJURE', 'IO']

logos = { 'APL':       './logos/apl_logo.png',
          'CLOJURE':   './logos/clojure_logo.png',
          'ELIXIR':    './logos/elixir_logo.png',
          'ERLANG':    './logos/erlang_logo.png',
          'IO':        './logos/io_logo.png',
          'LISP':      './logos/lisp_logo.png',
          'PERL':      './logos/perl_logo.png',
          'RUBY':      './logos/ruby_logo.png',
          'SELF':      './logos/self_logo.png',
          'SIMULA':    './logos/simula_logo.png',
          'SMALLTALK': './logos/smalltalk_logo.jpeg' }

dependencies = { 'APL'      : [],
                 'CLOJURE'  : ['ERLANG', 'LISP', 'RUBY'],    # C++,  HASKELL, C#, JAVA, ML, PROLOG, RACKET, SCHEME
                 'ELIXIR'   : ['CLOJURE', 'RUBY', 'ERLANG'], # DONE
                 'ERLANG'   : ['LISP', 'SMALLTALK'],         # PLEX, PROLOG
                 'IO'       : ['SMALLTALK', 'SELF', 'LISP'], # LUA,  PYTHON,  MORE
                 'SMALLTALK': ['LISP', 'SIMULA', 'APL'],     # MANY MORE
                 'SELF'     : ['APL', 'SMALLTALK'],          # DONE
                 'RUBY'     : ['LISP', 'SMALLTALK', 'PERL']} # MANY MORE

dot = gv.Digraph('pl-graph', format = 'png')

SKIPPED_LANGS = []

for lang in langs:
    if lang in SKIPPED_LANGS:
        continue
    image = Image.open(logos[lang])
    if image.height > image.width:
        dims = (int((75 / image.height) * image.width), 75)
    else: 
        dims = (75, int((75 / image.width) * image.height))
    new_image = image.resize(dims)
    name = './logos/resized/' + lang + '.png'
    new_image.save(name)
    
    dot.node(lang, image = name, fontsize = '-1')

for lang, deps in dependencies.items():
    for dep in deps:
        if lang in SKIPPED_LANGS or dep in SKIPPED_LANGS:
            continue
        dot.edge(dep, lang)

dot.render(directory='.').replace('\\', '/')
