import unittest
from unittest.mock import patch, Mock
from FileExplorer import FileExplorer

class TestFileExplorer(unittest.TestCase):
    @patch("os.listdir", return_value=["file1.txt", "folder1"])
    def test_get_directory_contents(self, mock_listdir):
        explorer = FileExplorer()
        contents = explorer.get_directory_contents()
        self.assertEqual(contents, ["file1.txt", "folder1"])

    @patch("os.path.isdir", return_value=True)
    @patch("os.listdir", return_value=["folder1"])
    def test_navigate_to_index(self, mock_listdir, mock_isdir):
        explorer = FileExplorer()
        explorer.get_directory_contents()
        explorer.navigate_to_index(0)
        self.assertTrue(mock_isdir.called)

    @patch("os.path.dirname", return_value="/parent")
    def test_navigate_to_parent(self, mock_dirname):
        explorer = FileExplorer()
        explorer.navigate_to_parent()
        self.assertEqual(explorer.get_current_path(), "/parent")

if __name__ == "__main__":
    unittest.main()
