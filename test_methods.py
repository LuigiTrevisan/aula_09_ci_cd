import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14
    
def test_sum():
    # given two numbers
    num1 = 2
    num2 = 5
    
    # when we calculate the sum
    output = methods.sum(num1, num2)
    
    # then the sum should be 7
    assert output == 7
    
def test_difference():
    # given two numbers
    num1 = 2
    num2 = 5
    
    # when we calculate the difference
    output = methods.difference(num1, num2)
    
    # then the difference should be -3
    assert output == -3
    
def test_multiplication():
    # given two numbers
    num1 = 2
    num2 = 5
    
    # when we calculate the multiplication
    output = methods.multiplication(num1, num2)
    
    # then the multiplication should be 10
    assert output == 10
    
def test_division():
    # given two numbers
    num1 = 2
    num2 = 5
    
    # when we calculate the division
    output = methods.division(num1, num2)
    
    # then the division should be 0.4
    assert output == 0.4    
