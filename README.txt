This is an implementation of salsa20 in Python3 for TCSS581 Cryptology

Instructions:

1. Use terminal to go to the location of the script, salsa20.py.
3. You can change the location of King James Bible, encryption 'key', 'counter' and 'nonce' near the end of the script.
4. Run 'python3 salsa20.py' (if you are using Python3).
5. The encrypted cyphertext file will be outputted to the same directory as the script.
6. We could not finish the script by the deadline, since we have some minor issues that still needs to be solved. However, 
if it works in the future, use 'time python3 salsa20.py' will return the runtime of this encryption.


The implementation attached here is authored by:
Tianyi Li
Dustin Ray

Our implementation is almost complete. The only remaining task to be done with our code is to process the strings
coming in from the text file into either binary or hexadecimal values such that they can then be processed
using arithematic functions in python. Currently we are processing strings directly and this is causing runtime
errors in our program, as strings cannot be added to integers. 

Per the instructors directions, this project also includes an attached version of a correct python implementation
of salsa20. Our version actually came quite close to the correct implementation, except for the need for bit processing
at the binary level. 
