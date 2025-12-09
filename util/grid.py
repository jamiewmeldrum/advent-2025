class Grid:
    def __init__(self, width, height):

        if width < 1 or height < 1:
            raise Exception("Must specify valid dimensions")
        
        self.width = width
        self.height = height

        grid = {}
        for y in range(0, height):
            for x in range(0, width):
                grid[(x, y)] = "."
        self.grid = grid


    def add_element(self, x, y, element):
        if x > self.width - 1 or x < 0:
            raise Exception("Invalid location provided for x")
        
        if y > self.height - 1 or y < 0:
            raise Exception("Invalid location provided for y")
        
        if self.element_in_range(x, y):
            self.grid[(x,y)] = element

    
    def append_if_in_range(self, x, y, neighbours_to_check):
        if self.element_in_range(x, y):
            neighbours_to_check.append((x, y))
    
    
    def get_value(self, x, y):
        if self.element_in_range(x, y):
            return self.grid[(x, y)]
        else:
            None

    def get_row(self, y):
        row = []
        for x in range(0, self.width):
            row.append(self.grid[(x, y)])
        return row

    
    def count_char(self, char):
        count = 0
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.grid[(x, y)] == char:
                    count += 1
        return count


    def element_in_range(self, x, y):
        x_in_range = (x <= (self.width - 1)) and x >= 0
        y_in_range = (y <= (self.height - 1)) and y >= 0
        return x_in_range and y_in_range
    

    def print(self):
        for y in range(0, self.height):
            line = ""
            for x in range(0, self.width):
                line += str(self.get_value(x,y))
            print(line)

    
    def copy(self):
        other = Grid(self.width, self.height)
        other.grid = self.grid.copy()
        return other
    

    def count_nearest_neighbours_with_value(self, x, y, value):

        neighbours_to_check = []

        self.append_if_in_range(x-1, y-1, neighbours_to_check)
        self.append_if_in_range(x, y-1, neighbours_to_check)
        self.append_if_in_range(x+1, y-1, neighbours_to_check)
        self.append_if_in_range(x-1, y, neighbours_to_check)
        self.append_if_in_range(x+1, y, neighbours_to_check)
        self.append_if_in_range(x-1, y+1, neighbours_to_check)
        self.append_if_in_range(x, y+1, neighbours_to_check)
        self.append_if_in_range(x+1, y+1, neighbours_to_check)
        
        matching_count = 0
        for neighbour in neighbours_to_check:
            if self.grid[neighbour] == value:
                matching_count += 1

        return matching_count