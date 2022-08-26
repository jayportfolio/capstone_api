# capstone_api


### To run the fastapi api:
* uvicorn api.main:app



### Curl testing commands
* http://127.0.0.1:8000/
* curl -X GET http://127.0.0.1:8000/hello/everybody
* curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[0]]}"
* curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[0,1,2,3,4,5,6,7,8]]}"