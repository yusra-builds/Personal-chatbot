print("\nWelcome to chatbot!")
name = input("\nWhat is your name?")
print("\nWelcome! ", name)
print("\nYou can ask me basic question.")
print("\nType bye to exit from the chatbot")


responses = { "hi" : "Hi welocome. How can i help you?",
"who are you?":"I am smart AI chatbot",
"motivate me":"Consistency is the key to success.",
"how are you?":"I am doing great!",
}


def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return  responses[eachKey]
        
    return "I am unable to tell this yet."
    
    
    
while True:
    userInput = input("\nPlease ask your question..")
    if "bye" in userInput.lower():
        print("\nBot response:Goodbye!")
        break
    reply = getResponseOfBot(userInput)
    print("Bot response:", reply)
    
    

       
 
   
   