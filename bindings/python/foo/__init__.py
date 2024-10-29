from _foo import lib

print("running foo/__init__.py")

handle = lib.new_handle(1)


def children(handle):
    print(f"before: ({handle._p}, {handle._i})")
    c = lib.children(handle).first
    print(f"after: ({handle._p}, {handle._i})")
    return c


c = children(handle)

print("\n\nchildren(c) is buggy, it writes the result for the first child to c:\n")

children(c)
children(c)
children(c)

print("\n\nCalling children(handle) multiple times works as expected:\n")

children(handle)
children(handle)
