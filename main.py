from grammar_reader import *
from rules import createToken
from cyk import CYK
from bonus import cekToken

def displayResult(string):
    print("=================================")
    print("    RESULT : SYNTAX "+string)
    print("=================================")

testFile = input("Masukkan file JS yang mau diperiksa : ")
testFilePath = "./test/"+testFile

print("TOKENIZING...")
tokens = createToken(testFilePath)
print("TOKENIZING - DONE")
cekToken(tokens)
print("READING CFG GRAMMAR...")
cfg = read_grammar('grammar_cfg.txt')
# print(cfg)
print("READING CFG GRAMMAR - DONE")

print("CONVERTING CFG TO CNF...")
cnf = convert_grammar(cfg)
# write_cnf(cnf, "cnf.txt")
# cnf_old = read_cnf()
print("CONVERTING CFG TO CNF - DONE")


print("CHECKING TO CYK...")
if(CYK(cnf,tokens)):
    print("CHECKING TO CYK - DONE")
    displayResult("TRUE")
else:
    print("CHECKING TO CYK - DONE")
    displayResult("FALSE")


