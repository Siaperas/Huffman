# Ternary Huffman
Scientists are looking for new ways of efficient data storage and a method of interest is the use of DNA as a storage medium. With the right encoding, one cubic centimeter of DNA can store 10<sup>16</sup> bits data, which means that you can store all the world's data in one pound DNA.

## How does the program work
But, how can we achieve this? To do so we take the contents of the file and we encode it using huffman coding. In this huffman coding we will use trits(0,1,2) instead of bits. So, the huffman encoding is created throught the routes that connect the root to each and every leaf node of our concievable ternary tree. If our file has an odd amount of unique characters we add an imaginary character that has a frequency of zero. After coding the text to its ternary coding, we are gonna encode the ternary coding using the DNA bases, A (adenine), C (cytocine), G (guanine), T (thymine). We shall encode using the following table.
By doing the opposite we can achieve the decoding of our already encoded file.

<table>
  <tr>
    <th>Previous base</th>
    <th colspan="3">Current trit</th>
  </tr>
  <tr>
    <td></td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>C</td>
    <td>G</td>
    <td>T</td>
  </tr>
    <tr>
    <td>C</td>
    <td>G</td>
    <td>T</td>
    <td>A</td>
  </tr>
    <tr>
    <td>G</td>
    <td>T</td>
    <td>A</td>
    <td>C</td>
  </tr>
    <tr>
    <td>T</td>
    <td>A</td>
    <td>C</td>
    <td>G</td>
  </tr>
</table>

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
