from langchain_community.llms import OpenAI
# To use HuggingFaceHub, you need to install the langchain-huggingface package
# from langchain import HuggingFaceHub
from langchain import PromptTemplate
from langchain.chains import LLMChain

template = "What is a {sentiment} {keyword} tip!"
prompt = PromptTemplate.from_template(template)
llm = OpenAI(model="gpt-3.5-turbo-instruct" , temperature=0.7)
# With HuggingFaceHub
# llm = HuggingFaceHub(repo_id="google/flan-t5-base",
#                      model_kwargs={
#                          "temperature": 0.9
#                      })

chain = LLMChain(llm = llm, prompt = prompt)
response = chain.run({'sentiment': "great", 'keyword': "food"})

print(response)
