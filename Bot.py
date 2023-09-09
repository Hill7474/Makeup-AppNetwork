
from chatterbot import ChatBot

chatbot = ChatBot("ChatBot")

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {ChatBot.get_response(query)}")
