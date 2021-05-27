import csv
import plotly.express as px
import numpy as np
def plotFigure(dataPath): 
    with open(dataPath) as f: 
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()
def getDataSource(dataPath): 
    iceCreamSales=[]
    coldDrinkSales=[]
    with open(dataPath) as f: 
        csvReader=csv.DictReader(f)
        for row in csvReader: 
            iceCreamSales.append(float(row["Coffee in ml"]))
            coldDrinkSales.append(float(row["sleep in hours"]))
    return{"x":iceCreamSales,"y":coldDrinkSales}
def findCorrelation(dataSource): 
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation: ",correlation[0,1])
def main():
    dataPath="correlation4.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)
main()