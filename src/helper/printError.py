from src.helper.colorLog import color as colorLog

def printError(errormsg: str) -> str:
    print(colorLog(1, 31,40, errormsg))