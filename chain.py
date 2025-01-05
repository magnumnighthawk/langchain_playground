from langchain_community.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

template = "What is a {sentiment} {keyword} tip!"
prompt = PromptTemplate.from_template(template)
llm = OpenAI(model="gpt-3.5-turbo-instruct" , temperature=0.7)

chain = LLMChain(llm = llm, prompt = prompt)
response = chain.run({'sentiment': "great", 'keyword': "food"})

print(response)
