import numpy as np
import matplotlib.pyplot as plt

def main():

    # First row is epochs, second is mean error
    data = [[],[]]

    # Read all lines of the file
    with open("OUTPUT.txt", 'r') as fin:
        lines = fin.readlines()

    # Process each line
    for line in lines:

        # Extract epoch and mean error
        # Otherwise, ignore the line
        if ("Epoch" in line):
            parts = line.strip().split(' ')

            epoch = int(parts[4].strip(','))
            mean_error = float(parts[7])

            data[0].append(epoch)
            data[1].append(mean_error)

    print(data) # DEBUG: check that the file was parsed correctly

    # Determine some limits on the y axis, ignoring outliers in a naive way
    ymax = max(data[1])
    if (ymax > 10):
        ymax = 10
        
    ymin = min(data[1])
    if (ymin < -10):
        ymin = 10
    
    # Plot the data
    plt.plot(data[0], data[1])
    plt.title("Training Process")
    plt.xlabel("Epoch")
    plt.ylabel("Mean Error")
    plt.ylim(ymin, ymax)
    plt.show()

if __name__ == "__main__":

    main()
