from utils import Elements, InvalidCompound, isInt, isElement, getElement, ungrouped_pattern, grouped_pattern
from ChemElement import ChemElement

class ChemCompound:
	def __init__(self, compoundstr, quantity=1):
		self.__str = compoundstr
		self.__quantity = quantity
		self.__elements = []
		self.parseElements(compoundstr)

	def __repr__(self):
		return "<MulchPy.ChemCompound {0}>".format(self.__str)

	def parseElements(self, compoundstr):
		if '(' in compoundstr:
			self.__elements = elems = self.parseGrouped(compoundstr)
		else:
			self.__elements = self.parseUngrouped(compoundstr)

	def parseGrouped(self, compoundstr):
		tokens = [x if x != '' else '1' for x in grouped_pattern.findall(compoundstr)[0]]
		elems = []
		coeff = 1
		sub = 1

		if isInt(tokens[0]):
			coeff = int(tokens[0])
		else:
			elems.extend(self.parseUngrouped(tokens[0]))

		if isInt(tokens[2]):
			sub = int(tokens[2])
		else:
			raise InvalidCompound("Unexpected '{0}' after group '({1})'".format(tokens[2], tokens[1]))

		innerElems = self.parseUngrouped(tokens[1])

		for elem in innerElems:
			elem.quantity = elem.quantity * coeff * sub

		elems.extend(innerElems)

		return elems

	def parseUngrouped(self, compoundstr):
		groups = ungrouped_pattern.findall(compoundstr)
		elems = []
		lastCoeff = None
		
		for group in groups:
			group = [x if x != '' else '1' for x in group]
			subelems = []

			for token in group:
				if isInt(token):
					token = int(token)
					if len(subelems) > 0:
						subelems[-1].quantity *= token
					else:
						lastCoeff = token
				elif isElement(token):
					elem = ChemElement(instance=getElement(token))

					if lastCoeff is not None:
						elem.quantity *= lastCoeff
						lastCoeff = None
					subelems.append(elem)
				else:
					raise InvalidCompound("Unknown element {0} found".format(token))
			elems.extend(subelems)
		return elems


	def getCompoundString(self):
		return self.__str

	def getCompoundQuantity(self):
		return self.__quantity

	def getElementSymbols(self):
		return [element.symbol for element in self.__elements]

	def getElementNames(self):
		return [element.name for element in self.__elements]

	def getElementData(self):
		return self.__elements