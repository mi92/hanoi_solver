# Functional Hanoi solver (more compact)

import fire

def solver(n, curr_pos='A', target_pos='B', off_pos='C'):
    if n == 1:
        print(f'Move piece {n} from {curr_pos} to {target_pos}')
    else:
        solver(n-1, curr_pos, off_pos, target_pos)
        print(f'Move piece {n} from {curr_pos} to {target_pos}')
        solver(n-1, off_pos, target_pos, curr_pos) 

if __name__ == "__main__":

    fire.Fire(solver)
    
