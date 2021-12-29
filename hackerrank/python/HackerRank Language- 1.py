import sys

all_lines = [line.replace('\n', '') for line in sys.stdin.readlines()]
languages = {'C','CPP','JAVA','PYTHON','PERL','PHP','RUBY','CSHARP','HASKELL','CLOJURE','BASH','SCALA','ERLANG','CLISP','LUA','BRAINFUCK','JAVASCRIPT','GO','D','OCAML','R','PASCAL','SBCL','DART','GROOVY','OBJECTIVEC'}

for line in all_lines[1:]:
    (id, lang) = line.split()
    print('VALID' if lang in languages else 'INVALID')