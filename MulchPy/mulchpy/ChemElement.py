class ChemElement:
	# Atomic Number, Symbol, Name, Mass
	def __init__(self, instance=None, an=None, symbol=None, name=None, ma=None, quantity=1):
		if instance == None:
			self.an = an
			self.symbol = symbol
			self.name = name
			self.ma = ma
		else:
			self.an = instance.an
			self.symbol = instance.symbol
			self.name = instance.name
			self.ma = instance.ma
		self.quantity = quantity

	def __repr__(self):
		return "<MulchPy.ChemElement #{0} [{1}] {2} ~{3}u>".format(self.an, self.symbol, self.name, self.ma)