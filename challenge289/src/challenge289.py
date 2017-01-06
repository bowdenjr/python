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
    a_powerlist.append(raw_input("Enter your power %d?" % (x+1)))  # check its a string in the list

for x in xrange(b_powers):
    b_powerlist.append(raw_input("Enter your opponent's power %d?" % (x+1)))

# Look up inputs in table a1>b1, a1>b2, a1>b3, a2>b1, a2>b2 etc.



# Multiply those lookups and output