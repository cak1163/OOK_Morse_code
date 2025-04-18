## On-Off Keying and Morse Code Detection
On-off keying, specifically binary amplitude-shift keying, is a type of digital modulation in which the carrier wave amplitude is varied between two levels to represent binary values "0" or "1." 

During transmission, a "1" is represented by sending a carrier wave at a fixed amplitude, while a "0" is represented by the absence of a carrier wave, resulting in a transmitted signal that is "on" or "off" according to an incoming data stream. At the receiver, the system detects if the carrier wave is present during each bit interval. If it is detected, the received bit is interpreted as a "1." If not, the bit is interpreted as a "0." 

This technique is used for garage, gate, and car keys, and is commonly used to transmit Morse code over radio frequencies in continuous wave (CW) operation.  

This GNU Radio project demonstrates how a random binary data stream can be used to transmit and receive a Morse code message.

# Approach

To implement this, I started  

# Code
The code for this project consists of two Morse code decoders: one corresponding to a random transmitted message, the other to the received message. Both of these use an incoming input signal and translate the input signal into Morse code and ASCII letters depending on the incoming amplitude and duration. 



# Future Enhancements
