from PIL import Image
import graphviz as gv

logos = { 'ALGOL':     './logos/algol_logo.png',
          'APL':       './logos/apl_logo.png',
          'BQN':       './logos/bqn_logo.png',
          'CLOJURE':   './logos/clojure_logo.png',
          'C':         './logos/c_logo.png',
          'CPP':       './logos/cpp_logo.png',
          'C#':        './logos/csharp_logo.png',
          'ELIXIR':    './logos/elixir_logo.png',
          'ERLANG':    './logos/erlang_logo.png',
          'F#':        './logos/fsharp_logo.png',
          'HASKELL':   './logos/haskell_logo.png',
          'IO':        './logos/io_logo.png',
          'J':         './logos/j_logo.png',
          'JAVA':      './logos/java_logo.png',
          'K':         './logos/kx-logo.png',
          'LISP':      './logos/lisp_logo.png',
          'OBJC':      './logos/objective-c.png',
          'PERL':      './logos/perl_logo.png',
          'PROLOG':    './logos/prolog_logo.png',
          'RACKET':    './logos/racket_logo.png',
          'RUBY':      './logos/ruby_logo.png',
          'RUST':      './logos/rust_logo.png',
          'SCALA':     './logos/scala_logo.png',
          'SCHEME':    './logos/scheme_logo.png',
          'SELF':      './logos/self_logo.png',
          'SIMULA':    './logos/simula_logo.png',
          'SMALLTALK': './logos/smalltalk_logo.jpeg',
          'SWIFT':     './logos/swift_logo.png' }

dependencies = { 'BQN'      : ['J', 'APL'],
                 'C'        : ['ALGOL'], # B BCPL PL/I FORTRAN
                 'CLOJURE'  : ['ERLANG', 'LISP', 'RUBY', 'RACKET', 'SCHEME', 'PROLOG', 'CPP', 'HASKELL', 'C#', 'JAVA'], # ML
                 'CPP'      : ['ALGOL', 'SIMULA', 'SMALLTALK', 'C', 'HASKELL'],                # ADA BCPL CLU ML Modula 2
                 'C#'       : ['CPP', 'HASKELL', 'JAVA', 'F#'], # Eiffel ML modula 3
                 'ELIXIR'   : ['CLOJURE', 'RUBY', 'ERLANG'],
                 'ERLANG'   : ['LISP', 'SMALLTALK', 'PROLOG'],                                 # PLEX
                 'F#'       : ['C#', 'ERLANG', 'HASKELL', 'SCALA'], # ML OCAML Python
                 'HASKELL'  : ['LISP', 'SCHEME'], # CLEAN FP ISWIM Miranda ML SML SASL SISAL
                 'IO'       : ['SMALLTALK', 'SELF', 'LISP'],                                   # LUA,    PYTHON, MORE
                 'J'        : ['APL'],
                 'JAVA'     : ['SIMULA', 'LISP', 'SMALLTALK', 'CPP', 'C#', 'OBJC'], # CLU ADA EIFFEL modula 3 oberon pascal
                 'K'        : ['SCHEME', 'APL'],
                 'OBJC'     : ['SMALLTALK', 'C'],
                 'PERL'     : ['CPP', 'C'],                                                    # many more
                 'SCALA'    : ['LISP', 'ERLANG', 'SCHEME', 'SMALLTALK', 'HASKELL', 'JAVA', 'F#'], # EIFFEL Ocaml oz SML
                 'SCHEME'   : ['ALGOL', 'LISP'],
                 'SELF'     : ['APL', 'SMALLTALK'],
                 'SIMULA'   : ['ALGOL'],
                 'SMALLTALK': ['LISP', 'SIMULA', 'APL'],                                       # MANY MORE
                 'SWIFT'    : ['RUBY', 'OBJC', 'CPP', 'RUST', 'HASKELL', 'C#'],                # PYTHONCLU D
                 'RACKET'   : ['SCHEME'],                                                      # EIFFEL
                 'RUBY'     : ['LISP', 'SMALLTALK', 'PERL'], # MANY MORE
                 'RUST'     : ['CPP', 'ERLANG', 'RUBY', 'SCHEME', 'SWIFT', 'HASKELL', 'C#'] #OCAML SML
}

dot = gv.Digraph('pl-graph', format = 'png')

SKIPPED_LANGS = ['IO', 'SELF']

for lang in logos.keys():
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
