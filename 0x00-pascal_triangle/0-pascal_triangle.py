def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        # Initialize the row with 1s
        row = [1] * (i + 1)
        
        # Update the elements inside the row, starting from the third row (i >= 2)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle
