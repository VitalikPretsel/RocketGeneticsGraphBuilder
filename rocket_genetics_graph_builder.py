import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Open dialog window to select the fitnesses.csv file
print("\nChoose first csv-file with fitnesses values ")
root = tk.Tk()
root.withdraw()
file_path1 = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
root.destroy()
print("csv-file with fitnesses: ", file_path1)
fitnesses_file = pd.read_csv(file_path1)
        
# Extract data from fitnesses.csv
fitnesses_data = fitnesses_file.values
fitnesses_data = fitnesses_data[:, :-1].astype(float)
best_fitness = fitnesses_data.max(axis=1)
mean_fitness = fitnesses_data.mean(axis=1)
index_of_best_fitness = np.argmax(best_fitness)
index_of_mean_fitness = np.argmax(mean_fitness)

# Create a new figure and plot the charts
fig, ax1 = plt.subplots()

# Plot best fitness
ax1.plot(range(0, len(best_fitness)), best_fitness, label='Best Fitness')
ax1.plot(range(0, len(mean_fitness)), mean_fitness, label='Mean Fitness')
ax1.set_xlabel('Generation Number')
ax1.set_ylabel('Fitness')
ax1.legend(loc='lower right')

title = 'Generation Fitness'

# Open dialog window to select the hits.csv file
manual_fill = input("\nDo you want to plot hits? (yes/no) ")
if manual_fill.lower()[0] == "y":
    print("\nChoose second csv-file with hits values ")
    root = tk.Tk()
    root.withdraw()
    file_path2 = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    root.destroy()
    print("csv-file with hits: ", file_path2)
    hits_file = pd.read_csv(file_path2)
    
    # Extract data from hits.csv
    hits_data = hits_file.values.flatten()
    index_of_max_hit = np.argmax(hits_data)

    # Create a secondary y-axis for percent of hits
    ax2 = ax1.twinx()
    ax2.plot(range(0, len(hits_data)), hits_data, 'g', label='Percent of Hits')
    ax2.set_ylabel('Percent of Hits')
    ax2.legend(loc='lower center')

    title = 'Generation Fitness and Percent of Hits'


# Open dialog window to select the params.csv file
manual_fill = input("\nDo you want to plot params? (yes/no) ")
if manual_fill.lower()[0] == "y":
    print("\nChoose third csv-file with params values ")
    root = tk.Tk()
    root.withdraw()
    file_path3 = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    root.destroy()
    print("csv-file with params: ", file_path3)
    params_file = pd.read_csv(file_path3)

    node_chance = params_file.iloc[:, 0].values
    con_chance = params_file.iloc[:, 1].values
    weight_chance = params_file.iloc[:, 2].values

    # Create a secondary y-axis for params values
    ax3 = ax1.twinx()
    ax3.plot(range(0, len(node_chance)), node_chance, 'gray', ls='--', label='Node mutation chance')
    ax3.plot(range(0, len(con_chance)), con_chance, 'gray', ls='-.', label='Connection mutation chance')
    ax3.plot(range(0, len(weight_chance)), weight_chance, 'gray', ls=':', label='Weight mutation chance')
    ax3.set_ylabel('Params value')
    ax3.legend(loc='center right')


plt.title(title)
plt.show()


# Plot some stats
print("====== Some stats ======")
print(f'Highest best fitness: {best_fitness[index_of_best_fitness]} at generation {index_of_best_fitness}')
print(f'Highest mean fitness: {mean_fitness[index_of_mean_fitness]} at generation {index_of_mean_fitness}')
if index_of_max_hit:
    print(f'Highest mean hits percent: {hits_data[index_of_max_hit]} at generation {index_of_max_hit}')



# Open dialog window to select the speciess.csv file
manual_fill = input("\nDo you want to plot species? (yes/no) ")
if manual_fill.lower()[0] == "y":
    print("\nChoose csv-file with species values ")
    root = tk.Tk()
    root.withdraw()
    file_path4 = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    root.destroy()
    print("csv-file with species: ", file_path4)

    import numpy
    from io import StringIO
    with open(file_path4, 'r') as file:
        lines = file.readlines()
    max_columns = max(len(line.split(',')) for line in lines)
    modified_lines = [line.strip() + (',' * (max_columns - len(line.split(',')))) + '\n' for line in lines]
    species_file = pd.read_csv(StringIO(''.join(modified_lines)), header=None)

    fig, ax = plt.subplots()

    all_values = [numpy.zeros(len(lines))]
    # Iterate through each set of values and colors
    for i in range(0, len(species_file.columns)-1, 2):
        print(f'{i/(len(species_file.columns)-1)*100}% ')
        bottoms = numpy.array(all_values).sum(axis=0)
        values = species_file.iloc[:, i].fillna(0).values
        all_values.append(values)
        colors = list(map(lambda c: ((str)(c)).strip(), species_file.iloc[:, i + 1].fillna('#FFFFFF').values))
        bars = ax.bar(range(len(species_file)), values, width=1, bottom=bottoms, color=colors)
    print('100%')
    #for bar in ax.patches:
    #    ax.text(bar.get_x() + bar.get_width() / 2,
    #        bar.get_height() / 2 + bar.get_y(),
    #        round(bar.get_height()), ha = 'center',
    #        color = 'black', weight = 'bold', size = 10)

    if (len(species_file) < 100):
        ax.set_xticks(range(len(species_file)))
        ax.set_xticklabels(species_file.index)
    ax.set_xlabel('Generation')
    ax.set_ylabel('Members count')

    plt.title("Species")
    plt.show()

