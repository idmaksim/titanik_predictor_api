# Simple survival predictor
## Info
This model predicts survival on titanik by your data

This model was trained on this dataset: https://www.kaggle.com/datasets/yasserh/titanic-dataset

## to run this project you need:
 - install requirements from requirements.txt
 - dev or release mode: fastapi [dev or run] src/app.py --reload --port 8090
## or
- install docker
- cmd: docker build -t [name of your image] .
- cmd: docker run -p [port:port] -d [optional if you dont need to see logs] --name [name of your container] [name of image]
