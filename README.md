# DataStructures
## A compilation of Python script implementing different data structures revised in the Data Structures Coursera MOOC.
More specifically, the scripts in this repository are inspired in selected exercises from the course and seek to shed light in the different implementations and applications of data structures. The objective of these is merely didactic, since implementations in lower level languages could be a lot faster. <br>
Contributors: Oscar Zendejas Rangel, Alan García Zermeño @garciaza2015, Luis Celedon, y Emilio Villa @villacu <br>
The following are short explanations of the scripts presented:
1. Brackets:

## 3. Hash:<br>
a). **Hash chains**. I this program we built a hash table using the chaining scheme in a telephone schedule, we call instructions: <ul>
<li> add string — insert string into the table. If there is already such string in the hash table, then just ignore the query. </li>
<li> del string — remove string from the table. If there is no such string in the hash table, then just ignore the query. </li>
<li> find string — output "yes" or "no" (without quotes) depending on whether the table contains string or not. </li>
<li> check 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to separate the elements of the list. If 𝑖-th list is empty, output a blank line. </li></ul>

In this script we use a toy example: <br>
   ```
   5
   12
   add world
   add HellO
   check 4
   find World
   find world
   del world
   check 4
   del HellO
   add luck
   add GooD
   check 2
   del good
   
   output:
    HellO world
    no
    yes
    HellO 
    GooD luck
   ```
b). **Substring equality**. In this program, you can input a string s, followed by a sequence of n triplets of integers: [a,b,l]. "a" is the index where yor first substring is going to begin, "b" is the index where yor second substring is going to begin and "l" is the length of both substrings. The program must print for each n triplets "yes" if the substrings are equal or "no" if not. <br>
  Toy Example:
  ```
  trololo
  4
  0 0 7
  2 4 3
  3 5 1
  1 3 2
  
  output:
   yes
   yes
   yes
   no
  ```


## 4. Trees:<br>
a). **Tree traversal: Binary Tree DS implemented using a list**. The script receives the tree in the following format: <br>
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
b). **Character Rope using splay tree**: The script receives a string and creates the rope, and then an integer n of the number of instructions to receive. <br>
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
