def solution(w: int, h: int) -> int:
    """
    Calculates the number of square tiles that can fit in a rectangular area with dimensions w and h,
    minus the number of tiles on the boundary.

    :param w: width of the rectangular area
    :param h: height of the rectangular area
    :return: the number of square tiles that can fit in the rectangular area, minus the number of tiles on the boundary
    """
    
    # Calculate the greatest common divisor of w and h using math.gcd
    from math import gcd
    gcd_w_h = gcd(w, h)
    
    # Calculate the number of tiles on the boundary
    boundary_tiles = (w + h - gcd_w_h)
    
    # Calculate the total number of tiles
    total_tiles = w * h
    
    # Calculate the number of tiles that can fit in the rectangular area, minus the number of tiles on the boundary
    answer = total_tiles - boundary_tiles
    
    # Return the answer
    return answer


"""
def solution(w, h):
    """
    Calculates the number of square tiles that can fit in a rectangular area with dimensions w and h,
    minus the number of tiles on the boundary.

    :param w: width of the rectangular area
    :param h: height of the rectangular area
    :return: the number of square tiles that can fit in the rectangular area, minus the number of tiles on the boundary
    """
    
    # Calculate the greatest common divisor of w and h
    🧮 = lambda a, b: a if not b else 🧮(b, a % b)
    gcd = 🧮(w, h)
    
    # Calculate the number of tiles on the boundary
    boundary_tiles = (w + h - gcd)
    
    # Calculate the total number of tiles
    total_tiles = w * h
    
    # Calculate the number of tiles that can fit in the rectangular area, minus the number of tiles on the boundary
    answer = total_tiles - boundary_tiles
    
    # Return the answer
    return answer
"""
