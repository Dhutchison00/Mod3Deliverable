from Lexier import Lexier
class Scanner:
    file = ''
    KEYWORDS = ['import' , 'integer', 'long', 'byte', 'double', 'string', 'unsigned', 'signed','symbol', 'foward', 'declarations', 'functions', 'global', 'contants', 'begin', 'endfun', 'loop', 'is', 'variables', 'set', 'call', 'exit', 'enumeratre', 'endenum', 'struct', 'endstruct', 'define', 'for', 'endfor', 'display', 'while', 'end', 'then', 'increment', 'set', 'destroy', 'allocate','function', 'return', 'type', 'integer', 'is', 'of', 'float', 'count', 'short', 'real', 'double','char', 'tbool','array','increment', 'array','do','input', 'implementations', 'lshift', 'rshift']
    OPERATORS =  ["+","=","-","*","/","'",'"', ",", "<", ">", "xor", "bor", "band", "and", ">=", "<="]
    CONSTANTS = ["\n","[","]","(",")"]
    preIdent = ['set', 'function', 'define']
    foundKey = []
    foundOp = []
    foundCon = []
    foundOther = []
    foundIdent = []
    lexiers = []
    fName = ""
    def __init__(self, fName):
        self.fName = fName
    # Load file from initialization
    def loadFile(self, fName):
        try:
            global file
            file = open(fName, 'r')
        except:
            print("File does not exist.")

    def generateLexems(self):
        self.loadFile(self.fName)
        inMultiComment = False
        identifier = False
        inString = False
        for line in file:
            nextLiteral = False
            words = line.split()
            str = ""
            for word in words:
                # If we reach a single line comment, go to the next line
                if(word == '//'):
                    break
                # Avoid writing down any tokens found between 'description' and '*/'
                if(word == 'description'):
                    inMultiComment = True
                # Once we reach a '*/', we are no longer in a multiline comment
                if(word == '*/'):
                    inMultiComment = False
                    break
                #If we find a " and we are already in a string, end the string
                if('"' in word and word.count('"') % 2 != 0 and inString):
                    str += word
                    self.lexiers.append(Lexier(str, 'STRING_LITERAL'))
                    inString = False
                    continue
                #If we find a ", and we are not already in a string, set ourselves to be in a string
                if('"' in word and word.count('"') %2 != 0 and not inString):
                    str += word + " "
                    inString = True
                    continue
                #If we find a string with no whitespace, exclude
                if('"' in word and word.count('"') == 2):
                    continue
                if(inString):
                    str+= word+" "
                #If we are not in a multicomment or a string, categorize the word
                if(not inMultiComment and not inString):
                    if(identifier or word in self.foundIdent):
                        self.foundIdent.append(word)
                        self.lexiers.append(Lexier(word, 'Identifier'))
                        identifier = False
                        continue
                    if(word in self.preIdent):
                        identifier = True
                        self.lexiers.append(Lexier(word, 'Keyword'))
                        continue
                    if(word in self.CONSTANTS):
                        self.foundCon.append(word)
                        self.lexiers.append(Lexier(word, 'Constant'))
                    elif(word in self.KEYWORDS):
                        self.foundKey.append(word)
                        self.lexiers.append(Lexier(word, 'Keyword'))
                    elif(word in self.OPERATORS):
                        self.lexiers.append(Lexier(word, 'Operator'))
                        #SPECIAL CASE, if an assignemnt operator, next lexeme needs to be a Literal or an Identifier
                        if(word == "="):
                            nextLiteral = True
                        self.foundOp.append(word)
                    elif(word not in self.foundIdent):
                        if(nextLiteral and word not in self.foundIdent):
                            self.lexiers.append(Lexier(word, 'Literal'))
                            nextLiteral = False
                        else:
                            self.lexiers.append(Lexier(word, 'Other'))
                            self.foundOther.append(word)
        #Close the File
        file.close()
    #Getters
    def getKeys(self):
        return self.foundKey
    def getOps(self):
        return self.foundOp
    def getCons(self):
        return self.foundCon
    def getOther(self):
        return self.foundOther
    def getIdent(self):
        return self.foundIdent
    def getLexiers(self):
        return self.lexiers


