# DataStructures
## A compilation of Python script implementing different data structures revised in the Data Structures Coursera MOOC.
More specifically, the scripts in this repository are inspired in selected exercises from the course and seek to shed light in the different implementations and applications of data structures. The objective of these is merely didactic, since implementations in lower level languages could be a lot faster. <br>
Contributors: Oscar Zendejas Rangel Alan García Zermeño, Luis Celedon, y Emilio Villa @villacu <br>
The following are short explanations of the scripts presented:
1. Brackets:
2. **Tree traversal: Binary Tree DS implemented using a list**. The script receives the tree in the following format: <br>
   -First line: Number N of three nodes<br>
   -The following N lines receive tree values: the key and the list index for the left and right children. If the node has no children, the value is -1.
   Example: 
   ```
   5
   4 1 2
   2 3 4
   5 -1 -1
   1 -1 -1
   3 -1 -1
   Output:
    1 2 3 4 5
    4 2 1 3 5
    1 3 2 5 4
   ```
3. **Character Rope using splay tree**: The script receives a string and creates the rope, and then an integer n of the number of instructions to receive. <br>
   After that it receives n three digit (i,j,k) instructions to take a slice of the string from i to j and then insert it at position k in the remaining string.<br>
   Example:
   ```
   theolivetrees
   3
   5 5 0
   5 5 1
   2 4 5
   Output:
    ilovethetrees
   ```
