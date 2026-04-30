from agents.base_agent import BaseAgent

class DesignAgent(BaseAgent):

    def think(self, figma_data):
        self.log("Processing design data")

        ui_spec = {
            "components": figma_data.get("components", []),
            "layout": figma_data.get("layout", {}),
            "styles": figma_data.get("styles", {})
        }

        self.memory.set("ui_spec", ui_spec)
        return ui_spec
