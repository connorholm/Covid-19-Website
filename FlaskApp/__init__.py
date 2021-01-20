from flask import Flask, render_template, url_for
from bs4 import BeautifulSoup
import requests
import os

def getInfo():
    #Gets the website and puts it into a document to be parsed using BeatifulSoup
    url = "https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0nhmw&gl=US&ceid=US%3Aen"
    r = requests.get(url)

    #Parsing through the website using BeatifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find( class_="tIUMlb")
    newCountryCases = result.find("strong").get_text()
    countyInfo = soup.find(class_="tZjT9b")
    totalCountyCases = countyInfo.find(class_="UvMayb").get_text()
    totalCountyDeaths = countyInfo.find_all(class_="UvMayb")[1].get_text()
    newCountryDeaths = countyInfo.find_all(class_="tIUMlb")[1].find("strong").get_text()
    countyName = soup.find(class_="wH7mg").get_text()
    totalMinnesotaCases = soup.find_all(class_="l3HOY")[13].get_text()
    newMinnesotaCases = soup.find_all(class_="l3HOY")[14].get_text()
    totalMinnesotaDeaths = soup.find_all(class_="l3HOY")[17].get_text()
    totalWorldCases = soup.find_all(class_="l3HOY")[1].get_text()
    newWorldCases = soup.find_all(class_="l3HOY")[2].get_text()
    totalWorldDeaths = soup.find_all(class_="l3HOY")[5].get_text()
    totalUSCases = soup.find_all(class_="l3HOY")[7].get_text()
    newUSCases = soup.find_all(class_="l3HOY")[8].get_text()
    usDeaths = soup.find_all(class_="l3HOY")[11].get_text()

    currentRisk = ""
    dailyCases = (int(newCountryCases))
    if dailyCases <100:
        currentRisk = "Low"
    elif dailyCases <200:
        currentRisk = "Low-Medium"
    elif dailyCases <300:
        currentRisk = "Medium"
    elif dailyCases <400:
        currentRisk = "High"
    information = {
        "countyName": countyName,
        "newCountyCases": newCountryCases,
        "newCountyDeaths": newCountryDeaths,
        "totalCountyCases": totalCountyCases,
        "totalCountyDeaths": totalCountyDeaths,
        'totalMinnesotaCases':totalMinnesotaCases,
        "newMinnesotaCases": newMinnesotaCases,
        "totalMinnesotaDeaths": totalMinnesotaDeaths,
        "worldCases": totalWorldCases,
        "newWorldCases": newWorldCases,
        "worldDeaths":totalWorldDeaths,
        "usCases": totalUSCases,
        "newUSCases": newUSCases,
        "usDeaths": usDeaths,
        "currentRisk": "High"
    }
    return information

#Grab image, title, and link to the site
#Grab data from https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen
def getNewsInfo():
    url = "https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen"
    r = requests.get(url)

    #Parsing through the website using BeatifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    newsImages = soup.find_all(class_="tvs3Id QwxBBf")
    imageSource = []
    for newsImage in newsImages:
        imageSource.append(newsImage["src"])
    imageSourceLength = len(imageSource)
    sourceCompanyHTML = soup.find_all(class_="wEwyrc AVN2gc uQIVzc Sksgp")
    sourceCompany = []
    for response in sourceCompanyHTML:
        sourceCompany.append(response.get_text())
    articlesTitle = soup.find_all(class_="DY5T1d")
    articleInfo = []
    sources = []
    titles = []
    newsInformation = []
    index = 0
    imageIndex = 0
    for stuff in articlesTitle:
        articleInfo.append(stuff)
        titles.append(stuff.get_text)
        sources.append("https://news.google.com"+ stuff["href"][1::])
        tempSource = "https://news.google.com"+ stuff["href"][1::]
        newsInformation.append(
            {
                "title":stuff.get_text(),
                "source": tempSource,
                "company":sourceCompany[index],
                "imageSource": imageSource[imageIndex]
            }
        )
        index+=1
        if imageIndex < imageSourceLength-1:
            imageIndex+=1
       
    return newsInformation[:5]

app = Flask(__name__)

newsInfo = getNewsInfo()
worldInfo = getInfo()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title= "Home", worldInfo = worldInfo)
@app.route("/news")
def news():
    return render_template('news.html', title="News", newsInfo = newsInfo, worldInfo = worldInfo)
@app.route("/prevention")
def prevention():
    return render_template('prevention.html', title="Prevention", worldInfo = worldInfo)
@app.route("/references")
def references():
    return render_template('references.html', title="References", worldInfo = worldInfo)
@app.route("/about")
def about():
    return render_template('about.html', title="About", worldInfo = worldInfo)

if __name__ == '__main__':
    app.run(debug=True)
