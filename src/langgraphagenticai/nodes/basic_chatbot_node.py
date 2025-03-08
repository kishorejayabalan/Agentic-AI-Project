from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot logic implementation
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processess the input state and generates a chatbot responses.
        """
        return {"messages": self.llm.invoke(state["messages"])}
