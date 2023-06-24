# ----------------------------------------------------- #
#          Code by A. Razquin, April 29 2023            #
#                amaiafisika@gmail.com                  #
# It runs the Optuna hypermarameter optimizer in Python #
# for optimizing a C++ program without Python bindings  #
# ----------------------------------------------------- #

import optuna 
import sys
import logging
import subprocess

from optuna.visualization import plot_contour
from optuna.visualization import plot_edf
from optuna.visualization import plot_intermediate_values
from optuna.visualization import plot_optimization_history
from optuna.visualization import plot_parallel_coordinate
from optuna.visualization import plot_param_importances
from optuna.visualization import plot_slice

def objective(trial):
    # Trial: single execution of the objective function
    # Suggest call parameters uniformly within the range 
    x = trial.suggest_float('x', -10, 10)
    y = trial.suggest_int('y', 10, 100, step=5)
    p = subprocess.Popen(["./test.x", str(x), str(y)], stderr=subprocess.PIPE, 
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    FuncValue = float(p.stdout.readline())
    print(FuncValue, x)
    return FuncValue

# Add stream handler of stdout to show the messages
optuna.logging.get_logger("optuna").addHandler(logging.StreamHandler(sys.stdout))

# Create the study object (an optimization session = set of trials)
study = optuna.create_study(study_name='Test-study',
                            direction='maximize', 
                            sampler=optuna.samplers.TPESampler(),
                            pruner=optuna.pruners.HyperbandPruner(),
                            storage='sqlite:///test.db',
                            load_if_exists=True)
# Pass the objective function method
study.optimize(objective, n_trials=100, timeout=60) #timeout in seconds

# Get the best parameter
found_params = study.best_params
found_value  = study.best_value
found_trial  = study.best_trial

# Visualization options 
# fig = optuna.visualization.plot_optimization_history(study)
# fig = optuna.visualization.plot_parallel_coordinate(study)
# fig = optuna.visualization.plot_contour(study) (doesn't work)
# fig = optuna.visualization.plot_slice(study)
# fig = optuna.visualization.plot_param_importances(study)
# fig = optuna.visualization.plot_edf(study)
# fig.show()

#https://adambaskerville.github.io/posts/PythonSubprocess/
