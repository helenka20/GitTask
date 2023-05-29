# Создаем граф
graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f'],
    'd': [],
    'e': ['f'],
    'f': []
}

# Реализуем функцию обхода графа в глубину с проверкой на некорректные значения входных параметров
def dfs_path(graph, current_vertex, target_vertex, visited=[]):
    visited.append(current_vertex)

    if current_vertex == target_vertex:
        return visited

    if current_vertex not in graph:
        raise ValueError(f"Вершина {current_vertex} не найдена в графе")

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs_path(graph, neighbor, target_vertex, visited)
            if path:
                return path

    return None

# Вызываем функцию для проверки
try:
    a = 'a'
    b = 'e'
    path = dfs_path(graph, a, b)
    if path:
        print(f"Длина пути от вершины {a} до вершины {b} составляет {len(path) - 1} штрихов")
    else:
        print(f"Путь от вершины {a} до вершины {b} не найден")
except ValueError as e:
    print(str(e))
