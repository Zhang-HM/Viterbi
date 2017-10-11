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
start --> cold = 0.2
start --> hot = 0.8
cold --> cold = 0.6
cold --> hot =0.4
hot --> hot = 0.7
hot --> cold = 0.3
----------------------------------
B1&B2 Probabilites
P(1|Hot) = 0.2      P(1|Cold) = 0.5
P(2|Hot) = 0.4      P(2|Cold) = 0.4
P(3|Hot) = 0.4      P(3|Cold) = 0.1
"""







#Implementing Viterbi's algorithm to compute the most likely weather
def viterbi(sequence):
    sequenceList = list(sequence)#to seprate each state in the input sequence as a list

#Program Execution begins here
sequence = input('Enter the sequence (Should be combinations of 1,2,3):\n')
print (sequence)
viterbi(sequence)