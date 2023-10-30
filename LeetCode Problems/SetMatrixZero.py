class SetMatrixZeros:
    def setZeroes(self, matrix):
        self.matrixZeros(matrix)

    def matrixZeros(self, arr):
        firstCol = False
        firstRow = False

        # Step 1: check for zeros and mark in the first row/col
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    if j == 0:
                        firstCol = True
                    if i == 0:
                        firstRow = True
                    arr[i][0] = 0
                    arr[0][j] = 0

        # Step 2: make rows and cols zeros if they have a zero, except first row/col
        for i in range(1, len(arr)):
            for j in range(1, len(arr[0])):
                if arr[i][0] == 0 or arr[0][j] == 0:
                    arr[i][j] = 0

        # Step 3: making the first row and first col zero if required

        # at least one element is zero in the first row: therefore making all zero
        if firstRow:
            arr[0] = [0] * len(arr[0])

        # at least one element is zero in the first col: therefore making all zero
        if firstCol:
            for i in range(len(arr)):
                arr[i][0] = 0
