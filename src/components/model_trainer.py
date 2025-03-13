#TRAINING OF THE MODEL 

import os 
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn .ensemble import RandomForestRegressor, AdaBoostRegressor,GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# ✅ Use R² Score for:
# ✔️ Regression Models (Linear Regression, Decision Trees, Random Forests, etc.)
# ✔️ Measuring Model Performance (Higher R² means a better model)

# ❌ Do NOT use R² Score for:
# ✖️ Classification Models (e.g., Logistic Regression, Decision Trees for classification)
# ✖️ Evaluating Individual Predictions (Better for overall model assessment)

from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models 

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
@dataclass
class TrainerConfig:
    trained_model_file_path: str = os.path.join(ROOT_DIR, "artifact", "trained_model.pkl")

class ModelTrainer:
    def __init__(self):
        self.TrainerConfig = TrainerConfig()
    
    def initiate_model_trainer(self, train_data,test_data):
        try:
            logging.info("Initiating Model Training")
            logging.info("Splitting X_train,Y_train,X_test,Y_test")
            X_train,y_train,X_test,y_test=(
                train_data[:,:-1],
                train_data[:,-1],
                test_data[:,:-1],
                test_data[:,-1]  
            )
            logging.info("Listing Models")
            models= {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "KNN": KNeighborsRegressor(),
                "XGBoost": XGBRegressor(),
                "CatBoost": CatBoostRegressor(),
                "AdaBoost": AdaBoostRegressor()
            }

            logging.info("Listing Parameters")
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,256]
                },
                "Linear Regression":{
                    'copy_X':[True,False],
                    'fit_intercept':[True,False],
                    'positive':[True,False],
                },
                "XGBoost":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,256]
                },
                "CatBoost":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 100]
                },
                "AdaBoost":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,256]
                },
                "KNN":{
                    'n_neighbors': [3, 5, 7, 9],
                    'weights': ['uniform', 'distance'],
                    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
                }
            }

            model_report:dict = evaluate_models(X_train,y_train,X_test,y_test,models=models,params=params)
            print(model_report)

            best_model = max(model_report,key=lambda x: model_report[x]["test_score"])
            best_model_instance = models[best_model]
            best_model_score = model_report[best_model]
            logging.info(f"Best Model: {best_model}")
            print(best_model_instance,best_model,best_model_score)

            if best_model_score["test_score"] < 0.6:
                logging.error("Model Score is less than 0.6")
                raise CustomException("Model Score is less than 0.6",sys)
            
            save_object(
                file_path=self.TrainerConfig.trained_model_file_path,
                obj=best_model_instance
            )

            y_pred = best_model_instance.predict(X_test)
            r2 = r2_score(y_test,y_pred)
            logging.info(f"R2 Score: {r2}")
            print(f"R2 Score: {r2}")
            logging.info("Model Training Completed")   
            return best_model,r2 



        except Exception as e:
            raise CustomException(e,sys)
        
    


