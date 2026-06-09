from ollama import chat

personalita = f"""
Jsi Karel, virtuální asistent. Chováš se slušně a vždy přátelsky. Chat obohacuješ různými relevantními emoji.
"""

historie = []

def ask(otazka, soubor = None):
    
    global historie

    zpravy_pro_model = [{'role': 'system', 'content': personalita}]
    zpravy_pro_model.extend(historie)
    zpravy_pro_model.append({'role': 'user', 'content': otazka})

    if soubor:
        zpravy_pro_model[-1]['images'] = soubor

    response = chat(
        model='gemma3:12b',
        messages = zpravy_pro_model,
    )
    
    odpoved = response.message.content
    
    historie.append({'role': 'user', 'content': otazka})
    historie.append({'role': 'assistant', 'content': odpoved})
    
    return(odpoved)
