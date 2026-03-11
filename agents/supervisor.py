from agents.budget_agent import BudgetAgent
from agents.investment_agent import InvestmentAgent
from services.llm_service import LLMService
from services.memory_service import MemoryService

def __init__(self):
    self.llm_service = LLMService()
    self.memory_service = MemoryService()
    self.budget_agent = BudgetAgent(self.llm_service)
    self.investment_agent = InvestmentAgent(self.llm_service)

def route(self, message):
        if "budget" in message.lower() or "expense" in message.lower():
            return "budget"
        if "invest" in message.lower() or "stock" in message.lower():
            return "investment"
        return "budget"

def handle_message(self, user_id, message):
        context = self.memory.load_memory(user_id)

        route = self.route(message)

        if route == "budget":
            response = self.budget_agent.run(message, context)
        else:
            response = self.investment_agent.run(message, context)

        self.memory.save_memory(user_id, {
            "user": message,
            "assistant": response
        })

        return response