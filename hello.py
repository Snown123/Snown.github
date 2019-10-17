print('==============================')
print('平方计算系统')
print('==============================')   
a=input('请输入你想计算的数字:\n')
while a !='Y':
    if a.isdigit():
        print('your answer is',int(a)*int(a))
    else:
        print('输入格式错误！')
    a=input('是否退出页面？Y/N:\n')
    if a == 'N':
        a=input('请输入你想计算的数字:\n')
if a=='Y':
    print('Bye!')
