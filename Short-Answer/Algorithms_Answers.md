#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n) as it's a simple linear loop that repeats n times;

b)
That's a nested loop with two cycles, both running log(n) times so the final complexity will be O(n^2);

c)
This one calls itself n times, so it's O(n);

## Exercise II
We can treat this task as a binary search on a sorted array (as number of floors goes up one after another). 

We count how many floors are there in the building, then divide floors in half and see if the egg breaks on a middle floor. If it does, we forget about upper floors and assign this floor as the highest. Then we repeat the process: divide floors in half, drop an egg and see if it breaks. If it does -- we go again (recursion!), and if it doesn't -- then we forget about lower floors and consider the current floor to be the lowes for our search. A runtime complexity of our attempts is O(log(n)), like any other binary search.

