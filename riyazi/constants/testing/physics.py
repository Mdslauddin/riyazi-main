
__all__ = [
    'Avogadro', 'Boltzmann', 'Btu', 'Btu_IT', 'Btu_th', 'G',
    'Julian_year', 'N_A', 'Planck', 'R', 'Rydberg',
    'Stefan_Boltzmann', 'Wien', 'acre', 'alpha',
    'angstrom', 'arcmin', 'arcminute', 'arcsec',
    'arcsecond', 'astronomical_unit', 'atm',
    'atmosphere', 'atomic_mass', 'atto', 'au', 'bar',
    'barrel', 'bbl', 'blob', 'c', 'calorie',
    'calorie_IT', 'calorie_th', 'carat', 'centi',
    'convert_temperature', 'day', 'deci', 'degree',
    'degree_Fahrenheit', 'deka', 'dyn', 'dyne', 'e',
    'eV', 'electron_mass', 'electron_volt',
    'elementary_charge', 'epsilon_0', 'erg',
    'exa', 'exbi', 'femto', 'fermi', 'fine_structure',
    'fluid_ounce', 'fluid_ounce_US', 'fluid_ounce_imp',
    'foot', 'g', 'gallon', 'gallon_US', 'gallon_imp',
    'gas_constant', 'gibi', 'giga', 'golden', 'golden_ratio',
    'grain', 'gram', 'gravitational_constant', 'h', 'hbar',
    'hectare', 'hecto', 'horsepower', 'hour', 'hp',
    'inch', 'k', 'kgf', 'kibi', 'kilo', 'kilogram_force',
    'kmh', 'knot', 'lambda2nu', 'lb', 'lbf',
    'light_year', 'liter', 'litre', 'long_ton', 'm_e',
    'm_n', 'm_p', 'm_u', 'mach', 'mebi', 'mega',
    'metric_ton', 'micro', 'micron', 'mil', 'mile',
    'milli', 'minute', 'mmHg', 'mph', 'mu_0', 'nano',
    'nautical_mile', 'neutron_mass', 'nu2lambda',
    'ounce', 'oz', 'parsec', 'pebi', 'peta',
    'pi', 'pico', 'point', 'pound', 'pound_force',
    'proton_mass', 'psi', 'pt', 'short_ton',
    'sigma', 'slinch', 'slug', 'speed_of_light',
    'speed_of_sound', 'stone', 'survey_foot',
    'survey_mile', 'tebi', 'tera', 'ton_TNT',
    'torr', 'troy_ounce', 'troy_pound', 'u',
    'week', 'yard', 'year', 'yobi', 'yocto',
    'yotta', 'zebi', 'zepto', 'zero_Celsius', 'zetta'
]
# SI prefixes
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deka = 1e1
deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21
yocto = 1e-24


# binary prefixes
kibi = 2**10
mebi = 2**20
gibi = 2**30
tebi = 2**40
pebi = 2**50
exbi = 2**60
zebi = 2**70
yobi = 2**80

"""
# physical constants
c = speed_of_light = _cd('speed of light in vacuum')
mu_0 = _cd('vacuum mag. permeability')
epsilon_0 = _cd('vacuum electric permittivity')
h = Planck = _cd('Planck constant')
hbar = h / (2 * pi)
G = gravitational_constant = _cd('Newtonian constant of gravitation')
g = _cd('standard acceleration of gravity')
e = elementary_charge = _cd('elementary charge')
R = gas_constant = _cd('molar gas constant')
alpha = fine_structure = _cd('fine-structure constant')
N_A = Avogadro = _cd('Avogadro constant')
k = Boltzmann = _cd('Boltzmann constant')
sigma = Stefan_Boltzmann = _cd('Stefan-Boltzmann constant')
Wien = _cd('Wien wavelength displacement law constant')
Rydberg = _cd('Rydberg constant')

"""

# mass in kg
gram = 1e-3
metric_ton = 1e3
grain = 64.79891e-6
lb = pound = 7000 * grain  # avoirdupois
blob = slinch = pound * g / 0.0254  # lbf*s**2/in (added in 1.0.0)
slug = blob / 12  # lbf*s**2/foot (added in 1.0.0)
oz = ounce = pound / 16
stone = 14 * pound
long_ton = 2240 * pound
short_ton = 2000 * pound

troy_ounce = 480 * grain  # only for metals / gems
troy_pound = 12 * troy_ounce
carat = 200e-6

"""
m_e = electron_mass = _cd('electron mass')
m_p = proton_mass = _cd('proton mass')
m_n = neutron_mass = _cd('neutron mass')
m_u = u = atomic_mass = _cd('atomic mass constant')
"""

# angle in rad
degree = pi / 180
arcmin = arcminute = degree / 60
arcsec = arcsecond = arcmin / 60

# time in second
minute = 60.0
hour = 60 * minute
day = 24 * hour
week = 7 * day
year = 365 * day
Julian_year = 365.25 * day


# length in meter
inch = 0.0254
foot = 12 * inch
yard = 3 * foot
mile = 1760 * yard
mil = inch / 1000
pt = point = inch / 72  # typography
survey_foot = 1200.0 / 3937
survey_mile = 5280 * survey_foot
nautical_mile = 1852.0
fermi = 1e-15
angstrom = 1e-10
micron = 1e-6
au = astronomical_unit = 149597870700.0
light_year = Julian_year * c
parsec = au / arcsec


# pressure in pascal
atm = atmosphere = _cd('standard atmosphere')
bar = 1e5
torr = mmHg = atm / 760
psi = pound * g / (inch * inch)

# area in meter**2
hectare = 1e4
acre = 43560 * foot**2

# volume in meter**3
litre = liter = 1e-3
gallon = gallon_US = 231 * inch**3  # US
# pint = gallon_US / 8
fluid_ounce = fluid_ounce_US = gallon_US / 128
bbl = barrel = 42 * gallon_US  # for oil

gallon_imp = 4.54609e-3  # UK
fluid_ounce_imp = gallon_imp / 160


# speed in meter per second
kmh = 1e3 / hour
mph = mile / hour
mach = speed_of_sound = 340.5  # approx value at 15 degrees in 1 atm. Is this a common value?
knot = nautical_mile / hour

# temperature in kelvin
zero_Celsius = 273.15
degree_Fahrenheit = 1/1.8  # only for differences

# energy in joule
eV = electron_volt = elementary_charge  # * 1 Volt
calorie = calorie_th = 4.184
calorie_IT = 4.1868
erg = 1e-7
Btu_th = pound * degree_Fahrenheit * calorie_th / gram
Btu = Btu_IT = pound * degree_Fahrenheit * calorie_IT / gram
ton_TNT = 1e9 * calorie_th
# Wh = watt_hour

# power in watt
hp = horsepower = 550 * foot * pound * g

# force in newton
dyn = dyne = 1e-5
lbf = pound_force = pound * g
kgf = kilogram_force = g  # * 1 kg
