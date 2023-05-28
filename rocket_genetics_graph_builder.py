import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# Open dialog windows to select the fitnesses.csv and hits.csv files
print("\nChoose first csv-file with fitnesses values ")
root = tk.Tk()
root.withdraw()
file_path1 = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
root.destroy()
print("csv-file with factors: ", file_path1)
fitnesses_file = pd.read_csv(file_path1)
        
print("\nChoose second csv-file with hits values ")
root = tk.Tk()
root.withdraw()
file_path2 = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
root.destroy()
print("csv-file with experiments results: ", file_path1)
hits_file = pd.read_csv(file_path2)

# Extract data from fitnesses.csv
fitnesses_data = fitnesses_file.values
fitnesses_data = fitnesses_data[:, :-1].astype(float)
best_fitness = fitnesses_data.max(axis=1)
mean_fitness = fitnesses_data.mean(axis=1)

# Extract data from hits.csv
hits_data = hits_file.values.flatten()

# Create a new figure and plot the charts
fig, ax1 = plt.subplots()

# Plot best fitness
ax1.plot(range(0, len(best_fitness)), best_fitness, label='Best Fitness')
ax1.plot(range(0, len(mean_fitness)), mean_fitness, label='Mean Fitness')
ax1.set_xlabel('Generation Number')
ax1.set_ylabel('Fitness')
ax1.legend(loc='lower right')

# Create a secondary y-axis for percent of hits
ax2 = ax1.twinx()
ax2.plot(range(0, len(hits_data)), hits_data, 'g', label='Percent of Hits')
ax2.set_ylabel('Percent of Hits')
ax2.legend(loc='lower center')

plt.title('Fitness and Percent of Hits')
plt.show()

