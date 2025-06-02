from z3 import *

freeIronOre = 60
freeIronIngot = -65
# Can you produce 65 iron ingots from 60 iron Ore?

freePower = 1000000000000000
#  power not included in the model yet


opt = Optimize()

rec_IronIngot = Real('rec_IronIngot')

rec_RecycleIronIngot = Real('rec_RecycleIronIngot')
rec_RecycleIronOre = Real('rec_RecycleIronOre')


# No negative values, otherwise you could reverse the production procces
opt.add(rec_IronIngot >= 0)
opt.add(rec_RecycleIronOre >= 0)
opt.add(rec_RecycleIronIngot >= 0)


# Iron ingot production must match consumption
opt.add((rec_IronIngot * 30 + freeIronIngot) == (rec_RecycleIronIngot * 1200))

# Iron ore production must match consumption
opt.add((freeIronOre) == (rec_RecycleIronOre * 1200 + rec_IronIngot * 30))

# prints 'sat' if possible and 'unsat' if impossible
print(opt.check())
