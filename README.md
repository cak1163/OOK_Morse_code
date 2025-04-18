# On-Off Keying and Morse Code Detection
On-off keying, specifically binary amplitude-shift keying, is a type of digital modulation in which the carrier wave amplitude is varied between two levels to represent binary values "0" or "1." 

During transmission, a "1" is represented by sending a carrier wave at a fixed amplitude, while a "0" is represented by the absence of a carrier wave, resulting in a transmitted signal that is "on" or "off" according to an incoming data stream. At the receiver, the system detects if the carrier wave is present during each bit interval. If it is detected, the received bit is interpreted as a "1." If not, the bit is interpreted as a "0." 

This technique is used for garage, gate, and car keys, and is commonly used to transmit Morse code over radio frequencies in continuous wave (CW) operation.  

This GNU Radio project demonstrates how a random binary data stream can be used to transmit and receive a Morse code message.

## Approach

1. Start with a signal that generates a random binary data stream
2. Use interpolation to increase the pulse duration of an incoming "1" or "0" to match a "dot," "dash," or "space" in Morse code
3. Decode the incoming pulses into Morse code and an ASCII letter sequence using the <ins>**Morse Generator and Decoder python file**</ins>
4. Modulate the binary data stream with a carrier wave with a variable frequency, automatically set at 20 kHz, this is the transmitted signal
5. Receive the transmitted signal and use envelope detection to obtain the original input signal
6. Set threshold levels for accuracy to remove unnecessary noise
7. Use the received input signal and decode it into Morse code and an ASCII letter sequence to confirm if it is the same sequence before transmission
8. Plot the transmitted and received binary data stream in the time domain

## Code
The code for this project consists of two Morse code decoders: one corresponding to a random transmitted message, the other to the received message. Both of these use an incoming input signal and translate the input signal into Morse code and ASCII letters depending on the incoming amplitude and duration. 



# Future Enhancements
