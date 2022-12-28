# Neighbor Join Algorithm in Python

## Usage

Download the file `NeighborJoin.py` and import it in your python script.

Use `NeighborJoin` class to create an object.

If you don't know how to wirte, you can reference my main script `main.py`.

## Description

input: a n*n distance matrix

for example:
    ```python
        D = np.array([
        [0, 4, 5, 10],
        [4, 0, 7, 12],
        [5, 7, 0, 9],
        [10, 12, 9, 0]]) 
    ```

output: a tree matrix and a sequence ID list
* the tree matrix will be like:
  * 
    ```
    [ 89. 256. 775.   1.   3.]
    [ 75.  89. 882.   2.   2.]
    [  0.  75. 802.   7.   7.]
    ...
    [  0.  75. 802.   7.   7.]
    ```
    * the first column is the id of parent node
    * the second column is the id of child1 node
    * the third column is the id of child2 node
    * the fourth column is the distance between parent node and child1 node
    * the fifth column is the distance between parent node and child2 node
    * the last row is the remaining node and its distance to the subtree or the distance between the subtrees (position 0 can be ignored)
* the sequence ID list will be like:
  * 
    ```
    [256. 775. 882. 802.]
    ```
    * the list stand for sequence 1, 2, 3, 4 ... respectively

