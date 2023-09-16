from chatterbot import ChatBot

chatbot = ChatBot("ChatBot")

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        try:
            response = chatbot.get_response(query)
            print(f"🪴 {response}")
        except Exception as e:
            print(f"An error occurred: {e}")
