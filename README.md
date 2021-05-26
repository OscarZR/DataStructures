# DataStructures
## A compilation of Python script implementing different data structures revised in the Data Structures Coursera MOOC.
More specifically, the scripts in this repository are inspired in selected exercises from the course and seek to shed light in the different implementations and applications of data structures. The objective of these is merely didactic, since implementations in lower level languages could be a lot faster. <br>
Contributors: Oscar Zendejas Rangel @OscarZR, Alan García Zermeño @garciaza2015, Luis Celedon, y Emilio Villa @villacu <br>
The following are short explanations of the scripts presented:

## 1. Basic Data Structures: <br>
a) **Check brackets in the code** All brackets in the code should be divided into pairs of matching brackets, such that in each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either one of them is nested inside another one as in (foo[bar]) or they are separate as in f(a,b)-g[c]. The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).
Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.
If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). 
Toy example 1: <br>
 ```
Input:
[()]

Output:
Success
 ```
 Toy example 2: <br>
 ```
Input:
foo(bar[i);

Output:
10
 ```
 
 b) **Compute tree height** You are given a description of a rooted tree. Your task is to compute and output its height. Recall that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a leaf to the root. You are given an arbitrary tree, not necessarily a binary tree. 
 Toy example 1: <br>
  ```
Input:
5
4 -1 4 1 1

Output:
3
 ```
 
## 2. Priority ques and Disjoint Sets: <br>
a) **Array to hipe**. In this problem we will convert an array of integers into a heap. This is an important step to understand sorting.
Toy example: <br>
 ```
Input:
5
5 4 3 2 1

Output:
3
1 4
0 1
1 3
 ```
Explanation: 
After swapping elements 4 in position 1 and 1 in position 4 the array becomes 5 1 3 2 4

After swapping elements 5 in position 0 and 1 in position 1 the array becomes 1 5 3 2 4

After swapping elements 5 in position 1 and 2 in position 3 the array becomes 1 2 3 5 4, this is already a heap.

Video example: https://drive.google.com/file/d/1NI4d3eSQHp3RxpgukNjzMqXVNYQgErc6/view?usp=sharing

b) **Merging Tables **. In this problem, our goal is to simulate a sequence of merge operations with tables in a database. All tables share the same set of columns.
We need to perform n of the following operations: <ul>
   <li> Consider table number destination. Traverse the path of symbolic links to get to the data. </li>
   <li> Consider the table number source, and traverse the path of symbolic links from it in the same manner as for destination. </li>
   <li> Now, destination and source, are the numbers of two tables with real data. If destination != source. copy all the rows from table source, to table destination, then clear the table source and instead of real data put a symbolic link to destination into it. </li>
   <li> Print the maximum size among all n tables . If the table contains only a symbolic link, its size is considered to be 0. </li></ul>


Toy example: <br>
 ```
 Input:
 5 5
 1 1 1 1 1
 3 5
 2 4
 1 4
 5 4
 5 3
 
 Output:
 2
 2
 3
 5
 5
 ```
 
 Video example: https://drive.google.com/file/d/1NI4d3eSQHp3RxpgukNjzMqXVNYQgErc6/view?usp=sharing
 
## 3. Hash:<br>
a). **Hash chains**. In this program we built a hash table using the chaining scheme in a telephone schedule, we call instructions: <ul>
<li> add string — insert string into the table. If there is already such string in the hash table, then just ignore the query. </li>
<li> del string — remove string from the table. If there is no such string in the hash table, then just ignore the query. </li>
<li> find string — output "yes" or "no" (without quotes) depending on whether the table contains string or not. </li>
<li> check 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to separate the elements of the list. If 𝑖-th list is empty, output a blank line. </li></ul>

Toy example: <br>
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
b). **Substring equality**. In this program, you can input a string s, followed by an integer n and a sequence of n triplets of integers: [a,b,l]. "a" is the index where yor first substring is going to begin, "b" is the index where yor second substring is going to begin and "l" is the length of both substrings. The program must print for each n triplets "yes" if the substrings are equal or "no" if not. <br>
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
