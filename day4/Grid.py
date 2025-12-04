class Grid:
    def __init__(self, width, height):

        if width < 1 or height < 1:
            raise Exception("Must specify valid dimensions")
        
        self.width = width
        self.height = height
        self.grid = {}


    def add_element(self, x, y, element):
        if x > self.width - 1 or x < 0:
            raise Exception("Invalid location provided for x")
        
        if y > self.width - 1 or y < 0:
            raise Exception("Invalid location provided for y")
        
        self.grid[(x,y)] = element
    
    
    def get_value(self, x, y):
        return self.grid[(x, y)]

    def element_in_range(self, x, y):
        x_in_range = (x <= (self.width - 1)) and x >= 0
        y_in_range = (y <= (self.height - 1)) and y >= 0
        return x_in_range and y_in_range
    

    def append_if_in_range(self, x, y, neighbours_to_check):
        if self.element_in_range(x, y):
            neighbours_to_check.append((x, y))


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
    

    def print(self):
        for y in range(0, self.width):
            line = ""
            for x in range(0, self.height):
                line += self.get_value(x,y)
            print(line)