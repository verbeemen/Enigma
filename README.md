# Enigma M3
The Enigma machine is an encryption device developed and used in the early- to mid-20th century to protect commercial, diplomatic and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military.

Enigma has an electromechanical rotor mechanism that scrambles the 26 letters of the alphabet. In typical use, one person enters text on the Enigma's keyboard and another person writes down which of 26 lights above the keyboard lights up at each key press. If plain text is entered, the lit-up letters are the encoded ciphertext. Entering ciphertext transforms it back into readable plaintext. The rotor mechanism changes the electrical connections between the keys and the lights with each keypress. The security of the system depends on Enigma machine settings that were changed daily, based on secret key lists distributed in advance, and on other settings that change for each message. The receiving station has to know and use the exact settings employed by the transmitting station to successfully decrypt a message.

As used in practice, the Enigma encryption proved vulnerable to cryptanalytic attacks by Germany's adversaries, at first Polish and French intelligence and, later, a massive effort mounted by the United Kingdom at Bletchley Park as part of the Ultra program. While Germany introduced a series of improvements to Enigma, and these hampered decryption efforts to varying degrees, they did not ultimately prevent Britain and its allies from exploiting Enigma-encoded messages as a major source of intelligence during the war. Many commentators say the flow of communications intelligence from Ultra's decryption of Enigma, Lorenz and other ciphers shortened the war significantly and may even have altered its outcome

## Sources
 - [https://en.wikipedia.org/wiki/Enigma_machine](https://en.wikipedia.org/wiki/Enigma_machine)
 - [http://users.telenet.be/d.rijmenants/en/enigmatech.htm](http://users.telenet.be/d.rijmenants/en/enigmatech.htm)
 - [https://www.cryptool.org/en/cto-ciphers/enigma](https://www.cryptool.org/en/cto-ciphers/enigma)
 
# Load packages


```python
# update objects|classes when we write code
%load_ext autoreload
%autoreload 2

# load packages
from enigma_m3 import Rotor
from enigma_m3 import Reflector
from enigma_m3 import EnigmaM3
import numpy as np
```

# Create Enigma Machines

How does it work?

 1) Create an enigma machine  
 2) Encode your message
 
 
![](https://waaromwiskunde.files.wordpress.com/2013/06/wiringdiagram.png)

## Encode
Encode the alphabet 


```python
# Create an enigma machine
enigma_m3 = EnigmaM3()

# Set the rotors
## A rotor contains out: 
### A version (1-8) 
### A start letter (A-Z) (the start letter is the visible letter on the rotor)

enigma_m3.set_slot_1( Rotor(version = 8, start_letter = 'L') ) # Left rotor
enigma_m3.set_slot_2( Rotor(version = 7, start_letter = 'S') ) # Middle rotor
enigma_m3.set_slot_3( Rotor(version = 6, start_letter = 'K') ) # Right rotor

# set the reflector
## There are different versions of Refectors, the most common of the Enigma M3 is B
enigma_m3.set_reflector(Reflector(version = 'B'))

# set the steckerboard
enigma_m3.set_steckerboard_char([('a','b'), ('x','y'), ('m','n')])

# encode the message
enigma_m3.get_code('ABCDEFGHIJKLMNOPQRSTUVWXYZ'*3)
```




    'NXQUPHXBYXMCKWROBQKAGZCAHFFADKOGKEPLJMPMDCAQOAQPSVPBJKDKYHREPAXDPAMALKYBBMPCQJ'



## Decode
Decode the previous message


```python
# Create an enigma machine
enigma_m3 = EnigmaM3()

# Set the rotors
enigma_m3.set_slot_1( Rotor(version = 8, start_letter = 'L') ) # Left rotor
enigma_m3.set_slot_2( Rotor(version = 7, start_letter = 'S') ) # Middle rotor
enigma_m3.set_slot_3( Rotor(version = 6, start_letter = 'K') ) # Right rotor

# set the reflector
enigma_m3.set_reflector(Reflector(version = 'B'))

# set the steckerboard
enigma_m3.set_steckerboard_char([('a','b'), ('x','y'), ('m','n')])

# decode the message
enigma_m3.get_code('NXQUPHXBYXMCKWROBQKAGZCAHFFADKOGKEPLJMPMDCAQOAQPSVPBJKDKYHREPAXDPAMALKYBBMPCQJ')
```




    'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'



# Random Steckers


```python
# Create an enigma machine
enigma_m3 = EnigmaM3()

# Set the rotors
enigma_m3.set_slot_1( Rotor(version = 8, start_letter = 'L') ) # Left rotor
enigma_m3.set_slot_2( Rotor(version = 7, start_letter = 'S') ) # Middle rotor
enigma_m3.set_slot_3( Rotor(version = 6, start_letter = 'K') ) # Right rotor

# set the reflector
enigma_m3.set_reflector(Reflector(version = 'B'))

# set the steckerboard
enigma_m3.set_steckerboard( np.random.choice(26, (10,2), replace=False) )

# encode the message
enigma_m3.get_code('ABCDEFGHIJKLMNOPQRSTUVWXYZ'*3)
```




    'TRSHTZLSFIZQVLZDAIKVYTFQJKYAEMOTKFKGQTNCXIBAMLYGTNVOULOMDTOFPUTZDCSRUMOXJUCGBJ'




![http://users.telenet.be/d.rijmenants/pics/hires-wehrmachtkey-bgs.jpg](http://users.telenet.be/d.rijmenants/pics/hires-wehrmachtkey-bgs.jpg)


