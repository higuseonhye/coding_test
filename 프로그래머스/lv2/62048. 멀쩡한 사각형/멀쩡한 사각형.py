def solution(w, h):
    """
    Calculates the number of square tiles that can fit in a rectangular area with dimensions w and h,
    minus the number of tiles on the boundary.

    :param w: width of the rectangular area
    :param h: height of the rectangular area
    :return: the number of square tiles that can fit in the rectangular area, minus the number of tiles on the boundary
    """
    
    # Calculate the greatest common divisor of w and h
    s = lambda a, b: a if not b else s(b, a % b)
    gcd = s(w, h)
    
    # Calculate the number of tiles on the boundary
    boundary_tiles = (w + h - gcd)
    
    # Calculate the total number of tiles
    total_tiles = w * h
    
    # Calculate the number of tiles that can fit in the rectangular area, minus the number of tiles on the boundary
    answer = total_tiles - boundary_tiles
    
    # Return the answer
    return answer
