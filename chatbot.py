import random

greetings = ["Hello!", "Hi there!", "Hey, how can I help you?"]
farewells = ["Goodbye!", "See you later!", "Take care!"]
unknown = ["Sorry, I didn't understand that.", "I'm not sure what you mean."]
thanks = ["You're welcome!", "No problem.", "Glad I could help!"]
apologies = ["I'm sorry about that.", "My apologies.", "I'll do better next time."]
confirmations = ["Got it!", "Understood.", "OK, I'll take care of that."]
clarifications = ["Can you please elaborate?", "I'm not sure I understand. Could you explain more?", "Can you give me more information?"]
suggestions = ["Have you tried this solution?", "Maybe you could try this.", "Here's a suggestion."]
acknowledgments = ["Thanks for letting me know.", "I appreciate your feedback.", "I'll pass this on to my team."]
encouragements = ["You can do it!", "Keep going!", "Don't give up!"]


def chatbot():
    print("Welcome to the customer interaction chatbot!")
    while True:
        user_input = input("User: ").lower()
        if "hello" in user_input:
            print("Chatbot: " + random.choice(greetings))
        elif "bye" in user_input:
            print("Chatbot: " + random.choice(farewells))
            break
        elif "thank" in user_input:
            print("Chatbot: " + random.choice(thanks))
        elif "sorry" in user_input:
            print("Chatbot: " + random.choice(apologies))
        elif "confirm" in user_input:
            print("Chatbot: " + random.choice(confirmations))
        elif "clarify" in user_input:
            print("Chatbot: " + random.choice(clarifications))
        elif "suggest" in user_input:
            print("Chatbot: " + random.choice(suggestions))
        elif "acknowledge" in user_input:
            print("Chatbot: " + random.choice(acknowledgments))
        elif "encourage" in user_input:
            print("Chatbot: " + random.choice(encouragements))
        else:
            print("Chatbot: " + random.choice(unknown))

chatbot()