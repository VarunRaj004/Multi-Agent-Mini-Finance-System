class BaseAgent:
    def __init__(self, name,llm_service):
        self.name = name
        self.llm_service = llm_service

    def run(self,user_input,context):
        raise NotImplementedError