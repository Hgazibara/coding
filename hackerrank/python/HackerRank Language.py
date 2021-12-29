import sys

languages = ['C', 'CPP', 'JAVA', 'PYTHON', 'PERL', 'PHP', 'RUBY', 'CSHARP', 'HASKELL', 'CLOJURE', 'BASH', 'SCALA', 'ERLANG', 'CLISP', 'LUA', 'BRAINFUCK', 'JAVASCRIPT', 'GO', 'D', 'OCAML', 'R', 'PASCAL', 'SBCL', 'DART', 'GROOVY', 'OBJECTIVEC']

N = sys.stdin.readline()

for request in sys.stdin:
    api_id, param = request.split()
    if param.replace('\n', '') in languages:
        print('VALID')
    else:
        print('INVALID')