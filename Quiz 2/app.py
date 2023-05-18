from flask import Flask, render_template, request
import heapq

app = Flask(__name__)

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

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        shortest_distance = dijkstra(graph, start, end)
        return render_template('index.html', shortest_distance=shortest_distance)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)