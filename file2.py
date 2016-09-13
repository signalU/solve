from sympy.logic import simplify_logic
from sympy import symbols
# from sympy.abc import a, b, c, d, e, f, g, h, i, j, k
from sympy import sympify
from sympy import S

def hello():
    print("Hello master Leo")
#
# atoms = ["aq", "b", "c", "d"]
# sentence = "(( (~aq & ~b) & c) | (d & ((aq | b) | ~(aq & b) ) ) )"
#
# atoms_string = ",".join(atoms)
# alias = atoms_string + " = symbols (' " + atoms_string + " ')"
# exec(alias)
# expression = None
# # expression =  (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) )
# # exec("expression = (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) ) ")
# exec("expression = " + sentence)
# print(expression)
#
# result = simplify_logic(expression, 'dnf')
# print(result)



def main():
    atoms = ["aq", "b", "c", "d"]
    sentence = "(( (~aq & ~b) & c) | (d & ((aq | b) | ~(aq & b) ) ) )"

    atoms_string = ",".join(atoms)
    alias = atoms_string + " = symbols (' " + atoms_string + " ')"
    exec(alias)
    expression = None
    # locals()['expression'] = None


    kw = {}
    # >> > exec("ret = 4") in kw
    # >> > kw['ret']
    #
    # 4

    # exec(code, d, d)
    # expression =  (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) )
    # exec("expression = (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) ) ")
    # exec("expression = " + sentence)
    # d = {}
    # ...
    # exec
    # "x=23" in d
    # ...
    # return d['x']
    d = {}
    ff = "expression = 'hee' "
    g = globals()
    l = locals()
    exec(ff.format(str), kw)
    # exec("expression = 'hee' " ) in d
    print(expression)
    print(kw['expression'])

    # result = simplify_logic(expression, 'dnf')
    # print(result)

if __name__ == '__main__':
    main()

