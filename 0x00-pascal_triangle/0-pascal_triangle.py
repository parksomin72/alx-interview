#!/usr/bin/python3

'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []  # Initialize an empty list to store the triangle
    
    if type(n) is not int or n <= 0:  # Check if n is a positive integer
        return triangle
    
    for i in range(n):  # Iterate from 0 to n-1 (inclusive)
        line = []  # Initialize an empty list for each row
        for j in range(i + 1):  # Iterate from 0 to i (inclusive)
            if j == 0 or j == i:  # The first and last elements of each row are 1
                line.append(1)
            elif i > 0 and j > 0:  # For elements not at the edges
                # Calculate the element as the sum of the two elements above it
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)  # Add the completed row to the triangle
    
    return triangle  # Return the completed Pascal's Triangle

# Test the function with the provided main code
def print_triangle(triangle):
    '''Prints the Pascal's Triangle in a formatted manner.
    '''
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

if __name__ == "__main__":
    # Test printing Pascal's Triangle up to the 5th row
    print_triangle(pascal_triangle(5))
