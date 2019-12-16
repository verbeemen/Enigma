import numpy as np

class Reflector:
    def __init__(self, version):
        
        # parameters
        self.version = None
        self.wiring_raw = None
        self.wiring = None
        
        # initialize the rotor
        self._initialize(version)

    def _initialize(self, version):
        if version in {'Beta'}:
            self.version = 'Beta'
            self.wiring_raw = 'LEYJVCNIXWPBQMDRTAKZGFUHOS'
            
        elif version in {'Gamma'}:
            self.version = 'Gamma'
            self.wiring_raw = 'FSOKANUERHMBTIYCWLQPZXVGJD'
            
        elif version in {'A'}:
            self.version = 'A'
            self.wiring_raw = 'EJMZALYXVBWFCRQUONTSPIKHGD'
            
        elif version in {'B'}:
            self.version = 'B'
            self.wiring_raw = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
            
        elif version in {'C'}:
            self.version = 'C'
            self.wiring_raw = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
            
        elif version in {'B Thin'}:
            self.version = 'B Thin'
            self.wiring_raw = 'ENKQAUYWJICOPBLMDXZVFTHRGS'
            
        elif version in {'C Thin'}:
            self.version = 'C Thin'
            self.wiring_raw = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'
            
        elif version in {'ETW'}:
            self.version = 'ETW'
            self.wiring_raw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            
        try:    
            self.wiring = np.array([ ord(letter) - 65 - e for e, letter in enumerate(list(self.wiring_raw))])
        except Exception as e:
            print(f'err ¯\_(ツ)_/¯ {e}')

    def get_wiring(self):
        return self.wiring
        
    def get_version(self):
        print(f"Reflector version: {self.version}")
       
    def get_letter(self, index):
        return ( index + self.wiring[index] ) % 26