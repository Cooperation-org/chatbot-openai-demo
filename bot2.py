from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os
import json
from IPython.display import display, Markdown
os.environ["OPENAI_API_KEY"] = 'open ai api key'


def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 256
    max_chunk_overlap = 20
    chunk_size_limit = 600

    llm_predictor = LLMPredictor(llm=ChatOpenAI(
        temperature=0, model_name="text-davinci-003", max_tokens=num_outputs))
    prompt_helper = PromptHelper(
        max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    index.save_to_disk('index.json')

    return index

def construct_index1(directory_path):
    max_input_size = 4096
    num_outputs = 256
    max_chunk_overlap = 20
    chunk_size_limit = 600

    llm_predictor = LLMPredictor(llm=ChatOpenAI(
        temperature=0, model_name="text-davinci-003", max_tokens=num_outputs))
    prompt_helper = PromptHelper(
        max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    index.save_to_disk('index1.json')

    return index



prompt = "Previously asked questions:\n"


def ask_me_anything(question):
    query = question
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(query, response_mode="compact")
    return response.response

f = open('textdata/ques.txt', 'w')
f.close()
# # construct_index('textdata')
count = 0
while count < 5:
    ques = input()
    if(ques == 'bye'):
        break
    f = open('textdata/ques.txt', 'w')
    f.write(prompt)
    f.close()
    construct_index('textdata')
    
    ans = ask_me_anything(ques)
    prompt = prompt + ques
    prompt = prompt + '\n'
    print(ans)
