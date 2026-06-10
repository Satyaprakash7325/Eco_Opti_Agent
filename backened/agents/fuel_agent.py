from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

class FuelSuggestions(BaseModel):
    suggestions: list[str] = Field(..., description="A list of three actionable suggestions for reducing emissions from fuel usage.")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN", "dummy_key")
)

parser = PydanticOutputParser(pydantic_object=FuelSuggestions)

def calculate_fuel_emissions(uses_diesel, uses_lpg):
    emission = 0
    if uses_diesel:
        emission += 200  # Arbitrary base kg for diesel generator
    if uses_lpg:
        emission += 150  # Arbitrary base kg for LPG
    return float(emission)

fuel_prompt = PromptTemplate(
    input_variables=[
        "uses_diesel", "uses_lpg", "estimated_fuel_emission"
    ],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    template="""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an industrial fuel optimization expert. You must reply strictly in JSON format.
{format_instructions}
<|eot_id|><|start_header_id|>user<|end_header_id|>
The user provides the following fuel usage details:
- Uses Diesel Generator: {uses_diesel}
- Uses LPG/Propane: {uses_lpg}
The estimated fuel CO2 emission is {estimated_fuel_emission} kg/month.

Provide exactly three actionable suggestions to reduce fuel-based emissions.
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""
)

def run_fuel_agent(input_data):
    uses_diesel = input_data.get("uses_diesel", False)
    uses_lpg = input_data.get("uses_lpg", False)
    
    fuel_emission = calculate_fuel_emissions(uses_diesel, uses_lpg)
    input_data["estimated_fuel_emission"] = fuel_emission
    
    try:
        chain = fuel_prompt | llm | parser
        response = chain.invoke(input_data)
        
        if response and hasattr(response, "suggestions"):
            return response.suggestions, fuel_emission
        else:
            return ["No fuel suggestions available."], fuel_emission
            
    except Exception as e:
        print(f"Error in Fuel Agent: {e}")
        return ["No fuel suggestions available due to an error."], fuel_emission