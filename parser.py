#parser.py - The code to parse the user's response.
import question
import statement

#The limited alphabet and characters that the parser will understand
alphabet = list("abcdefghijklmnopqrstuvwxyz1234567890 ")

def parse(response):
  
  #Removes trailing whitespace, makes lowercase, and limits to characters in the alphabet
  response = "".join(
    filter( 
      
      lambda x: 
        x in alphabet
      ,
      response
        .lower()
        .strip()
      
    )
  )

  if response == "i am the one who knocks":
    
    print("That's very relatable.")
    return

  #Check if the input has any question words
  questionWords = [
    "who",
    "what",
    "where",
    "when",
    "why",
    "how",
    "which",
    "do",
    "does",
    "did",
    "are",
    "will",
    "is",
    "was",
    "can",
    "should"
  ]
  
  #Question words with contractions added
  contractedQuestionWords = list(
    map(
      
      lambda x:
        x + "s"
      ,
      questionWords[:6]
      
    )
  )
  
  #List of words in response
  firstWord = response.split(" ")[0]

  #If the first word is a question word or a contracted form
  if firstWord in [
    *questionWords, *contractedQuestionWords
  ]:
    
    #If the question word is contracted, remove the trailing s.
    if firstWord in contractedQuestionWords:
      firstWord = firstWord[:-1]
    
    #Handle question case
    question.handle(response, firstWord)
  else:
    #Handle statement case
    statement.handle(response)