from __future__ import print_function
import sys
from chaining.classification import Classification
# from .classification import Classification


def main():
    # sys.stdout.write(str(sys.argv))
    # sys.stdout.flush()
    # data = sys.argv[1]
    cla = Classification()
    conclusions = cla.conclusions()
    predecessors = cla.antecedent()
    # print(conclusions)
    # print(predecessors)
    final_conclusions = set(conclusions) - set(predecessors)
    # print(final_conclusions)
    intermediate_conclusions = set(conclusions) & set(predecessors)
    # print(len(intermediate_conclusions), intermediate_conclusions)
    only_predecessors = set(predecessors) - set(conclusions)
    # print(len(only_predecessors), only_predecessors)
    # print(conclusions - predecessor)

    # print("Final conclusions ")
    # cla.show_names(final_conclusions)
    # print("INTERMEDIATE ")
    # cla.show_names(intermediate_conclusions)
    # print("ONLY PREDECESSORS ")
    # cla.show_names(only_predecessors)
    final_conclusions2 = list()
    intermediate_conclusions2 = list()
    only_predecessors2 = list()
    for item in final_conclusions:
        final_conclusions2.append({"_id": item})
    final_conclusions = final_conclusions2

    for item in intermediate_conclusions:
        intermediate_conclusions2.append({"_id": item})
    intermediate_conclusions = intermediate_conclusions2

    for item in only_predecessors:
        only_predecessors2.append({"_id": item})
    only_predecessors = only_predecessors2


    data = {
        "final": final_conclusions,
        "intermediate": intermediate_conclusions,
        "only_predecessors": only_predecessors
    }

    sys.stdout.write(str(data))
    sys.stdout.flush()

if __name__ == '__main__':
    main()
