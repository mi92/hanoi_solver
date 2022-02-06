# Tower of Hanoi solver

This repository contains a simple recursive solver for the Tower of Hanoi problem.  

<img src="img/hanoi_gif.gif" width="600"> [img source](https://commons.wikimedia.org/wiki/File:Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif) 

To setup up the environment (only for convenience packages, most code uses standard operations), use  

```$ poetry install```   
```$ poetry shell```  


To run the solver with 4 disks, run:  
```$ python src/solver.py --n 4```

To run the solver with 10 disks, run:    
```$ python src/solver.py --n 10```  

While `src/solver.py` contains a documented class with explanations, this solver can be squeezed into 
only a hand full of functional code. For comparison, inspect `src/solver_fn.py` that does basically the 
same (except for counting the steps). It may be similarly invoked with:  

```$ python src/solver_fn.py --n 4```


For a nice visualisation, check out this [clip](https://www.youtube.com/watch?v=YstLjLCGmgg).
