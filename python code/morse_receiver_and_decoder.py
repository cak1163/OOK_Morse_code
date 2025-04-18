# Morse Code Receiver and Decoder
# Embedded Python Block (gr.sync_block)

import numpy as np
from gnuradio import gr
import time as t

class blk(gr.sync_block):
    def __init__(self):
	# Initialize block and parameters

        gr.sync_block.__init__(
            self,
            name='Morse Receiver and Decoder',
            in_sig=[np.float32],
            out_sig=[]
        )

        # Morse code output 
        self.morse_output = ''

	# Morse code translation
        self.morse_phrase = ''
        self.letter = ''

	# Morse code dictionary
        self.morse_code = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
            '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
            '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
            '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
            '--..': 'Z','-----': '0', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7',
            '---..': '8', '----.': '9'
        }

        self.last_bit = None # Store previous bit for comparison
        self.counter = 0 # Tracks bit duration
        self.samp_rate = 100000 # Signal sample rate
        self.samples_per_ms = self.samp_rate // 1000 # Convert sample rate from seconds to miliseconds


    def decode_morse(self, code):
        if code != '':
            letter = self.morse_code.get(code, '?') # '?' if not in Morse code dictionary
            self.morse_phrase = self.morse_phrase + f"{code} " # Appending Morse code
            self.letter = self.letter + letter

    def work(self, input_items, output_items):
	# Threshold to determine binary "1" for input values > 0.1V

        bits = (input_items[0] > 0.1).astype(np.int8)

	# Threshold and duration conditions for all bits
        for i in bits:
            
            # Initialization for first sample
            if self.last_bit is None:
                self.last_bit = i # Store for comparison
                self.counter = 1 # Initialize duration of bit

            elif i == self.last_bit:
		# Increment counter if current bit is the same as previous

                self.counter = self.counter + 1
		# Changed bit, determine duration period in miliseconds
            else:
                duration = self.counter / self.samples_per_ms
		
		# Morse code characterization from duration 
                if self.last_bit == 1:
                    if duration <= 1:
                        self.morse_output = self.morse_output + '.'
                    elif duration > 1:
                        self.morse_output = self.morse_output + '-'
		
                else:
                    if 1 < duration <= 2:
                        self.decode_morse(self.morse_output)
                        self.morse_output = ''
                    elif 2 < duration <= 3:
                        self.decode_morse(self.morse_output)
                        self.morse_output = ''
                        self.letter = self.letter + ' '
                        self.morse_phrase = self.morse_phrase + '  '
                    
		# Other shorter or longer pauses do nothing

                self.last_bit = i
                self.counter = 1

        return len(input_items[0])

    def stop(self):
	# Output information at the end of run

        self.decode_morse(self.morse_output)
        if self.letter or self.morse_phrase != '':

            # Delaying receiver output from transmission
            t.sleep(0.1) 
            
            # Decoded message in Morse code and ASCII letters
            print("Received Morse:  ", self.morse_phrase)
            print("Received Phrase:  ", self.letter)
        return True