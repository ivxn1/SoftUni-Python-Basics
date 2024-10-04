x_height = float(input())
y_lenght = float(input())
h_height_triangle = float(input())

green_paint_liter = 3.4
red_paint_liter = 4.3

# front/back wall
area_front_back_wall = x_height * x_height
area_front_door = 1.2 * 2
area_front_wall_without_door = area_front_back_wall - area_front_door

green_paint_front_wall = area_front_wall_without_door / green_paint_liter
green_paint_back_wall = area_front_back_wall / green_paint_liter

# side walls
area_side_wall = x_height * y_lenght
area_side_window = 1.5 * 1.5
area_side_wall_without_window = area_side_wall - area_side_window

green_paint_side_walls = (area_side_wall_without_window / green_paint_liter) * 2

# roof - rectangle
area_rectangle = x_height * y_lenght
red_paint_rectangles = 2 * (area_rectangle / red_paint_liter)

# roof - triangle
area_triangle = 1/2 * x_height * h_height_triangle
red_paint_triangles = 2 * (area_triangle / red_paint_liter)

total_green_paint = green_paint_back_wall + green_paint_front_wall + green_paint_side_walls
total_red_paint = red_paint_triangles + red_paint_rectangles

print(f'{total_green_paint: .2f}')
print(f'{total_red_paint: .2f}')
