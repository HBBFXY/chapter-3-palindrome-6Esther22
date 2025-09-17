num=input("请输入一个5位数:")
if len(num)!=5 or not num.isdigit():
    print("输入错误,请输入一个5位纯数字!")
else:
    if num==num[::-1]:
        print("{:}是回文数".format(num)) 
    else:
        print("{:}不是回文数".format(num))
