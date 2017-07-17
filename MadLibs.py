#! python3

adjective = input('Enter an adjective\n')
noun = input('Enter a noun (location)\n')
verb = input('Enter a verb (past form)\n')
noun2 = input('Entera a noun\n')

sentence = ('The ' + adjective +' panda walked to the '
      + noun + ' and then ' + verb + '. A nearby ' + noun2 +
      ' was unaffected by these events. ')

print(sentence)

file = open('pandatext.txt','w')
file.write(sentence)
file.close()

