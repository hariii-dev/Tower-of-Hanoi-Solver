def hanoi_solver(n: int) -> str:
    """Solves the Tower of Hanoi puzzle and returns a string representation 
    of the rods' states after each move.
    
    Args:
        n (int): The total number of disks.
        
    Returns:
        str: A newline-separated string showing the state of the three rods.
    """
    # Initialize the three rods. 
    # Rod A starts with all disks in decreasing size [n, n-1, ..., 1]
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    
    def get_state_string() -> str:
        """Helper function to format the current state of the rods."""
        return f"{rods['A']} {rods['B']} {rods['C']}"
    
    # Store the initial arrangement
    history = [get_state_string()]
    
    def move_disks(disks: int, source: str, target: str, auxiliary: str) -> None:
        """Recursive helper function to transfer disks between rods."""
        if disks == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            history.append(get_state_string())
            return
        
        # Step 1: Move top n-1 disks from source to auxiliary using target as buffer
        move_disks(disks - 1, source, auxiliary, target)
        
        # Step 2: Move the remaining largest disk from source to target
        disk = rods[source].pop()
        rods[target].append(disk)
        history.append(get_state_string())
        
        # Step 3: Move the n-1 disks from auxiliary to target using source as buffer
        move_disks(disks - 1, auxiliary, target, source)

    # Execute the solver if there are disks present
    if n > 0:
        move_disks(n, 'A', 'C', 'B')
        
    return "\n".join(history)
