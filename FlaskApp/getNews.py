from PIL import Image
from bs4 import BeautifulSoup
import requests
import io

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


