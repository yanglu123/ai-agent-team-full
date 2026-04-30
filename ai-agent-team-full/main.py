from concurrent.futures import ThreadPoolExecutor

from agents.project_agent import ProjectAgent
from agents.product_agent import ProductAgent
from agents.design_agent import DesignAgent
from agents.dev_agent import DevAgent
from agents.test_agent import TestAgent

from memory.shared_memory import SharedMemory
from memory.isolated_memory import IsolatedMemory

from tools.figma_parser import parse_figma
from tools.code_generator import generate_code
from tools.logger import log_step

def main():
    shared = SharedMemory()

    product = ProductAgent("ProductAgent", shared)
    design = DesignAgent("DesignAgent", shared)
    project = ProjectAgent("ProjectAgent", shared)
    tester = TestAgent("TestAgent", shared)

    requirement = "Build login page"

    log_step("Step 1: Product Analysis")
    product.think(requirement)

    log_step("Step 2: Design Parsing")
    figma = parse_figma("data/figma.json")
    ui_spec = design.think(figma)

    log_step("Step 3: Task Decomposition")
    tasks = project.think(requirement)

    log_step("Step 4: Parallel Development")
    dev_agents = [
        DevAgent("DevAgent-1", IsolatedMemory()),
        DevAgent("DevAgent-2", IsolatedMemory())
    ]

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for i, task in enumerate(tasks):
            agent = dev_agents[i % 2]
            futures.append(executor.submit(agent.think, task["type"]))

        results = [f.result() for f in futures]

    log_step("Step 5: Code Generation")
    code = generate_code(ui_spec)
    print("\nGenerated Code:\n", code)

    log_step("Step 6: Testing")
    report = tester.think(results)

    print("\nFinal Report:", report)

if __name__ == "__main__":
    main()
