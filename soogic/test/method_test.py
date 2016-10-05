# coding: utf-8

class Method_test(object):
    """ This is Test written by Bain"""

    def __init__(self):
        pass

    def say(self, msg):
        print 'I said: \'%s\' %r' % (msg, self)

    @classmethod
    def scream(cls):
        print 'This is so cool: %r' % cls

    @staticmethod
    def shout(name, msg):
        print '%s says: \'%s\'' % (name, msg)

    @staticmethod
    def murmur(**kwargs):
        for key, value in kwargs.iteritems():
            print "%s is %s" % (key, value)

    def show_info(self):
        print "dict: %r" % self.__dict__
        print "doc: %r" % self.__doc__
        print "module: %r" % self.__module__

    @classmethod
    def show_class_info(cls):
        print "dict: %r" % cls.__dict__
        print "doc: %r" % cls.__doc__
        print "module: %r" % cls.__module__


Method_test.scream()
Method_test.shout('林志玲', 'I love u')
Method_test().say('I love u 2')
Method_test.murmur(mary='nothing', andrian='the swordman', bain='the captain', shawn='the cook')
Method_test().show_info()
Method_test.show_class_info()
