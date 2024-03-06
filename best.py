import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("liver_patient_register")

all_runs = mlflow.search_runs(search_all_experiments=True)
sorted_df = all_runs.sort_values(by=['metrics.test_rmse'], ascending=[True])

