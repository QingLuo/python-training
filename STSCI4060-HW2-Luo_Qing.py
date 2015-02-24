print '''\nSTSCI 4060 HW2
Student Name: Qing Luo
***** Question 1 *****\n'''

print '''\nA. Define a variable called "story"\n'''
story='''Once upon a time, deep in an ancient
jungle,there lived a tiger. This tiger
liked to eat fish, but the jungle had
very little fish to offer. One day, an
explorer found the tiger and discovered
it liked fish. The explorer took the
tiger back to NYC, where it could
eat as much fish as it wanted. However,
the tiger became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of fish.

-- The End of the Story --
'''

print '''\nB. Change the content of the story into a format string\n'''
story=story.replace('tiger','%s').replace('fish','%s')
print story

print '''\nC. Create a tuple called “t1” to hold the words of “tiger” and “fish”\n'''
t1=('tiger','tiger', 'fish', 'fish', 'tiger', 'fish', 'tiger', 'fish', 'tiger', 'fish')
story=story % t1
print story

print '''\nD.  changing the animal and its food from “tiger’ and “fish” to “monkey” and “bananas"\n'''
story=story.replace('tiger','mockey').replace('fish','bananas')
print story
story=story.replace('mockey','%s').replace('bananas','%s')
print story
t2=('mockey','mockey', 'bananas', 'bananas', 'mockey', 'bananas', 'mockey', 'bananas', 'mockey', 'bananas')
story=story % t2
print story

print '''\n***** Question 2 *****\n'''

print '''\nA. replace mockey to animal, bananas to food, NYC to city\n'''
story=story.replace('mockey','%(animal)s').replace('bananas','%(food)s').replace('NYC','%(city)s')

print '''\nB. replace into cat mice and Beijing\n'''
myDict={'animal':'cat', 'food':'mice', 'city':'Beijing'}
print "\nThe dictionary is\n", myDict
story=story % myDict
print story

print '''\nC. replace into fox, rabbits and London\n'''
story=story.replace('cat','%(animal)s').replace('mice','%(food)s').replace('Beijing','%(city)s')
myDict={'animal':'fox', 'food':'rabbits', 'city':'London'}
story=story % myDict
print story

print '''\n***** Question 3 *****\n'''
u=[1,-2,3,4]
v=[2,3,-2,1]
uv=u[0]*v[0]+u[1]*v[1]+u[2]*v[2]+u[3]*v[3]
print "\nThe list representation of vector u is\n", u
print "\nThe list representation of vector v is\n", v
print "\nThe dot product u•v is\n", uv



