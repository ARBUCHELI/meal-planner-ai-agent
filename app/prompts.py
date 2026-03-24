import json

def get_draft_prompt(params, schema):
    return {
        "system": "You are a registered dietician who writes weekly dinner plans.",
        "user": f"""
Create a 7-day dinner plan for {params["people"]} people.

- Calories: {params["daily_calories"]}
- Budget: ≤ {params["budget_usd"]}
- Allergens: {", ".join(params["allergens"])}
- Pantry: {", ".join(params["pantry"])}

Return JSON:
{schema}
"""
    }


def get_critique_prompt(plan, params):
    return {
        "system": "You are a stern dietary QA inspector.",
        "user": f"""
Plan:
{json.dumps(plan)}

Rules:
- Budget ≤ {params["budget_usd"]}
- Calories ±15% of {params["daily_calories"]}
- No allergens: {", ".join(params["allergens"])}
- Use pantry items: {", ".join(params["pantry"])}

Return JSON:
{{"fixes": [], "suggestions": []}}
"""
    }


def get_revision_prompt(plan, critique, schema):
    return {
        "system": "You are a senior meal planner applying corrections.",
        "user": f"""
Plan:
{json.dumps(plan)}

Fixes:
{json.dumps(critique["fixes"])}

Suggestions:
{json.dumps(critique["suggestions"])}

Return JSON:
{schema}
"""
    }


def get_grocery_prompt(plan, pantry):
    return {
        "system": "You are a helpful kitchen assistant.",
        "user": f"""
Plan:
{json.dumps(plan)}

Exclude pantry: {", ".join(pantry)}

Return JSON:
{{"shopping_list":[{{"item":"","estimated_qty":""}}]}}
"""
    }