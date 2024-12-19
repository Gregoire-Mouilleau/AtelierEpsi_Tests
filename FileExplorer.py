import os

class FileExplorer:
    def __init__(self, os_module=os):
        self.os = os_module
        self.current_path = os.path.expanduser('~')

    def get_directory_contents(self):
        """Get the contents of the current directory."""
        try:
            return self.os.listdir(self.current_path)
        except PermissionError:
            print("Access denied.")
            return []

    def navigate_to_index(self, index):
        """Navigate to a subdirectory based on its index."""
        contents = self.get_directory_contents()
        selected = contents[index]
        full_path = self.os.path.join(self.current_path, selected)
        if self.os.path.isdir(full_path):
            self.current_path = full_path
        return full_path

    def navigate_to_parent(self):
        """Move to the parent directory."""
        self.current_path = self.os.path.dirname(self.current_path)

    def get_current_path(self):
        """Return the current directory path."""
        return self.current_path
