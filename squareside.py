'''
This module contains functions.
'''
def user_input() -> tuple:
    '''
    This function takes data from user: 3 sides of triangle and accuracy.
    Return tuple with this data.
    '''
    print("Enter only 4 parameters: 3 sides of triangle and accuracy")
    side_1 = input()
    side_2 = input()
    side_3 = input()
    accuracy = input() 
    return side_1, side_2, side_3, accuracy

def triangle_area(side_1: float, side_2: float, side_3: float) -> float:
    '''
    This function counts area of big triangle by using Geron's formula.
    Return area.
    >>> triangle_area(3, 4, 5)
    6.0
    '''
    sp = (side_1 + side_2 + side_3)/2 #semi-perimetr
    geron_area = (sp*(sp-side_1)*(sp-side_2)*(sp-side_3))**0.5
    return geron_area

def square_area(geron_area: float, side_3: float, accuracy: int) -> float:
    '''
    This function counts side of square in triangle.
    Return this side.
    >>> square_area(6, 4)
    4.760330578512396
    '''
    height = 2*geron_area/side_3
    side = 2*geron_area/(height + side_3)
    side = '{:.{}f}'.format(side, accuracy)
    return side

def write_in_file(side: float) -> None:
    '''
    This function writes area of aquare into a txt-file.
    Returns None
    '''
    with open("square_side.txt", "w", encoding="utf-8") as file:
        file.write(side)

if __name__ == '__main__':
    tpl = user_input()
    triangle = triangle_area(float(tpl[0]), float(tpl[1]), float(tpl[2]))
    square = square_area(triangle, float(tpl[2]), int(tpl[3]))
    write_in_file(square)