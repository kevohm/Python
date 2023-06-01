class FileSystem():
    """A File stystem for shell"""

    def __init__(self) -> None:
        self.files = {}

    def create(self, fileName) -> None:
        ext = "unknown"
        if(fileName.find(".") != -1):
            ext = fileName.split(".")[1]
        self.files[ext] = fileName

    def listFiles(self):
        print(self.files)