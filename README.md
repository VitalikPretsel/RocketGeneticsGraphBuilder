# RocketGeneticsGraphBuilder
This project is chart builder for `fits.csv` and `hits.csv` files, generated in process of training a Neural Network with Genetic Algorithms. 
View this repo: [PlanetGravity](https://github.com/VitalikPretsel/PlanetGravity).

## Interface
Interface is straightforward:
1) In dialog window choose `fits.csv` file.
2) If you answer `y` to prompt, in dialog window choose `hits.csv` file.
3) If you answer `y` to prompt, in dialog window choose `params.csv` file. It's better to choose only hits or params, because otherwise legend won't look good on chart.
4) The result is chart with three plotted datasets: "Best fitness of generation", "Avarage fitness of generation", "Percent of hits for generation".
5) If you answer `y` to prompt, in dialog window choose `species.csv` file.
6) The result is stacked column diagram, each color indicates different species.
