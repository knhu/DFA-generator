# Name: pa1.py
# Author(s): Kevin Nhu, Mickie Enad
# Date: 09/23
# Description: This project revolves around creating a simple DFA simulator that takes in a string 
# from an input file and determines if it exists within the specified language in the DFA txt file or not.
from os import read
import sys

class DFA:
	""" Simulates a DFA """

	# Initializing the five components of DFA (number of states, alphabet, transition functions, start state, and set of accept states)
	def __init__(self, filename):
		"""
		Initializes DFA from the file whose name is
		filename
		"""
		# Add your code
		
		# Opening the dfa input files
		self.f = open(filename,'r')

		# Reading in and saving the first line as number of states 
		self.numberOfStates = self.f.readline()

		# Reading in and saving the second line as alphabet
		self.alphabet_string = self.f.readline()
		
		# Splitting line into tokens in order to make a list of elements in alphabet
		self.alphabet_elements = []
		for x in self.alphabet_string.strip():
			self.alphabet_elements.append(x)

		# Initializing transition functions, set of accept states, and start state
		self.read_transition=[]
		self.q_accept=[]
		self.q_start=''

		# Created for loop to continuously read in transition function lines and add them to read_transition list
		for line in self.f:
			if "'" in line:
				self.read_transition.append(line.strip())
			else: # Once the transition functions have all been read, we then read in and save start state into q_start
				self.q_start=line
				break
		
		# Initializing current state
		self.q_cur=''
		# Reading in accept state and saving it into q_accept
		self.q_accept = self.f.readline()
		# Initializing transition functions as dictionary 
		self.transition_functions = {}
		
		# For loop to map (current state, symbol being read) to appropriate state according to DFA input file
		for y in self.read_transition:
			z = y.split()
			self.transition_key = tuple(z[:2])
			self.transition_value = z[2]
			self.transition_functions[self.transition_key] = self.transition_value

	# Helper function to handle the individual transitions
	# Takes in character i from input string as an argument
	def transition(self, i):
		z = "'{}'".format(i)
		
		# If DFA encounters a combination of state and character being read that is not in transition functions, set q_cur to empty string
		if ((self.q_cur, z) not in self.transition_functions.keys()):
			self.q_cur = ''
		# Otherwise, let q_cur be the next appropriate state depending on the transition functions
		self.q_cur = self.transition_functions[(self.q_cur, z)]

		
	# Function that handles the simulation of DFA
	def simulate(self, str):
		""" 
		Simulates the DFA on input str.  Returns
		True if str is in the language of the DFA,
		and False if not.
		"""
		# Sets q_cur as the start state q_start upon every new computation of DFA
		self.q_cur=self.q_start.strip()
		# For loop to perform computations for every character in the string
		for ch in str:
			self.transition(ch)

		if self.q_cur in self.q_accept:
			# Returns True if computation completes on an accept state (input string is in the language)
			return True # "Accept"
		else: # Otherwise, returns False if computation completes on a reject state (input string is not in the language)
			return False # "Reject"
		
		
