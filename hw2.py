def exchange(money) :
    coin500 = money // 500    
    m1 = money % 500
    coin100 = m1 // 100
    m2 = m1 % 100
    coin50 = m2 // 50
    m3 = m2 % 50
    coin10 = m3 // 10
    print('500원 동전의 개수:', coin500)
    print('100원 동전의 개수:', coin100)
    print('50원 동전의 개수:', coin50)
    print('10원 동전의 개수:', coin10)
    
def get_interger(prompt) :
    return int(input(prompt))

m = get_interger('동전으로 교환하고자 하는 금액은? ')
exchange(m)
