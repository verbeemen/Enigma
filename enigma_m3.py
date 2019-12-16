import numpy as np
from rotor import Rotor
from reflector import Reflector

class EnigmaM3:
    def __init__(self):
        self.reflector = None
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None
        self.steckerboard = {}
    
    #-------#
    # Slots #
    #-------#
    def set_slot_1(self, rotor):
        self.slot_1 = rotor

    def get_rotor_slot_1(self):
        return self.slot_1
        
    def set_slot_2(self, rotor):
        self.slot_2 = rotor
        
    def get_rotor_slot_2(self):
        return self.slot_2
    
    def set_slot_3(self, rotor):
        self.slot_3 = rotor
        
    def get_rotor_slot_3(self):
        return self.slot_3
    
    #-----------#
    # Reflector #
    #-----------#
    def set_reflector(self, reflector):
        self.reflector = reflector

    def get_reflector(self):
        return self.reflector
       
    #--------------#
    # Steckerboard #
    #--------------#
    def _set_steckerboard(self, steckers):
        
        # set the steckers
        self.steckerboard = {}
        for stecker in steckers:
            self.steckerboard[stecker[0]] = stecker[1]
            self.steckerboard[stecker[1]] = stecker[0]
    
    def set_steckerboard(self, steckers = np.array([])):
        """
            - a list of tuples like: - [(0,1), (24,25), (13,14)]
                                     - [[0,1], [24,25], [13,14]]
                                     - np.random.choice(26, (10,2), replace=False)'
        """
        self._set_steckerboard(steckers)
    
    def set_steckerboard_char(self, steckers = np.array([])):
        """
         - a list of tuple characters like '[("a","b"), ("x","z"), ("m","n")]'
        """
        # if we use characters then we convert the characters to numbers
        if len(steckers) > 0:
            steckers = np.vectorize( lambda x: ord(x.upper())-65 )(np.array(steckers))
            self._set_steckerboard(steckers)
        else:
            self._set_steckerboard([])
        
    def get_steckerboard(self):
        return self.steckerboard
    
    #-----------------#
    # Encode | Decode #
    #-----------------#
    
    def get_letter(self, letter):
        letter = ord(letter.upper())-65

        # steckerboard
        letter = self.steckerboard.get(letter,letter)

        # righter disk
        self.slot_3.rotate()
        letter = self.slot_3.get_letter_forward(letter)
        
        # middle disk
        if self.slot_3.must_rotate():
            self.slot_2.rotate()
        letter = self.slot_2.get_letter_forward(letter)
        
        # left disk
        if self.slot_2.must_rotate():
            self.slot_1.rotate()
        letter = self.slot_1.get_letter_forward(letter)
        
        # reflector
        letter = self.reflector.get_letter(letter)
        
        # back prop
        letter = self.slot_1.get_letter_backward(letter)
        letter = self.slot_2.get_letter_backward(letter)
        letter = self.slot_3.get_letter_backward(letter)

        #steckerboard
        letter = self.steckerboard.get(letter,letter)
            
        return chr(letter+65)
    
    def get_code(self, input):
        # execute get_letter for each letter 
        return ''.join([self.get_letter(l) for l in list(input)])