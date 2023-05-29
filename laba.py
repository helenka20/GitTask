# будем использовать словарь для хранения списка смежности графа
graph = {
    '1': ['3'],
    '2': ['4'],
    '3': [],
    '4': ['2']
}

# функция обхода графа в глубину
def dfs(vertex, visited):
    visited.add(vertex) # добавляем вершину в множество посещенных
    print(vertex, end=" ")
    for neighbor in graph[vertex]: # проходим по всем соседним вершинам
        if neighbor not in visited: # если вершина еще не посещена, посещаем ее рекурсивно
            dfs(neighbor, visited) 

# стартовая вершина и множество посещенных вершин
start_vertex = '1'
visited_vertices = set()

# запускаем обход графа
dfs(start_vertex, visited_vertices)

