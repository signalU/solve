

from sympy.logic import simplify_logic
from sympy.abc import x, y, z, a, b, c, d
from sympy import S

# b = (~x & ~y & ~z) | ( ~x & ~y & z)
expression =  (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) )
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

