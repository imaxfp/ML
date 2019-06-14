import numpy as np
import logging

print(np.version)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s\n\r%(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler("{0}/{1}.log".format("./", "matrix")),
        logging.StreamHandler()
    ])
logger = logging.getLogger()

logger.info("np version - " + str(np.version))


# https://www.tutorialspoint.com/python/python_matrix.htm
def deleteRowForSpecificColumnMaxValue(matrix, column):

    num_rows, num_columns = matrix.shape
    # find max element in the column
    maxIndex = 0
    # Find max in specific column number
    maxTmp = 0
    for j in range(0, num_rows):
        if (maxTmp < matrix[j, column]):
            maxTmp = matrix[j, column]
            maxIndex = j
    return np.delete(matrix, maxIndex, 0)


# https://docs.scipy.org/doc/numpy-1.16.1/reference/arrays.ndarray.html
matrix = np.array([[1, 2, 3, 4],
                   [1, 2, 10, 4],
                   [1, 2, 3, 4],
                   [1, 2, 3, 7]])

# np.array([1,1,2,3,5,8,13,21,34]).reshape(3,3)
logger.info("initial matrix")
logger.info(matrix)

matrix = deleteRowForSpecificColumnMaxValue(matrix, 2)

logger.info("Matrix without row by max element in the specific column")
logger.info(matrix)

# logger.info("Matrix row by the specific column with max element in column have been deleted.", matrix)
