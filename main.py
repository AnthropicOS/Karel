import agent
import speak
import gradio as gr

def dotaz_na_karla(otazka, dummy):
    
    text = otazka["text"]
    priloha = otazka["files"]
    
    odpoved = agent.ask(text, priloha)
    yield odpoved


gr.ChatInterface(fn=dotaz_na_karla, multimodal=True).launch()

    
