class Color:
    def __init__(self, r, g, b):
        self.r = self.clamp(r)
        self.g = self.clamp(g)
        self.b = self.clamp(b)

    def __add__(self, color):
        new_r = self.clamp(self.r + color.r)
        new_g = self.clamp(self.g + color.g)
        new_b = self.clamp(self.b + color.b)
        return Color(new_r, new_g, new_b)
    
    def __sub__(self, color):
        new_r = self.clamp(self.r - color.r)
        new_g = self.clamp(self.g - color.g)
        new_b = self.clamp(self.b - color.b)
        return Color(new_r, new_g, new_b)

    @staticmethod
    def clamp(value):
        return max(0, min(255, value))
    
    def __repr__(self):
        return f'Color({self.r}, {self.g}, {self.b})'
