class ProblemALG004r:
    def __init__(self, n, rotation=0):
        if n % 2 == 0:
            raise ValueError("The dimension 'n' must be odd")
        self.n = n
        self.rotation = rotation % 4
        self.magic_square = [[0] * n for k in range(n)]
        self.generate_magic_square()
        self.rotate()

    def generate_magic_square(self):
        num = 1
        row, col = 0, self.n // 2

        while num <= self.n * self.n:
            self.magic_square[row][col] = num
            num += 1
            
            new_row = (row - 1) % self.n
            new_col = (col + 1) % self.n
            
            if self.magic_square[new_row][new_col] != 0:
                row = (row + 1) % self.n
            else:
                row, col = new_row, new_col
    
    def rotate(self):
        rotated_square = [[0] * self.n for k in range(self.n)]
        for k in range(self.rotation):
            for i in range(self.n):
                for j in range(self.n):
                    rotated_square[j][self.n - 1 - i] = self.magic_square[i][j]
            self.magic_square = rotated_square
            rotated_square = [[0] * self.n for k in range(self.n)]
    
    def print_magic_square(self):
        for row in self.magic_square:
            print(" ".join(str(num) for num in row))
    
# Example usage
n = 7
rotation = 0
magic_square = ProblemALG004r(n, rotation)
magic_square.print_magic_square()
