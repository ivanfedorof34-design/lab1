"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    result = np.zeros_like(vectors[0])
    for i in range(len(matrices)):
        result = result + matrices[i] @ vectors[i]
    return result
    raise NotImplementedError  # TODO


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    result = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] > threshold:
                result[i, j] = 1
    return result
    raise NotImplementedError  # TODO


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    result = []
    for row in matrix:
        unique = []
        for value in row:
            if value not in unique:
                unique.append(value)
        result.append(unique)
    return result
    raise NotImplementedError  # TODO


def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    result = []
    for j in range(matrix.shape[1]):
        unique = []
        for i in range(matrix.shape[0]):
            value = matrix[i, j]
            if value not in unique:
                unique.append(value)
        result.append(unique)
    return result
    raise NotImplementedError  # TODO


def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    np.random.seed(seed)
    matrix = np.random.normal(mean, std, (rows, columns))
    row_means = np.mean(matrix, axis=1)
    column_means = np.mean(matrix, axis=0)
    row_variances = np.var(matrix, axis=1)
    column_variances = np.var(matrix, axis=0)
    return MatrixStatistics(
        matrix=matrix,
        row_means=row_means,
        column_means=column_means,
        row_variances=row_variances,
        column_variances=column_variances,
    )
    raise NotImplementedError  # TODO


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    result = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            if (i + j) % 2 == 0:
                result[i, j] = first
            else:
                result[i, j] = second
    return result
    raise NotImplementedError  # TODO


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    image[:] = background_color
    center_y = image_height // 2
    center_x = image_width // 2
    start_y = center_y - height // 2
    end_y = start_y + height
    start_x = center_x - width // 2
    end_x = start_x + width
    image[start_y:end_y, start_x:end_x] = shape_color
    return image
    raise NotImplementedError  # TODO


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    image[:] = background_color
    center_y = image_height // 2
    center_x = image_width // 2
    for y in range(image_height):
        for x in range(image_width):
            value = ((x - center_x) ** 2) / (semi_axis_x ** 2) + \
                    ((y - center_y) ** 2) / (semi_axis_y ** 2)
            if value <= 1:
                image[y, x] = shape_color
    return image
    raise NotImplementedError  # TODO


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    mean = np.mean(values)
    variance = np.var(values)
    std = np.std(values)
    maxima = []
    minima = []
    for i in range(1, len(values) - 1):
        if values[i] > values[i - 1] and values[i] > values[i + 1]:
            maxima.append(i)
        if values[i] < values[i - 1] and values[i] < values[i + 1]:
            minima.append(i)
    moving_average = []
    for i in range(len(values) - window + 1):
        part = values[i:i + window]
        moving_average.append(np.mean(part))
    return TimeSeriesStatistics(
        mean=mean,
        variance=variance,
        std=std,
        maxima=maxima,
        minima=minima,
        moving_average=np.array(moving_average),
    )
    raise NotImplementedError  # TODO


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    if class_count is None:
        class_count = int(np.max(labels)) + 1
    result = np.zeros((len(labels), class_count), dtype=int)
    for i in range(len(labels)):
        result[i, labels[i]] = 1
    return result
    raise NotImplementedError  # TODO
