# cpp-optuna
Run [Optuna](https://optuna.org/) hyperparameter optimization software for a C++ program without Python bindings.

The program [cpp-optuna.py](https://github.com/arazquinliz/optuna-cpp/blob/main/cpp-optuna.py) runs a Optuna hyperparameter optimization run to optimize the arguments for a C++ program, [test.cpp](https://github.com/arazquinliz/optuna-cpp/blob/main/test.cpp). 

## Usage
The C++ code has to be compiled beforehand separately to create the executable and must only contain a single IO line with the score function result to be optimized: 

```g++ test.cpp -o test.x```

To run the optimization process use:

```python3 cpp-optuna.py```

The trials, runtime, and parameter ranges can be tuned within cpp-optuna.py. The number of parameters to be optimized should be simultaneously considered in both the .cpp and .py files.

## Requirements
Optuna 3.1 or newer

## Note
More elegant ways of using Optuna for C++ exist (see [this binding](https://github.com/not522/optuna-cpp)), but this code offers a simple option with no Python bindings. It is not recommended for computationally heavy C++ algorithms. By changing the .py file other optimization software could also be used. 

## LICENSE 
Apache License 2.0

----------------------------------
Date: April 29 2023
