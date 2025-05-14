import re
from werkzeug.datastructures import FileStorage

def verify_extension(file:FileStorage, extension):
    pattern = rf"\{extension}$"

    match = re.search(pattern, file.filename, re.IGNORECASE)
    if not bool(match):
        raise Exception("File must be a '.cook' file")

def verify_filestorage(file:FileStorage, expected_type: type=str, extension:str= ".cook", max_size_mb:int=3, min_size_mb: int=0  ):
    verify_extension(file,extension)
    
    if type(file) != FileStorage:
        raise Exception(f"{file} is not a flask FileStorage type")
    
    
