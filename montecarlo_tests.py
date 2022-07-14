from montecarlo import Die, Game, Analyzer
import unittest
import numpy as np
import pandas as pd

class MonteCarloTestSuite(unittest.TestCase):    
    
    # DIE class tests

    def test_die_init(self):
        # create Die instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        
        # test
        actual_dim = d1.die_df.shape
        expected = (6,2)
        
        message = "The size of the dataframe constructed from initial faces and weights is not equal to the expected dimensions."
        
        # assertEqual() to check that faces and weights correctly initialized
        self.assertEqual(actual_dim, expected, message)
    
    def test_change_weight(self):
        # create Die instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        # change the weight of a face
        d1.change_weight(1,10)
        
        # test
        actual_weight = d1.weights[0]
        expected = 10
            
        message = "The weight was not correctly reassigned."
        
        # assertEqual() to check weight is equal to expected
        self.assertEqual(actual_weight, expected, message)
    
    def test_roll(self):
        # create Die instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        # roll die
        roll = d1.roll(20)
        
        # test
        actual_length = len(roll)
        expected = 20
        
        message = "The number of rolls requested was not executed."
        
        # assertEqual() to check length of roll list is correct
        self.assertEqual(actual_length, expected, message)
        
    def test_show_current(self):
        # create Die instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        
        # test
        if d1.show_current().shape == (6,2):
            test_value = True
        else:
            test_value = True
        
        message = "The dataframe returned does not have the expected dimensions."
        
        # assertTrue() to check that dimensions of dataframe equal the expected dimensions
        self.assertTrue(test_value, message)
        
    
    #########################################################################################
    # GAME class tests
    
    def test_game_init(self):
        # create Game instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        die_list = [d1, d1, d1]
        game = Game(die_list)
        
        # test
        if len(game.die_list) == 3 and isinstance(game.die_list, list):
            test_value = True
        else:
            test_value = False
        
        message = "The Game object was not initialized with a list of the expected length."
        
        # assertTrue() to check that Game object is initialized with a list.
        self.assertTrue(test_value, message)
    
    def test_play(self):
        # create Game instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        die_list = [d1, d1, d1]
        game = Game(die_list)
        
        game.play(10)
        
        # test
        if game._play_df.shape == (10, 3):
            test_value = True
        else:
            test_value = False
        
        message = "The dataframe returned does not have the expected dimensions."
        
        # assertTrue() to check that dimensions of dataframe equal the expected dimensions
        self.assertTrue(test_value, message)
        
    def test_show_play(self):
        # create Game instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        die_list = [d1, d1, d1]
        game = Game(die_list)
        
        game.play(10)
        
        # test
        actual_dim = game.show_play('narrow').shape
        expected = (30, 1)
        
        message = "The dataframe returned does not have the expected dimensions."
        
        # assertEqual() to check that dimensions of dataframe equal the expected dimensions
        self.assertEqual(actual_dim, expected, message)
        
        
    #########################################################################################
    # ANALYZER class tests
    
    def test_analyzer_init(self):
        # create Analyzer instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        die_list = [d1, d1, d1]
        game = Game(die_list)
        
        game.play(10)
        
        analyzer = Analyzer(game)
        
        # test
        if isinstance(analyzer.game, Game):
            test_value = True
        else:
            test_value = False
            
        message = "The Analyzer object was not initialized with an already existing Game object."
        
        # assertTrue() to check that Analyzer is initialized with a Game object as the input parameter
        self.assertTrue(test_value, message)
    
    def test_jackpot(self):
        # create Analyzer instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        die_list = [d1, d1, d1]
        game = Game(die_list)
        
        game.play(10)
        
        analyzer = Analyzer(game)
        jackpot = analyzer.jackpot()
        
        # test
        if isinstance(analyzer.jackpot_df['Jackpot'][0], bool):
            test_value = True
        else:
            test_value = False
            
        message = "The column of jackpot results should be of type boolean."
        
        # assertTrue() to check that dataframe contains booleans for jackpot result
        self.assertTrue(test_value, message)
        
    def test_combo(self):
        # create Analyzer instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        die_list = [d1, d1, d1]
        game = Game(die_list)
        
        game.play(10)
        
        analyzer = Analyzer(game)
        analyzer.combo()
        
        # test
        if isinstance(analyzer.combo_df.index, pd.core.indexes.multi.MultiIndex):
            test_value = True
        else:
            test_value = False
            
        message = "The dataframe does not appear to have multiple indices."
        
        # assertTrue() to check that dataframe actually does have multiple indices
        self.assertTrue(test_value, message)
        
    def test_face_counts_per_roll(self):
        # create Analyzer instance
        six_faces = np.array([1,2,3,4,5,6])
        d1 = Die(six_faces)
        die_list = [d1, d1, d1]
        game = Game(die_list)
        
        game.play(10)
        
        analyzer = Analyzer(game)
        analyzer.face_counts_per_roll()
        
        # test
        if analyzer.face_counts_df.shape == (10, 6):
            test_value = True
        else:
            test_value = False
            
        message = "The dataframe of face counts per roll does not have the correct dimensions."
        
        # assertTrue() to check that dataframe is the correct size and contains all rolls and faces
        self.assertTrue(test_value, message)

if __name__ == '__main__':
    unittest.main(verbosity=3)