#from PIL import Image
from bs4 import BeautifulSoup
import requests
import io

def getInfo():
    #Gets the website and puts it into a document to be parsed using BeatifulSoup
    url = "https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0mmpz&gl=US&ceid=US%3Aen"
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

    totalWorldCases = soup.find_all(class_="l3HOY")[1].get_text()
    newWorldCases = soup.find_all(class_="l3HOY")[2].get_text()
    totalWorldDeaths = soup.find_all(class_="l3HOY")[5].get_text()
    totalUSCases = soup.find_all(class_="l3HOY")[7].get_text()
    newUSCases = soup.find_all(class_="l3HOY")[8].get_text()
    usDeaths = soup.find_all(class_="l3HOY")[11].get_text()
    information = {
        "countyName": countyName,
        "newCountyCases": newCountryCases,
        "newCountyDeaths": newCountryDeaths,
        "totalCountyCases": totalCountyCases,
        "totalCountyDeaths": totalCountyDeaths,
        "worldCases": totalWorldCases,
        "newWorldCases": newWorldCases,
        "worldDeaths":totalWorldDeaths,
        "usCases": totalUSCases,
        "newUSCases": newUSCases,
        "usDeaths": usDeaths
    }
    return information

if __name__ == "__main__":
    print(getInfo())