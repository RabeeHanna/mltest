from math import log
from cPickle import dump, load


strings = ["The quick brown fox jumped over the lazy dog",
           "I have the best lazy dog in the whole world",
           "Adina has three dogs",
           "I prefer to not have any pets",
           "dogs are the most common type of lazy pet",
           "the whole lazy pet lazy pet"
           ]

'''
f = open('text.txt')
strings = [f.read()]
f.close()
f = open("sawyr10.txt")
strings.append(f.read())
f.close()
'''
allwords = {}
allwordslen = 0

def inc(d,i):
    if not i in d[0]:    
        d[0][i] = 1.0
    else:
        d[0][i] += 1.0
    d[1] += 1.0


def getprobs(word):
    # assigns probabilities
    try:
        return allnextword[word]
    except:
        try:
            dd = allwords[word]
        except:
            return ''
        ddd = {}
        highestprob = 0
        nextword = ''
        prob = 0

        for nw in dd[0].keys():
            prob = - log(dd[0][nw],10) - log(dd[1],10)
            ddd[nw] = prob
            if (prob == 0.0) or (prob < highestprob):
                highestprob = prob
                nextword = nw
        #return ddd,nextword
        allnextword[word] = nextword
        
        '''
        for nw in range(5):
            prob = - log(dd[0][nw],10) - log(dd[1],10)
            ddd[nw] = prob
            if (prob == 0.0) or (prob < highestprob):
                highestprob = prob
                nextword = nw
        #return ddd,nextword
        allnextword[word] = nextword
        '''
        return nextword

try:
    allwordsfile = open('dump.dat', 'rb')
    allwords = load(allwordsfile)
    allwordsfile.close()
    print('all word dump found')
except:
    print('all word dump not found')
    for s in strings:
        s = s.replace('"', '')
        s = s.replace(',', '')
        s = s.replace('-', ' ')
        s = s.replace('?', '.')
        s = s.replace('!', '.')
        s = s.replace(' of ', ' ')
        s = s.replace(' the ', ' ')
        s = s.replace('. the ', ' ')
        s = s.replace(' a ', ' ')
        s = s.replace('. a ', ' ')
        s = s.replace('[', '')
        s = s.replace(']', '')
        ssplit = s.lower().split()
        for i in range(len(ssplit)):
            allwordslen += 1
            if ssplit[i] not in allwords:
                if i != len(ssplit) - 1:
                    allwords[ssplit[i]] = [{ssplit[i+1]:1.0},1.0]
                else:
                    allwords[ssplit[i]] = [{'.':1.0},1.0]
            else:
                #print(ssplit[i], allwords[ssplit[i]])
                if i != len(ssplit) - 1:
                    inc(allwords[ssplit[i]],ssplit[i+1])
                else:
                    inc(allwords[ssplit[i]],'.')
        allwordsfile = open('dump.dat', 'wb+')
        dump(allwords, allwordsfile, -1)
        allwordsfile.close()
    
try:
    allnextwordfile = open('dump2.dat', 'rb')
    allnextword = load(allnextwordfile)
    allnextwordfile.close()
    print('next word dump found')
except:
    print('next word dump not found')
    allnextword = {}
    for w in allwords.keys():
        allnextword[w] = getprobs(w)
    allnextwordfile = open('dump2.dat', 'wb+')
    dump(allnextword, allnextwordfile, -1)
    allnextwordfile.close()



#print([pow(10, x) for x in getprobs('lazy')])
#print(getprobs('the'))

'''
def makesentance(firstword, n):        
    word = firstword
    sentance = word
    for i in range(n):
        word = getprobs(word)
        sentance += ' ' + word
    print (sentance)
'''
