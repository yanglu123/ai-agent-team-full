from agents.base_agent import BaseAgent

class ProductAgent(BaseAgent):

    def think(self, requirement):
        self.log("Analyzing requirement")

        prd = {
            "title": "Login Feature",
            "description": requirement,
            "features": [
                "User login",
                "Input validation",
                "Error handling"
            ]
        }

        self.memory.set("prd", prd)
        return prd
