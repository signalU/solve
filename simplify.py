from sympy.logic import simplify_logic
from sympy import symbols
# from sympy.abc import a, b, c, d, e, f, g, h, i, j, k
from sympy import sympify
from sympy import S
import sys


def alias_atoms(atoms, sentence):
    # _locals = locals()
    namespace = {}
    atoms_string = ",".join(atoms)
    alias = atoms_string + " = symbols (' " + atoms_string + " ')"
    # exec(alias)
    exec("from sympy import symbols\n"+alias.format(str), namespace)
    # expression = None
    # expression =  (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) )
    # exec("expression = (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) ) ")
    # exec('expression = ' + sentence)
    text = 'expression = ' + sentence
    exec(text.format(str), namespace)
    # print(namespace["expression"])
    expression = namespace["expression"]

    # print(expression)

    result = simplify_logic(expression, 'dnf')
    # print(result)
    return result

# expression = None
#
# print(type(  sympify("value") ))
# print(type( type(a)))
#
# # b = (~x & ~y & ~z) | ( ~x & ~y & z)
# # expression =  (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) )
# # expression =  (( (~dic["aa"] & ~dic["bb"]) & dic["cc"]) | (dic["dd"] & ((dic["aa"] | dic["bb"]) | ~(dic["aa"] & dic["bb"]) ) ) )
#
# #exec(m + " = " + "( "+~dic["aa"] + " & " + ~dic["bb"] + ")" )
# # m = "(" + dic["aa"] + "&" +dic["bb"] +")"
# # expression =  (( (~dic["aa"] & ~dic["bb"]) & dic["cc"]) | (dic["dd"] & ((dic["aa"] | dic["bb"]) | ~(dic["aa"] & dic["bb"]) ) ) )
# expression1 =  (~dic["aa"] & ~dic["bb"])
#
# result = simplify_logic(expression1)
# # print(simplify_logic(expression))
# # print(result)
# #
# # print(type(result))
# # print(S(expression))
# #
# # print(result >> (~a & ~b ))
#
#
# # expression2 = simplify_logic(expression >> (~a & ~b ), 'cfn')
# # print(expression2)
#
# expression2 = result
# impl = a & b
# result2 = simplify_logic(expression2, 'cnf')
# # result2 = simplify_logic(expression2, 'cnf')
# # print(expression2)
# # print(result2)
#
#
# result2 = simplify_logic(expression2, 'dnf')
# # print(result2)
#
# print(result2.args)
#
# for arg in result2.args:
#     print(arg >> impl)
