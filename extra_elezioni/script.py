from textract import process
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

programmi = {
    "bernardo": str(BeautifulSoup(process("bernardo.pdf"), "lxml").text).lower(),
    "sala": str(BeautifulSoup(process("sala.pdf"), "lxml").text).lower(),
    "michetti": str(BeautifulSoup(process("michetti.pdf"), "html.parser").text).lower(),
    "gualtieri": str(BeautifulSoup(process("gualtieri.pdf"), "lxml").text).lower(),
    "raggi": str(BeautifulSoup(process("raggi.pdf"), "lxml").text).lower(),
    "lorusso": str(BeautifulSoup(process("lorusso.pdf"), "lxml").text).lower(),
    "sganda": str(BeautifulSoup(process("sganda.pdf"), "lxml").text).lower(),
    "damilano": str(BeautifulSoup(process("damilano.pdf"), "lxml").text).lower()
}

result = "Numero di volte che compaiono queste parole nei programmi:\n"

for sindaco in programmi.keys():
    covid = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("covid"), programmi[sindaco]))
    covid_19 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("covid-19"), programmi[sindaco]))
    coronavirus = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("coronavirus"), programmi[sindaco]))
    pandemia = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("pandemia"), programmi[sindaco]))
    epidemia = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("epidemia"), programmi[sindaco]))

    wordcloud = WordCloud(max_font_size=80, width=700, height=400).generate(programmi[sindaco])
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.savefig(f"wordcloud_{sindaco}.png", dpi=1000)

    result += f"{sindaco}: covid={covid}, covid-19={covid_19}, coronavirus={coronavirus}, pandemia={pandemia}, epidemia={epidemia}\n"

with open('result.txt', 'w') as f:
    f.write(result)

