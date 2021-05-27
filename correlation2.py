import csv
import plotly.express as px
import numpy as np
def plotFigure(dataPath): 
    with open(dataPath) as f: 
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()
def getDataSource(dataPath): 
    iceCreamSales=[]
    coldDrinkSales=[]
    with open(dataPath) as f: 
        csvReader=csv.DictReader(f)
        for row in csvReader: 
            iceCreamSales.append(float(row["Marks In Percentage"]))
            coldDrinkSales.append(float(row["Days Present"]))
    return{"x":iceCreamSales,"y":coldDrinkSales}
def findCorrelation(dataSource): 
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation: ",correlation[0,1])
def main():
    dataPath="correlation3.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)
main()