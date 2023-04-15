def order(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I want to order {} {}'.format(args[0],kwargs['item3']))

order(10,29,63,89,67,89,item1='milk',item2='chips',item3='eggs',item4='fruits')
