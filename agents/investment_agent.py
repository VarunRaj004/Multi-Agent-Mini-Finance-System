from agents.base_agent import BaseAgent

class InvestmentAgent(BaseAgent):
    def run(self,user_input,context):
        prompt = f"You are an investment advisor. User input: {user_input}, Context: {context}"
        return self.llm_service.generate(prompt)