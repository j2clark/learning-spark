# References

## DataFrames

[Spark SQL, DataFrames and Datasets Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)

## MLlib (Machine Learning)
[Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)

### Common Evaluation metrics for Regression:

y: actual value
py: predicted value
n: number of entries

* MAE - Mean Absolute Error: Average error = |y - py|/n)
* MSE - Mean Squared Error: Average squared error = (y - py)**2 / n;  errors are amplified; more popular than MAE
* RMSE - Root Mean Square Error: sqrt(MSE); result has same units as y (MSE units is y**2 ); most popular error metric for regression 
* R Squared Values (coefficient of determination) - statistical measure of regression model; in basic sense, measure of how much variance (0 - 100%). Should NOT be used as sole source for evaluating model

