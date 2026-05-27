from ollama import chat
import prikazy
import time

def ask(otazka):
    
    datum = time.strftime("%d.%m.%Y")
    cas = time.strftime("%H:%M")
    
    stav_stopek = prikazy.zjisti_stopky()
    
    personalita = f"""
Jsi Karel, virtuální asistent. Odpovídej vždy jako čistý text bez Markdownu (žádné tučné písmo, odrážky ani nadpisy).

### PRAVIDLA PRO PŘÍKAZY
Tyto příkazy smíš použít POUZE v případě, že tě o to uživatel explicitně požádá (např. "zapni stopky"). Pokud o nich uživatel nemluví, tyto řetězce nikdy nevypisuj:
- Pro spuštění stopek přidej na úplný konec zprávy: //timer-start
- Pro zastavení stopek přidej na úplný konec zprávy: //timer-stop

### KONTEXTOVÉ INFORMACE
Následující údaje použij pouze tehdy, pokud se na ně uživatel přímo zeptá. Jinak je ignoruj:
- Aktuální čas: {cas}
- Aktuální datum: {datum}
- Stav stopek: {stav_stopek}
"""

    
    response = chat(
        model='gemma3:12b',
        messages=[
        
        {'role': 'system', 'content': personalita},
        {'role': 'user', 'content': otazka}
    
        ],
    )
    
    odpoved = prikazy.zpracuj_prikazy(response.message.content)
    return(odpoved)