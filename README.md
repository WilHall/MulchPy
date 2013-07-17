#MulchPy

The Mulch Chemistry Stoichiometry C++ Library, ported to Python. Mulch can be found [on Github](https://github.com/DeweyDev/mulch).

![Orange](http://www.arktimes.com/binary/fedc/1305756869-orange.png)

###How To Use

MulchPy works almost identically to Mulch. Simply create a new ```ChemEquation``` object and supply the chemical equation as a string:

```
from mulchpy import ChemEquation
combustion = ChemEquation("CH4 + O2 = H2O + CO2")
```

You can also create a blank ```ChemEquation``` object, and then set its equation later:

```
combustion = ChemEquation()
combustion.setEquation("CH4 + O2 = H2O + CO2")
```

After creating your ```ChemEquation``` object, you can get the equation back in string form:

```
equation_str = combustion.getEquation()
```

You can also get a list of compound strings that were parsed from the given equation string:

```
compounds = combustion.getCompoundStrings()
```

For more information about the compounds in an equation, you can obtain a list of ```ChemCompound``` objects for the equation:

```
compounds = combustion.getCompoundData()
```

The ```getCompoundData()``` method returns a list of ```ChemCompound``` objects, which have the following methods available:

 * ```getCompoundString()``` - Returns the compound string for this ```ChemCompound``` instance
 * ```getElementSymbols()``` - Returns a list of element symbols contained in the compound
 * ```getElementNames()``` - Returns a list of element names contained in the compound
 * ```getElementData()``` - Returns a list of ChemElement objects describing the compound. Each ```ChemElement``` object has attributes for Element Name (```name```), Element Symbol (```symbol```), Atomic Number(```an```), Atomic Mass (```ma```), and the Quantity of the element in the compound (```quantity```).