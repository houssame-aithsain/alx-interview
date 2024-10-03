def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.
    
    Args:
        n (int): The number of rows in the triangle.
        
    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        # Start with an empty row
        row = [1] * (i + 1)  # Create a row with '1's
        
        # Each element (except the first and last) is the sum of the two elements above
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle.append(row)
    
    return triangle
