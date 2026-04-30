import time
from agents.base_agent import BaseAgent

class DevAgent(BaseAgent):

    def think(self, task):
        self.log(f"Executing task: {task}")
        time.sleep(1)

        result = {
            "task": task,
            "status": "completed",
            "output": f"{task}_code"
        }

        self.memory.add(task, result)
        return result
