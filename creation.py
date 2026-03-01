def add_matrices(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    """
    Складывает две матрицы одинакового размера поэлементно.

    Args:
        matrix1: Первая матрица.
        matrix2: Вторая матрица.

    Returns:
        Матрица-результат сложения.

    Raises:
        ValueError: Если размеры матриц не совпадают.

    Example:
        >>> add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[6, 8], [10, 12]]
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


def subtract_matrices(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    """
    Вычитает вторую матрицу из первой поэлементно.

    Args:
        matrix1: Уменьшаемая матрица.
        matrix2: Вычитаемая матрица.

    Returns:
        Матрица-результат вычитания.

    Raises:
        ValueError: Если размеры матриц не совпадают.

    Example:
        >>> subtract_matrices([[5, 6], [7, 8]], [[1, 2], [3, 4]])
        [[4, 4], [4, 4]]
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны иметь одинаковые размеры для вычитания")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_by_scalar(matrix: list[list[float]], scalar: float) -> list[list[float]]:
    """
    Умножает каждый элемент матрицы на скаляр.

    Args:
        matrix: Исходная матрица.
        scalar: Числовой множитель.

    Returns:
        Матрица после умножения на скаляр.

    Example:
        >>> multiply_by_scalar([[1, 2], [3, 4]], 2)
        [[2, 4], [6, 8]]
    """
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    return result

def multiply_matrices(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    """
    Перемножает две матрицы (стандартное матричное умножение).

    Args:
        matrix1: Первая матрица размера m×k.
        matrix2: Вторая матрица размера k×n.

    Returns:
        Матрица размера m×n после умножения.

    Raises:
        ValueError: Если количество столбцов matrix1 не равно количеству строк matrix2.

    Example:
        >>> multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)

    if cols_matrix1 != rows_matrix2:
        raise ValueError("Несовместимые размеры матриц для умножения")

    rows_result = len(matrix1)
    cols_result = len(matrix2[0])

    result = [[0 for _ in range(cols_result)] for _ in range(rows_result)]

    for i in range(rows_result):
        for j in range(cols_result):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    """
    Транспонирует матрицу (меняет строки и столбцы местами).

    Args:
        matrix: Исходная матрица размера m×n.

    Returns:
        Транспонированная матрица размера n×m.

    Example:
        >>> transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    if not matrix or not matrix[0]:
        raise ValueError("Матрица не может быть пустой")

    rows = len(matrix)
    cols = len(matrix[0])

    # Проверка, что все строки одинаковой длины
    for row in matrix:
        if len(row) != cols:
            raise ValueError("Все строки должны иметь одинаковое количество столбцов")

    transposed = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
    return transposed



def trace(matrix: list[list[float]]) -> float:
    """
    Вычисляет след матрицы (сумму диагональных элементов).

    Args:
        matrix: квадратная матрица

    Returns:
        Сумма диагональных элементов (след матрицы)

    Raises:
        ValueError: если матрица не квадратная

    Example:
        >>> trace([[1, 2], [3, 4]])
        5.0
    """
    if not is_square(matrix):
        raise ValueError("Matrix must be square to calculate trace")

    trace_sum = 0.0
    for i in range(len(matrix)):
        trace_sum += matrix[i][i]
    return trace_sum



def is_square(matrix: list[list[float]]) -> bool:
    """
    Проверяет, является ли матрица квадратной.

    Args:
        matrix: любая матрица

    Returns:
        True, если матрица квадратная (количество строк == количеству столбцов),
        False в противном случае

    Example:
        >>> is_square([[1, 2], [3, 4]])
        True
        >>> is_square([[1, 2, 3], [4, 5, 6]])
        False
    """
    if not matrix:  # проверка на пустую матрицу
        return True  # пустая матрица считается квадратной по определению

    rows = get_rows(matrix)
    cols = get_cols(matrix)
    return rows == cols



def is_symmetric(matrix: list[list[float]]) -> bool:
    """
    Проверяет, является ли матрица симметричной относительно главной диагонали (A = A^T).

    Args:
        matrix: квадратная матрица

    Returns:
        True, если матрица симметрична, False в противном случае

    Raises:
        ValueError: если матрица не квадратная

    Example:
        >>> is_symmetric([[1, 2], [2, 3]])
        True
        >>> is_symmetric([[1, 2], [3, 4]])
        False
    """
    if not is_square(matrix):
        raise ValueError("Matrix must be square to check symmetry")

    size = len(matrix)

    # Проверка симметрии: A[i][j] должно быть равно A[j][i] для всех i, j
    for i in range(size):
        for j in range(i + 1, size):  # проверяем только верхнюю треугольную часть
            if matrix[i][j] != matrix[j][i]:
                return False
    return True





