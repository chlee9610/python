def read_single_digit(sn) :
    if sn == 1 :
        return '일'
    elif sn == 2 :
        return '이'
    elif sn == 3 :
        return '삼'
    elif sn == 4 :
        return '사'
    elif sn == 5 :
        return '오'
    elif sn == 6 :
        return '육'
    elif sn == 7 :
        return '칠'
    elif sn == 8 :
        return '팔'
    elif sn == 9 :
        return '구'
    elif sn == 0 :
        return '영'

def read_number(rn) :
    hn = rn // 100
    tn = (rn % 100) // 10
    on = rn % 10
    a = read_single_digit(hn)
    b = read_single_digit(tn)
    c = read_single_digit(on)
    print(f'{a} {b} {c}')


num = int(input('세 자리 정수 입력: '))
read_number(num)
