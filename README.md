# SeniorProjectBitcoinPricePrediction
This is my senior project for Computer Science at Roanoke College 2022.<br>
<br>
This project is designed to Improve the results of previous work done for Bitcoin Price Prediction. The machine learning
algorithm used is Random Forest. More Information about this project can be found within BitcoinPricePredictionUsingRandomForest.pdf. If any questions arise about the code, data, or results contact Cameron - cgzerrilla@gmail.com.<br>
<br>
Files<br>
1.The_Application_of_Random_Forest_on_the_Closing_Price_Prediction_of_Bitcoin_CameronZerrilla.pdf - final report for the project<br>
//Data Files <br>
<br>
2.Bitcoindata.csv - holds only the bitcoin data<br>
3.BitcoinandEthereumdata.csv - holds the Bitcoin and Ethereum data<br>

4.BitNas.csv - holds the Bitcoin and Nasdaq data<br>
<br>
The only difference with this .csv is that since NASDAQ does not report on holidays or weekends I had to do simple python code to fill in the empty
dates with the previous dates' values. For instance any data from a Friday would have been reflected on to Saturday and Sunday to avoid null values.
<br>

<br>
//Result Files<br>
Each of the files containts the results for each set of trees for instance column RMSE 8020 of file BitcoinNasdaqRowResults row 35 represents the RMSE results for an 80 20 training test split for a set of 34 trees each column has a title so the row number -1 is the number of trees used in the set.<br>
<br>
5.BitcoinResults.xlsx<br>
6.BitcoinNasdaqResults.xlsx<br>
7.BitcoinandEthereumresults.xlsx<br>
<br>
//Code Files <br>
The file below is used for all my machine learning proccesses <br>
CodeUsedForBitcoinMachineLearning.py <br>
<br>
The file howToUseCode gives a little more detail on how to alter and manipulate the code to get the desired results/tests <br>
howToUseCode.txt<br>
<br>
