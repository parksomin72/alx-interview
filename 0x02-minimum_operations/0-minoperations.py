def minOperations(n):
    if n <= 1:
        return 0
    
    # Initialize variables
    operations = 0
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    
    return operations
