from utils import Elements, InvalidCompound, isInt, element_pattern, quantity_pattern

class ChemCompound:
	def __init__(self, compoundstr):
		self.__str = compoundstr
		self.__elements = []
		self.parseElements(compoundstr)

	def __repr__(self):
		return "<MulchPy.ChemCompound {0}>".format(self.__str)

	def old_parseElements(self, compoundstr):
		tokens = [str.lower() for str in compound_pattern.findall(compoundstr)]

		lastElement = None

		for token in tokens:
			if not isInt(token): # Compound
				if token in Elements: # One Element
					lastElement = token
					self.__elements.append({'element': Elements[token], 'quantity': 1})
				else: # Multiple Elements
					elementStr = ""
					for letter in token:
						if letter in Elements: # Single letter is an element
							lastElement = letter
							self.__elements.append({'element': Elements[letter], 'quantity': 1})
						else: # Multiple letters make up an element
							elementStr += letter
							if elementStr in Elements: # If the collected letters make up an element
								lastElement = elementStr
								self.__elements.append({'element': Elements[elementStr], 'quantity': 1})
								elementStr = ""
			else: # Quantity
				if lastElement:
					# Set the quantity of the compound
					self.__elements.append({'element': Elements[lastElement], 'quantity': int(token)})
					lastElement = None
				else:
					raise InvalidEquation("Compound quantity found without associated compound")

	def parseElements(self, compoundstr):
		tokens = element_pattern.findall(compoundstr)

		lastElement = None

		for token in tokens:
			if not isInt(token):
				if token.lower() in Elements: # Single Element, I.E. H
					lastElement = token.lower()
					self.__elements.append({'element': Elements[token.lower()], 'quantity': 1})
				else: # Element with Quantity, I.E. H2
					pieces = quantity_pattern.findall(token)[0]
					if len(pieces) < 2:
						raise InvalidCompound("Unknown element '{0}' in compound".format(pieces[0]))
					if pieces[0].lower() not in Elements:
						raise InvalidCompound("Unknown element '{0}' in compound".format(pieces[0]))
					
					lastElement = pieces[0].lower()
					self.__elements.append({'element': Elements[pieces[0].lower()], 'quantity': int(pieces[1])})

	def getCompoundString(self):
		return self.__str

	def getElementSymbols(self):
		return [element.symbol for element in self.__elements]

	def getElementNames(self):
		return [element.name for element in self.__elements]

	def getElementData(self):
		return self.__elements