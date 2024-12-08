import matplotlib.pyplot as plt

def plot_metrics(metrics, metric_name):
    for key, values in metrics.items():
        plt.scatter(range(1, len(values) + 1), values, label=key)  # Используем scatter для точек
        plt.plot(range(1, len(values) + 1), values)  # Соединяем точки линиями (опционально)

    plt.title(f"{metric_name} Метрика")
    plt.xlabel("Тестовый набор")
    plt.ylabel("Значение")
    plt.legend()
    plt.grid()
    plt.show()
