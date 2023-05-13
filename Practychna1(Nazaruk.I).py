import numpy as np

def T(Tx,Ty,a):
    return [ float(a[0])+Tx, float(a[1])+Ty]


def S(Sx,Sy,a):
    return  [float(a[0])*Sx,  float(a[1])*Sy]


def R(r,a):
    return [float(a[0])*np.cos(r*np.pi/180)-float(a[1])*np.sin(r*np.pi/180),
            float(a[0])*np.sin(r*np.pi/180)+float(a[1])*np.cos(r*np.pi/180)]


c1=input('x axis component:')

c2=input('y axis component')


c = [c1,c2] 



for i in [0,0,0]:
    op = input('choose: T, R, or S ' )
    if op == 'S':
                    
        Sx = float(input('x axis Scalation: '))
   
        Sy = float(input('y axis Scalation: '))
    
        c = S(Sx,Sy,c)
        

    if op == 'T':
                    
        Tx = float(input('x axis Translation: '))
                    
        Ty = float(input('y axis Translation: '))
                      
        c = T(Tx,Ty,c)
        

    if op == 'R':
        r = float(input('Angle : '))
        c = R(r,c)
        
        
    else:
        pass
           
print('output vector: '+str(c))
