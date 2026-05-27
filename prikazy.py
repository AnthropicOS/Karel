import re
import time
import math

start_time = time.perf_counter()
end_time = time.perf_counter()
bezi = False

def zapni_stopky():
    global bezi, start_time
    bezi = True
    start_time = time.perf_counter()
    end_time = time.perf_counter()

def vypni_stopky():
    global bezi, end_time
    end_time = time.perf_counter()
    bezi = False

def zjisti_stopky():

    
    vysledek = end_time - start_time

    minuty = math.floor(vysledek / 60)
    sekundy = math.floor(vysledek % 60)

    if bezi is True:
        return(f"Stopky běží, ukazují {minuty}min a {sekundy}sec")

    return(f"Stopky jsou zastavené, ukazují {minuty}min a {sekundy}sec")

def zpracuj_prikazy(text):
        
    odpoved = text
    
    hledat = re.search("//timer-start", text)
    if hledat is not None:
        zapni_stopky()
        odpoved = text.replace("//timer-start", "")
    
    hledat = re.search("//timer-stop", text)
    if hledat is not None:
        vypni_stopky()
        odpoved = text.replace("//timer-stop", "")
        
    return(odpoved)
