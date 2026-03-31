
import random
name = input("What's your name? ")
print("Hello", name)

emotions = {'happy' : " I'm so glad to hear that!",
            'sad': 'That sounds really hard, Would you like some company?',
            'angry': "Your rage is valid, you do not suppress, you transmute. "}

greetings = [f'Hi! {name}', f'Hello, {name}',f"hey, {name} "]


while True:
    responses = []
    user_input = input("You: ").lower()

    print("Bot: ", end = '')
    
    if "bye" in user_input:
        responses.append("Goodbye!")
        print(" ".join(responses))
        break   
    if "hello" in user_input:
        
        greeting = random.choice(greetings)
        responses.append (greeting)
        
    if "how are you" in user_input:
        responses.append(f"I'm fine. What about you, {name} ?")
    for i in emotions:
        if i in user_input:
            responses.append(emotions[i]) 
        
    if not responses:
        responses.append("I don't understand that yet." )
    print(" ".join(responses))        
    