import unittest
import StringIO
import HTMLTestRunner
from tests import testRegister
from tests import testSignOn
from tests import testEditProfile
import sys
import unittest

class Test_HTMLTestRunner(unittest.TestCase):
    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(testRegister),
            unittest.defaultTestLoader.loadTestsFromTestCase(testSignOn),
            unittest.defaultTestLoader.loadTestsFromTestCase(testEditProfile)
            ])

        # Invoke TestRunner
        buf = StringIO.StringIO()
        #runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=buf,
                    title='<Demo Test>',
                    description='This demonstrates the report output by HTMLTestRunner.'
                    )
        runner.run(self.suite)


if __name__ == "__main__":
    unittest.main()
    # Testing HTMLTestRunner with HTMLTestRunner would work. But instead
    # we will use standard library's TextTestRunner to reduce the nesting
    # that may confuse people.
    #HTMLTestRunner.main(argv=argv)