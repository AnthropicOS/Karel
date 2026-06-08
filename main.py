import agent
import speak
import gradio as gr
import threading

def dotaz_na_karla(otazka, dummy):
    
    text = otazka["text"]
    priloha = otazka["files"]
    
    odpoved = agent.ask(text, priloha)

    vlakno_hlasu = threading.Thread(target=speak.speak, args=(odpoved,))
    vlakno_hlasu.start()
    
    yield odpoved

gr.ChatInterface(fn=dotaz_na_karla, multimodal=True).launch()

    
