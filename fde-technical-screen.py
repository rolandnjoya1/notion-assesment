# Test cases with objects for each category. you can change the values for each package to test the sort method
test_packages = [
    {"name": "Package A", "width": 50, "height": 40, "length": 30, "mass": 10},    
    {"name": "Package B", "width": 80, "height": 70, "length": 60, "mass": 15},   
    {"name": "Package C", "width": 200, "height": 50, "length": 40, "mass": 10},   
    {"name": "Package D", "width": 50, "height": 40, "length": 30, "mass": 25},    
    {"name": "Package E", "width": 50, "height": 40, "length": 30, "mass": 10}, 
    {"name": "Package F", "width": 200, "height": 100, "length": 80, "mass": 30}   
]

def sort(width: int, height: int, length: int, mass: int) -> str:

    volume = width * height * length
    
    # Define the criteria for bulky and heavy packages 
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in [width, height, length])
    is_heavy = mass >= 20
    
    # Determine the stack 
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Function to sort each package results
sorted_outcomes = []
for pkg in test_packages:
    # Sort the package into the appropriate stack
    stack = sort(pkg["width"], pkg["height"], pkg["length"], pkg["mass"])
    # Collect the result with the name of each package
    sorted_outcomes.append({"name": pkg["name"], "stack": stack})

# Test sort method
for outcome in sorted_outcomes:
    print(outcome)

