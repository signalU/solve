from __future__ import print_function
import sys
from backwards.classification import Classification
# from .classification import Classification


def main():
    # print("something")
    # print(sys.argv[1])
    _id_final = sys.argv[1]
    _id_final =  _id_final.replace(" ","")

    cla = Classification()
    conclusions = cla.conclusions()
    val = list()
    val = cla.propositions_implies_from(_id_final, [])
    final_conclusions = _id_final

    _id_guided = list()
    # print(val)
    for v in val:
        # print(v)
        _id_guided.append(str(v["_id"]))
        # v["_id"]= str(v["_id"])
        # _id_guided.append(v)

    # print(_id_guided)

    predecessors = cla.control_antecedent(_id_guided)

    only_predecessors = set(predecessors) - set(conclusions)
    intermediate_conclusions = set(conclusions) & set(predecessors)

    # cla.show_names(only_predecessors)
    # cla.show_names(intermediate_conclusions)


    # final_conclusions2 = list()
    intermediate_conclusions2 = list()
    only_predecessors2 = list()


    # for item in final_conclusions:
    #     final_conclusions2.append({"_id": item})
    # final_conclusions = final_conclusions2

    final_conclusions = [{"_id": final_conclusions}]

    for item in intermediate_conclusions:
        intermediate_conclusions2.append({"_id": item})
    intermediate_conclusions = intermediate_conclusions2

    for item in only_predecessors:
        only_predecessors2.append({"_id": item})
    only_predecessors = only_predecessors2

    rules2 = list()
    for item in _id_guided:
        rules2.append({"_id": item})

    # print(val)

    data = {
        "rules": rules2,
        # "rules": val,
        "final": final_conclusions,
        "intermediate": intermediate_conclusions,
        "only_predecessors": only_predecessors
    }
    # print(data)

    sys.stdout.write(str(data))
    sys.stdout.flush()

if __name__ == '__main__':
    main()