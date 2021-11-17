import re

class Scanner():
    def __init__(self,inputData):
        self.__inputString = inputData
        self.__inputString = re.sub("\{.*\}","",self.__inputString)
        self.__tokens = self.__inputString.split()
        self.result = []

        for test in self.__tokens:
            self.find(test)

    def find(self,inp):
        if len(inp) == 0:
            return
        match = re.search("^if[^a-zA-z0-9]|^then[^a-zA-z0-9]|^else$|^end$|^repeat$|^until$|^read$|^write$",inp)
        if match != None:
            self.result.append(tuple(("keyword",match.group())))
            return self.find(inp[len(match.group()):])
        match = re.search("^=|^\(|^\)|^\{|^\}|^\<|^\>|^\+|^\-|^\/|^\:\=|^\*",inp)
        if match != None:
            self.result.append(tuple(("operator",match.group())))
            return self.find(inp[len(match.group()):])
        match = re.search("^[a-zA-z_][a-zA-z0-9_]*",inp)
        if match != None:
            self.result.append(tuple(("identifier",match.group())))
            return self.find(inp[len(match.group()):])
        match = re.search("^[0-9][0-9]*",inp)
        if match != None:
            self.result.append(tuple(("numerical literal",match.group())))
            return self.find(inp[len(match.group()):])
        match = re.search("^;|^\,|^\:",inp)
        if match != None:
            self.result.append(tuple(("special character",match.group())))
            return self.find(inp[len(match.group()):])
        return
        