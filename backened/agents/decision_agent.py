# from langchain_core.runnables import RunnableLambda
# from langchain_core.output_parsers import StrOutputParser
# from langchain.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os

# # Load Gemini LLM using API key from environment
# llm = ChatGoogleGenerativeAI(
#     model="gemini-pro",
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# # Prompt template for Decision Agent
# decision_prompt = PromptTemplate(
#     input_variables=["input"],
#     template="""
# You are an intelligent sustainability decision agent. Based on the analysis from the other agents and the CO₂ emission stats provided below, give the business:

# 1. A concise summary of total emissions.
# 2. Key contributors to emissions.
# 3. Prioritized action recommendations (e.g., switch to LED lights, install solar panels, optimize vehicle usage, switch to electric fleet, etc.).
# 4. Estimated impact if each recommended action is implemented.

# Use clear bullet points in your response.

# Input:
# {input}

# Response:
# """.strip()
# )

# # Output parser
# parser = StrOutputParser()

# # Decision Agent chain
# decision_chain = decision_prompt | llm | parser

# # Define run_decision_agent function for main.py
# run_decision_agent = RunnableLambda(lambda input: decision_chain.invoke({"input": input}))
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN", "dummy_key")
)

decision_prompt = PromptTemplate(
    input_variables=["input"],
    template="""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an intelligent sustainability decision agent. You have received an analysis of a business's CO2 emissions and a list of suggestions from various specialized agents.

Your task is to review all the provided information and synthesize it into a final, prioritized sustainability plan.
<|eot_id|><|start_header_id|>user<|end_header_id|>
Input from agents:
{input}

Based on this, provide a concise summary of the business's carbon footprint and then give exactly three prioritized, highly actionable recommendations. Do not just repeat the suggestions you were given. Instead, combine and optimize them to form the most impactful three recommendations.

For each of the three recommendations, state the action and its estimated impact.

Response:
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
""".strip()
)

parser = StrOutputParser()
decision_chain = decision_prompt | llm | parser

run_decision_agent = RunnableLambda(lambda input: decision_chain.invoke({"input": input}))