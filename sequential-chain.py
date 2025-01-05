from langchain_community.llms import OpenAI
from langchain.chains import SequentialChain, LLMChain
from langchain_core.prompts import PromptTemplate

llm = OpenAI(model="gpt-3.5-turbo-instruct" , temperature=0.7)

first_template = "Generate an interesting recipe for {food_type}!"
first_prompt = PromptTemplate.from_template(first_template)
first_chain = LLMChain(llm = llm, prompt = first_prompt, output_key="recipe")

cooking_time_template = "How long does it take to cook this recipe: {recipe}? Give the answer in minutes."
cooking_time_prompt = PromptTemplate.from_template(cooking_time_template)
cooking_time_chain = LLMChain(llm = llm, prompt = cooking_time_prompt, output_key="cooking_time")

nutrition_template = "What is the nutritional value of {recipe}?"
nutrition_prompt = PromptTemplate.from_template(nutrition_template)
nutrition_chain = LLMChain(llm = llm, prompt = nutrition_prompt, output_key="nutrition")

overall_chain = SequentialChain(
    chains=[first_chain, cooking_time_chain, nutrition_chain],
    input_variables=["food_type"],
    output_variables=["recipe", "cooking_time", "nutrition"],
    verbose=True
)

response = overall_chain("pasta carbonara")

print(response)