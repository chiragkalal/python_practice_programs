You are given a maze with a width of W and height of H. The maze is configured with either 1 or 0, 1 representing the wall while 0 represents a walkable path. We want to know the shortest path from start-point S to goal G.
Diagonal move is not allowed.

 

Test case

The first line contains the integers W and H. The subsequent H lines contain strings of length W representing the maze grid. Every character in the string is either 1, 0, S, or G. The limitations for W,H,S,G are given below:

There is only one S and one G.
4 <= W <= 100
3 <= H <= 100
Output should be minimal steps from S to G.
 
Example

input

5 3
11111
1S0G1
11111
output

2
input

8 5
11111111
1S000001
11101101
1G000001
11111111
output

6
 

Analysis of output value
In the first example, 2 is outputted since we just need to move right twice.
In the second example, 6 is outputted since the shortest path is right, right, down, down, left, left.