#psuedorandom.py - Creates a semi-random number within a certain range. Used to give consistent answers to inputs.

def generate(userInput, numRange):
  #Generates a psuedo-random number using the user-input.
  magicNumber = abs(
    hash(
      userInput
    )
  )

  #Fits that number into the range.
  return numRange[
    magicNumber % len(numRange)
  ]