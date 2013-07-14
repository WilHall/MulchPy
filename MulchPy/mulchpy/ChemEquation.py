from utils import Elements, InvalidEquation
from ChemCompound import ChemCompound

class ChemEquation:
	
	def __init__(self, equationstr=None):
		self.__compounds = {
			'left': [],
			'right': []
		}

		if equationstr is not None:
			self.setEquation(equationstr)

	def __repr__(self):
		return "<MulchPy.ChemEquation {0}>".format(self.__str)

	def setEquation(self, equationstr):
		self.__str = equationstr
		equationstr = equationstr.replace(' ', '')

		self.validateEquationStr()

		sides = equationstr.split('=')

		self.__compounds['left'] = self.parseCompounds(sides[0])
		self.__compounds['right'] = self.parseCompounds(sides[1])

	def validateEquationStr(self):
		if '=' not in self.__str:
			raise InvalidEquation("Equation missing an equals sign")
		elif self.__str.count('=') > 1:
			raise InvalidEquation("Equation has multiple equal signs")

	def parseCompounds(self, subequationstr):
		tokens = subequationstr.split('+')
		compounds = []

		for token in tokens:
			compounds.append(ChemCompound(token))

		return compounds

	def getEquation(self):
		return self.__str

	def getCompoundStrings(self):
		data = [compound.getCompoundString() for compound in self.__compounds['left']]
		data.extend([compound.getCompoundString() for compound in self.__compounds['right']])
		return data
	
	def getCompoundData(self):
		data = self.__compounds['left']
		data.extend(self.__compounds['right'])
		return data



	
