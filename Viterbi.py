"""

Desc: Viterbi's algorithm to predict weather
Submitted By : Vidya Sri Mani

In Detail:
Programmatically implement the Viterbi algorithm and run it with the HMM in
Figure 1 to compute the most likely weather sequence and probability for a given
observation sequence. Example observation sequences: 331, 122313, 331123312,. etc

"""

"""
Given Information
----------------------------------
Start   : 0
Hot     : 1
Cold    : 2

Probabilities
----------------------------------
start --> hot = 0.8
start --> cold = 0.2

hot --> hot = 0.7
hot --> cold = 0.3

cold --> hot =0.4
cold --> cold = 0.6


----------------------------------
B1&B2 Probabilites
P(1|Hot) = 0.2      P(1|Cold) = 0.5
P(2|Hot) = 0.4      P(2|Cold) = 0.4
P(3|Hot) = 0.4      P(3|Cold) = 0.1
"""

def initializeProbabilities():
    trans = {
        0: [0.8, 0.2],
        1: [0.7, 0.3],
        2: [0.4, 0.6]
    }

    obs = {
        1: [0.2, 0.5],
        2: [0.4, 0.4],
        3: [0.4, 0.1]
    }
    return  trans,obs

#computing probability for each element in the list
def computeProbability(listVals):
    prob = 1
    for val in listVals:
        prob*=val
    return prob


def traceback(finalState,bkPointer):
    #print('in traceback')
    output = list()
    if finalState == 1:
        output.append('HOT')
    else:
        output.append('COLD')

    for i in bkPointer[::1]:
        if i[finalState-1] == 1:
            output.append('HOT')
        else:
            output.append('COLD')
        finalState=i[finalState-1]

    return output.reverse()

#Implementing Viterbi's algorithm to compute the most likely weather
def viterbi(sequence):
    start = 0
    hot = 1
    cold = 2
    sequenceList = list(sequence)#to seprate each state in the input sequence as a list
    weatherSeqList = list()
    bkPointer = list()#is this really needed?
    trans,obs= initializeProbabilities()

    #sequenceList[1] gives the first element
    hotPrevious=trans[start][hot-1] * obs[int(sequenceList[0])][hot-1]
    coldPrevious=trans[start][cold-1] * obs[int(sequenceList[0])][cold-1]
    weatherSeqList.append([hotPrevious,coldPrevious])

    for s in sequenceList:
        hotToHot = trans[hot][hot-1]*obs[int(s)][hot-1]* hotPrevious
        coldToHot = trans[cold][hot-1] * obs[int(s)][hot-1] * coldPrevious
        if coldToHot > hotToHot:
            hotStat = cold
            currHot = coldToHot
        else:
            hotStat = hot
            currHot = hotToHot

        hotToCold = trans[hot][cold-1]*obs[int(s)][cold-1]* hotPrevious
        coldToCold = trans[cold][cold-1]*obs[int(s)][cold-1]* coldPrevious

        if hotToCold > coldToCold:
            coldStat = hot
            currCold = hotToCold
        else:
            coldStat = cold
            currCold = coldToCold

        bkPointer.append([hotStat, coldStat])
        weatherSeqList.append([currHot,currCold])

        hotPrevious = currHot
        coldPrevious = currCold
    l = len(weatherSeqList)-1

    if(weatherSeqList[l][0]>weatherSeqList[l][1]):
        finalState=hot
    else:
        finalState=cold

    weatherSeq = traceback(finalState,bkPointer)
    print('Weather sequence:\n')
    print(weatherSeq)



#Program Execution begins here
sequence = input('Enter the sequence (Should be combinations of 1,2,3):\n')
print (sequence)
viterbi(sequence)