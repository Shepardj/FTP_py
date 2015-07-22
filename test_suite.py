__author__ = 'rnida'

from ftplib import FTP   # For exceptions
from ftp_Library import *

import unittest

class TestFTP(unittest.TestCase):


    def setUp(self):
        self.ftp = ftpAPI()
        self.ftp.login_for_testing('ftp.swfwmd.state.fl.us')

    def test_pwd(self):
        self.assertEqual(self.ftp.pwd(), '/')

    def test_ls(self):
        self.assertEqual(self.ftp.ls(), ['README.txt', 'lost+found', 'pub', 'public', 'pvt'])

    def test_ls_attributes(self):  # does this test do anything?
        self.assertEqual( self.ftp.ls_attributes() , None )

    def test_cd_one_down(self):
        self.ftp.cd('pub')
        self.assertEqual(self.ftp.pwd(), '/pub')

    def test_cd_two_down(self):
        self.ftp.cd('pub')
        self.ftp.cd('CFCA')
        self.assertEqual(self.ftp.pwd(), '/pub/CFCA')

    def test_cd_one_up(self):
        self.ftp.cd()
        self.assertEqual(self.ftp.pwd(), '/')

    def test_cd_dir_not_found(self):
        with self.assertRaises(NotADirectoryException):
            self.ftp.cd('foo')

    # This test fails because I don't know how to raise exceptions...
    def test_cd_permission_denied(self):
        with self.assertRaises(FTP.error_reply):
            self.ftp.cd('lost+found')

    def test_get_existing_to_current(self):
        self.assertEqual(self.ftp.getFile('README.txt'), '226 Transfer complete.')

    def test_get_not_found_file_to_current(self):
        with self.assertRaises(FileNotFoundException):
            self.ftp.getFile('FOO.txt')


if __name__ == '__main__':
    unittest.main()


