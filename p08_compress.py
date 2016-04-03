#     P08 (**) Eliminate consecutive duplicates of list elements.
#     If a list contains repeated elements they should be replaced with a single copy of the element.
#       The order of the elements should not be changed.
#
# Example:
#     * (compress '(a a a a b c c a a d e e e e))
# (A B C A D E)


def comp_rec(c, acc, l):
    if not l:
        return acc
    else:
        if c == l[0]:
            return comp_rec(c, acc, l[1:])
        else:
            head = l.pop(0)
            return comp_rec(head, acc + [head], l)


def compress(l):
    head = l.pop(0)
    return comp_rec(head, [head], l)


def comp_reduce(acc, elem):
    if not acc:
        return acc + [elem]
    else:
        if acc[-1] == elem:
            return acc
        else:
            return acc + [elem]


def compress_2(l):
    return reduce(comp_reduce, l, [])


if __name__ == "__main__":
    test = [1,1,1,1,2,2,2,1,1,1,4,5,5,5,5]
    print test
    print compress(test)
    print compress_2(test)


