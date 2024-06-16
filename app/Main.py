import Utils
import ReadCsv
import Charts

def run():
    data = ReadCsv.readCsv('Data.csv')
    Continent = input('Type ContinentN => ')
    dataC = Utils.GetPopulationByContinent(data,Continent)
    
    countries = list(map(lambda x: x['Country/Territory'], dataC))
    percentages = list(map(lambda x: x['World Population Percentage'], dataC))
    Charts.Generate_PieChart(countries,percentages)
    
    
    country = input('Type Country => ')

    result = Utils.GetPopulationByCountry(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = Utils.GetPopulation(country)
        Charts.Generate_BarChart(country['Country/Territory'],labels, values)
    
      
if __name__ == '__main__':
  run()