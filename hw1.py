def get_radius(prompt) :
    r = int(input(prompt))
    return r

input_prompt=input('넓이를 구하고자 하는 원의 반지름은?  ')
a = int(input_prompt)

def get_circle_area(a) :
    area = a*a*3.14
    return area

b = get_circle_area(a)
print('반지름 4인 원의 넓이 = 3.14 x', a,'x', a,'=', b)
