# ECO-OPTI-AGENT
# 🌱 EcoOptiAgent – AI-Driven Carbon Optimization

**[Live Demo](your-render-url-here)**

EcoOptiAgent is a full-stack multi-agent AI system designed to optimize carbon emissions for businesses. It uses intelligent agents, HTML/JS frontend, and a Python Flask backend to analyze emission patterns and provide actionable recommendations for sustainability.

---

## 🚀 Features

1. Multi-Agent Architecture (Electricity Agent,Transport Agent,Fuel Agent,,GreenInfra Agent,Optimization Agent,Decision Agent)
2. Emission Trend Analysis with chating
3. Smart Emission Predictor (based on historical data)
4. Adaptive User Preferences
5. Full-Stack Integration (React, JS, Flask, Python)
6. Interactive Carbon Management Dashboard

---

## 🧰 Tools & Technologies

| Category         | Stack                            |
|------------------|----------------------------------|
| Frontend         | HTML, CSS, JavaScript, React     |
| Backend          | Python, Flask, LangGraph, Gemini API |
| Version Control  | Git & GitHub                     |

           |


---

## 🛠 Installation

### Prerequisites

- Node.js & npm installed
- Python 3.8+ with pip
- Git

### Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/Satyaprakash7325/Eco_Opti_Agent.git
   cd Eco_Opti_Agent
   ```

2. Install backend dependencies:
   ```bash
   cd backened
   pip install -r requirement.txt
   ```

3. Start the Flask server (which also serves the frontend):
   ```bash
   python main.py
   ```
4. Open your browser and navigate to `http://localhost:5000`

### Render Deployment
This repository is configured with a `render.yaml` Blueprint. To deploy:
1. Push this repository to GitHub.
2. In the Render Dashboard, create a new "Blueprint".
3. Select this repository.
4. Render will automatically build and deploy both the backend and frontend.
5. Provide your `GOOGLE_API_KEY` as an environment variable in the Render Dashboard (optional: if not provided, the app will gracefully degrade to use mock data for demonstration purposes).


🧠 Project Structure:

EcoOptiAgent/
├── backend/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── decision_agent.py
│   │   ├── electricity_agent.py
│   │   ├── fuel_agent.py
│   │   ├── greeninfra_agent.py
│   │   ├── optimizer_agent.py
│   │   ├── router_agent.py
│   │   └── transport_agent.py
│   ├── prompts/
│   ├── main.py
│   ├── utils.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── FullLogo_NoBuffer.jpg
│
├── list_models.py
├── .gitignore
├── README.md



🧠 Architecture:


2. backend/
   ├── app.py            → Flask server: connects frontend with agents
   ├── utils.py          → Utility functions for data handling
   ├── requirements.txt  → Python dependencies
   └── agents/
       ├── decision_agent.py      → Central logic for emissions optimization
       ├── electricity_agent.py   → Analyzes electricity consumption patterns
       ├── fuel_agent.py          → Handles emission data from fuel usage
       ├── transport_agent.py     → Manages transport-related emissions
       ├── greeninfra_agent.py    → Suggests green infrastructure options
       ├── optimizer_agent.py     → Optimizes decisions across agents
       └── router_agent.py        → Routes communication between agents
   
📝 License:

This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with proper attribution.
See the LICENSE file for details.

🤝 Contribution:
Contributions, issues, and feature requests are welcome!

To contribute:

1.Fork the repository.

2.Create your feature branch: git checkout -b feature/YourFeature

3.Commit your changes: git commit -m 'Add some feature'

4.Push to the branch: git push origin feature/YourFeature

5.Open a pull request.



📞 Support:

For any questions or support, please contact:
📧 sunyaslokapriyadarshi@gmail.com


  















