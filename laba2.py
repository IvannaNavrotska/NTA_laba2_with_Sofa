from sympy import factorint
import time

def algoritm_evklida_with_a_b(b:int, a:int):
    '''
    Алгоритм евкліда теж таблична реалізація, при цікавості можна вивести табличкою. Ця функція була переписана з того, що я писала на с++
    ще на першому курсі, але повертаємо тільки обернене
    а число за модулем якого ми шукаємо обернене
    b число для якого ми шукаємо обернене
    додатково є вимога що а та b повинні бути інтови, щоби випадково не було приколів
    '''
    if b>a:
        b%=a
    q=0
    u=1; v=0; u1=0; v1=1
    while a>b:
        c=a
        while c>b:
            c=c-b
            q+=1
        a=b; b=c
        u2=u-u1*q
        v2=v-v1*q
        u=u1; v=v1; u1=u2; v1=v2; q=0
    return v1
def summ(x_spisok, p):
    sum=0
    for i in range(len(x_spisok)):
        sum+=x_spisok[i]*pow(p, i)
    return sum
 
def massive_x(x_spisok, l, p, beta, alpha, n, p_index, tabliza):
    for i in range(1, l+1):
        stepin=summ(x_spisok, p)
        p_v_stevini=pow(alpha, stepin, n)
        dla_x=beta*algoritm_evklida_with_a_b(p_v_stevini, n)
        stepin=int((n-1)/(p**(len(x_spisok)+1)))
        #print("stepin=", stepin)
        dla_x=pow(dla_x, stepin, n)
        #print("dla=", dla_x)
        #print(x_spisok, i)
        x_n=poshuk(p, tabliza, dla_x, p_index )
        x_spisok.append(x_n)
    #x_spisok.pop()
    #print(x_spisok)
   # for i in x_spisok:
   #     print(i)
    #print(x_spisok[4], x_spisok, len(x_spisok))
    #print(x_spisok[5])
    return x_spisok
    

def chine_theorem(porivniia):
    m=1
    for i in range(len(porivniia)):
        m*=porivniia[i][1]
    m_i=[]
    n_i=[]
    x0=0
    for i in range(len(porivniia)):
        t=m/porivniia[i][1]
        m_i.append(t)
        k=algoritm_evklida_with_a_b(m_i[i], porivniia[i][1])
        n_i.append(k)
        x0+=t*k*porivniia[i][0]%m
    return int(x0)





def poshuk(znachennia_p,tabliza, dla_xo, i ):
    x0=None
    for j in range(znachennia_p):
            #print(dla_xo, tabliza[i][j], j)
            if dla_xo==tabliza[i][j]:
                x0=j
                #print("j=",j)
                break
    return x0
    
def sum_for_x(spisok, p, l):
    x=0
    for i in range(l):
        print(spisok[i], p**i )
        x+=spisok[i]*p**i
    x=x%(p**l)
    return [x, p**l]


def algoritm_SPG(alpha, beta, n):
    kanonich_rozklad=factorint(n-1)
    znachennia_p=list(kanonich_rozklad.keys())
    znachennia_l=list(kanonich_rozklad.values())
    tabliza=[]
    for i in range(len(znachennia_p)):
        spisok=[]
        for j in range(znachennia_p[i]):
            stepin=int(((n-1)*j)/znachennia_p[i])
            r=pow(alpha, stepin, n)
            spisok.append(int(r))
        tabliza.append(spisok)

    
    x_spisok=[]
    porivniia=[]
    for i in range(len(znachennia_p)):
        print(i)
        x_spisok=[]
        massive_x(x_spisok, znachennia_l[i], znachennia_p[i], beta, alpha, n, i, tabliza)
        x=sum_for_x(x_spisok, znachennia_p[i], znachennia_l[i])
        porivniia.append(x)
       



    x=chine_theorem(porivniia)

            
        
    return x


print(algoritm_SPG(5, 11, 97))




def brute_force(alpha, beta, p):

    five_minutes = 300
    start_time = time.time()

    for x in range(0, p-1):

        if time.time() - start_time > five_minutes:
            return "час вийшов"

        if (alpha**x)%p == beta%p:
            return x
        
    return "дл не знайдено, потрібно більше часу"


print(brute_force(5, 11, 97))



def time_(alg, alpha, beta, p):

    times = []
    
    for i in range(6):
        
        start = time.time()
        alg(alpha, beta, p)
        finish = time.time()

        times.append(finish - start)
        
    av_time = sum(times)/6

    return av_time


alpha = 117
beta = 191
p = 739

spg = algoritm_SPG(alpha, beta, p)
bf = brute_force(alpha, beta, p)

print(f"СПГ: х = {spg}")
print(f"Перебір: х = {bf}")

time1 = time_(algoritm_SPG, alpha, beta, p)
time2 = time_(brute_force, alpha, beta, p)

print("час роботи СПГ:", time1)
print("час роботи перебору:", time2)



