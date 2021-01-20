from pyppeteer import launch
import json
import time
import asyncio

def getUSData():
    return asyncio.get_event_loop().run_until_complete(coviddatagrabber())

def convertNumString(number):
    stringNumber = '{:,}'.format(number)
    return stringNumber
async def coviddatagrabber():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://api.covidtracking.com/v1/us/current.json')
    await page.evaluate('datainfo = document.body.innerText')
    di = await page.evaluate('datainfo')
    dij = json.loads(di)[0]
    positiveCases = dij['positive']
    information = {
        "positiveCases": convertNumString(positiveCases),
        "positiveCasesInt": dij['positive'],
        "negativeCases": convertNumString(dij['negative']),
        "negativeCasesInt": str(dij['negative']),
        "deaths" : convertNumString(dij["death"]),
        "deathsInt" : dij["death"],
        "positiveIncrease": convertNumString(dij['positiveIncrease']),
        "positiveIncreaseInt": dij['positiveIncrease'],
        "deathIncrease": convertNumString(dij['deathIncrease']),
        "deathIncreaseInt": str(dij['deathIncrease'])
    }
    return information

