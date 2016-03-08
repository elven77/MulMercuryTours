import StringIO
import unittest
import HTMLTestRunner
import sys
from tests.testRegister import Register
from tests.testEditProfile import TestEditProfile
from tests.testSignOn import TestSignOn


class Test_HTMLTestRunner(unittest.TestCase):

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Register),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSignOn),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestEditProfile)
        ])

        # Invoke TestRunner
        # buf = StringIO.StringIO()
        fp = file('my_report.html', 'wb')
        # runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='<Demo Test>',
            description='This demonstrates the report output by HTMLTestRunner.'
        )
        runner.run(self.suite)


##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    if len(sys.argv) > 1:
        argv = sys.argv
    else:
        argv = ['runTestSuite.py', 'Test_HTMLTestRunner']
    unittest.main(argv=argv)
    # Testing HTMLTestRunner with HTMLTestRunner would work. But instead
    # we will use standard library's TextTestRunner to reduce the nesting
    # that may confuse people.
    #HTMLTestRunner.main(argv=argv)