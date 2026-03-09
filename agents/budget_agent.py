from agents.base_agent import BaseAgent

class BudgetAgent(BaseAgent):
    def run(self,user_input,context):
        prompt = f"Given the user's financial data and goals, provide a budget recommendation. User input: {user_input}, Context: {context}"
        return self.llm_service.generate(prompt)
