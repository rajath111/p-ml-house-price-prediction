# House Price Prediction
Predicts the price of a house using Linear Regression model. 

Motivation behind this project is to create a service that uses trained ML model. So, the trained ML model can used for prediction by other services.

I have taken boston houssing data from kaggle. It can be found here: https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset.

Features:
1. RM - Average number of rooms
2. LSTAT - % lower status of the population
3. PTRATIO - Pupil to teacher ratio

Target:  
1. MEDV - Median value of house in dollars($)

I have used **scikit-learn** module to build and train a **linear regresion model**. And saved the model under ```./model``` folder.

To comsume to trained model, I have created an **Flask application**. We can make **POST** request to the endpoint ```/predict``` to get predicted housing price.

POST data:
```
{
    "rm": 6.5,
    "lstst": 9.14,
    "ptratio": 20.1,
}
```

## Requirements
1. Python: v^3.0
2. Docker CRI: Required only if you want to run the application inside a docker container


## Run service locally

1. Update pip to latest version
    ```
    py -m pip install -U pip
    ```
2. Create a virtual environment
    ```
    python -m venv boston-env
    ```
1. Activate the virtual environment
    ```
    boston-env\Scripts\activate
    ```
1. Install required packages
    ```
    pip install -r requirements.txt
    ```
1. Run the flask application
    ```
    python app.py
    ```

## Run in Docker container
Run the below commands under 

1. Build an Image
    ```
    docker build -t housepred:v1 .
    ```
2. Run the container
    ```
    docker run -p 8080:8080 -n housepredapp housepred:v1
    ```

## Validation
After the service is running successfully, run the below command in terminal.

```
curl -H "Content-Type: application/json" -d "{\"rm\": 6.5,\"lstst\":9.14, \"ptratio\":20.1}" -X POST http://localhost:8080/predict
```
