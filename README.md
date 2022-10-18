# neuroforge_assignment

## Solution

Implementation of A Horse on the Phone pad using python programming language

This problem can be solved by a simple recursion, however it will be costly in terms of calculation and memory( call stack). while iterating through a small sample of the problem, we can see that a lot of calculations get repeated. In such case, it's preferable to write a dynamic programming algorithm. Basically we build our solution from ground-up.

The solution at a position x and N hops = the sum of all the solutions of x's neighbors with N-1 hops
We know also that at a position x with 0 hops. The result is 1.

To run the dynamic programming solution:

```python dp_solution.py --start x --hops n```

This solution has a linear time complexity o(n) and a constant space complexity o(1).

Once I implemented this solution I tried to scour the internet for other possible implementation. I came across a solution that utilizes numpy library. I am aware of how fast numpy can do calculations. So I implemented the solution
to run it:



```
pip install -r requirements.text
python matmul_solution.py --start x --hops n
```

I wrote a small script to compare the performance between the 2 solutions


``` python test_performance_solutions.py```

The DP solution is faster :D 

## Unit Testing

The 2 solutions are expected to generate the same results. So they have the same unit tests. In this case I decided to write 5 unit-tests to test

- Validity of start position and nbr of hops
- result when number of hops is 0
- result when start position is 5
- result with a random starting position and 1 hop
- result with rand position and nbr hops>=2 to see if the equation at the top is verified

To run the tests:

``` 
python dp_solution_test.py
python matmul_solution_test.py    
```