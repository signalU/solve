

from sympy.logic import simplify_logic
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k
from sympy import sympify
from sympy import S


# def alias_atoms(atoms):
#     atoms_string = ",".join(atoms)
#     alias = atoms_string + " = symbols (' " + atoms_string + " ')"



dic = {
    "aa": a,
    "bb": b,
    "cc": c,
    "dd": d
}

print(type(  sympify("value") ))
print(type( type(a)))

# b = (~x & ~y & ~z) | ( ~x & ~y & z)
# expression =  (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) )
# expression =  (( (~dic["aa"] & ~dic["bb"]) & dic["cc"]) | (dic["dd"] & ((dic["aa"] | dic["bb"]) | ~(dic["aa"] & dic["bb"]) ) ) )

#exec(m + " = " + "( "+~dic["aa"] + " & " + ~dic["bb"] + ")" )
# m = "(" + dic["aa"] + "&" +dic["bb"] +")"
# expression =  (( (~dic["aa"] & ~dic["bb"]) & dic["cc"]) | (dic["dd"] & ((dic["aa"] | dic["bb"]) | ~(dic["aa"] & dic["bb"]) ) ) )
expression =  (~dic["aa"] & ~dic["bb"])

result = simplify_logic(expression)
# print(simplify_logic(expression))
# print(result)
#
# print(type(result))
# print(S(expression))
#
# print(result >> (~a & ~b ))


# expression2 = simplify_logic(expression >> (~a & ~b ), 'cfn')
# print(expression2)

expression2 = result
impl = a & b
result2 = simplify_logic(expression2, 'cnf')
# result2 = simplify_logic(expression2, 'cnf')
# print(expression2)
# print(result2)


result2 = simplify_logic(expression2, 'dnf')
# print(result2)

print(result2.args)

for arg in result2.args:
    print(arg >> impl)

