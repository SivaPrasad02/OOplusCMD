class A:
    def __init__(self,object):
        self.object = object
        self.class_name = 'A'
        self.object
    def execute(self):
        print("The name of Class is {}".format(self.class_name))
        print('The name of the object is {}'.format(self.object))
        return 'A'
    def shutdown(self):

        del self.object
        del self.class_name
class B:
    def __init__(self,object):
        self.object = object
        self.class_name = 'B'
        self.object
    def execute(self):
        print("The name of Class is {}".format(self.class_name))
        print('The name of the object is {}'.format(self.object))
        return 'B'
    def shutdown(self):

        del self.object
        del self.class_name
class C:
    def __init__(self,object):
        self.object = object
        self.class_name = 'C'
        self.object
    def execute(self):
        print("The name of Class is {}".format(self.class_name))
        print('The name of the object is {}'.format(self.object))
        return 'C'
    def shutdown(self):

        del self.object
        del self.class_name