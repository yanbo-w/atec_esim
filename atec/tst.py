t = int(input())
for i in range(1, t + 1):
    d, s = [int(s) for s in input().split(" ")]
    res = ''
    if s==1:
        c,e = [float(s) for s in input().split(" ")]
        for day in range(1, d + 1):
            a,b = [float(s) for s in input().split(" ")]
            if 1.0*a/c+1.0*b/e <= 1.0:
                res+='Y'
            else:
                res+='N'
    elif s==2:
        c1,e1 = [float(s) for s in input().split(" ")]
        c2,e2 = [float(s) for s in input().split(" ")]
        k1 = 1.0*e1/(e2+0.0001)
        k2 = 1.0*c1/(c2+0.0001)
        for day in range(1, d + 1):
            a,b = [float(s) for s in input().split(" ")]
            if k1==k2:
                if a*e2-c2*(e1+e2-b) <= 0 and c1+c2-a >=0:
                    res+='Y'
                else:
                    res+='N'
            elif k1>k2:
                if a*e2-c2*(e1+e2-b)>=c1*e2-c2*e1 and c1+c2<=a:
                    res+='Y'
                else:
                    res+='N'
            elif k1<k2:
                if -a*e1+c1*(e1+e2-b)>=c1*e2-c2*e1 and c1+c2<=a:
                    res+='Y'
                else:
                    res+='N'
        print(res)
            