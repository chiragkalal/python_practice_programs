Implement a data structure that supports the following operations.



// assume K provides good hashCode()
void evict(); // Remove the eldest entry(the least recently accessed(add or get) entry).
void add(K key, V value); // Add items that match the key and value to the data structure.
V get(K key); // Returns the value of the item that matches the key. An exception occurs if no item is found.
V remove(K key); // Returns the value of the item that matches the key and then removes it from the data structure. An exception occurs if no item is found.


Each line of the input represent the commands that operate on the data structure. Parameters can be added to each command by separating them with a blank space. (Undefined commands are ignored until the next valid command.)



evict: Performs the evict operation described above. 

add: Performs the add operation described above. The first parameter represents the key, and the second parameter represents the value.

get: Performs the get operation using the first parameter as a key. Outputs the acquired results. If an exception occurs or no item is found, "-1" will be displayed.

remove: Performs the remove operation using the first parameter as a key. Outputs the acquired results. If an exception occurs or no item is found, "-1" will be displayed.

exit: Stops receiving new inputs, displays final output and quits.



You may be given an input as follows.



input



add 5 3
add 1 2
get 5
evict
get 1
remove 5
exit


output



Output the results of the processed commands. Results for each command are displayed on separate lines. 

Your program should output the following result when given the sample input above.



3
-1
3
