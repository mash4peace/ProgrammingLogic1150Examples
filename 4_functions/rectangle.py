"""
Function to calculate rectangle areas
"""


def rectangle_area(height, width):
    area = height * width
    return area


def main():
    rect_height = float(input('Enter height of rectangle: '))
    rect_width = float(input('Enter width of rectangle: '))
    rect_area = rectangle_area(rect_height, rect_width)

    print(f'The area of this rectangle is {rect_area}')


main()
