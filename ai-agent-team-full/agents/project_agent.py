from agents.base_agent import BaseAgent

class ProjectAgent(BaseAgent):

    def think(self, requirement):
        self.log(f"Decomposing requirement: {requirement}")

        tasks = [
            {"id": 1, "type": "design_parse"},
            {"id": 2, "type": "ui_development"},
            {"id": 3, "type": "logic_development"},
            {"id": 4, "type": "testing"}
        ]

        self.memory.set("tasks", tasks)
        return tasks
