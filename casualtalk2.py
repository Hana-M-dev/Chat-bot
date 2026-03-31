
import random
name = input("What's your name? ").capitalize()
print("Hello", name)

emotions = {
    'sad': [
        "That sounds really hard.",
        "I'm sorry you're feeling that way.",
        "That must be tough.",
        "Do you want to talk about it?"
    ],
    'happy': [
        "That's great to hear!",
        "I'm really glad you're feeling good!",
        "That sounds awesome!",
        "Keep that energy going!"
    ],
    'angry': [
        "That sounds frustrating.",
        "I get why you'd feel that way.",
        "Want to talk about what happened?",
        "Take a breath, I'm here."
    ],
    'tired': [
        "You should get some rest.",
        "Sounds like you need a break.",
        "Don't push yourself too hard.",
        "Take it easy for a bit."
    ],
    'excited': [
        "That's exciting!",
        "Tell me more!",
        "I love that energy!",
        "What are you excited about?"
    ]
}

def greet(user_input,name):
    greet_words = ['hello', 'hey','hi',]
    greetings = [f'Hey {(name)}',f'Hello {(name)}',f'Hi {(name)}']
    if any(word in user_input for word in greet_words):
        return random.choice(greetings)
    
                    
def format_response(response: str, name):
    use_name = random.choice([True,False])
    if use_name:
        if '?' in response or '!' in response:
            response = f'{name} {response}'    
        else:
            response = response.replace('.', '')
            response = f'{response} , {name}.'
    return response

    
while True:
    responses = []
    user_input = input("You: ").lower()

    print("Bot: ", end = '')
    
    if "bye" in user_input:
        responses.append("Goodbye!")
        print(" ".join(responses))
        break   
    greetus = greet(user_input, name)
    if greetus:
        responses.append(greetus)
    
    if "how are you" in user_input:
        responses.append(f"I'm fine. What about you?")
        
    for i in emotions:
        if i in user_input:
            response = random.choice(emotions[i])
            response = format_response(response,name)
            responses.append(response) 
        
    if not responses:
        responses.append("I don't understand that yet." )

        
    print(" ".join(responses))        
    