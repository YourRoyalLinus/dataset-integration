import csv

class DataFile:
    """A class to represent a File provided by the user containing data

    Attributes:
        path (property): str
            - absolute path of the file
        delimeter (read-only property): str
            - delimeter of the file
        has_headers (read-only property): bool
            - boolean indicating whether the file has headers
    Methods
        _examine_file (implementation detail)
            - return a tuple of (delimeter, has_headers) to represent the
            str delimeter of the file and a boolean to indicate whether the 
            file has headers
    """
    def __init__(self, path):
        """
        Constructs the necessary atributes for a DataFile object

        Positional Arguments:
            path : str
                - absolute path of the file
        
        When attempting to set the path provided, only a valid, openable file
        will be permitted, otherwise an error will be given.
        After the path is set, the file will be examined to set
        delimeter and has_headers using the 
        file_manager.examine_file function.
        """
        self.path = path
        self._delimeter, self._has_headers = self._examine_file()

    def __repr__(self) -> str:
        cls = type(self).__name__
        return "{}({})".format(cls, self.__dict__)

    def __str__(self) -> str:
        cls = type(self).__name__
        return "{0} object representing {1} {2} headers".format(cls, self.path,
                                                "WITH" if self.has_headers else
                                                "WITHOUT")

    @property
    def path(self) -> str:
        """Return the _path attribute managed by the property"""
        return self._path
    
    @path.setter
    def path(self, value) -> None:
        """Setter for _path attribute managed by the property
        Before setting _path property, check that the file exists
        and can be opened. Only if exists and openable, set the path
        """
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
    def delimeter(self) -> str:
        """Return the read-only _delimeter attribute managed by the property"""
        return self._delimeter

    @property
    def has_headers(self) -> bool:
        """Return the read-only _has_headers attribute managed by the 
        property
        """
        return self._has_headers

    def _examine_file(self) -> tuple:
        """Return the file delimeter as a string and a boolean indicating 
        whether the file contains headers as a tuple(delimeter, has_headers)
        """
        first_n_bytes = 1024
        sniffer = csv.Sniffer()

        with open(self.path, 'r') as f:
            sample = f.read(first_n_bytes)


        return (sniffer.sniff(sample).delimiter, sniffer.has_header(sample))
    

