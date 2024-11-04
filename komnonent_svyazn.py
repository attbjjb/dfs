# Функция поиска в глубину
def dfs(graph, node, visited, component):
    visited.add(node)  # Помечаем текущую вершину как посещенную
    component.append(node)  # Добавляем текущую вершину в компоненту
    for neighbor in graph[node]:  # Проходим по всем смежным вершинам
        if neighbor not in visited:  # Если смежная вершина еще не посещена
            dfs(graph, neighbor, visited, component)  # Рекурсивно вызываем DFS для смежной вершины

# Функция нахождения компонентов связности графа
def find_connected_components(graph):
    visited = set()  # Множество для отслеживания посещенных вершин
    components = []  # Список для хранения найденных компонент

    for node in graph:  # Проходим по всем вершинам графа
        if node not in visited:  # Если вершина еще не посещена
            component = []  # Создаем новый список для текущей компоненты
            dfs(graph, node, visited, component)  # Запускаем DFS для этой вершины
            components.append(component)  # Добавляем найденную компоненту в список компонент

    return components  # Возвращаем список компонент связности

# Функция для ввода графа
def input_graph():
    graph = {}  # Инициализируем пустой словарь для графа
    num_vertices = int(input("количество вершин графа: "))  # Запрашиваем количество вершин

    for _ in range(num_vertices):  # Цикл для ввода каждой вершины
        vertex = input("имя (номер) вершины: ")  # Запрашиваем имя (номер) вершины
        edges = input(f"смежные вершины для {vertex} (ввести через запятую без пробелов): ")  # Запрашиваем смежные вершины
        # Преобразование строки в список смежных вершин
        adjacency_list = [edge.strip() for edge in edges.split(",") if edge.strip()]  # Создаем список смежных вершин
        graph[vertex] = adjacency_list  # Добавляем вершину и её смежные вершины в граф

    return graph  # Возвращаем построенный граф

# Вывод списка смежности графа
if __name__ == "__main__":
    graph = input_graph()  # Вводим граф с помощью функции input_graph
    print("Список смежности графа:")  # Выводим сообщение
    for vertex, edges in graph.items():  # Проходим по всем вершинам и их смежным вершинам
        print(f"{vertex}: {edges}")  # Выводим вершину и её смежные вершины

    # Вывод компонентов связности графа
    components = find_connected_components(graph)  # Находим компоненты связности графа
    print("Компоненты связности:", components)  # Выводим найденные компоненты