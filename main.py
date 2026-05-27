import agent
import speak

while True:
    otazka = input("Zeptej se na cokoliv: ")
    odpoved = agent.ask(otazka)
    
    print(odpoved)
    speak.speak(odpoved)