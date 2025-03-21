def solution(n, k):
    # 10진법 수를 k진법으로 변환
    k_num = ""
    while n!=0:
        k_num += str(n%k)
        n = n // k
        if n==0:
            break

    k_num = k_num[::-1]
    
    # 0을 기준으로 숫자들을 필터해서 저장
    lst = k_num.split('0')
    cnt = 0
    
    # 숫자가 소수인지 판별함
    for i in lst:
        if i == "1":
            pass
        elif (i == "2") or (i == "3") or (i == "5") or (i == "7"):
            cnt += 1
        elif i != "":
            num = int(i)
            nn = 0
            for j in range(2, int(num**(1/2)) + 1):
                if (num % j == 0):
                    nn += 1
            if nn < 1:
                cnt += 1
                    
    return cnt