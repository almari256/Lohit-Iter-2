def is_toc(line) : 

    if (
        line.lower().startswith('item')
    ) : return True 

    return False

def get_history() : return '\n'.join(open('Assets/Logs/chat_logs.json').read().split('\n')[- 6 :])