from pyppeteer import launch
import json
import time
import asyncio
information = {
    "hi": "hello"
}
def getStateData(stateIntials):
    return asyncio.get_event_loop().run_until_complete(coviddatagrabber(stateIntials))

def convertNumString(number):
    stringNumber = '{:,}'.format(number)
    return stringNumber
async def coviddatagrabber(stateIntials):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://api.covidtracking.com/v1/states/'+ str(stateIntials) +'/current.json')
    await page.evaluate('datainfo = document.body.innerText')
    di = await page.evaluate('datainfo')
    dij = json.loads(di)
    information = {
        "state": str(dij['state']),
        "positiveCases": convertNumString(dij['positive']),
        "positiveCasesInt": (dij['positive']),
        "negativeCases": convertNumString(dij['negative']),
        "negativeCasesInt": (dij['negative']),
        "deaths" : convertNumString(dij["death"]),
        "deathsInt" : (dij["death"]),
        "positiveIncrease": convertNumString(dij['positiveIncrease']),
        "positiveIncreaseInt": (dij['positiveIncrease']),
        "deathIncrease": convertNumString(dij['deathIncrease']),
        "deathIncreaseInt": (dij['deathIncrease'])
    }
    return information
