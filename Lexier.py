class Lexier:
    #Instance Vars
    token = None
    lexeme = None
    
    #Initizlize Lexier Object
    def __init__(self, lexeme, token):
        self.token = token
        self.lexeme = lexeme
        
        #If token is "Other" categorize it further (I.e lexeme = ';', set token to "semicolon")
        if(token == "Other"):
            self.__categorizeOther(lexeme)
        #If token is a Constant, categorize it further
        if(token == "Constant"):
            self.__categorizeConstant(lexeme)
        # If token is a Operator, categorize it further
        if (token == "Operator"):
            self.__categorizeOperator(lexeme)
        #If token is a Literal, find out what type of literal
        if(token == "Literal" or token == "Other"):
            self.__categorizeLiteral(lexeme)
    #Further Categorize Literal
    def __categorizeLiteral(self, lexeme):
        try:
            i = eval(lexeme)
            if type(i) == int:
                self.token = 'INTEGER_LITERAL'
            elif type(i) == float:
                self.token =  'DOUBLE_LITERAL'
            elif type(i) == bool:
                self.token =  'BOOLEAN_LITERAL'
        except:
            self.token = "Other"
    #Further Categorize Other
    def __categorizeOther(self, lexeme):
        if(lexeme == ";"):
            self.token = "Semicolon"
    #Further Categorize Constants 
    def __categorizeConstant(self, lexeme):
        if (lexeme == "("):
            self.token = "Left Parenthesis"
        if (lexeme == ")"):
            self.token = "Right Parenthesis"
        if (lexeme == "["):
            self.token = "Left Bracket"
        if (lexeme == "]"):
            self.token = "Right Bracket"
    #Further Categorize Operators
    def __categorizeOperator(self, lexeme):
        if(lexeme == "+" or lexeme == "-" or lexeme == "*" or lexeme == "/"):
            self.token = "Arithmetic Operator"
        if(lexeme == "="):
            self.token = "Assignement Operator"
        if(lexeme in ["<", ">", "xor", "bor", "band", "and", ">=", "<="]):
            self.token = "Conditional Operator"
    
    # Getters
    def getLexeme(self):
        return self.lexeme
    def getToken(self):
        return self.token