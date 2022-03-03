import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx

APL       = 0
SMALLTALK = 1
LISP      = 2
SIMULA    = 3
SELF      = 4
RUBY      = 5
PERL      = 6
ELIXIR    = 7
ERLANG    = 8
CLOJURE   = 9
IO        = 10

langs = [APL, SMALLTALK, LISP, SIMULA, SELF, RUBY, \
         PERL, ELIXIR , ERLANG, CLOJURE, IO]

logos = { APL:       './logos/apl_logo.png',
          CLOJURE:   './logos/clojure_logo.png',
          ELIXIR:    './logos/elixir_logo.png',
          ERLANG:    './logos/erlang_logo.png',
          IO:        './logos/io_logo.png',
          LISP:      './logos/lisp_logo.png',
          PERL:      './logos/perl_logo.png',
          RUBY:      './logos/ruby_logo.png',
          SELF:      './logos/self_logo.png',
          SIMULA:    './logos/simula_logo.png',
          SMALLTALK: './logos/smalltalk_logo.jpeg' }

dependencies = { APL:       [], 
                 CLOJURE  : [ERLANG, LISP, RUBY],    # C++,  HASKELL, C#, JAVA, ML, PROLOG, RACKET, SCHEME
                 ELIXIR   : [CLOJURE, RUBY, ERLANG], # DONE
                 ERLANG   : [LISP, SMALLTALK],       # PLEX, PROLOG
                 IO       : [SMALLTALK, SELF, LISP], # LUA,  PYTHON,  MORE
                 SMALLTALK: [LISP, SIMULA, APL],     # MANY MORE
                 SELF     : [APL, SMALLTALK],        # DONE
                 RUBY     : [LISP, SMALLTALK, PERL]} # MANY MORE

G=nx.DiGraph()

SKIPPED_LANGS = [SIMULA]

for lang in langs:
    if lang in SKIPPED_LANGS:
        continue
    G.add_node(lang, image = mpimg.imread(logos[lang]))

for lang, deps in dependencies.items():
    for dep in deps:
        if lang in SKIPPED_LANGS or dep in SKIPPED_LANGS:
            continue
        G.add_edge(dep, lang)

# spring | spectral | random | kamada_kawai | planar
pos = nx.kamada_kawai_layout(G)

fig=plt.figure(figsize=(5,5))
ax=plt.subplot(111)
ax.set_aspect('equal')
nx.draw_networkx_edges(G,pos,ax=ax)

plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

trans=ax.transData.transform
trans2=fig.transFigure.inverted().transform

piesize=0.075 # this is the image size
p2=piesize/1.5

for n in G:
    xx,yy=trans(pos[n]) # figure coordinates
    xa,ya=trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-p2,ya-p2, piesize, piesize])
    a.set_aspect('equal')
    a.imshow(G.nodes[n]['image'])
    a.axis('off')
ax.axis('off')
plt.show()
