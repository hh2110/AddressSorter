# printing the geocode object
def printGeocodeResult(geoc):
    for k in geoc:
        for i, j in k.items():
            print(i,': ', j,'\n')

# checking if we have a aprital match when we search address
def checkPartialMatch(geoc):
    for k, j in geoc[0].items():
        if k=='partial_match':
            if j==True:
                return True;
            else:
                print('partial match came up non-true, \
                      check address', j)
                return False
    return 
