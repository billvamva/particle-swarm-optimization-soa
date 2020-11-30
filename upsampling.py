import numpy as np
import copy

class upsampling:

    # each upsampling instance can be set to have different points
    def __init__(self, points):
        self.points = points
    

    # main method of upsampling class
    def create(self, *args):
    # *args: list as input     
        input = np.array(*args)
        
        if input.size != self.points:
            n = self.points // input.size
            
            new_input = np.repeat(input, n)
            
            return new_input
        
        else:
            return input
    
if __name__ == '__main__':
    num_points = 10
    init_OP = np.zeros(num_points) # initial drive signal (e.g. a step)
    init_OP[:int(0.25*num_points)],init_OP[int(0.25*num_points):] = -1, 0.5
    
    p = upsampling(20)
    print(init_OP)
    init_OP = p.create(init_OP)
    print(init_OP)