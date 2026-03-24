import json
from app.agent import MealPlannerAgent
from app.prompts import (
    get_draft_prompt,
    get_critique_prompt,
    get_revision_prompt,
    get_grocery_prompt
)
from app.schemas import MENU_SCHEMA

def main():
    with open("data/sample_input.json") as f:
        params = json.load(f)

    agent = MealPlannerAgent()

    prompts = {
        "draft": get_draft_prompt(params, MENU_SCHEMA),
        "critique": lambda plan: get_critique_prompt(plan, params),
        "revise": lambda plan, critique: get_revision_prompt(plan, critique, MENU_SCHEMA),
        "groceries": lambda plan: get_grocery_prompt(plan, params["pantry"])
    }

    result = agent.run(prompts)

    print("\nFINAL PLAN")
    print(json.dumps(result["plan"], indent=2))

    print("\nGROCERY LIST")
    print(json.dumps(result["groceries"], indent=2))


if __name__ == "__main__":
    main()