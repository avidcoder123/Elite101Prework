#question.py - Handle questions. 
import psuedorandom

def handle(response, questionWord):

  survey = False
  #See if the user is asking about the chatbot itself
  if "you" in response:
    #Survey is the variable to determine if the user is asking about Proton.
    survey = True

  #Hardcoded responses
  if survey and (
    "named after" in response or (
      "name" in response 
      and "how" in response)
  ):
    
    #Who are you named after, how were you name, how did you get your name, etc
    print("I'm named after Werner Heisenberg, the creator of the Heisenberg Uncertainty Principle.")
    
  elif questionWord == "who":
    
    if survey:
      #Who are you?
      print("I'm Heisenbot, your friendly chatbot!")
    else:
      #Asking who someone was
      print("They were probably a really great person!")
      
  elif questionWord == "what":
    
    if survey:
      #Asking about a bot's favorite thing?
      if "favorite" in response:
        #Favorite color?
        if "color" in response:
          print("My favorite color is sky blue.")
        else:
          print("I don't really prefer one over the other.")
        print("What's yours?")
      elif "name" in response:
        print("I'm Heisenbot, your friendly chatbot!")
      else:
        print("I'm not a very advanced robot, but I can talk to you!")
    else:
      print("It sounds like something really interesting!")
      
  elif questionWord == "where":
    if survey:
      #Where are you from?
      print("I was created in Austin, Texas.")
    else:
      print("The world's an amazing place and anything could be anywhere!")
      
  elif questionWord == "when":
    
    if survey:
      print("I was programmed in 2022.")
    else:
      #Say a random year between 0 and 2022 CE, based on the question.
      year = psuedorandom.generate(
        response, 
        range(2023)
      )
      
      print(f"I think somewhere around the year {year}.")
      
  elif questionWord == "why":
    if survey:
      #Why were you created/Why are you x?
      print("I was created to demonstrate how a simple robot could have basic conversation with a human. I'm not perfect yet, though!")
    else:
      print("There's probably a really good reason.")
      
  elif questionWord == "how":
    if survey:
      if "created" in response:
        #How were you created?
        print("I'm made in Python!")
      elif "named" in response:
        print("I'm named after Werner Heisenberg, the creator of the Heisenberg Uncertainty Principle.")
      else:
        #How are you?
        print("I'm great! How about you?")
    else:
      #How many
      if "many" in response:
        #Generate a random number between 1-100
        num = psuedorandom.generate(
          response,
          range(1, 101)
        )
        
        print(f"I'd say around {num}.")
      else:
        print("There's lots of ways something can happen.")
      
  elif questionWord == "which":
    if survey:
      if "language" in response:
        print("I was made in Python!")
      else:
        print("I like to say that I embrace all the possibilities.")
    else:
      print("Any one of them works.")
  else:
    #Yes/No Question: Choose a random answer
    choices = [
      "Yes.",
      "No."
    ]
    
    #Choose a random answer based on the question
    answer = choices[
      psuedorandom.generate(
        response,
        range(2)
      )
    ]
    
    print(answer)