# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:00:09 2020

@author: Araib Irshad
"""


#>>>>>>>TEXT TO MORSE WITH SOUND<<<<<<
#First displays the encoded message and then asks the user for playback

class Morse_Code():
    def __init__(self):
        self.code ={'A':'. -','B':'- . . .','C':'- . - .','D':'- . .','E':'.','F':'. . - .',
           'G':'- - .','H':'. . . .','I':'. .','J':'. - - -','K':'- . -','L':'. - . .',
           'M':'- -','N':'- .','O':'- - -','P':'. - - .','Q':'- - . -','R':'. - .',
           'S':'. . .','T':'-','U':'. . -','V':'. . . -','W':'. - -','X':'- . . -','Y':'- . - -',
           'Z':'- - . .','1':'. - - - -','2':'. . - - -','3':'. . . - -','4':'. . . . -',
           '5':'. . . . .','6':'- . . . .','7':'- - . . .','8':'- - - . .',
           '9':'- - - - .','0':'- - - - -',' ':'       '}
        self.enc_msg = ''
        self.msg = input('Please enter the message to be encoded').upper()
        self.morse()
        cont = input('Please press Y if you want to play the code as sound. Press any other key to exit').upper()
        if cont == 'Y':    
           self.play_morse()
        else:
            return
        
    def morse(self):
 
        for letter in self.msg:
          self.enc_msg += self.code[letter]
          self.enc_msg += '   '
        print(self.enc_msg)
    
    def play_morse(self):
        import numpy as np
        import sounddevice as sd
        import time
        
        # Samples per second
        sps = 44100

        # Frequency / pitch in Hz
        freq_hz = 440.0
        
       
#waveform generation from https://gist.github.com/akey7/94ff0b4a4caf70b98f0135c1cd79aff3
#creates an array of samples of the sine waveform of duration 0.1s or 0.3s.
        dot_waveform = np.sin(2*np.pi *np.arange(0.1 * sps)* freq_hz / sps)
        dash_waveform = np.sin(2*np.pi *np.arange(0.3 * sps)* freq_hz / sps)
        
        #>>>>>>>>>>>>>>><<<<<<<<<<<
        for l in self.enc_msg:
            if l == '.':
                sd.play(dot_waveform,sps) #playing the sample values in the waveform sample array through speakers.
                #time.sleep(1.0)
             
              
              
            elif l =='-':
                sd.play(dash_waveform,sps)
                
            elif l == ' ':
                time.sleep(0.35) 
        return
                             
               
                
    
Morse_Code()    
