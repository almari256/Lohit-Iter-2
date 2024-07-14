from create_vc import create_vc
from extractors import extractors
from halo import Halo
from answers import answers
from tqdm import tqdm

def agent_1(pdf_path) : 

    # spinner = Halo(
    #     text = f'Extracting Table of Contents from {pdf_path} and creating Vectorstore at main_vectors' , 
    #     spinner = 'dots')

    # spinner.start()

    print(f'Extracting Table of Contents from {pdf_path} and creating Vectorstore at main_vectors')

    text = extractors.pdf_to_text(pdf_path)

    table_of_contents = extractors.extract_toc(text)

    vectorstore = create_vc.create_vc(text)

    # spinner.stop()

    return table_of_contents , vectorstore

def agent_2(query , times_to_run) : 

    # spinner = Halo(
    #     text = f'Generating {times_to_run} for {query}' , 
    #     spinner = 'dots')

    # spinner.start()

    print(f'Generating {times_to_run} for {query}')

    prompt = open('Assets/prompt/agent_2/prompt.txt').read().format(times_to_run , query)

    response = answers.run_llm(prompt)

    open('Assets/prompt/agent_2/logs.txt' , 'a').write(
        f'''
Original Query : {query}

Times to run : {times_to_run}

New Queries : {response}

\n\n
        ''')

    questions = response.split('\n')

    # spinner.stop()

    return questions

def agent_3(questions , vc) : 

    # spinner = Halo(
    #     text = f'Generating answers for {questions}' , 
    #     spinner = 'dots')

    # spinner.start()

    print(f'Generating answers for {questions}')

    n_answers = '\n'.join([
        answers.run_rag(question , vc)
        for question
        in questions
    ])

    # spinner.stop()

    open('Assets/prompt/agent_3/logs.txt' , 'a').write(
        f'''
Questions : {questions}

Answers : {n_answers}

\n\n
        '''
    )

    return n_answers

def agent_4(n_response , query) : 

    # spinner = Halo(
    #     text = f'Generating response for original query {query}' , 
    #     spinner = 'dots')

    # spinner.start()

    print(f'Generating response for original query {query}')

    response = answers.summarize(query , n_response)

    # spinner.stop()

    open('Assets/prompt/agent_4/logs.txt' , 'a').write(
        f'''
N Response : {n_response}

Original Query : {query}

Response : {response}

\n\n
        '''
    )

    return response

def run_agent(pdf_path , times_to_run = 2) : 

    queries , vectorstore = agent_1(pdf_path)

    # queries = [queries[0]]

    all_responses = dict()

    for query in tqdm(queries , total = len(queries)) : 

        # spinner = Halo(
        #     text = f'Getting Variations for {query}' , 
        #     spinner = 'dots')

        # spinner.start()

        print(f'Getting Variations for {query}')

        n_variations = agent_2(query , times_to_run)

        n_response = agent_3(n_variations , vectorstore)

        main_response = agent_4(n_response , query)

        all_responses[query] = main_response

    return all_responses