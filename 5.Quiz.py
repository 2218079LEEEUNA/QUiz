def a(b):
    if len(b) != 13: # 주민번호 개수가 13이 아닐 경우 False
        return False

    c = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
     #for을 사용하여 각각의 숫자를 곱하고 더하고 range를 사용하여 검정 코드를 제외한 12개를 곱하고 더함.
    total = sum(int(b[i]) * c[i]for i in range(12)) # 주민등록번호와 미리 지정된 값 (c)를 곱해준다.

    remainder = total % 11 # 더한 결과를 11로 나누어 준다.

    result = 11 - remainder # 11에서 나머지의 결과를 뺀다.

    if result >= 10: # 주민등록번호 유효성 검사 결과가 10이나 그 이상인 경우가 나올 수 있기 때문에 그걸 처리해야 한다.
        result -= 10

    return result == int(b[12]) # 나머지와 검증코드가 같은지 확인하기

b = input("주민등록번호를 입력하세요: ") # 사용자에게 주민등록번호 입력받기
if a(b):
    print("유효한 주민등록번호입니다.") # 유효한지 유효하지 않은지 사용자에게 제공하기
else:
    print("유효하지 않은 주민등록번호입니다.")
