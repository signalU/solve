# a, b, c,d = symbols('a,b,c,d')


from sympy import symbols
from sympy.logic import simplify_logic

atoms = ['a', 'b', 'c', 'd']
atoms_string = ",".join(atoms)

# print(atoms_string)
exec(atoms_string + " = symbols (' " + atoms_string + " ')")
expression = None
# expression =  (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) )
exec("expression = (( (~a & ~b) & c) | (d & ((a | b) | ~(a & b) ) ) ) ")
print(expression)

result = simplify_logic(expression, 'dnf')
print(result)
# print(atoms_string + " = symbols (' " + atoms_string + " ')")
# print(type(atoms_string + " = symbols (' " + atoms_string + " ')"))

