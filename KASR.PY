n1=int(input('nfractional:'))
d1=int(input('d fractional:'))

n2=int(input('n fractional'))
d2=int(input('d fractional'))
a={'n':n1,'d':d1}
b={'n':n2,'d':d2}

result={}

def sum():
    result={
    'n':a['n']*b['d']+b['n']*a['d'],
    'd':a['d']*b['d']
    }
    return result
    


def tafrigh():
    result={
        'n':a['n']*b['d']-b['n']*a['d'],
        'd':a['d']*b['d']
    }       
    return result
def zarb():
    result={
        'n':a['n']*b['d'],
        'd':a['d']*b['d']
    }
    return result
def taghsim():
    result={

        'n':a['n']*b['d'],
        'd':a['d']*b['n']
    }

    return result


while True:
    select=input('1-sum\n2-tafrigh\n3-zarb\n4-taghsim\n5-exit\n')
    if select=='1':
       res=sum()
       print(res)
    elif select=='2':
       res=tafrigh()
       print(res)
    elif select=='3':
        res=zarb()
        print(res)
    elif select =='4':
        res=taghsim()
        print(res)
    else:
        print('tahnk you')
        break

#######################


