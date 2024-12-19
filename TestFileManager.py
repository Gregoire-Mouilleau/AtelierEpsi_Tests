import unittest
import os
from FileSelector import FileSelector
from unittest.mock import patch

class TestFileSelector(unittest.TestCase):
    @patch("os.listdir", return_value=["file1.txt", "file2.txt", "folder1"])
    def test_select_files_by_indices(self, mock_listdir):
        selector = FileSelector()
        selector.load_directory_contents("/test")

        expected = [
            os.path.join("/test", "file1.txt"),
            os.path.join("/test", "folder1"),
        ]
        selected = selector.select_files_by_indices("0,2", "/test")

        self.assertEqual(selected, expected)

    def test_invalid_indices(self):
        selector = FileSelector()
        selector.current_directory_contents = ["file1.txt"]

        selected = selector.select_files_by_indices("abc", "/test")
        self.assertEqual(selected, [])

if __name__ == "__main__":
    unittest.main()
