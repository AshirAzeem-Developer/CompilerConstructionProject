# intermediate_code_generator.py

# Function to generate intermediate code
def generate_intermediate_code():
    # Create an empty list to store the intermediate code instructions
    intermediate_code = []

    # Creating a list
    n = 10

    # Iterate each element in the list
    for ele in range(n):
        # Check if the number is even
        if ele % 2 == 0:
            # Check if the number is greater than or equal to 5
            if ele >= 5:
                intermediate_code.append("PRINT: number is even and bigger than 5")
            else:
                intermediate_code.append("PRINT: number is even and less than 5")
        else:
            # Check if the number is greater than or equal to 5
            if ele >= 5:
                intermediate_code.append("PRINT: number is odd and bigger than 5")
            else:
                intermediate_code.append("PRINT: number is odd and less than 5")

    # Print the intermediate code instructions
    for instruction in intermediate_code:
        print(instruction)

# Call the function to generate intermediate code
generate_intermediate_code()
