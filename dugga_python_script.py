numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

#1a) For loop for absolute values greater or equal to 10
large_numbers = [] # List to store absolute values greater or equal to 10
for num in numbers:
    if abs(num) >= 10: # Check if absolute value is greater or equal to 10
        large_numbers.append(abs(num)) # Append absolute value to the list
print(sum(large_numbers))

#1b) List of cubes of negative numbers
cubes_negative = [] # List to store cubes of negative numbers
for num in numbers:
    if num < 0: # Check if the number is negative
        cubes_negative.append(num ** 3) # Append the cube of the number to the list
print(cubes_negative)

#1c) First repeated absolute value
unique_abs_values = set() # Set to store unique absolute values
duplicates =[] # List to store duplicates
flag = True # Flag to ensure only the first duplicate is printed
for num in numbers:
    abs_value = abs(num) # Get the absolute value
    if abs_value not in unique_abs_values: # Check if absolute value is unique
        unique_abs_values.add(abs_value) # If it is, add it to the set
    elif abs_value in unique_abs_values and flag == True: # If it's a duplicate and flag is True
        print(f'Repeat found:', abs_value) # Print the duplicate absolute value
        duplicates.append(abs_value) #Append to duplicates list for next if loop
        flag = False # Set flag to False to prevent further prints
if len(duplicates) == 0: # Check if no duplicates were found and if so, print message
            print("No repeats found") 

#Part 2

import csv 
import pandas as pd
import matplotlib.pyplot as plt

#2.1 Read the CSV file into a pandas DataFrame with a comma as separator
data = pd.read_csv('brca_head500_genes.csv', sep=',') 

#2.2.1 Create a function, that plots a histogram of colum fpkm_log2 
def plot_fpkm_histogram(data, output_file='fpkm_histogram.png'): #Set input and output paths
    """Reads the CSV file "data", then plots and saves a histogram of the fpkm_log2 column.""" #Function docstring
    plt.hist(data['fpkm_log2'], bins=30, edgecolor='black') #Plot histogram with suffiecient bins and black edges
    plt.title('Histogram of fpkm_log2') #Set title
    plt.xlabel('fpkm_log2') #Set x label
    plt.ylabel('Frequency') #Set y label
    plt.savefig(output_file) #Save the figure to the specified output
    plt.close() #Close the plot to free memory

#2.2.2 call the function
plot_fpkm_histogram(data)

#2.2.3, same histogram but with different labels 
def plot_fpkm_distribution(data, output_file='fpkm_distribution.png'):
    """Reads the CSV file "data", then plots and saves a histogram of log2(FPKM) values."""
    plt.figure(figsize=(10,8)) # Set figure size for better visibility
    plt.hist(data['fpkm_log2'], bins=30, edgecolor='black')
    plt.title('Distribution of gene expression')
    plt.xlabel('Expression')
    plt.ylabel('Number of genes')
    plt.tight_layout() # Styling adjustment to prevent label cutoff
    plt.savefig(output_file)
    plt.close()

plot_fpkm_distribution(data)
