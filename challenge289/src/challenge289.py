"""
challenge 289

In the popular Pokémon games all moves and Pokémons have types that determine how effective certain moves are against certain Pokémons.
These work by some very simple rules, a certain type can be super effective, normal, not very effective or have no effect at all against another type.
These translate respectively to 2x, 1x, 0.5x and 0x damage multiplication.
If a Pokémon has multiple types the effectiveness of a move against this Pokémon will be the product of the effectiveness of the move to it's types.

The program should take the type of a move being used and the types of the Pokémon it is being used on.
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

Since probably not every dailyprogrammer user is an avid Pokémon player that knows the type effectiveness multipliers by heart here is a Pokémon type chart.
http://pokemondb.net/type

"""


# Ask how many inputs there are on both sides
# Enter those inputs eg a1, a2, a3 . b1, b2, b3
# Look up inputs in table a1 > b1, a1 > b2, a1 > b3, a2> b1, a2>b2 etc.
# Multiply those lookups and output

#Considerations
#Need the lookups to function dynamically, ie want it to know how many lookups it needs to do (factorial maths)
#Can stop if any are zero

