'''
Group Members:
Andrew Hutchison
Dalton Harvey

CS 4308: Concepts of Programming Languages, Section W02

Deliverable 2
March 24th, 2022
'''


from Scanner import Scanner
from Lexier import Lexier
class Parser:
    nextToken = None
    scanner = None
    def __init__(self, fName):
        #On Parser initialization, create a scanner object with the proper file name
        self.scanner = Scanner(fName)

    def parse(self):
        #Have initialized scanner run through the file
        self.scanner.generateLexems()
        # Return ordered list of lexemes and their corresponding token
        lexiers = self.scanner.getLexiers()
        #For every lexeme the scanner detects, print out the token and lexeme
        for lexier in lexiers:
            print("Next token is:",lexier.getToken(),"|| Next lexeme is:",lexier.getLexeme())
            print("")

#Main function that initializes a Parser object and executes parse()
def main():
    #Take in file input for the parser
    fName = input("What .scl file would you like to open? ")
    parser = Parser(fName)
    parser.parse()
#Call the main function
main()

