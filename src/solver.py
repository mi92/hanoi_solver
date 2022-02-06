import fire

class HanoiSolver:
    """ Hanoi Solver class """
    def __init__(
            self, 
            n: int, 
            curr_pos: str = 'A',
            target_pos: str = 'B',
            off_pos: str = 'C'
        ):
        """
        Parameters:
        - n: Number of disks in the game.
        - curr_pos: Current position (or starting position) of the tower
            to be considered.
        - target_pos: Target position where the considered tower should 
            move.
        - off_pos: `Off` position (or hold position), which is used as a
            buffer in intermediate steps.
        """
        self.n = n
        self.curr_pos = curr_pos
        self.target_pos = target_pos
        self.off_pos = off_pos

        # Additionally, we track the number of moves that are made:
        self.counter = 0

    def _move(
        self, n: int, 
        curr_pos: str, 
        target_pos: str
        ):
        """ 
        Move command, moves a piece from curr_pos to target_pos,
        prints it, and tracks the number of moves with a counter.
        """
        print(f'Move piece {n} from {curr_pos} to {target_pos}')
        self.counter += 1

    def _solve(
        self, 
        n: int, 
        curr_pos: str, 
        target_pos: str, 
        off_pos: str
        ):
        """
        Parameters: see class __init__ docstring.
        Here, the recursive `magic` happens. Basically, this function implements 
        the command "move a tower of n disks from curr_pos to target_pos".

        First, the trivial case n = 1 is handled. Then for larger towers,
        we divide the problem of solving a tower of size n into the three 
        sub-problems, as described below.
        
        Intuitively, we divide the tower of size n into a head piece (the 
        largest piece at the bottom), and a remaining tail, i.e., the tower of
        n-1 pieces on top. Then, we take three steps:

        1.) We move the tail to the off position, as we wish to move the head 
        to the target position which only works when the entire tail is out of 
        the way.

        2.) We move the head to the target position.

        3.) We move the tail from the off position (where it waited) to the 
        target position.
        
        In essence, since _solve() already moves a tower of size n from one 
        position to the next, we can recursively call it on smaller towers, 
        given that we handle the edge case n = 1 properly.
        """
        if n == 1:
            # trivial case:
            self._move(n, curr_pos, target_pos)

        else:
            # 1.) Tail to off position
            self._solve(n-1, curr_pos, off_pos, target_pos)

            # 2.) Head to target position
            self._move(n, curr_pos, target_pos)

            # 3.) Tail from off position to target position
            self._solve(n-1, off_pos, target_pos, curr_pos)

    def __call__(self):
        """ 
        The call runs the solver and prints the number of steps it took
        to solve the Hanoi towers.
        """
        self._solve(self.n,
                self.curr_pos,
                self.target_pos,
                self.off_pos,
        )
        print(f'Took {self.counter} steps.')


if __name__ == "__main__":

    fire.Fire(HanoiSolver) 
