__author__ = 'rnida'

from ftp_Library import *

import unittest

class TestFTP(unittest.TestCase):


    def setUp(self):
        self.ftp = ftpAPI()
        self.ftp.test_login('ftp.swfwmd.state.fl.us')

    def test_pwd(self):
        self.assertEqual(self.ftp.pwd(), '/')

    def test_ls(self):
        self.assertEqual(self.ftp.ls(), ['README.txt', 'lost+found', 'pub', 'public', 'pvt'])


    def test_ls_attributes(self):
        self.assertEqual( self.ftp.ls_attributes() , None )

if __name__ == '__main__':
    unittest.main()


