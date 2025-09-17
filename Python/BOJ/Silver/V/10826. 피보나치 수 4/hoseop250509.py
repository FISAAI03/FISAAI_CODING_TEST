n = int(input())

fn_1 = 1
fn_2 = 0
if n == 0:
    print(fn_2)
elif n == 1:
    print(fn_1)
else:
    for _ in range(2, n+1):
        fn = fn_1 + fn_2
        fn_2, fn_1 = fn_1, fn

    print(fn)
