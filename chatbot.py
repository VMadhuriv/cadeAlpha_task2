import nltk
from nltk.chat.util import Chat, reflections



# Define chat pairs for the chatbot
pairs = [
    ["my name is (.*)", ["Hi %1, how can I help you today?"]],
    ["(hi|hello|hey)", ["Hello! How can I assist you?"]],
    ["what is your name?", ["I am a chatbot."]],
    ["(what is your name|what should i call you|whats your name|who are you)",["you can call me chatbot"]],
    ["how are you?", ["I'm just a program, but I'm doing well. How about you?"]],
    ["(Iam fine|iam good)",["ohh nice"]],
    ["(bye|goodbye)", ["Goodbye! Have a great day."]],
    [("thanks|thank you|thats helpfull|thank you for chating with me"),["my plessure"]],
    ["(what is python|what is java|what is c )",["it is a programming language"]],

    ["default", ["I'm not sure how to respond to that."]]
]

# Create a chatbot using the defined pairs
chatbot = Chat(pairs, reflections)

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat() 
