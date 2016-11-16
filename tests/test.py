import unittest
import zipper
import pathlib


class TestZipperMethods(unittest.TestCase):

    def setUp(self):
        self.current_folder = pathlib.Path(".").absolute()
        self.files = [
            'example.jpg',
            'example_9pyK5Dy.jpg',
            'example_pTR63bN.jpg',
            'example_syUA8fW.jpg'
        ]

    def _open_file(self, file_name='public.zip'):
        path_file = str(self.current_folder.joinpath(file_name))
        return zipper.open(path_file)

    def test_open(self):
        f = self._open_file()
        self.assertNotEqual(f, None)
        zipper.close(f)

    def test_list_files(self):
        f = self._open_file()
        self.assertListEqual(self.files, zipper.get_all_files_name(f))
        zipper.close(f)

    def test_extract_files(self):
        f = self._open_file()
        file_paths = zipper.extract_all_files(f)
        for path in file_paths:
            self.assertEqual(pathlib.Path(path).exists(), True)
        zipper.close(f)

    def test_failed_extract_files(self):
        f = self._open_file("public2.zip")
        self.assertRaises(zipper.NotValidContent, lambda: zipper.extract_all_files(f))
        zipper.close(f)


if __name__ == '__main__':
    unittest.main()
