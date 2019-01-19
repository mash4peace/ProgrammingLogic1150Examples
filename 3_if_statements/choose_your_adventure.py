import sys

print('Welcome, adventurer!')

print('You are standing at the edge of a dark scary-looking forest.')
choice = input('Enter R to run away, or W to walk into the forest.: ')

if choice.upper() == 'R':
    print('The forest is too scary for many scary beasts, so they live just outside it. One of these ate you. THE END')
    sys.exit()
else:
    print('You start walking into the forest. It doesn\'t take long for you to loose sight of the sun')

print('As you push through the undergrowth, you hear the sound of something behind you. Whatever it is, is very large.')

choice = input('Enter T to turn around, or B to curl up into a ball: ')

if choice.upper() == 'B':
    print('Well, now what are you going to do? The creature is still there, and now you are not moving. It eats you. THE END')
    sys.exit()

else:
    print('You turn around, and find yourself face to face with an enormous, hairy beast.')

print('The beast is at least twice your height, and looks angry.')

choice = input('Press Y to yell at the top of your lungs, or S to draw your sword: ')

#  To be continued!! Extra credit for adding your own story
