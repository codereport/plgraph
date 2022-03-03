from PIL import Image
import graphviz as gv

logos = { 'ALGOL':     './logos/algol_logo.png',
          'APL':       './logos/apl_logo.png',
          'BQN':       './logos/bqn_logo.png',
          'CLOJURE':   './logos/clojure_logo.png',
          'C':         './logos/c_logo.png',
          'CPP':       './logos/cpp_logo.png',
          'C#':        './logos/csharp_logo.png',
          'D':         './logos/d_logo.png',
          'ELIXIR':    './logos/elixir_logo.png',
          'ELM':       './logos/elm_logo.png',
          'ERLANG':    './logos/erlang_logo.png',
          'F#':        './logos/fsharp_logo.png',
          'FORTRAN':   './logos/fortran_logo.png',
          'HASKELL':   './logos/haskell_logo.png',
          'IO':        './logos/io_logo.png',
          'J':         './logos/j_logo.png',
          'JS':        './logos/javascript_logo.png',
          'JAVA':      './logos/java_logo.png',
          'K':         './logos/kx-logo.png',
          'KOTLIN':    './logos/kotlin_logo.png',
          'LISP':      './logos/lisp_logo.png',
          'MIRANDA':   './logos/miranda_logo.jpg',
          'ML':        './logos/ml_logo.png',
          'OBJC':      './logos/objective-c.png',
          'OCAML':     './logos/ocaml_logo.jpg',
          'PERL':      './logos/perl_logo.png',
          'PROLOG':    './logos/prolog_logo.png',
          'PYTHON':    './logos/python_logo.png',
          'RACKET':    './logos/racket_logo.png',
          'RUBY':      './logos/ruby_logo.png',
          'RUST':      './logos/rust_logo.png',
          'SCALA':     './logos/scala_logo.png',
          'SCHEME':    './logos/scheme_logo.png',
          'SELF':      './logos/self_logo.png',
          'SIMULA':    './logos/simula_logo.png',
          'SMALLTALK': './logos/smalltalk_logo.jpeg',
          'SML':       './logos/sml_logo.jpg',
          'SWIFT':     './logos/swift_logo.png',
          'TS':        './logos/ts.png' }

dependencies = { 'BQN'      : ['J', 'APL'],
                 'C'        : ['ALGOL'], # B BCPL PL/I FORTRAN
                 'CLOJURE'  : ['ERLANG', 'LISP', 'RUBY', 'RACKET', 'SCHEME', 'PROLOG', 'CPP', 'HASKELL', 'C#', 'JAVA', 'SML'],
                 'CPP'      : ['ALGOL', 'SIMULA', 'SMALLTALK', 'C'],                # ADA BCPL CLU Modula 2
                 'C#'       : ['CPP', 'HASKELL', 'JAVA', 'F#', 'SML'], # Eiffel ML modula 3
                 'ELIXIR'   : ['CLOJURE', 'RUBY', 'ERLANG'],
                 'ELM'      : ['HASKELL', 'SML', 'F#'], # ocaml
                 'ERLANG'   : ['LISP', 'SMALLTALK', 'PROLOG', 'SML'],                                 # PLEX
                 'F#'       : ['C#', 'ERLANG', 'HASKELL', 'SCALA', 'SML', 'PYTHON'], # OCAML
                 'HASKELL'  : ['LISP', 'SCHEME', 'MIRANDA'], # CLEAN FP ISWIM Miranda SML SASL SISAL
                 'IO'       : ['SMALLTALK', 'SELF', 'LISP'],                                   # LUA,    PYTHON, MORE
                 'J'        : ['APL'],
                 'JAVA'     : ['SIMULA', 'LISP', 'SMALLTALK', 'CPP', 'C#', 'OBJC'], # CLU ADA EIFFEL modula 3 oberon pascal
                 'K'        : ['APL'], # scheme
                 'KOTLIN'   : ['C#', 'JAVA', 'SML', 'SCALA'], # Eiffel groovy JS Python
                 'MIRANDA'  : ['ML'], 
                 'ML'       : ['LISP'], # ISWIM
                 'OBJC'     : ['SMALLTALK', 'C'],
                 'OCAML'    : ['ML'],
                 'PERL'     : ['CPP', 'C'],                                                    # many more
                 'PYTHON'   : ['ALGOL', 'C', 'CPP', 'HASKELL', 'LISP', 'SML', 'PERL'], # ADA CLU DYLAN modula 3
                 'SCALA'    : ['LISP', 'ERLANG', 'SCHEME', 'SMALLTALK', 'HASKELL', 'JAVA', 'F#', 'SML'], # EIFFEL Ocaml oz
                 'SCHEME'   : ['ALGOL', 'LISP'],
                 'SELF'     : ['APL', 'SMALLTALK'],
                 'SIMULA'   : ['ALGOL'],
                 'SMALLTALK': ['LISP', 'SIMULA', 'APL'],                                       # MANY MORE
                 'SML'      : ['ML'], #PASCAL
                 'SWIFT'    : ['RUBY', 'OBJC', 'CPP', 'RUST', 'HASKELL', 'C#', 'PYTHON'],                # CLU D
                 'RACKET'   : ['SCHEME'],                                                      # EIFFEL
                 'RUBY'     : ['LISP', 'SMALLTALK', 'PERL', 'CPP', 'PYTHON'], # CLU DYLAN ADA LUA EIFFEL
                 'RUST'     : ['CPP', 'ERLANG', 'RUBY', 'SCHEME', 'SWIFT', 'HASKELL', 'C#', 'SML'] #OCAML
}

dependencies_light = { 
                 'ALGOL'    : ['FORTRAN'],
                 'BQN'      : ['J', 'APL'],
                 'C'        : ['ALGOL', 'FORTRAN'],                         # B BCPL PL/I FORTRAN
                 'CLOJURE'  : ['JAVA', 'RACKET'],
                 'CPP'      : ['SIMULA', 'C', 'D'],                         # ADA BCPL CLU Modula 2
                 'C#'       : ['JAVA', 'F#'],                               # Eiffel ML modula 3
                 'D'        : ['CPP'],
                 'ELIXIR'   : ['CLOJURE', 'RUBY', 'ERLANG'],
                 'ELM'      : ['HASKELL'],                                  # ocaml
                 'ERLANG'   : ['SMALLTALK', 'PROLOG'],                      # PLEX
                 'F#'       : ['C#', 'SML', 'OCAML'],
                 'HASKELL'  : ['SCHEME', 'MIRANDA'],                        # CLEAN FP ISWIM Miranda SML SASL SISAL
                 'J'        : ['APL'],
                 'JAVA'     : ['SMALLTALK', 'CPP', 'OBJC'],                 # CLU ADA EIFFEL modula 3 oberon pascal
                 'JS'       : ['SELF', 'JAVA', 'SCHEME'],
                 'K'        : ['APL'],                                      # scheme
                 'KOTLIN'   : ['C#', 'JAVA', 'SCALA'],                      # Eiffel groovy JS Python
                 'MIRANDA'  : ['ML'],
                 'ML'       : ['LISP'],
                 'OBJC'     : ['SMALLTALK', 'C'],
                 'OCAML'    : ['ML'],
                 'PERL'     : ['CPP', 'C'],                                 # many more
                 'PYTHON'   : ['CPP', 'PERL'],                              # ADA CLU DYLAN modula 3
                 'SCALA'    : ['HASKELL', 'JAVA'],                          # EIFFEL Ocaml oz
                 'SCHEME'   : ['ALGOL', 'LISP'],
                 'SELF'     : ['APL', 'SMALLTALK'],
                 'SIMULA'   : ['ALGOL'],
                 'SMALLTALK': ['LISP', 'SIMULA', 'APL'],                    # MANY MORE
                 'SML'      : ['ML'],                                       #PASCAL
                 'SWIFT'    : ['OBJC', 'CPP', 'HASKELL', 'PYTHON', 'RUST'], # CLU
                 'RACKET'   : ['SCHEME'],                                   # EIFFEL
                 'RUBY'     : ['SMALLTALK', 'PERL'],                        # CLU DYLAN ADA LUA EIFFEL
                 'RUST'     : ['CPP', 'HASKELL', 'SWIFT', 'OCAML'],
                 'TS'       : ['JS']
}

dot = gv.Digraph('pl-graph', format = 'png')

SKIPPED_LANGS = ['IO', 'FORTRAN']

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

for lang, deps in dependencies_light.items():
    for dep in deps:
        if lang in SKIPPED_LANGS or dep in SKIPPED_LANGS:
            continue
        dot.edge(dep, lang)

dot.render(directory='.').replace('\\', '/')
