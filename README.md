# Karel, virtuální asistent
Karel je asistent běžící na LLM modelu Gemma 3 od googlu. Pracuje převážně s textem, ale zvládne zpracovat i obrázek.

## Instalace
Pro funkčnost Karla je nutné [doinstalovat Ollamu](https://ollama.com/download) s modelem a Python knihovny přes PIP:
```
ollama pull gemma3:12b
```
```
pip install -r requirements.txt
```

## Spouštění
Pro jednoduchost je v souborech přidán .bat soubor, který slouží k rychlému spuštění programu.
Poté je vše dostupné z webového prohlížeče na adrese 127.0.0.1:7860

## Knihovny
Na frontend jsme využili Gradio, který zjednodušuje tvorbu UI.
Na backend jsme využili knihovnu Ollama s open-source modelem gemma 3.
TTS provozuje knihovna Piper.

## Parametry
Při testování jsme použili GPU AMD RX6700XT 12GB VRAM, přičemž při načtení modelu se kompletně využila i s 2GB RAM (=celkem 14GB paměti)
Jednoduché souvětí se generuje 5 - 10 sekund a spotřeba GPU při provozu je kolem 80W

## Cíl
Cílem celé práce bylo zhotovit lokálního AI Asistenta, který nahrazuje korporátní modely (např. Anthropic, Google, OpenAI...)

### Výhody
Model běží kompletně lokálně a offline, takže je 100% soukromý a důvěryhodný. Narozdíl od veřejných modelů, kde společnosti sbírají veškeré data uživatelů.
Není potřeba platit předplatné 

### Nevýhody
I se základním hardwarem je model extrémně pomalý - obzvlášť při analýze obrázků. Občas může poskytovat nesmyslný výstup.

## Verdikt
Používání lokálního modelu je velice nepraktické. Bylo by možné později přidat knihovny pro analýzu PDF souborů

---
<small>© 2026 AnthropicOS & vitek07k</small>
