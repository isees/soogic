class Classic_Class:
    """### old-style classes have disappeared in Python 3, and inheritance from object has become implicit.
    So, always prefer new style classes unless you need backward compat with old software. """

    def __init__(self):
        pass


class New_Class(object):
    """### I inherit class object:) """

    pass

print Classic_Class.__doc__
print Classic_Class
print type(Classic_Class)
print type(Classic_Class())
print
print New_Class.__doc__
print New_Class
print type(New_Class)
print type(New_Class())

