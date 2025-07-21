def add(a,b):
    
     if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):  # Fixed typo here
    raise ValueError("Inputs must be numbers")
    return a + b

   def subtract(a, b):  # Fixed indentation here
        return a - b
        def multiply(a,b):
            return a * b