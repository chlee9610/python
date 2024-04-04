def get_fixed_price(saleprice, sale) :
    price = saleprice / ((100 - sale)/100)
    return price

sale = int(input('할인율은? '))
a = int(input('A 상품의 할인된 가격은? '))
price_a = get_fixed_price(a,sale)
b = int(input('B 상품의 할인된 가격은? '))
price_b = get_fixed_price(b,sale)
print('A 상품의 정가는',int(price_a),'원')
print('B 상품의 정가는',int(price_b),'원')
