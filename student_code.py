import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB
		
        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        #Checks to see if the fact is actually a fact
        if(isinstance(fact, Fact)):
        	#Checks if the fact is in the facts list
        	if(fact not in self.facts):
        		#Assuming the fact is not already in the fact list,
        		#add the fact to the end of the fact list.
        		self.facts.append(fact)


        

        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        bindingsArr=[]
        answer=ListOfBindings()

        #Checks to see if the fact is actually a fact
        if(isinstance(fact, Fact)):
        	#Check every fact in the KB's fact list
        	for f in self.facts:
        		#Check if the passed in fact matches the facts in the KB's fact list
        		matched = match(fact.statement, f.statement)
        		#Checks to see if the passed in fact did match the facts in the KB's fact list
        		if (matched != False):
        			#If it did match, pass the match to the answer array for list of bindings
        			answer.add_bindings(matched)
        		else:
        			continue

        

        if (answer.list_of_bindings):
        	return answer

        return False

        print("Asking {!r}".format(fact))
