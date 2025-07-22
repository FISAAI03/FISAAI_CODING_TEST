# 리스트의 최대공약수를 구하고, 그 최대공약수의 모든 약수를 구하는 함수
def get_gcd_divisors(numbers):
    # 두 수의 최대공약수(GCD)를 구하는 내부 함수
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # 리스트 전체의 최대공약수 계산
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = gcd(current_gcd, num)

    # 최대공약수의 모든 약수를 구함
    divisors = []
    for i in range(1, int(current_gcd ** 0.5) + 1):
        if current_gcd % i == 0:
            divisors.append(i)
            # 예를 들어 36의 약수 중 6*6처럼 중복되지 않게 하기 위해 조건 체크
            if i != current_gcd // i:
                divisors.append(current_gcd // i)

    return sorted(divisors)  # 오름차순 정렬하여 반환

# 문제의 해결 함수
def solution(arrayA, arrayB):
    # arrayA의 최대공약수와 그 약수 리스트 구하기
    divisors_of_gcd_A = get_gcd_divisors(arrayA)
    gcd_A = divisors_of_gcd_A[-1]  # 가장 큰 약수 = 최대공약수

    # arrayB의 최대공약수와 그 약수 리스트 구하기
    divisors_of_gcd_B = get_gcd_divisors(arrayB)
    gcd_B = divisors_of_gcd_B[-1]  # 가장 큰 약수 = 최대공약수

    candidate_results = []

    # A의 최대공약수로 B 배열의 어떤 수든 나누어 떨어지지 않을 경우 → 유효 후보
    if gcd_A > 1:
        is_valid = True
        for b in arrayB:
            if b % gcd_A == 0:
                is_valid = False
                break
        if is_valid:
            candidate_results.append(gcd_A)

    # B의 최대공약수로 A 배열의 어떤 수든 나누어 떨어지지 않을 경우 → 유효 후보
    if gcd_B > 1:
        is_valid = True
        for a in arrayA:
            if a % gcd_B == 0:
                is_valid = False
                break
        if is_valid:
            candidate_results.append(gcd_B)

    # 유효한 최대공약수가 있다면 그 중 가장 큰 값을 반환, 없다면 0 반환
    if candidate_results:
        return max(candidate_results)
    else:
        return 0
