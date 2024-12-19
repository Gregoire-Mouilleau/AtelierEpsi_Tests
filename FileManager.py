import os
import shutil

class FileManager:
    def __init__(self, file_explorer, file_selector, shutil_module=shutil):
        self.explorer = file_explorer
        self.selector = file_selector
        self.shutil = shutil_module

    def display_directory_contents(self):
        """Display contents of the current directory."""
        print(f"\nCurrent Directory: {self.explorer.get_current_path()}")
        for idx, item in enumerate(self.explorer.get_directory_contents()):
            print(f"{idx}: {item}")

    def select_files(self, indices):
        """Delegate file selection to FileSelector."""
        self.selector.load_directory_contents(self.explorer.get_current_path())
        self.selector.select_files_by_indices(indices, self.explorer.get_current_path())

    def copy_files(self, destination):
        """Copy selected files to a destination."""
        selected_files = self.selector.get_selected_files()
        for file in selected_files:
            self.shutil.copy(file, destination)
        print("Files copied successfully.")

    def move_files(self, destination):
        """Move selected files to a destination."""
        selected_files = self.selector.get_selected_files()
        for file in selected_files:
            self.shutil.move(file, destination)
        print("Files moved successfully.")

    def delete_files(self):
        """Delete selected files."""
        selected_files = self.selector.get_selected_files()
        for file in selected_files:
            if os.path.isfile(file):
                os.remove(file)
            elif os.path.isdir(file):
                shutil.rmtree(file)
        print("Files deleted successfully.")
