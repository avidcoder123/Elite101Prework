#statement.py - Handling non-questions
import psuedorandom

def handle(userInput):

  #Handle interjections
  interjections = [
    "hi",
    "hello",
    "hey"
  ]
  
  #Is the first word an interjection?
  if userInput.split(" ")[0] in interjections:
    print("Hello!")
    return
  
  responses = [
    "That's amazing!",
    "Okay.",
    "I get that.",
    "That's understandable.",
    "Thanks for letting me know.",
    "Why is that so?",
    "Could you explain why?"
  ]
  
  #Choose a response vased on the length of the question; this way the answer is always the same for each question
  response = responses[
    psuedorandom.generate(
      userInput,
      range(len(responses))
    )
  ]
  
  print(response)
  