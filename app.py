import os 
from agents import agents
import json
os.environ['OPENAI_API_KEY'] = 'sk-proj-akdeZO2k0thnW5qqSQPiT3BlbkFJFVW45H5G0FVUuzST2rLo'


def main() : 

    all_responses = agents.run_agent('test.pdf')

    open('final_result.json' , 'w').write(json.dumps(all_responses))

if __name__ == '__main__' : main()