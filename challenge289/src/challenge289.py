"""
challenge 289

In the popular Pokemon games all moves and Pokemon have types that determine how effective certain moves are against certain Pokemon.
These work by some very simple rules, a certain type can be super effective, normal, not very effective or have no effect at all against another type.
These translate respectively to 2x, 1x, 0.5x and 0x damage multiplication.
If a Pokemon has multiple types the effectiveness of a move against this Pokemon will be the product of the effectiveness of the move to it's types.

The program should take the type of a move being used and the types of the Pokemon it is being used on.
Example inputs
 fire -> grass
 fighting -> ice rock
 psychic -> poison dark
 water -> normal
 fire -> rock

 Example outputs
2x
4x
0x
1x
0.5x

Since probably not every dailyprogrammer user is an avid Pokemon player that knows the type effectiveness multipliers by heart here is a Pokemon type chart.
http://pokemondb.net/type

"""
# Considerations
# Need the lookups to function dynamically, ie want it to know how many lookups it needs to do (factorial maths)
# could just have the user choose a number that represents an attack value
# Can stop if any are zero

# Ask how many inputs there are on both sides
a_powers = int(raw_input("How many powers does your attack have?"))
b_powers = int(raw_input("How many powers does your opponent's attack have?"))

# Enter those inputs eg a1, a2, a3 . b1, b2, b3
a_powerlist = []
b_powerlist = []

for x in xrange(a_powers):
    a_powerlist.append(raw_input("Enter your power (%d)?" % (x + 1)).upper())  # should check its a string in the list

for x in xrange(b_powers):
    b_powerlist.append(raw_input("Enter your opponent's power (%d)?" % (x + 1)).upper())

# Return position number in the power list table, then lookup those pair in the multiplier table

powerlist = ["NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING", "POISON", "GROUND", "FLYING", "PSYCHIC",
             "BUG", "ROCK", "GHOST", "DRAGON", "DARK", "STEEL", "FAIRY"]

for x in xrange(a_powers):
    print powerlist.index(a_powerlist[x])

for x in xrange(b_powers):
    print powerlist.index(b_powerlist[x])


multiplier_table = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],
                    [1,	0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],
                    [1,	2, 0.5,	1,	0.5, 1,	1,	1,	2,	1,	1,	1,	2, 1, 0.5, 1,	1,	1],
                    [1,	1,	2,	0.5,	0.5,	1,	1,	1,	0,	2,	1,	1,	1,	1, 0.5, 1,	1,	1],
                    [1,	0.5,	2,	1,	0.5, 1, 1, 0.5, 2, 0.5, 1,	0.5, 2, 1, 0.5, 1, 0.5,	1],
                    [1,	0.5,	0.5,	1,	2,	0.5, 1,	1,	2,	2,	1,	1,	1,	1,	2,	1,	0.5, 1],
                    [2,	1,	1,	1,	1,	2,	1,	0.5,	1,	0.5,	0.5,	0.5,	2,	0,	1,	2,	2,	0.5],
                    [1,	1,	1,	1,	2,	1,	1,	0.5,	0.5,	1,	1,	1,	0.5,	0.5,	1,	1,	0,	2],
                    [1,	2,	1,	2,	0.5,	1,	1,	2,	1,	0,	1,	0.5,	2,	1,	1,	1,	2,	1],
                    [1,	1,	1,	0.5,	2,	1,	2,	1,	1,	1,	1,	2,	0.5,	1,	1,	1,	0.5,	1],
                    [1,	1,	1,	1,	1,	1,	2,	2,	1,	1,	0.5,	1,	1,	1,	1,	0,	0.5,	1],
                    [1,	0.5,	1,	1,	2,	1,	0.5, 0.5, 1,	0.5,	2,	1,	1,	0.5,	1,	2,	0.5,	0.5],
                    [1,	2,	1,	1,	1,	2,	0.5,	1,	0.5,	2,	1,	2,	1,	1,	1,	1,	0.5,	1],
                    [0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	2,	1,	1,	2,	1,	0.5, 1,	1],
                    [1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	2,	1,	0.5,	0],
                    [1,	1,	1,	1,	1,	1,	0.5,	1,	1,	1,	2,	1,	1,	2,	1,	0.5,	1,	0.5],
                    [1,	0.5,	0.5,	0.5,	1,	2,	1,	1,	1,	1,	1,	1,	2,	1,	1,	1,	0.5, 2],
                    [1,	0.5,	1,	1,	1,	1,	2, 0.5, 1,	1,	1,	1,	1,	1,	2,	2,	0.5, 1]]

output_mult = 1

# Use a_powerlist iteratively for each defense power, and return the multiplier
# Multiply those lookups and output

for x in xrange(b_powers):
    for y in xrange(a_powers):
        output_mult *= multiplier_table[powerlist.index(a_powerlist[y])][powerlist.index(b_powerlist[x])]

print "Your multiplier is %r" %output_mult


