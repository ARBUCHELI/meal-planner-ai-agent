# 🍽️ Meal Planner AI Agent

An AI-powered meal planning agent that generates weekly dinner plans, critiques them, refines them, and produces a grocery list — all using LLMs.

---

## 🚀 Features

- 🧠 Multi-step AI agent (planner → critic → refiner)
- 🔁 Iterative improvement loop
- 🛒 Automatic grocery list generation
- ⚙️ Modular prompt architecture
- 📦 Clean and scalable project structure
- 🎯 Deterministic outputs using seeded requests

---

## 📁 Project Structure


meal-planner-agent/
│
├── app/
│ ├── init.py
│ ├── agent.py
│ ├── prompts.py
│ ├── schemas.py
│ └── utils.py
│
├── data/
│ └── sample_input.json
│
├── .env.example
├── .gitignore
├── requirements.txt
├── main.py
└── README.md


---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/meal-planner-agent.git
cd meal-planner-agent
2. Create a virtual environment
python -m venv venv
Activate it:

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_api_key_here
▶️ Run the Project
python main.py
🧠 How It Works

This project implements a self-reflection AI agent pattern, where the system improves its own output iteratively.

Step-by-step flow:
Draft
Generates an initial 7-day meal plan based on constraints.
Critique
Evaluates the plan against rules:
Budget limit
Calorie targets
Allergen restrictions
Pantry usage
Revise
Applies fixes and improvements to the plan.
Loop
Repeats the process until:
No issues remain, or
Maximum iterations reached
Grocery List
Generates a shopping list excluding pantry items.
📥 Input Example
{
  "people": 2,
  "days": 7,
  "daily_calories": 2000,
  "allergens": ["peanuts", "shellfish"],
  "budget_usd": 110,
  "pantry": ["rice", "lentils", "frozen spinach"]
}
📤 Output Example
Meal Plan
{
  "menu": [
    {
      "day": "Monday",
      "dish": "Lentil Spinach Curry with Rice",
      "ingredients": ["lentils", "spinach", "rice", "spices"],
      "calories": 2000,
      "est_cost_usd": 8
    }
  ],
  "total_cost": 105
}
Grocery List
{
  "shopping_list": [
    {
      "item": "chicken breast",
      "estimated_qty": "1kg"
    }
  ]
}
🛠 Tech Stack
Python
OpenAI API
JSON-based prompt engineering
🧩 Architecture
File	Responsibility
agent.py	Core agent loop and orchestration
prompts.py	Prompt generation (separation of concerns)
schemas.py	JSON output schema definitions
main.py	Entry point
data/	Sample inputs
💡 Design Pattern

This project uses a reflection-based agent architecture:

🧠 Planner → generates solution
🔍 Critic → evaluates constraints
🔁 Refiner → improves output
🛠 Tool → generates grocery list

This is a common real-world AI agent pattern used in production systems.

🧪 Best Practices Used
Deterministic outputs (seed + temperature=0)
JSON schema enforcement
Prompt modularization
Separation of concerns
Iterative refinement loop
🚀 Future Improvements
✅ Add schema validation with Pydantic
🌐 Expose as FastAPI API
⚛️ Connect to a React frontend
🔄 Streaming responses
🧠 Tool calling (function calling)
📊 Logging and observability
⚠️ Notes
Always validate LLM outputs in production
Costs depend on OpenAI API usage
Results may vary depending on prompt tuning
📄 License

MIT

👨‍💻 Author

Built as a real-world AI agent example demonstrating modern prompt engineering and agent design patterns.

