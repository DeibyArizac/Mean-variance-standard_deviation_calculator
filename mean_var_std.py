import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    
    # Convertir la lista en una matriz de 3x3
    arr = np.array(lst).reshape(3, 3)
    
    # Calcular la media, varianza, desviación estándar, máximo, mínimo y suma
    mean = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)]
    variance = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)]
    std_dev = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)]
    max_val = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr)]
    min_val = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr)]
    sum_val = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr)]
    
    # Crear el diccionario con los resultados
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    
    return calculations

# Probar la función con una lista de ejemplo
if __name__ == "__main__":
    # Lista de ejemplo con 9 elementos
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(result)
