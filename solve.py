from __future__ import print_function
import webbrowser
import sys
from sympy.logic import simplify_logic
from sympy import symbols

# from writeDB import insert_proposition
from tokenizer import tokenizer
from simplify import alias_atoms
# from file2 import hello


def open_an_url(url):
    # Opens in safari browser
    webbrowser.get('firefox').open_new(url)


def main():
    # arguments = "(( (!a & !b) & c) | (d & ((a | b) | !(a & b) ) ) )"
    # print("This is the beginning and I'am awesome")
    # a = True
    # b = False
    # c = True
    # d = False
    # q = arguments.replace("!", "not ").replace("&", " and ").replace("|", " or ")
    # print(q)
    # f = (((not a and not b) and c) or (d and ((a or b) or not (a and b))))
    # if f:
    #     print("It was true")

    sys.stdout.write(str(sys.argv))
    sys.stdout.flush()

    # print("I'am the best ever")
    # alldata = sys.argv
    data = sys.argv[1]
    # qwe = "sakqw"
    # insert_proposition(data)
    data = data.replace("and", "&").replace("or", "|").replace("!", "~").replace(" not ", "~")
    atoms = tokenizer(data)
    alias_atoms(atoms, data)


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
    main()
