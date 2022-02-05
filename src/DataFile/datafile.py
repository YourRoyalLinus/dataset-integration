from .file_manager import examine_file

class DataFile:

    def __init__(self, path):
        self.path = path
        self._delimeter, self._has_headers = examine_file(self)

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, value):
        try:
            with open(value, 'r') as f:
                pass  
        except FileNotFoundError as ex:
            print(f"ERROR - File does not exist: {value}")
            exit(-1)  
        except IOError as e:
            print(f"ERROR - Unable to open file: {value}")
            exit(-1)
        
        self._path = value

    @property
    def delimeter(self):
        return self._delimeter

    @property
    def has_headers(self):
        return self._has_headers
    
    
