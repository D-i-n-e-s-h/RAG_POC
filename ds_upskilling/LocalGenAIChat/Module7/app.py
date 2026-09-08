from llm.agent_loop import AgentLoop


def main():

    agent = AgentLoop()

    while True:

        user_input = input("You : ")

        if user_input.lower() == "exit":
            break

        response = agent.run(user_input)

        print(f"\nAssistant : {response}\n")


if __name__ == "__main__":
    main()