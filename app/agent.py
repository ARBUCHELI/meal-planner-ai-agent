from openai import OpenAI
import json

class MealPlannerAgent:
    def __init__(self, model="gpt-4o", max_passes=3, seed=42):
        self.client = OpenAI()
        self.model = model
        self.max_passes = max_passes
        self.seed = seed

    def get_completion(self, prompt, system_prompt, json_mode=False):
        response = self.client.chat.completions.create(
            model=self.model,
            seed=self.seed,
            temperature=0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"} if json_mode else None,
        )
        return response.choices[0].message.content

    def draft_plan(self, prompt):
        raw = self.get_completion(prompt["user"], prompt["system"], json_mode=True)
        return json.loads(raw)

    def critique_plan(self, prompt):
        raw = self.get_completion(prompt["user"], prompt["system"], json_mode=True)
        return json.loads(raw)

    def revise_plan(self, prompt):
        raw = self.get_completion(prompt["user"], prompt["system"], json_mode=True)
        return json.loads(raw)

    def build_grocery_list(self, prompt):
        raw = self.get_completion(prompt["user"], prompt["system"], json_mode=True)
        return json.loads(raw)

    def run(self, prompts):
        plan = self.draft_plan(prompts["draft"])

        for _ in range(self.max_passes):
            critique = self.critique_plan(prompts["critique"](plan))

            if not critique["fixes"] and not critique["suggestions"]:
                break

            plan = self.revise_plan(
                prompts["revise"](plan, critique)
            )

        groceries = self.build_grocery_list(
            prompts["groceries"](plan)
        )

        return {
            "plan": plan,
            "groceries": groceries
        }