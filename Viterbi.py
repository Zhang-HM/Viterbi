"""

Desc: Viterbi's algorithm to predict weather
Submitted By : Vidya Sri Mani

In Detail:
Programmatically implement the Viterbi algorithm and run it with the HMM in
Figure 1 to compute the most likely weather sequence and probability for a given
observation sequence. Example observation sequences: 331, 122313, 331123312,. etc

"""

#Implementing Viterbi's algorithm to compute the most likely weather
def viterbi(sequence):
    print('In viterbi')

#Program Execution begins here
sequence = input('Enter the sequence (Should be combinations of 1,2,3):\n')
print (sequence)
viterbi(sequence)