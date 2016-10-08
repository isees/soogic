class A(object):
    def __method(self):
        """Double underline means the method won't be overridden & it's private:)"""
        print "This is a method from A"

    def method(self):
        self.__method()


class B(A):
    def __method(self):
        """Let's try if we can overridden the method from A"""
        print "This is a method from B"


b = B()
b.method()
