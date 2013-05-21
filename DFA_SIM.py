#########################################################
#	@name:		DFA_SIM.py                              #
#	@author:	Rohan Jyoti                             #
#	@type:		Python Script File                      #
#	@purpose:	CS373 Extra Credit                      #
#########################################################

from pprint import pprint
from sets import Set
import os
import re
from tokenize import generate_tokens
from cStringIO import StringIO

#This portion here is essentially the main function

#createQ
print("========================= Q: The Set of States =========================")
print ("Please enter Q, the set of states as follows: q0,q1,q2,q3...; i.e. use commas to separate and no spaces, no brackets")
inputQ = raw_input("Q={} -> ")
setQ = Set([])
setQ = inputQ.split(',')

print("\n\n")

#createSigma
print("========================= Sigma: The Input Alphabet =========================")
print ("Please enter Sigma, the alphabet as follows: 0,1...; i.e. use commas to separate and no spaces, no brackets")
inputSigma = raw_input("Sigma={} -> ")
setSigma = Set([])
setSigma = inputSigma.split(',')

print("\n\n")

#createDelta
print("========================= Delta: The Transition Function =========================")
transition_dict = {}
for x in setQ:
	transition_dict[x] = {} 

print("Please enter the transition terminal when prompted: ex: q0(0) -> q1")
for state in setQ:
	for symbol in setSigma:
		while(1):
			next_state = raw_input(state+"("+symbol+") -> ")
			if next_state not in setQ:
				print("Not valid state, please try again")
			else:
				(transition_dict[state])[symbol] = next_state
				break

print("\n\n")

#createStart
print("========================= Start: The Start State =========================")
print("Please enter the q0 the start state as follows: q0; i.e. only one state, no space, comma, or any other character")
while(1):
	start = raw_input("start state: ")
	if start not in setQ:
		print("Not valid state, please try again")
	else:
		break
	
print("\n\n")

#createFinal
print("========================= F: The Set of Accept States =========================")
print("Please enter the set containing the accept/final states as follows: q0,q1,...; i.e. use commas to separate and no space")

while(1):
	inputF = raw_input("F={} -> ")
	setFinal = Set([])
	setFinal = inputF.split(',')
	errCount=0
	for x in setFinal:
		if x not in setQ:
			print(x + " is not a valid state, please try again")
			errCount+=1
		
	if errCount==0:
		break

print("\n\n")

#getInputString
print("========================= Input String: The Sring to Simulate on the DFA =========================")
print("Please enter the string you want to simulate on the DFA as folllow: 011010...")

exitClause = "no"
while(exitClause == "no"):
	inputString = raw_input("Input String: ")
	if inputString == "exit":
		exitClause = inputString
		break
	errCount=0
	for x in inputString:
		if x not in setSigma:
			print(x + " is not a valid symbol, please try again")
			errCount+=1
	if errCount==0: #go on to simulate input string on DFA
		print("\nSimulating input on DFA")
		print(".")
		print(".")
		print(".")

		#simulateDFA
		currentState = start
		for currentSymbol in inputString:
			currentState = (transition_dict[currentState])[currentSymbol]
		if currentState in setFinal:
			print("DFA accepts "+ inputString)
		else:
			print("DFA rejects "+ inputString)
	







