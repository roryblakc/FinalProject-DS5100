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

### Die Class
`Die(faces)`  
* Input parameter: A numpy array of die faces.  
* Defaults to a weight of 1 for all faces.

#### Attributes
* `.faces` -- the array of faces
* `.weights` -- an array of weights
* `.die_df` -- a dataframe containing faces and corresponding weights

#### Methods
* `change_weight(face, weight)`
  * Change the weight of any face. No return value.
* `roll(num_rolls=1)`
  * Simulate rolling the die. Defaults to 1 roll. Returns the list of rolls.
* `show_current()`
  * View the dataframe with the current faces and corresponding weights.


Example:  
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


### Game Class
`Game(die_list)`  
* Input parameter: A list of one or more Die objects built from the same array of faces. May contain differently weighted faces.  

#### Attributes
* `.die_list` -- the list of Die objects
* `._play_df` -- protected dataframe of all rolls upon calling the `play()` method

#### Methods
* `play(num_rolls)`
  * Simulate rolling a list of dice one or more times. No return value, but results are stored in dataframe.
* `show_play(form="wide")`
  * Returns a dataframe displaying the results of the `play()` method. The user can specify either 'wide' or 'narrow'. Defaults to 'wide'.

Example:  
`# create a game of 3 6-sided die`  
`die_list = [die, die, die]`  
`game = Game(die_list)`  
`game.play(5)`  
`game.show_play()`
|          | Die 1   | Die 2   | Die 3   |
| -------- | ------- | ------- | ------- |
| Roll # 1 | 1       | 6       | 3       |
| Roll # 2 | 2       | 5       | 3       |
| Roll # 3 | 1       | 1       | 1       |
| Roll # 4 | 4       | 2       | 4       |
| Roll # 5 | 6       | 3       | 5       |


### Analyzer Class
`Analyzer(game)`  
* Input parameter: A Game object.

Example:  
`# create an analyzer with the Game object instantiated above.`  
`analyzer = Analyzer(game)`


