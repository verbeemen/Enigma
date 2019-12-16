import numpy as np

class Rotor:
    def __init__(self, version, start_letter):
        
        # parameters
        self.version = None
        self.notch_raw = None
        self.notch = None
        self.wiring_raw = None
        self.wiring = None
        self.start_letter = None
        self.rotor_letter = None
        self.start_letter_raw = None
        
        # initialize the rotor
        self._initialize(version, start_letter)

    def _initialize(self, version, start_letter):
        """
        Initialize a rotor.
        
        Parameters:
        version: Version of an existing rotor
        start_leter: which letter should be put on top
        """
        if version in {1, 'I'}:
            self.version = 'I'
            self.wiring_raw = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
            self.notch_raw = {'R'}
            
        elif version in {2, 'II'}:
            self.version = 'II'
            self.wiring_raw = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
            self.notch_raw = {'F'}
            
        elif version in {3, 'III'}:
            self.version = 'III'
            self.wiring_raw = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
            self.notch_raw = {'W'}
            
        elif version in {4, 'IV'}:
            self.version = 'IV'
            self.wiring_raw = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
            self.notch_raw = {'K'}
            
        elif version in {5, 'V'}:
            self.version = 'V'
            self.wiring_raw = 'VZBRGITYUPSDNHLXAWMJQOFECK'
            self.notch_raw = {'A'}
            
        elif version in {6, 'VI'}:
            self.version = 'VI'
            self.wiring_raw = 'JPGVOUMFYQBENHZRDKASXLICTW'
            self.notch_raw = {'A', 'N'}
            
        elif version in {7, 'VII'}:
            self.version = 'VII'
            self.wiring_raw = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
            self.notch_raw = {'A', 'N'}
            
        elif version in {8, 'VIII'}:
            self.version = 'VIII'
            self.wiring_raw = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'
            self.notch_raw = {'A', 'N'}
            
        try:    
            # translate the notches to an integer [0-25]
            self.notch = {ord(notch) - 65 for notch in self.notch_raw}
            
            # create the wiring
            self.wiring = np.zeros((26,2), dtype=np.int8)
            for e, letter in enumerate(list(self.wiring_raw)):
                letter = ord(letter)-65
                self.wiring[e][0] = letter - e
                self.wiring[letter][1] = e - letter
                
            # move the rotor
            self.start_letter_raw = start_letter.upper()
            self.start_letter = ord(self.start_letter_raw) - 65
            self.rotor_letter = self.start_letter 
            self.wiring = np.roll(self.wiring, -self.start_letter, axis= 0)
            
        except Exception as e:
            print(f'err ¯\_(ツ)_/¯ {e}')
        
    def set_rotor(start_letter):
        self._initialize(self.version, start_letter)
        
    def get_wiring(self):
        return self.wiring
        
    def get_version(self):
        print(f"Rotor version: {self.version}")
        
    def get_notch(self):
        return self.notch
    
    def get_letter_rotor(self):
        return self.rotor_letter
    
    def get_letter_forward(self, index):
        return ( index + self.wiring[index][0] ) % 26
    
    def get_letter_backward(self, index):
        return ( index + self.wiring[index][1] ) % 26
        
    def must_rotate(self):
        return self.rotor_letter in self.notch
        
    def rotate(self):
        self.wiring = np.roll(self.wiring, -1, axis= 0)
        self.rotor_letter = (self.rotor_letter + 1) % 26
