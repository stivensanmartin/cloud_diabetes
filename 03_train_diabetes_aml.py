# 04-run-pytorch.py
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig

if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml', _file_name='config.json')
    experiment = Experiment(workspace=ws, name='day1-experiment-train-diabetes')
    config = ScriptRunConfig(source_directory='./src',
                             script='train_diabetes_remote.py',
                             compute_target='cpu-cluster-udea')

    # set up pytorch environment
    env = Environment.from_conda_specification(
        name='diabetes-env',
        file_path='./.azureml/diabetes-aml-env.yml'
    )
    config.run_config.environment = env

    run = experiment.submit(config)

    aml_url = run.get_portal_url()
    print(aml_url)