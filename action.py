from persistence import *

import sys

def buyProduct(splittedline : list[str]):
    repo.activities.insert(Activitie(*splittedline))
    productRecord = repo.products.find(id = splittedline[0])
    repo.products.update({"quantity": str(int(productRecord[0].quantity) + int(splittedline[1]))},{"id" : splittedline[0]})

def sellProduct(splittedline : list[str]):
    productRecord = repo.products.find(id = splittedline[0])
    if(abs(int(splittedline[1])) <= int(productRecord[0].quantity)):
        repo.activities.insert(Activitie(*splittedline))
        repo.products.update({"quantity": str(int(productRecord[0].quantity) - int(splittedline[1]))},{"id" : splittedline[0]})

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip("\n").split(", ")
            buyProduct(splittedline) if(int(splittedline[1]) > 0) else sellProduct(splittedline)
if __name__ == '__main__':
    main(sys.argv)