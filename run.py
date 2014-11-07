from mdconfig import *

program = MD(dt=10, name="molecular-dynamics-fys3150") # dt in femtoseconds, name is the name of the executable you have

# Create new FCC lattice
program.runNewSystem(numberOfUnitCells = 10, FCCLatticeConstant = 5.26) # lattice constant in angstroms

# Enable the thermostat for a while to reach a desired temperature. You need to figure out how long it needs to run.
program.runThermostat(temperature = 300, timesteps = 100)

# Thermalize for some time (Note: thermalizing means without the thermostat, equilibrate). Here as well you need to figure out how long it needs to thermalize before we start sampling
program.runThermalize(timesteps = 100)

# Now that it is thermalized, we can trust the states enough to do statistical sampling.
program.runThermalize(timesteps = 10000)

program.saveState(path="states/myFavoriteState")

# In your main function in your c++ program you can read in these variables as arguments like this: 
# First, we assume some default values, then if arguments are given, use them instead

# int numTimeSteps = 1000;
# double dt = UnitConverter::timeFromSI(1e-14); 
# int numUnitCells = 10;
# float latticeConstant = 5.26;
# bool loadState = false;
# bool thermostatEnabled = false;
# float temperature = 300;
# if(args>1) {
#     dt = UnitConverter::timeFromSI(atof(argv[1])*1e-15);
#     numTimeSteps = atoi(argv[2]);
#     numberOfUnitCells = atoi(argv[3]);
#     latticeConstant = atof(argv[4]);
#     loadState = atoi(argv[5]);
#     thermostatEnabled = atoi(argv[6]);
#     temperature = atof(argv[7]);
# }