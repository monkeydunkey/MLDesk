'''
Base class for unit test case
'''

class testSuite(object):

    def __init__(self):
        self.testcases_ = []
        self.dataDict = {}

    def setup():
        '''
        Things to setup before running the test cases
        '''
        pass

    def teardown():
        '''
        Tear down code to run once the test cases are complete
        '''
        pass

    def register(func):
        if type(func) == type([]):
            self.testcases_.extend(func)
        else:
            self.testcases_.append(func)

    def runTest(func, args):
        '''
        Function to run the actual test, this function will be enclosed by
        decorators to time the test case and other stuff
        '''
        pass


    def runTests():
        '''
        Run all the test cases in this test suite
        '''
        for f in self.testcases_:
            #use inspect module's getargspec to get the function signature and
            #check for the presence of the requried keywords in the data_dict
