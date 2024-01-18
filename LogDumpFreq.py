import sys
import numpy as np

def generate_and_save_values(start, stop, steps, target_pts):
    fac = (stop/start)**(1/(steps-1))
    
    # Open the file for writing
    with open(f"DumpFreq_tw_{stop}_pts_{target_pts}.txt", 'w') as file:
        unique_values = set()  # Use a set to keep track of unique values
        
        for i in range(1, steps+1):
            value = int(np.floor(start * fac**(i-1)))
            unique_values.add(value)
        
        if len(unique_values) != target_pts:
            print(f"Number of points generated {len(unique_values)} :: ",  
                  f"Need {target_pts} points ::",
                   "Run again with a different value")
        else:
            print("Done!")

        # Write the values to the file
        for value in sorted(unique_values):
            file.write(f"{value}\n")

def main():

    start = 1             # first frame number
    target_pts = 80       # number of data points you want

    while True:
        try:
            steps = int(input(f"Enter a number equal or more than {target_pts} : "))
            if steps <= 0:
                raise ValueError("Number of values must be positive.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer value for the number of values to be generated.")

    while True:
        try:
            p = sys.argv[1] if len(sys.argv) > 1 else input("Enter the exponent: ")
            p = int(p)
            if p <= 0:
                raise ValueError("Exponent must be a positive integer.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer value for the exponent.")

    stop = 1 * 10 ** p  # last frame number

    generate_and_save_values(start, stop, steps, target_pts)

if __name__ == "__main__":
    main()

