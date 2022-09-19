#main.py - The entry point of the program.
import parser

print("Hi there! I'm Heisenbot, your friendly chatbot!")
print("Type below to talk to me!\n")

while True:
  
  #Create a line for the user to type a question into.
  response = input("> ")
  if response == "":
    continue

  #Feed this information into the parser.
  parser.parse(response)
  print("")