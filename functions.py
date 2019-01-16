import Levenshtein as lev

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

# levenshtein distance funtion
# to measure difference between two strings
def SimilarityBtwStrings(inp, res):
    # only consider whole of input but part of result - first 2 elements
    
    # first get a list of result words
    rWordList=[]
    #list1 is based on commas
    list1=res.split(', ')[0:2] #this number 2 gets us the first 2 elements
    for rPhrase in list1:
        if ' ' in rPhrase:
            list2=rPhrase.split(' ')
            for rWord in list2:
                rWordList.append(rWord)
        else:
            rWordList.append(rPhrase)
    rWordList=[i.lower() for i in rWordList]
    
    iWordList=inp.strip().split(' ')
    iWordList=[i.lower() for i in iWordList]

    for i in iWordList:
        for r in rWordList:
            if r!='peshawar' and i!='peshawar' and \
               r!='phase' and i!='phase' and \
               r.isdigit()!=True and i.isdigit()!=True:
                   if lev.distance(i,r) < 2:
                       return 1
      
    return 0
