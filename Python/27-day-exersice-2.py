# Упражнение 1

# Is the Triangle Valid?

# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов 
# три натуральных числа, и возвращает значение True, если существует невырожденный треугольник со 
# сторонами side1, side2, side3, или False в противном случае.

# Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.


def is_valid_triangle(side1, side2, side3):

    if (side1 + side2) > side3 and (side1+side3) > side2 and (side2+side3) > side1:
        return True

    else: 
        return False
    

side1 = int(input())
side2 = int(input())
side3 = int(input())

print(is_valid_triangle(side1, side2, side3))

#----------------------------------------------------------------

# Упражнение 2


