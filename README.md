
## Intro
The dataset is the cross-sell dataset for Insurance product downloaded from Kaggle - link [here](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction). Our challenge is to build a binary classification model that predicts whether a customer is going to buy a complementary product.

*The components of our Machine Learning project are as follow:*

- **Data Engineering:**
For simplicity, we develop our model locally and then push it to production to predict on new data. In practice, we should have a data repository that can record new data for continual learning and improvement of the model.

- **Exploratory data analysis**
We use jupyter notebook to analyze, visualize and perform some preliminary data transformation.

- **Data Modeling**
We build a baseline model and experiment with two different automl tools: PyCaret and H2O automl.All experiments are tracked with Mlflow. The best model is chosen for deployment


- **ML Implementation**
Deploy the trained model to backend. We build our backend using FastAPI and frontend using Streamlit. The app is dockerized for easy deployment on cloud services (if needed).

____
## Demo Instruction
To check out the app, download folder 'app' and run 'docker-compose up' in the directory.
