class ChemElement:
	# Atomic Number, Symbol, Name, Mass
	def __init__(self, an, symbol, name, ma):
		self.an = an
		self.symbol = symbol
		self.name = name
		self.ma = ma

	def __repr__(self):
		return "<MulchPy.ChemElement #{0} [{1}] {2} ~{3}u>".format(self.an, self.symbol, self.name, self.ma)