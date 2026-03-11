import json
import os

MEMORY_FILE = "memory/memory.json"

class MemoryService:
    def __init__(self,memory_file = MEMORY_FILE):
        self.memory_file = memory_file

        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump({}, f)

    def load_memory(self ,user_id):
        with open(self.memory_file,'r') as f:
            data = json.load(f)
            return data.get(user_id, {})
        
    def save_memory(self, user_id, msg):
         with open(self.memory_file, "r") as f:
            data = json.load(f)

         if user_id not in data:
            data[user_id] = []

         data[user_id].append(msg)

         with open(self.memory_file, "w") as f:
            json.dump(data, f, indent=2)