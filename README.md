# Metadata
* Name:        Rory Black
* Project:     Monte Carlo Simulator
* Course:      DS 5100
* Description: Implementation of a simple Monte Carlo simulator using a set of related classes.

# Synopsis
The Monte Carlo simulator is comprised of three classes: **Die**, **Game**, **Analyzer**.

## Installing and Importing
To install the package, navigate to head directory. Execute the code below.
* `pip install -e .`  

Instalation is successful if you are returned the following line.  
"Successfully installed MonteCarloPackage"

To import each class, execute the code below. All methods from all three classes will be accessible upon importing the classes.
* `from montecarlo import Die`
* `from montecarlo import Game`
* `from montecarlo import Analyzer`

## Classes
To create an instance of each of the class objects, follow the instructions below.

### Die Class
* Input parameter: A numpy array of die faces.

Example:
`# create a standard 6-sided die`
`faces = np.array([1, 2, 3, 4, 5, 6])`
`die = Die(faces)`


