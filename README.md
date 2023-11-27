# my_new_car
### Structure
1. Scrape data daily.
[![Scrape BMW hybrid electro](https://github.com/JeanneDuPre/my_new_car/actions/workflows/bmw_hybrid_electro.yml/badge.svg)](https://github.com/JeanneDuPre/my_new_car/actions/workflows/bmw_hybrid_electro.yml)
[![Scrape BMW aktuell](https://github.com/JeanneDuPre/my_new_car/actions/workflows/bmw_aktuell.yml/badge.svg)](https://github.com/JeanneDuPre/my_new_car/actions/workflows/bmw_aktuell.yml)
[![Scrape Autos hybrid electro](https://github.com/JeanneDuPre/my_new_car/actions/workflows/autos_hybrid_electro.yml/badge.svg)](https://github.com/JeanneDuPre/my_new_car/actions/workflows/autos_hybrid_electro.yml)
2. feature engineering
   - data.py
3. visualization
4. model

### 1. Scraping daily

### 2. Feature Engineering
2.1. Clean the types, empty rows, duplicates ...
2.2. Handling outliers by removing the items in which the 7 score for the price, horsepower, or mileage is higher than 3 (more than three standard deviations from the mean)
2.3. Replace category values with boolean markers by using get_dummies
2.4. Checking Correlation 
2.5. 
### 3. Visualization
## pie chart brand
## line chart price and mileage
## line chart price and year
## Comparison of electric cars and gasoline cars (BMW | Tesla)

### 4. Model (Price Prediction)
4.1. LinearRegression from sklearn
4.2. CatBoostRegressor from catboost
4.3. OLS from statsmodels


