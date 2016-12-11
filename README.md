# Ternary Huffman


## How does the program work


## How to run
In order to run this file from the terminal we have to give the following order

```
python dna_store.py [-d] input output huffman
```
Depending on the system where the program is run, you may need to write python3.

We can observe that the program receives four parameters:
* If ```d``` is not given the program will code the ```input``` file to the output file using huffman and will save the huffman map to the given ```huffman``` csv. If ```d``` is given we will do the opposite and decoded the ```input``` file using the huffman.csv file we have given.
* The parameter ```input``` represents either a coded input file or a normal text file depending on whether the parameter d is given.
* The parameter ```output``` represents either the encoded output file or the decoded output file depending on whether the parameter d is given. 
* ```huffman``` represents a csv file that maps each character in its ternary code
