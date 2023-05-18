# QUIZ 2 DAA E

## Description
This application is a program that can calculate the minimum distance between two points on a graph using Dijkstra's algorithm. This application is built using Flask (Python) and can be accessed through a web browser.

### Import Library
```python
from flask import Flask, render_template, request
import heapq
```
In this section, we import the Flask library to create a web application, render_template to generate HTML output, and heapq to implement Dijkstra's algorithm.

### Application Initialization
```python
app = Flask(__name__)
```
In this section, we create an instance of the Flask class and store it in the `app` variable.

### Dijkstra Function
```python
def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]
```
In this section, we define the `dijkstra` function that will be used to calculate the minimum distance between two points on the graph. The function accepts three parameters: the graph, the start point, and the end point. It returns the minimum distance between the start and end points on the graph.

### Chart
```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
```
In this section, we define the graph that will be used to calculate the minimum distance. This graph is stored as a dictionary in the `graph` variable. Each vertex in the graph is represented as a key in the dictionary, and each edge connecting the vertices is represented as a nested dictionary containing the vertices connected to the vertex and their distances.

### Index Function
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        shortest_distance = dijkstra(graph, start, end)
        return render_template('index.html', shortest_distance=shortest_distance)
    return render_template('index.html')
```
In this section, we define the `index` function that will be called when the user accesses the main page of the application. This function will display a form to enter the start and end points on the graph.

If the user submits the form, this function will call the `dijkstra` function with the chart parameters, start point, and end point provided by the user. The `dijkstra` function will return the minimum distance between the start and end points on the graph.

After the application receives the result from the `dijkstra` function, it will display the result on the web page using the provided HTML template.

### Running the Application
```python
if __name__ == '__main__':
    app.run(debug=True)
```
In this section, we run the Flask application by calling the `run` method on the `app` instance. If `debug` is set to `True`, the application will display a more detailed error message if an error occurs.

## How to Run
To run this application, make sure you have Python and Flask installed on your computer. Then, follow these steps:

1. Clone this repository to your computer.
2. Open a terminal or command prompt and navigate to the directory where this repository is stored.
3. Run the `python app.py` command to run the application.
4. Open a web browser and access `http://localhost:5000` to access the application.

## The implementation used 
- Python
- Flask
- HTML
- Bootstrap

## Reference
- [Dijkstra's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

# Templates Folder

## Description
`index.html` is an HTML template file used to display a web page in an application that calculates the minimum distance between two points on a graph using the Dijkstra algorithm.

### Form
```html
<form method="POST" class="mt-4">
    <div class="mb-3">
        <label for="" class="form-label">Titik Awal:</label>
        <input type="text" class="form-control" id="start" name="start" required>
    </div>
    <div class="mb-3">
        <label for="end" class="form-label">Titik Akhir:</label>
        <input type="text" class="form-control" id="end" name="end" required>
    </div>
    <button type="submit" class="btn btn-primary">Hitung Jarak</button>
</form>
```
In this section, we define a form that will be used to enter the starting and ending points on the graph. This form will be sent to the server when the user clicks the "Hitung Jarak" button.

### Alert
```html
{% if shortest_distance %}
    <div class="alert alert-success mt-4" role="alert">
        Jarak minimum: {{ shortest_distance }}
    </div>
{% endif %}
```
In this section, we display the result of the minimum distance calculation on the web page using an alert. This alert will only be displayed if the `shortest_distance` variable has a value (i.e., if the user has submitted the form).

### Bootstrap
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
```
In this section, we import the Bootstrap library to enhance the appearance of the web page. We also import the JavaScript files required by Bootstrap.

## The implementation used 
- HTML
- Bootstrap

## References
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [HTML Tutorial - W3Schools](https://www.w3schools.com/html/)
