# Data Visualization - Tutorial

**Abstract.** Humans can more easily perceive differences in line lengths, shapes, and colors (hues) than process sequences of text or numbers. This ability makes data visualization a powerful tool for exploring, understanding, and communicating data. Creating effective data visualizations is a crucial research skill. Visualizations support research at various stages, from early prototypes over systematic experiments to final publications in papers/theses, presentations, or applications/demonstrations. This process often involves presenting the same data at different levels of detail or adapting styles for different audiences. Fortunately, many free tools are available for different types of visualizations, allowing us to choose what best fits our needs. This tutorial provides an overview of common visualization types and tools. We will discuss strategies for managing data visualizations in research, including automation, customization, and best practices. Through hands-on examples, we will explore the plotting library Matplotlib for static graphs and Chart.js for interactive web-based visualizations. Participants will be encouraged to share their experiences and insights throughout the session.

## Hands-on Examples

The following hands-on examples showcase exemplary data visualizations alongside the tools used to create them.
For each tool, we provide a brief description, present a sample output, and outline the steps to reproduce the visualizations.  


### Matplotlib for Static Graphs

[Matplotlib](https://matplotlib.org/stable/gallery/index.html) is widely regarded as the standard tool for creating static graphs in scientific publications, because it enables creating publication-ready output, has extensive customization options, and has wide adoption and support in the community. Matplotlib has different [interfaces](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html). Our examples cover the implicit, stateful "pyplot" interface.
Matplotlib might not be the ideal choice for interactive applications, complex 3D visualizations, or users without a programming background. Its steep learning curve and the need for fine-grained control can be challenging for beginners.

**Exemplary Visualization**

<img width="290" alt="matplot_line_chart_example1" src="https://github.com/user-attachments/assets/39dc4445-d26b-432f-a772-f9ce59c3a279" />
<img width="545" alt="matplot_line_chart_example2" src="https://github.com/user-attachments/assets/ace5d36f-f230-4dec-a58d-4644c6ade4ef" />

<img width="290" alt="matplot_bar_chart_example1" src="https://github.com/user-attachments/assets/f681d0a5-ab3f-47ea-b044-015c2b89a2c2" />
<img width="290" alt="matplot_bar_chart_example2" src="https://github.com/user-attachments/assets/a6c2ca28-9a13-4985-9aba-18593b7f84a9" />
<img width="290" alt="matplot_bar_chart_example3" src="https://github.com/user-attachments/assets/7b868dc3-2b9b-4a29-a7cb-57a728831624" />



**Setup**

1. Download the provided Jupyter notebook [tutorial.ipynb](https://github.com/klauck/data_visualization_tutorial/blob/main/1_matplotlib/tutorial.ipynb)

2. Open https://jupyter.org/try-jupyter/lab/ in your browser

3. Upload and open the downloaded Jupyter notebook (see Step 1)


### Chart.js for Interactive Web Applications

[Chart.js](https://www.chartjs.org/docs/latest/samples/information.html) is one of many ([D3](https://d3js.org/) or [Highcharts](https://www.highcharts.com/) are exemplary alternatives) free JavaScript libraries for creating interactive charts.

**Exemplary Visualization**

<img width="860" alt="chart_js_example" src="https://github.com/user-attachments/assets/36aa96f3-0683-42a1-8ae9-4455cf03eac2" />

**Setup**

1. Download the provided HTML page [dynamic_bar_chart.html](https://github.com/klauck/data_visualization_tutorial/blob/main/2_chart_js/dynamic_bar_chart.html)
2. Open the downloaded HTML page in your browser (see Step 1)
3. Open the downloaded HTML page in a text editor
   1. Inspect the code
   2. Optionally, adapt and reload the HTML page 

**More Advanced Chart.js Project Examples**

- A web application for analyzing database index selection approaches: [https://github.com/klauck/index_analysis](https://github.com/klauck/index_analysis)

  <img width="700" alt="chart.js index analysis" src="https://raw.githubusercontent.com/klauck/index_analysis/refs/heads/main/screenshot.png" />


### Python `curses` for Terminal Applications

Using [`curses`](https://docs.python.org/3/howto/curses.html), you can create terminal applications, such as visualizations or games.

**Exemplary Visualization**

<img width="300" alt="curses_example" src="https://github.com/user-attachments/assets/dfaa02ee-e993-4581-a3c5-9b2de2355f78" />


**Setup**

1. Download the provided Python script [dynamic_barplot.py](https://github.com/klauck/data_visualization_tutorial/blob/main/3_curses/dynamic_barplot.py)
2. Open a terminal, go to the download location, and run `python dynamic_barplot.py`
3. Optionally, adapt the code and rerun the application

**More Advanced Curses Project Examples**

- A visualization of the load-balancing in database clusters. [https://github.com/hyrise/replication](https://github.com/hyrise/replication)
  
  <img width="700" alt="curses load balancing" src="https://github.com/hyrise/replication/blob/main/screenshot.png" />

- A simple Tetris game implemented using Python's curses library: [https://github.com/klauck/tetris](https://github.com/klauck/tetris)
  
  <img width="250" alt="curses tetris" src="https://github.com/klauck/tetris/blob/main/Screenshot.png" />

## License

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">Data Visualization - Tutorial</span> by <span property="cc:attributionName">Stefan Halfpap</span> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p> 
