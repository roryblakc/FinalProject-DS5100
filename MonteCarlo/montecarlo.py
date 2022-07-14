import numpy as np
import pandas as pd
import random

class Die:
    '''Create a Die object to then be able to change the weight of any faces and simulate rolling the die. Object is initialized with the input of an array of faces.'''
    def __init__(self, faces):
        self.faces = faces
        self.weights = np.ones(len(faces))
        self.die_df = pd.DataFrame({
            'face': self.faces,
            'weight': self.weights})
        
    def change_weight(self, face, weight):
        '''Allows the user to change the weight for any face of a Die object. Input parameters are a face and changed weight. Returns nothing.'''
        if face in self.faces:
            # index to weight for index of face
            # change weight
            if type(weight) == float or type(weight) == int:
                weight = float(weight)
                index = np.where(self.faces == face)
                self.weights[index] = weight
                # update df with new weight
                self.die_df['weight'] = self.weights 
            else:
                return("The weight needs to entered as a number.")
        else:
            return("This is not a valid face.")
        
    def roll(self, num_rolls=1):
        '''Allows user to simulate rolling a single die. Input parameter is how many rolls. Returns the list of faces produced on all rolls.'''
        rolls_list = random.choices(self.faces, weights=self.weights, k=num_rolls)
        return rolls_list
    
    def show_current(self):
        '''Returns a dataframe with the current faces and corresponding weights of a Die object.'''
        return self.die_df
    
class Game:
    '''Create a Game object from a list of one or more Die objects of the same kind to simulate rolling multiple dice.'''
    # all die in die list must have same faces
    def __init__(self, die_list):
        self.die_list = die_list
    
    def play(self, num_rolls):
        '''Allows user to simulate rolling multiple dice at once. Input parameter is the number of rolls as an int. No return value.'''
        self._play_df = pd.DataFrame()
        # iterate through die and append rolls to df
        for die in self.die_list:
            die_rolls = die.roll(num_rolls)
            die_rolls = pd.Series(die_rolls)
            self._play_df = pd.concat([self._play_df, die_rolls], axis=1)
        # name columns with die number
        dice_number = range(1, len(self.die_list)+1)
        # list to rename columns in df with "Die __" format
        self.column_names = ["Die " + str(d) for d in dice_number]
        self._play_df.columns = self.column_names
        # name rows with roll number
        roll_number = range(1, num_rolls+1)
        # loop to rename rows in df with "Roll __" format
        self.row_names = ["Roll # " + str(r) for r in roll_number]
        self._play_df.index = self.row_names
    
    def show_play(self, form='wide'):
        '''Allows user to see results of the .play() method as a dataframe. Input parameter is either "wide" or "narrow". Returns a dataframe in the correct format.'''
        # exception if user does not pass wide or narrow
        form = form.lower()
        try:
            if form == 'wide':
                return(self._play_df)
            elif form == 'narrow':
                narrow_df = self._play_df.stack()
                narrow_df = pd.DataFrame(narrow_df)
                narrow_df.columns = ['Face Returned']
                return(narrow_df)
        except:
            print('Must specify either "wide" or "narrow".')
        
class Analyzer:
    '''Create an Analyzer object to reveal information about a Game object. Object is initialized with the input of an existing Game object.'''
    def __init__(self, game):
        self.game = game
        self.face_dtype = type(self.game.die_list[0].faces[0])
        
    def jackpot(self):
        '''Allows user to see how many rolls resulted in all die returning the same face. The number of jackpots among all rolls is returned as an integer.'''
        # returns number of jackpots
        self.num_jackpots = 0
        # empty df for jackpots by roll
        self.jackpot_df = pd.DataFrame(index = self.game.row_names, columns = ['Jackpot'])
        # if only one value returned for all dice same roll, jackpot
        for i in range(len(self.game._play_df.index)):
            if (len(self.game._play_df.iloc[i].value_counts()) == 1):
                # add true to df for roll #
                self.jackpot_df.iat[i, 0] = True
                # increment num_jackpots by 1
                self.num_jackpots += 1
            else:
                # add false to df for roll #
                self.jackpot_df.iat[i, 0] = False
        return self.num_jackpots
    
    def combo(self):
        '''Allows user to view the counts for each combination of faces returned each roll. No return value, but .combo_df is an accessible attribute of any instance.'''
        # make multi-index df of combo counts
        self.combo_df = pd.DataFrame(self.game._play_df.groupby(self.game.column_names).size())
        self.combo_df.columns = ['Counts']
        
    def face_counts_per_roll(self):
        '''Allows user to view the counts of which faces were returned with each roll. No return value, but .face_counts_df is an accessible attribute of any instance.'''
        self.face_counts_df = pd.DataFrame()
        # append rolls row by row
        for x in self.game.row_names:
            self.face_counts_df = pd.concat([self.face_counts_df, self.game._play_df.T[x].value_counts()], axis=1)
        # fill all nan values with 0 and make all values ints
        self.face_counts_df = self.face_counts_df.fillna(0)
        self.face_counts_df = self.face_counts_df.astype(int)
        # transpose to make columns = faces, rows = roll #
        self.face_counts_df = self.face_counts_df.T

            
            
        
        
    
    
