from __future__ import print_function
import webbrowser
import sys
from sympy.logic import simplify_logic
from sympy import symbols

from writeDB import insert_proposition, insert_sentence
from tokenizer import tokenizer
from simplify import disjunctive_normal_form
# from file2 import hello


def open_an_url(url):
    # Opens in safari browser
    webbrowser.get('firefox').open_new(url)


def main():
    sys.stdout.write(str(sys.argv))
    sys.stdout.flush()

    data = sys.argv[1]

    data = data.replace("and", "&").replace("or", "|").replace("!", "~").replace(" not ", "~")
    data = data.split("->")
    consequent = data[1]
    data = data[0]
    print(data)
    atoms = tokenizer(data)

    predecessor = disjunctive_normal_form(atoms, data)
    print("")
    print(predecessor.atoms(), "Atoms")
    print(predecessor, "predecessor")
    print(predecessor.args, "Arguments")

    # pre = str(predecessor.args)
    # succe = consequent

    # insert_sentence(pre, succe)

    # expr.args[2].args

    print(predecessor.args[0].args)
    print(predecessor.args[1].args)
    print(len(predecessor.args))

    for item in predecessor.args:
        # item = item.args
        # print(list
        print(item)
        pre = str(item)
        succe = consequent
        insert_sentence(pre, succe)


        # print(list(item.atoms()))
    # text = str(predecessor.args)
    # print(text)
    # # text.replace("And", "")
    # text = text.split("And")
    # print(text, type(text))



    # hello()
    # atoms_string = ",".join(atoms)
    # alias = atoms_string + " = symbols (' " + atoms_string + " ')"
    # exec(alias)
    # expression = None
    # # expression =  (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) )
    # # exec("expression = (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) ) ")
    # exec('expression = ' + data)
    # print(expression)
    #
    # result = simplify_logic(expression, 'dnf')
    # print(result)

    # open_an_url("www.youtube.com")


if __name__ == '__main__':
    try:
        main()
    # except OSError as err:
    #     print("OS error: {0}".format(err))
    # except ValueError:
    #     print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.stderr.write(str(sys.argv))
        sys.stderr.flush()
        raise
