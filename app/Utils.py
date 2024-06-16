def GetPopulation(contryDict):
    populationDict = {
        '2022': int(contryDict['2022 Population']),
        '2020': int(contryDict['2020 Population']),
        '2015': int(contryDict['2015 Population']),
        '2010': int(contryDict['2010 Population']),
        '2000': int(contryDict['2000 Population']),
        '1990': int(contryDict['1990 Population']),
        '1980': int(contryDict['1980 Population']),
        '1970': int(contryDict['1970 Population'])
    }
    
    return populationDict.keys(), populationDict.values()

def GetPopulationByCountry(data,country):
    return list(filter(lambda item: item['Country/Territory'] == country, data))

def GetPopulationByContinent(data,continent):
    return list(filter(lambda item: item['Continent'] == continent, data))