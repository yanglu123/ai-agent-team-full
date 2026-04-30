from agents.base_agent import BaseAgent

class TestAgent(BaseAgent):

    def think(self, results):
        self.log("Running tests")

        passed = all(r["status"] == "completed" for r in results)

        report = {
            "passed": passed,
            "total": len(results)
        }

        self.memory.set("test_report", report)
        return report
