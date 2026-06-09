import agent
import speak
import gradio as gr
import threading

def dotaz_na_karla(otazka, air, mluvit):
    
    text = otazka["text"]
    priloha = otazka["files"]
    
    odpoved = agent.ask(text, priloha)

    if mluvit:
        vlakno_hlasu = threading.Thread(target=speak.speak, args=(odpoved,))
        vlakno_hlasu.start()
    
    yield odpoved

hlasovy_toggle = gr.Checkbox(label="Zapnout Karlovy hlasivky", value=True)

gr.ChatInterface(
    fn=dotaz_na_karla, 
    multimodal=True,
    title="Asistent Karel",
    additional_inputs=[hlasovy_toggle],
    additional_inputs_accordion="Nastavení hlasu"
).launch()