class Property_Test(object):
    """Property Test"""

    def __init__(self):
        self._stride_length = 2

    @classmethod
    def class_method(cls):
        print cls.__doc__

    @staticmethod
    def static_method():
        print __doc__

    @property
    def stride_length(self):
        return self._stride_length

    @stride_length.setter
    def stride_length(self, value):
        if value > 10:
            raise ValueError("This pedometer is based on the human stride - a stride length above 10m is not supported")
        else:
            self._stride_length = value

    @stride_length.deleter
    def stride_length(self):
        # del self._stride_length
        self._stride_length = 0


pt = Property_Test()
pt.class_method()
Property_Test.static_method()
print "stride_length=%r" % pt.stride_length
pt.stride_length = 10
print "stride_length=%r" % pt.stride_length
del pt.stride_length
print "stride_length=%r" % pt.stride_length
