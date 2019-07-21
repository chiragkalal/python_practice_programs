""" 
Let's assume you are given a window size of W and an array of integers S and that you can only see the W numbers of S in the window frame. Each time we slide the window over by one frame (from the left), we want you to output the maximum value within the window.

Print each element with white space in-between.

Test case

Each test case has only 1 line, and the first character is W, followed by array S. So below the input is W = 2 and S = [2,1,2,-1,3]. 

Limits

The length of S is always larger than or equal to W.
The window size W will be an integer in the range, 0 < W < 3,000,000,000.
An element Nn in the stream will be an integer in the range, -3,000,000,000 < Nn < 3,000,000,000.
 
Examples

input

2 2 1 2 -1 3
output

2 2 2 3
Analysis of output value

Since the window size is 2, output would be made in the following order:

2 1 2 -1 3 //Output 2 with 2 and 1

2 1 2 -1 3 //After excluding the initial data, output 2 with 1 and 2

2 1 2 -1 3 //Output 2 with 2 and -1

2 1 2 -1 3 //Output 3 with -1 and 3
"""

inp = input()
list_inp = inp.split(' ')

W = int(list_inp[0])

str_s = list_inp[1:]

S = [ int(num) for num in str_s]

if len(S) >= W and W in range(0, 3000000000):
    fl = []
    for i in range(0, len(S)-W+1):
        if S[i] not in range(-3000000000, 3000000000):
            break
        winw = S[i:i+W]
        print(winw)
        fl.append(max(winw))

    str_fl = [ str(item) for item in fl ]
    print(" ".join(str_fl))