from openai import OpenAI
from base_utils import base_utils

def run_llm(prompt) :

    client = OpenAI()

    stream = client.chat.completions.create(
        model = 'gpt-3.5-turbo' , 
        messages = [
            {
                'role' : 'user' , 
                'content' : prompt}] , 
        stream = True)
    response = ''

    for chunk in stream : 

        if chunk.choices[0].delta.content : response += chunk.choices[0].delta.content

    return response

def run_rag(query , vc) : 

    similar_docs = vc.similarity_search(query)

    context = '\n'.join([
        doc.page_content 
        for doc 
        in similar_docs
    ])

    prompt = open('Assets/prompt/agent_3/prompt.txt').read().format(context , query)

    response = run_llm(prompt)

    return response

def summarize(query , n_response) : 

    history = base_utils.get_history()

    prompt = open('Assets/prompt/agent_4/prompt.txt').read().format(n_response , history , query)

    response = run_llm(prompt)

    return response