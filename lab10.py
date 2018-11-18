#Lab 10 - Team 10
# M. Mariscal, W. Robleh, C. Piwarski


#Warm UP
#PART A:
def warmup():
  while True:
    name = requestString("Enter a word")
    if name == ("stop"):
      break


# https://www.poftut.com/python-how-to-print-without-newline-or-space/
# For printing solutions in python2 without making a new line
import sys

#This function operates a game of hangman. Users guess characters to unveil the word before
#they run out of turns.
def hangman():
  
  #initialize variables
  word = 'sausage'
  wordLength = len(word)
  guessCount = 6
  guessedLetters = ''
  incorrectGuesses = 0
  description = 'Explain the game'
  print description
  print ('Total Amount of Guesses: %d' % guessCount) #String Formatting. First String Op
  
  #begin game
  while incorrectGuesses < guessCount:
    
    characterCount = 0
    #output correct characters and dashes
    for character in word:
      if character in guessedLetters:
        sys.stdout.write(character)#This allows for the to print Without Newline or Space 
        sys.stdout.flush()
        characterCount += 1
      else:
        sys.stdout.write('_ ')
        sys.stdout.flush()
    print '\n'
    if characterCount == wordLength:
      break
    print ('Incorrect Guesses: %d' % incorrectGuesses) 
  
    badCharacter = True
    while badCharacter: #determining if they guessed the right character or not 
      guess = requestString('Enter in a letter: ')
      print 'Your guess is %s' % guess
      if checkInput(guess): # if this passes it determines if its good
        badCharacter = False
        if guess in word: #string find method. Third String op.
          guessedLetters += guess #string concatenation. Second String Op
          badCharacter = False
        elif guessedLetters.count(guess) > 0: #string count method. Fourth string op.
          badCharacter = True
          print 'Letter already guessed. Try again.'
        else:
          incorrectGuesses += 1
          guessedLetters += guess
          goodCharacter = False
      else:
        badCharacter = True
        print 'Incorrect input. Enter in a single letter'
      print 'You have used %d out of %d guesses' % (incorrectGuesses, guessCount)
  if incorrectGuesses == 6:
  	print 'Sorry please play again'
  else:
  	print 'You win!'
  return
  
#checks the input to see if it is a letter based on the ascii table.
def checkInput(input):
  if len(input) > 1:
    return False
  if input == '':
    return False
  value = ord(input)
  if value > 64 and value < 90:
    return True
  elif value > 96 and value < 122:
    return True 





