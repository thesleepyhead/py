#codechef april cookoff
T = input('enter no of test case')
try :
    Te = int(T)
except :
    print('wrong input')
    exit()
x = range(0,Te)
for b in x :
    N = input('total no of floor')
    Q = input('no of request')
    try :
        Qw = int(Q)
    except :
        print('wrong input')
        exit()
    y = range(0,Qw)
    ai = []
    ad = []
    for j in y :
        fi = input('enter initial floor')
        di = input('enter final floor')
        try :
            fii = int(fi)
            fdd = int(di)
        except :
            print('wrong input')
            exit()
        ai.append(fii)
        ad.append(fdd)
    tot = ai[0]
    f2 = 0
    for j in y :

        if ad[j]>ai[j] :
            f1 = ad[j]-ai[j]
        else :
            f1 = ai[j]-ad[j]
        if j!=0 :
            if ai[j]>ad[j-1] :
                f2 = ai[j]-ad[j-1]
            else :
                f2 = ad[j-1]-ai[j]
        ft = f1+f2
        tot = tot+ft
    print(tot)
