import simplify
import re
# from simplify import generate_atoms
# scanner = re.Scanner([
#     [r"[0-9]+", lambda scanner, token: ("INTEGER", token)],
#     [r"[a-z_]+", lambda scanner, token: ("IDENTIFIER", token)],
#     [r"[,.]+", lambda scanner, token: ("PUNCTUATION", token)],
#     [r"\s+", None],  # None == skip token.
# ])


# scanner=re.Scanner([
#   (r"[0-9]+",   	lambda scanner,token:("INTEGER", token)),
#   (r"[a-z_]+",  	lambda scanner,token:("IDENTIFIER", token)),
#   (r"[,.]+",    	lambda scanner,token:("PUNCTUATION", token)),
#   (r"\s+", None), # None == skip token.
# ])

def f(token_type, value):
    if token_type == "IDENTIFIER":
        if value not in atoms:
            atoms.extend(value)
    elif token_type == "O_PARENTHESES":
        pass
    elif token_type == "C_PARENTHESES":
        pass
    elif token_type == "AND":
        pass
    elif token_type == "OR":
        pass
    elif token_type == "NOT":
        pass
    else:
        pass




scanner = re.Scanner([
    # [r"[0-9]+", lambda scanner, token: ("INTEGER", token)],
    [r"[a-z_]+", lambda scanner, token: ["IDENTIFIER", token]],
    [r"[,.]+", lambda scanner, token: ["PUNCTUATION", token]],
    [r"[\(]+?", lambda scanner, token: ["O_PARENTHESES", token]],
    [r"[\)]+?", lambda scanner, token: ["C_PARENTHESES", token]],
    [r"[&]+?", lambda scanner, token: ["AND", token]],
    [r"[|]+?", lambda scanner, token: ["OR", token]],
    [r"[!]+?", lambda scanner, token: ["NOT", token]],
    [r"[\~]+?", lambda scanner, token: ["NOT", token]],

    # [r"[\(\(]+", lambda scanner, token: ("PARENTHESES", token)]
    [r"\s+", None],  # None == skip token.
])

# results, remainder = scanner.scan("   pigeons,  and cows, andh  spiders. (( )) ( )  ")
results, remainder = scanner.scan("   (( (~a & !b) & c) | (d & ((a | b) | !(a & b) ) ) ) ")
for i in results:
     print(i)

atoms = []
for res in results:
    f(res[0], res[1])

print("ATOMS: ", atoms)
# print(atoms)
# generate_atoms(atoms)


# print(results)
