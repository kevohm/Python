class File():
    """A class for file objects"""
    
    _file_types = ["pdf","jpg","png","txt","mp4"]

    def __init__(self,name=None, ext=None) -> None:
        if name is None or ext is None:
            return
        self.name = name
        self.ext = ext
    
    def __str__(self) -> str:
        return "Current file is {}.{}".format(self.name, self.ext)
    
f = File("s","e")
print(str(f.__class__))
