import re

from ChemElement import ChemElement

class InvalidEquation(Exception):
	pass

class InvalidCompound(Exception):
	pass

def isInt(str):
	try:
		int(str)
		return True
	except ValueError:
		return False

element_pattern = re.compile(r'([A-Z][a-z]*\d*)')
quantity_pattern = re.compile(r'(\w+)(\d+)')

Elements = {
'h': ChemElement(
		an=1,
		symbol='H',
		name="Hydrogen",
		ma=1.0079
	),
'he': ChemElement(
		an=2,
		symbol='He',
		name="Helium",
		ma=4.0026
	),
'li': ChemElement(
		an=3,
		symbol='Li',
		name="Lithium",
		ma=6.941
	),
'be': ChemElement(
		an=4,
		symbol='Be',
		name="Beryllium",
		ma=9.0122
	),
'b': ChemElement(
		an=5,
		symbol='B',
		name="Boron",
		ma=10.811
	),
'c': ChemElement(
		an=6,
		symbol='C',
		name="Carbon",
		ma=12.0107
	),
'n': ChemElement(
		an=7,
		symbol='N',
		name="Nitrogen",
		ma=14.0067
	),
'o': ChemElement(
		an=8,
		symbol='O',
		name="Oxygen",
		ma=15.9994
	),
'f': ChemElement(
		an=9,
		symbol='F',
		name="Fluorine",
		ma=18.9984
	),
'ne': ChemElement(
		an=10,
		symbol='Ne',
		name="Neon",
		ma=20.1797
	),
'na': ChemElement(
		an=11,
		symbol='Na',
		name="Sodium",
		ma=22.9897
	),
'mg': ChemElement(
		an=12,
		symbol='Mg',
		name="Magnesium",
		ma=24.305
	),
'al': ChemElement(
		an=13,
		symbol='Al',
		name="Aluminum",
		ma=26.9815
	),
'si': ChemElement(
		an=14,
		symbol='Si',
		name="Silicon",
		ma=28.0855
	),
'p': ChemElement(
		an=15,
		symbol='P',
		name="Phosphorus",
		ma=30.9738
	),
's': ChemElement(
		an=16,
		symbol='S',
		name="Sulfur",
		ma=32.065
	),
'cl': ChemElement(
		an=17,
		symbol='Cl',
		name="Chlorine",
		ma=35.453
	),
'ar': ChemElement(
		an=18,
		symbol='Ar',
		name="Argon",
		ma=39.948
	),
'k': ChemElement(
		an=19,
		symbol='K',
		name="Potassium",
		ma=39.0983
	),
'ca': ChemElement(
		an=20,
		symbol='Ca',
		name="Calcium",
		ma=40.078
	),
'sc': ChemElement(
		an=21,
		symbol='Sc',
		name="Scandium",
		ma=44.9559
	),
'ti': ChemElement(
		an=22,
		symbol='Ti',
		name="Titanium",
		ma=47.867
	),
'v': ChemElement(
		an=23,
		symbol='V',
		name="Vanadium",
		ma=50.9415
	),
'cr': ChemElement(
		an=24,
		symbol='Cr',
		name="Chromium",
		ma=51.9961
	),
'mn': ChemElement(
		an=25,
		symbol='Mn',
		name="Manganese",
		ma=54.938
	),
'fe': ChemElement(
		an=26,
		symbol='Fe',
		name="Iron",
		ma=55.845
	),
'co': ChemElement(
		an=27,
		symbol='Co',
		name="Cobalt",
		ma=58.9332
	),
'ni': ChemElement(
		an=28,
		symbol='Ni',
		name="Nickel",
		ma=58.6934
	),
'cu': ChemElement(
		an=29,
		symbol='Cu',
		name="Copper",
		ma=63.546
	),
'zn': ChemElement(
		an=30,
		symbol='Zn',
		name="Zinc",
		ma=65.39
	),
'ga': ChemElement(
		an=31,
		symbol='Ga',
		name="Gallium",
		ma=69.723
	),
'ge': ChemElement(
		an=32,
		symbol='Ge',
		name="Germanium",
		ma=72.64
	),
'as': ChemElement(
		an=33,
		symbol='As',
		name="Arsenic",
		ma=74.9216
	),
'se': ChemElement(
		an=34,
		symbol='Se',
		name="Selenium",
		ma=78.96
	),
'br': ChemElement(
		an=35,
		symbol='Br',
		name="Bromine",
		ma=79.904
	),
'kr': ChemElement(
		an=36,
		symbol='Kr',
		name="Krypton",
		ma=83.8
	),
'rb': ChemElement(
		an=37,
		symbol='Rb',
		name="Rubidium",
		ma=85.4678
	),
'sr': ChemElement(
		an=38,
		symbol='Sr',
		name="Strontium",
		ma=87.62
	),
'y': ChemElement(
		an=39,
		symbol='Y',
		name="Yttrium",
		ma=88.9059
	),
'zr': ChemElement(
		an=40,
		symbol='Zr',
		name="Zirconium",
		ma=91.224
	),
'nb': ChemElement(
		an=41,
		symbol='Nb',
		name="Niobium",
		ma=92.9064
	),
'mo': ChemElement(
		an=42,
		symbol='Mo',
		name="Molybdenum",
		ma=95.94
	),
'tc': ChemElement(
		an=43,
		symbol='Tc',
		name="Technetium",
		ma=98
	),
'ru': ChemElement(
		an=44,
		symbol='Ru',
		name="Ruthenium",
		ma=101.07
	),
'rh': ChemElement(
		an=45,
		symbol='Rh',
		name="Rhodium",
		ma=102.9055
	),
'pd': ChemElement(
		an=46,
		symbol='Pd',
		name="Palladium",
		ma=106.42
	),
'ag': ChemElement(
		an=47,
		symbol='Ag',
		name="Silver",
		ma=107.8682
	),
'cd': ChemElement(
		an=48,
		symbol='Cd',
		name="Cadmium",
		ma=112.411
	),
'in': ChemElement(
		an=49,
		symbol='In',
		name="Indium",
		ma=114.818
	),
'sn': ChemElement(
		an=50,
		symbol='Sn',
		name="Tin",
		ma=118.71
	),
'sb': ChemElement(
		an=51,
		symbol='Sb',
		name="Antimony",
		ma=121.76
	),
'te': ChemElement(
		an=52,
		symbol='Te',
		name="Tellurium",
		ma=127.6
	),
'i': ChemElement(
		an=53,
		symbol='I',
		name="Iodine",
		ma=126.9045
	),
'xe': ChemElement(
		an=54,
		symbol='Xe',
		name="Xenon",
		ma=131.293
	),
'cs': ChemElement(
		an=55,
		symbol='Cs',
		name="Cesium",
		ma=132.9055
	),
'ba': ChemElement(
		an=56,
		symbol='Ba',
		name="Barium",
		ma=137.327
	),
'la': ChemElement(
		an=57,
		symbol='La',
		name="Lanthanum",
		ma=138.9055
	),
'ce': ChemElement(
		an=58,
		symbol='Ce',
		name="Cerium",
		ma=140.116
	),
'pr': ChemElement(
		an=59,
		symbol='Pr',
		name="Praseodymium",
		ma=140.9077
	),
'nd': ChemElement(
		an=60,
		symbol='Nd',
		name="Neodymium",
		ma=144.24
	),
'pm': ChemElement(
		an=61,
		symbol='Pm',
		name="Promethium",
		ma=145
	),
'sm': ChemElement(
		an=62,
		symbol='Sm',
		name="Samarium",
		ma=150.36
	),
'eu': ChemElement(
		an=63,
		symbol='Eu',
		name="Europium",
		ma=151.964
	),
'gd': ChemElement(
		an=64,
		symbol='Gd',
		name="Gadolinium",
		ma=157.25
	),
'tb': ChemElement(
		an=65,
		symbol='Tb',
		name="Terbium",
		ma=158.9253
	),
'dy': ChemElement(
		an=66,
		symbol='Dy',
		name="Dysprosium",
		ma=162.5
	),
'ho': ChemElement(
		an=67,
		symbol='Ho',
		name="Holmium",
		ma=164.9303
	),
'er': ChemElement(
		an=68,
		symbol='Er',
		name="Erbium",
		ma=167.259
	),
'tm': ChemElement(
		an=69,
		symbol='Tm',
		name="Thulium",
		ma=168.9342
	),
'yb': ChemElement(
		an=70,
		symbol='Yb',
		name="Ytterbium",
		ma=173.04
	),
'lu': ChemElement(
		an=71,
		symbol='Lu',
		name="Lutetium",
		ma=174.967
	),
'hf': ChemElement(
		an=72,
		symbol='Hf',
		name="Hafnium",
		ma=178.49
	),
'ta': ChemElement(
		an=73,
		symbol='Ta',
		name="Tantalum",
		ma=180.9479
	),
'w': ChemElement(
		an=74,
		symbol='W',
		name="Tungsten",
		ma=183.84
	),
're': ChemElement(
		an=75,
		symbol='Re',
		name="Rhenium",
		ma=186.207
	),
'os': ChemElement(
		an=76,
		symbol='Os',
		name="Osmium",
		ma=190.23
	),
'ir': ChemElement(
		an=77,
		symbol='Ir',
		name="Iridium",
		ma=192.217
	),
'pt': ChemElement(
		an=78,
		symbol='Pt',
		name="Platinum",
		ma=195.078
	),
'au': ChemElement(
		an=79,
		symbol='Au',
		name="Gold",
		ma=196.9665
	),
'hg': ChemElement(
		an=80,
		symbol='Hg',
		name="Mercury",
		ma=200.59
	),
'tl': ChemElement(
		an=81,
		symbol='Tl',
		name="Thallium",
		ma=204.3833
	),
'pb': ChemElement(
		an=82,
		symbol='Pb',
		name="Lead",
		ma=207.2
	),
'bi': ChemElement(
		an=83,
		symbol='Bi',
		name="Bismuth",
		ma=208.9804
	),
'po': ChemElement(
		an=84,
		symbol='Po',
		name="Polonium",
		ma=209
	),
'at': ChemElement(
		an=85,
		symbol='At',
		name="Astatine",
		ma=210
	),
'rn': ChemElement(
		an=86,
		symbol='Rn',
		name="Radon",
		ma=222
	),
'fr': ChemElement(
		an=87,
		symbol='Fr',
		name="Francium",
		ma=223
	),
'ra': ChemElement(
		an=88,
		symbol='Ra',
		name="Radium",
		ma=226
	),
'ac': ChemElement(
		an=89,
		symbol='Ac',
		name="Actinium",
		ma=227
	),
'th': ChemElement(
		an=90,
		symbol='Th',
		name="Thorium",
		ma=232.0381
	),
'pa': ChemElement(
		an=91,
		symbol='Pa',
		name="Protactinium",
		ma=231.0359
	),
'u': ChemElement(
		an=92,
		symbol='U',
		name="Uranium",
		ma=238.0289
	),
'np': ChemElement(
		an=93,
		symbol='Np',
		name="Neptunium",
		ma=237
	),
'pu': ChemElement(
		an=94,
		symbol='Pu',
		name="Plutonium",
		ma=244
	),
'am': ChemElement(
		an=95,
		symbol='Am',
		name="Americium",
		ma=243
	),
'cm': ChemElement(
		an=96,
		symbol='Cm',
		name="Curium",
		ma=247
	),
'bk': ChemElement(
		an=97,
		symbol='Bk',
		name="Berkelium",
		ma=247
	),
'cf': ChemElement(
		an=98,
		symbol='Cf',
		name="Californium",
		ma=251
	),
'es': ChemElement(
		an=99,
		symbol='Es',
		name="Einsteinium",
		ma=252
	),
'fm': ChemElement(
		an=100,
		symbol='Fm',
		name="Fermium",
		ma=257
	),
'md': ChemElement(
		an=101,
		symbol='Md',
		name="Mendelevium",
		ma=258
	),
'no': ChemElement(
		an=102,
		symbol='No',
		name="Nobelium",
		ma=259
	),
'lr': ChemElement(
		an=103,
		symbol='Lr',
		name="Lawrencium",
		ma=262
	),
'rf': ChemElement(
		an=104,
		symbol='Rf',
		name="Rutherfordium",
		ma=261
	),
'db': ChemElement(
		an=105,
		symbol='Db',
		name="Dubnium",
		ma=262
	),
'sg': ChemElement(
		an=106,
		symbol='Sg',
		name="Seaborgium",
		ma=266
	),
'bh': ChemElement(
		an=107,
		symbol='Bh',
		name="Bohrium",
		ma=264
	),
'hs': ChemElement(
		an=108,
		symbol='Hs',
		name="Hassium",
		ma=277
	),
'mt': ChemElement(
		an=109,
		symbol='Mt',
		name="Meitnerium",
		ma=268
	)
}