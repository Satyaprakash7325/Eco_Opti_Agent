from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
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

optimizer_prompt = PromptTemplate(
    input_variables=["total_emissions", "emissions_breakdown", "all_suggestions"],
    template="""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an intelligent sustainability optimizer. Your task is to analyze the information and provide a single, prioritized suggestion for the business.
<|eot_id|><|start_header_id|>user<|end_header_id|>
Context:
- Total monthly CO₂ emissions: {total_emissions} kg
- Emissions breakdown by source: {emissions_breakdown}
- Raw suggestions from specialized agents: {all_suggestions}

Based on the emissions data and the provided suggestions, identify the most cost-effective and highest-impact action the business can take immediately. Your response should be a single, concise recommendation (e.g., "The highest-impact first step is to upgrade all lighting to energy-efficient LEDs, as this will reduce your largest source of emissions.").
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""
)

def run_optimizer_agent(state: dict) -> dict:
    total_emissions = state["total_emissions"]
    emissions_breakdown = state["emissions_breakdown"]
    all_suggestions = state["all_suggestions"]
    
    formatted_breakdown = ", ".join([f"{source}: {emissions} kg" for source, emissions in emissions_breakdown.items()])
    formatted_suggestions = "\n".join(all_suggestions)
    
    chain = optimizer_prompt | llm
    optimizer_output = chain.invoke({
        "total_emissions": total_emissions,
        "emissions_breakdown": formatted_breakdown,
        "all_suggestions": formatted_suggestions
    })
    
    state["optimizer_output"] = optimizer_output
    
    return state