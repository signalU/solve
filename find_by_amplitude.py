
# Busqueda amplitud
# Busqueda  profundidad
# Busqueda por profundidad iterativa


def swap(difference, parent):
    tb = list(parent)
    x, y = tb.index(white_space), tb.index(white_space) + difference
    tb[x], tb[y] = tb[y], tb[x]
    tb = ''.join(tb)
    set_game(game, tb, parent)


def position(d, p):
    for i in d:
        swap(i, p)


def f(x, p):
    right = 1
    left = -1
    down = 3
    up = -3
    if x == 0:
        # left_upper_corner(p)
        position([right, down], p)
    elif x == 1:
        # upper_middle(p)
        position([right, left, down], p)
    elif x == 2:
        position([down, left], p)
    elif x == 3:
        position([up, right, down], p)
    elif x == 4:
        position([right, left, down, up], p)
    elif x == 5:
        position([up, left, down], p)
    elif x == 6:
        position([right, up], p)
    elif x == 7:
        position([right, left, up], p)
    elif x == 8:
        position([up, left], p)
    else:
        print("Internal error system")


def set_game(game, table, parent):
    if table not in game:
        game[parent].append(table)
        game[table] = []

    if parent == last:
        am = parents

    if table not in parents:
        parents.append(table)


    return None


def print_game():
    for i in game.items():
        print(i)
    print("--------------")


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_amplitude_path(graph, start, end, path=[]):
    path = path +[start]
    if start == end:
        return path
    amplitude = None
    for node in parents:
        if node != end:
            newpath = find_amplitude_path(graph, node, end, path)
            if newpath:
                if not amplitude or len(newpath) < len(amplitude):
                    amplitude = newpath
    return amplitude


def find_longest_amplitude_path(graph, start, end):
    a = 1
    path = [start]
    if start == end:
        return path
    for node in parents:
        path.append(node)
        if node != end:
            pass
            # if node not in path:
                # if a == 1:

        else:
            print("Amplitude path:")
            a =0
            return path
    return path


def find_longest_deeply_path(graph, start, end):
    # path = deeply_path + start
    # deeply_path.append(start)
    path = [start]
    if start == end:
        return path
    if not graph[start]:
        return None
    deeply = None
    for node in graph[start]:
        if node != end:
            deeply_path.append(start)
            newpath = find_longest_deeply_path(graph, node, end)
            if newpath:
                deeply = newpath
                if not deeply:
                    deeply = newpath
        else:
            return node
    return deeply


def remove_duplicates(l):
    return list(set(l))


if __name__ == '__main__':
    white_space = "*"
    # table = "2831647"+white_space+"5"
    # parents = [table]
    first = "2831647*5"
    table = first
    parents = [table]
    last = "123*84765"
    # last = "1238*4765"


    game = {table: []}
    n_posible_state = 181440
    fo = 0
    for i in range(40):
        fo += 1
        f(parents[i].index(white_space), parents[i])
        if parents[i] == last:
            break

    print("total for: ", fo)

    # last = "28316*754"
    # last = "28316*754"
    # last = "28316475*"
    deeply_path = []
    am = []

    # print_game()
    # print("Total :", len(game))
    # print(len(parents))
    # print(find_shortest_path(game, "2831647"+white_space+"5", "1238"+white_space+"4765"))
    # print("There is at ", len(find_shortest_path(game, "2831647"+white_space+"5", "1238"+white_space+"4765")), " level")
    # print(find_amplitude_path(game, first, last))
    # print(find_longest_amplitude_path(game, first, last))
    amplitude = find_longest_amplitude_path(game, first, last)
    print(amplitude)

    print("It's", len(amplitude), "node" )
    # print(len(parents))
    # print(len(sorted(set(parents))))

    for raw in amplitude:
        print(raw)



    # print(find_longest_deeply_path(game, first, last))
    # print(deeply_path)
