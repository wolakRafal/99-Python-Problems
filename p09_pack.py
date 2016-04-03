# P09 (**) Pack consecutive duplicates of list elements into sublists.
#     If a list contains repeated elements they should be placed in separate sublists.
#
#     Example:
# * (pack '(a a a a b c c a a d e e e e))
# ((A A A A) (B) (C C) (A A) (D) (E E E E))

def pack_rec(c, acc, l):
    if not l:
        return acc
    else:
        head = l.pop(0)
        new_acc = merge(acc, head)
        if c == head:
            return pack_rec(c, new_acc, l)
        else:
            return pack_rec(head, new_acc, l)


def merge(l, elem):
    if not l:
        return [[elem]]
    else:
        head = l.pop(0)
        if elem == head[0]:
            return [head + [elem]] + l
        else:
            return [[elem]] + ([head] + l)

def pack(l):
    # head = l.pop(0)
    return list(reversed(pack_rec(None, [], l)))


if __name__ == "__main__":
    test = [1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 4, 5, 5, 5, 5]
    print test
    print pack(test)
