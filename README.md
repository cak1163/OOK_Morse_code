When activated, a car key fob transmits a high-frequency pulse (around 315 MHz). This GNU radio project will use this pulse to detect Morse code by doing the following:

1. Detect the pulse with an SDR source block
2. Isolate the pulse signal from noise using a bandpass filter centered at 315 MHz +/- 25 kHz
3. Use Amplitude Shift Keying to distinguish between a binary "1" or binary "0"
4. Use a threshold duration to distinguish if a bit duration is a short or long pulse
5. Define a short pulse as a "dot" and a long pulse as a "dash" in Morse code
6. Assign definitions with an ASCII letter

 
