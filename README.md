# Metadata
* Name:        Rory Black
* Project:     Monte Carlo Simulator
* Course:      DS 5100
* Description: Implementation of a simple Monte Carlo simulator using a set of related classes.

# Synopsis
The Monte Carlo simulator is comprised of three classes: **Die**, **Game**, **Analyzer**.

## Installing and Importing
To install the package, navigate to the root of this directory. Execute the code below.
* `pip install -e .`  

Instalation is successful if you are returned the following line.  
"Successfully installed MonteCarloPackage"

To import each class, execute the code below. All methods from all three classes will be accessible upon importing the classes.
* `from montecarlo import Die`
* `from montecarlo import Game`
* `from montecarlo import Analyzer`

## Using the Classes
To create an instance of each of the class objects, follow the instructions below.

### Die Class Demo

`# create a standard 6-sided die`   
`faces = np.array([1, 2, 3, 4, 5, 6])`  
`die = Die(faces)`  
`die.change_weight(1, 2)`  
`die.roll(3)`  
[1, 4, 1]  
`die.show_current()`  
| Face  | Weight |
| ----- | ------ |
| 1     | 2      |
| 2     | 1      |
| 3     | 1      |
| 4     | 1      |
| 5     | 1      |
| 6     | 1      |


### Game Class Demo

`# create a game of 3 6-sided die`  
`die_list = [die, die, die]`  
`game = Game(die_list)`  
`game.play(3)`  
`game.show_play()`
|          | Die 1   | Die 2   | Die 3   |
| -------- | ------- | ------- | ------- |
| Roll # 1 | 1       | 6       | 3       |
| Roll # 2 | 2       | 5       | 3       |
| Roll # 3 | 1       | 1       | 1       |

`game.show_play('narrow')`  
|          |         | Face Returned |
| -------- | ------- | ------------- |
| Roll # 1 | Die 1   | 1             |
|          | Die 2   | 6             |
|          | Die 3   | 3             |
| Roll # 2 | Die 1   | 2             |
|          | Die 2   | 5             |
|          | Die 3   | 3             |
| Roll # 3 | Die 1   | 1             |
|          | Die 2   | 1             |
|          | Die 3   | 1             |



### Analyzer Class Demo

`# create an analyzer with the Game object instantiated above.`  
`analyzer = Analyzer(game)`  
`analyzer.jackpot()`  
1  
`analyzer.jackpot_df`  
|          | Jackpot |
| -------- | ------- |
| Roll # 1 | False   |
| Roll # 2 | False   |
| Roll # 3 | True    |

`analyzer.combo()`  
`analyzer.combo_df`  

|          |         |         | Counts   |
| -------- | ------- | ------- | -------- |
|  Die 1   | Die 2   | Die 3   |          |
|  1       | 1       | 1       | 1        |
|          | 6       | 3       | 1        |
|  2       | 5       | 3       | 1        |

`analyzer.face_counts_per_roll()`  
`analyzer.face_counts_df`  

|          | 1    | 2    | 3    | 4    | 5    | 6    |
| -------- | ---- | ---- | ---- | ---- | ---- | ---- |
| Roll # 1 | 2    | 1    | 0    | 0    | 0    | 0    |
| Roll # 2 | 1    | 0    | 0    | 0    | 1    | 1    |
| Roll # 3 | 1    | 0    | 2    | 0    | 0    | 0    |


# API Description  

## Die Class  
`Die(faces)`  

### Documentation
* Create a Die object to then be able to change the weight of any faces and simulate rolling the die. Object is initialized with the input of an array of faces.  

### Parameter  
* A numpy array of die faces.  
  * Defaults to a weight of 1 for all faces.

### Methods
* `__init__(faces)`  
  * Create a Die object with input parameter of an array of faces. Weights default to 1 for every face. No return value.
* `change_weight(face, weight)`
  * Change the weight of any face. No return value.
* `roll(num_rolls=1)`
  * Simulate rolling the die. Defaults to 1 roll. Returns the list of rolls.
* `show_current()`
  * View the dataframe with the current faces and corresponding weights.  

### Attributes  
* `.faces` -- the array of faces
* `.weights` -- an array of weights
* `.die_df` -- a dataframe containing faces and corresponding weights 


## Game Class
`Game(die_list)` 

### Documentation
* Create a Game object from a list of one or more Die objects of the same kind to simulate rolling multiple dice.

### Parameter  
* A list of one or more Die objects built from the same array of faces. May contain differently weighted faces.  

### Methods
* `__init__(die_list)`
  * Create a Game object from a list of one or more Die objects of the same kind to simulate rolling multiple dice.
* `play(num_rolls)`
  * Simulate rolling a list of dice one or more times. No return value, but results are stored in dataframe.
* `show_play(form="wide")`
  * Returns a dataframe displaying the results of the `play()` method. The user can specify either 'wide' or 'narrow'. Defaults to 'wide'.

### Attributes
* `.die_list` -- the list of Die objects


## Analyzer Class
`Analyzer(game)`  

### Documentation 
* Create an Analyzer object to reveal information about a Game object. Object is initialized with the input of an existing Game object.

### Parameter
* A Game object.

### Methods
* `__init(game)`
  * Create an Analyzer object to reveal information about a Game object. Object is initialized with the input of an existing Game object.
* `jackpot()`
  * Evaluate how many rolls returned the same face for all dice. Returns an integer of the number of jackpots.  
* `combo()`
  * Evaluate the counts of combinations of rolls and faces returned. No return value.  
* `face_counts_per_roll()`
  * Evaluate which faces are returned with each roll. No return value.

### Attributes
* `.game` -- the Game object from which the Analyzer object was constructed
* `.face_dtype` -- the data type of the faces of the list of die  
* `.num_jackpots` -- the number of jackpots counted upon calling the `jackpot()` method
* `.jackpot_df` -- a dataframe containing booleans indicated whether or not a single roll resulted in a jackpot
* `.combo_df` -- a dataframe displaying the counts of each combination of rolls upon calling the `.combo()` method
* `.face_counts_df` -- a dataframe displaying the counts of each face appearing with each roll upon calling the `.face_counts_per_roll()` method


# Manifest

Below is the structure of the files within this repo.

* MonteCarlo  
  * __init__.py  
  * montecarlo.py  
* .gitignore  
* FinalProjectSubmission.ipynb
* LICENSE  
* README.md  
* montecarlo_demo.ipynb  
* montecarlo_results.txt  
* setup.py  


