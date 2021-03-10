# Dati alla mano - Covid Della Sera
File relativi agli articoli della rubrica Dati alla mano del progetto PCTO Covid Della Sera.

## Struttura
Gli articoli si trovano nelle rispettive cartelle (in ordine di pubblicazione).
Presentano:
- Un file HTML(la struttura dell'articolo)
- Un file Jupyter Notebook, visualizzazione grafica del codice Python utilizzato per realizzare i grafici.
- Uno o più file .csv, utilizzati da [Flourish](https://flourish.studio) per creare un grafico gradevole e facilmente embeddabile nel file html.

## Testare il codice in locale
- Installare Python (testato su v3.9)
- Creare una virtual environment 
``python -m venv venv``
- Entrare nella virtual environment
    - Su Windows:
``./venv/Scripts/activate.bat``
    - Su Linux/Mac OS:
``source venv/bin/activate``
- Installare i prerequisiti:
``pip install -r requirements.txt``
- Avviare l'interfaccia Jupyter:
``jupyter lab``
- Selezionare il file e avviarlo nell'interfaccia.