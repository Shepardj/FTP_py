__author__ = 'rnida'

from ftplib import FTP   # For exceptions
from ftp_Library import *

import unittest

class TestFTP(unittest.TestCase):


    def setUp(self):
        self.ftp = ftpAPI()
        self.local = LocalFileSystem()
        # self.ftp.login_for_testing('ftp.swfwmd.state.fl.us')
        self.ftp.login_for_testing('ftp.edubnetwork.com')

    def test_pwd(self):
        self.assertEqual(self.ftp.pwd(), '/')

#BROKE with server change
    def test_ls(self):
        self.assertEqual(self.ftp.ls(), 'Maildir\nlogs\ntest_folder')

    def test_ls_attributes(self):  # does this test do anything?
        self.assertEqual( self.ftp.ls_attributes() , None )

    def test_cd_one_down(self):
        self.ftp.cd('test_folder')
        self.assertEqual(self.ftp.pwd(), '/test_folder')

# BROKE with server change
    def test_cd_two_down(self):
        self.ftp.cd('test_folder')
        self.ftp.cd('dummy_folder')
        self.assertEqual(self.ftp.pwd(), '/test_folder/dummy_folder')

    def test_cd_one_up(self):
        self.ftp.cd()
        self.assertEqual(self.ftp.pwd(), '/')

    def test_cd_dir_not_found(self):
         self.assertEqual(self.ftp.cd('foo'), 'Cannot cd into <foo>')

# BROKE with server change
    # This test fails because I don't know how to raise exceptions...
    # def test_cd_permission_denied(self):
    #     self.assertEqual(self.ftp.cd('lost+found'), 'Unexpected error: 550 Permission denied.')

# BROKE with server change
    # def test_get_existing_to_current(self):
    #     self.assertEqual(self.ftp.getFile('README.txt'), '226 Transfer complete.')

# BROKE with server change
    # def test_get_not_found_file_to_current(self):
    #     with self.assertRaises(FileNotFoundException):
    #         self.ftp.getFile('FOO.txt')

# DON'T RUN THIS... it changes the desination... so then it will break next try
    # def test_mv_rename_one(self):
    #     self.ftp.cd('test_folder')
    #     self.ftp.mv('dummy.txt','dummy2.txt')
    #     self.assertEqual(self.ftp.ls(), ['dummy_folder', 'dummy2.txt'])

#DON'T MOVE A FILE... it will not error and will break the resulting product
    # def test_mv_file_not_found(self):
    #     with self.assertRaises(FileNotFoundException):
    #         self.ftp.mv('Maildir', 'FOO2.txt')


    def test_mv_not_a_file(self):
        #tried to move a dir
        self.assertEqual(self.ftp.mv('pub', 'pub2'), 'Cannot find <pub>')


#--------------local file system tests
    def test_local_cd(self):
        oldDir = self.local.currentDirectory
        self.assertEqual(self.local.cd("foo"), oldDir + "/foo")

if __name__ == '__main__':
    unittest.main()


