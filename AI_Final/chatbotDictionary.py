import random
def chat():
    print("Hey there! I am Robot 2.0 at your service")

    responses = {
        "my name is": "Hello {name}, How are you?",
        "hi": "Hello, my name is Hiesenberg",
        "what is your name?": "I am a bot created by Heisenberg. You can call me crazy!",
        "how are you?": "I'm doing good. How about you?",
        "sorry": ["It's alright", "It's OK, never mind"],
        "i am fine": "Great to hear that. How can I help you?",
        "good": "Nice to hear that. How can I help you? :)",
        "age?": "I'm a computer program, dude. Seriously, you are asking me this?",
        "what do you want?": "Make me an offer I can't refuse",
        "created?": ["Raghav created me using Python's NLTK library", "Top secret ;)"],
        "location?": "Indore, Madhya Pradesh",
        "how is your health": "I'm a computer program, so I'm always healthy",
        "sports": "I'm a very big fan of Football",
        "who is": ["Messi", "Ronaldo", "Rooney"],
        "who is": "Brad Pitt",
        "i am looking for online guides and courses to learn data science, can you suggest?": "Crazy_Tech has many great articles with step-by-step explanations along with code. You can explore",
        "quit": "Thank you for using our intelligence services"
    }

    while True:
        user_input = input("> ")
        found_response = False

        for pattern, response in responses.items():
            if pattern in user_input.lower():
                if "{name}" in response:
                    name = user_input.split("is", 1)[1].strip()
                    response = response.format(name=name)
                print(response)
                found_response = True
                break

        if not found_response:
            print("Sorry, I didn't understand that. Can you please rephrase?")

        if user_input.lower() == "quit":
            break


if __name__ == "__main__":
    chat()