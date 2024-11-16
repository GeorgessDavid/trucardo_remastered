import sys

def setLog(path:str, function):
    original_stdout = sys.stdout
    
    with open(path, 'a', encoding="UTF-8") as doc:
        sys.stdout = doc
        function()
    sys.stdout = original_stdout