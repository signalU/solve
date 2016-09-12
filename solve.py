def main():
    arguments = "(( (!a & !b) & c) | (d & ((a | b) | !(a & b) ) ) )"
    print("This is the beginning and I'am awesome")
    a = True
    b = False
    c = True
    d = False
    q = arguments.replace("!", "not ").replace("&", " and ").replace("|", " or ")
    print(q)
    f = (((not a and not b) and c) or (d and ((a or b) or not (a and b))))
    if f:
        print("It was true")


if __name__ == '__main__':
    main()
