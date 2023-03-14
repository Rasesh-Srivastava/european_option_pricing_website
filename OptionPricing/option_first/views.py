import math
from django.shortcuts import render
from django.http import HttpResponse
from math import log, sqrt, pi, exp
from scipy.stats import norm
# Create your views here.
# def home(request):
#     data = request.POST.get('name')
# def calc(S):
#     # print(type(S))
#     # temp = S.upper()
#     return S

def d1(S,K,T,r,sigma):
    return 0.0 if (T==0 or K==0 or sigma == 0) else (log(S/K)+(r+(sigma**2)/2.0)*T)/(sigma*sqrt(T))
def d2(S,K,T,r,sigma):
    return 0.0 if (T==0 or K==0 or sigma == 0) else d1(S,K,T,r,sigma)-sigma*sqrt(T)

def bs_call(S,K,T,r,sigma):
    return 0.0 if T==0 else S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
  
# def bs_put(S,K,T,r,sigma):
#     return K*exp(-r*T)-S+bs_call(S,K,T,r,sigma)
def bs_put(S,K,T,r,sigma):
    return 0.0 if T==0 else K*exp(-r*T)*norm.cdf(-1*d2(S,K,T,r,sigma)) - S*norm.cdf(-1*d1(S,K,T,r,sigma))

def calc_u(sigma,T,n=2.0):
    t = float(T)
    s = float(sigma)
    rough = math.sqrt(t/n)
    u = math.exp(s*rough)
    return float(u)

def calc_p(r,T,u,d,n=2.0):
    if(T!=0.0):
        t = float(T)
        R = float(r)
        p = float(0.0 if (u==0 or u == d) else (math.exp(R*(t/n)) - d)/(u-d))
        return p
    else:
        return 0.0

def calc_Cuu(S,u,K):
    s = float(S)
    Cuu = max(u*u*s - float(K),0)
    return float(Cuu)

def calc_Cdd(S,d,K):
    s = float(S)
    Cdd = max(d*d*s - float(K),0)
    return float(Cdd)

def calc_Cud(S,u,d,K):
    s = float(S)
    Cud = max(u*d*s - float(K),0)
    return float(Cud)

def calc_TwoStep_calloptionPrice(p,r,T,Cuu,Cud,Cdd,n=2.0):
    C = float(p*p*Cuu + (1-p)*(1-p)*Cdd + 2*p*(1-p)*Cud)
    C = C * math.exp(-1*float(r)*float(T))
    return C

def calc_PutOptionPrice(S,K,r,T,C):
    P = float(C) - float(S) + (float(K) * math.exp(-1*float(r)*float(T)))
    return P

def nCr(n, r):
 
    return (fact(n) / (fact(r)* fact(n - r)))
 
# Returns factorial of n
def fact(n):
    if n == 0:
        return 1
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res

def calc_a(S,K,n,d,u):
    if(S==0):
        return n+1
    else:
        rough = float((math.log(K/S) - n*math.log(d))/(math.log(u)-math.log(d)))
        a = int(math.floor(rough)) + 1
        return int(a)


def calc_sum(a,n,p):
    summation = 0.0
    if(a>n):
        return 0.0
    else:
        for j in range(a,n+1):
            summation = summation + (nCr(n,j) * (math.pow(p,j)) * (math.pow(1-p,n-j)))

        return summation


def home(request):
    # S = float(0.0 if request.POST.get('S') is None else request.POST.get('S'))
    # T = float(0.0 if request.POST.get('T') is None else request.POST.get('T'))
    # K = float(0.0 if request.POST.get('K') is None else request.POST.get('K'))
    # r = float(0.0 if request.POST.get('r') is None else request.POST.get('r')) / 100.0
    # sigma = float(0.0 if request.POST.get('sigma') is None else request.POST.get('sigma'))
    # n = float(1000 if request.POST.get('n') is None else request.POST.get('n'))
    # n = int(math.floor(n))
    # u = calc_u(sigma,T)
    # d = 1/(u)
    # p = calc_p(r,T,u,d)
    # Cuu = calc_Cuu(S,u,K)
    # Cdd = calc_Cdd(S,d,K)
    # Cud = calc_Cud(S,u,d,K)
    # C = calc_TwoStep_calloptionPrice(p,r,T,Cuu,Cud,Cdd)
    # P = calc_PutOptionPrice(S,K,r,T,C)



    # bs_C = bs_call(S,K,T,r,sigma)
    # bs_P = bs_put(S,K,T,r,sigma) #- calc_PutOptionPrice(S,K,r,T,bs_C)



    # # n = 1000
    # u_n = calc_u(sigma,T,n)
    # d_n = 1/u_n
    # p_n = calc_p(r,T,u_n,d_n,n)
    # p_dash = float(u_n*p_n*math.exp(-1*r*(T/n)))
    # a = calc_a(S,K,n,d_n,u_n)
    # # print (fact(7))
    # n_C = S*calc_sum(a,n,p_dash) - K*math.exp(-1*r*(T))*calc_sum(a,n,p_n)
    # n_P = calc_PutOptionPrice(S,K,r,T,n_C)
    # print(nCr(6,3))
    # print(type(S))
    # print(T)
    return render(request, 'option_first/home.html')#,{'title': 'Rasesh','S': S,'T': T,'K': K,'r': r*100,'sigma': sigma,'u': u,'d': d,'p': p,'Cuu':Cuu,'Cdd':Cdd,'Cud':Cud,'C':round(C,6),'P':round(P,6),'bs_C':round(bs_C,6),'bs_P':round(bs_P,6),'n_C':round(n_C,6),'n_P':round(n_P,6),'n':n,'u_n':u_n,'d_n':d_n,'a':a,'p_n':p_n,'p_dash':p_dash})
def black(request):
    S = float(0.0 if request.POST.get('S') is None else request.POST.get('S'))
    T = float(0.0 if request.POST.get('T') is None else request.POST.get('T'))
    K = float(0.0 if request.POST.get('K') is None else request.POST.get('K'))
    r = float(0.0 if request.POST.get('r') is None else request.POST.get('r')) / 100.0
    sigma = float(0.0 if request.POST.get('sigma') is None else request.POST.get('sigma'))
    bs_C = bs_call(S,K,T,r,sigma)
    bs_P = bs_put(S,K,T,r,sigma) #- calc_PutOptionPrice(S,K,r,T,bs_C)
    return render(request, 'option_first/black.html',{'title': 'Rasesh','S': S,'T': T,'K': K,'r': r*100,'sigma': sigma,'bs_C':round(bs_C,6),'bs_P':round(bs_P,6)})


def twoStep(request):
    S = float(0.0 if request.POST.get('S') is None else request.POST.get('S'))
    T = float(0.0 if request.POST.get('T') is None else request.POST.get('T'))
    K = float(0.0 if request.POST.get('K') is None else request.POST.get('K'))
    r = float(0.0 if request.POST.get('r') is None else request.POST.get('r')) / 100.0
    sigma = float(0.0 if request.POST.get('sigma') is None else request.POST.get('sigma'))
    # n = float(1000 if request.POST.get('n') is None else request.POST.get('n'))
    # n = int(math.floor(n))
    u = calc_u(sigma,T)
    d = 1/(u)
    p = calc_p(r,T,u,d)
    Cuu = calc_Cuu(S,u,K)
    Cdd = calc_Cdd(S,d,K)
    Cud = calc_Cud(S,u,d,K)
    C = calc_TwoStep_calloptionPrice(p,r,T,Cuu,Cud,Cdd)
    P = calc_PutOptionPrice(S,K,r,T,C)
    return render(request, 'option_first/twoStep.html',{'title': 'Rasesh','S': S,'T': T,'K': K,'r': r*100,'sigma': sigma,'u': u,'d': d,'p': p,'Cuu':Cuu,'Cdd':Cdd,'Cud':Cud,'C':round(C,6),'P':round(P,6)})


def nStep(request):
    S = float(0.0 if request.POST.get('S') is None else request.POST.get('S'))
    T = float(0.0 if request.POST.get('T') is None else request.POST.get('T'))
    K = float(0.0 if request.POST.get('K') is None else request.POST.get('K'))
    r = float(0.0 if request.POST.get('r') is None else request.POST.get('r')) / 100.0
    sigma = float(0.0 if request.POST.get('sigma') is None else request.POST.get('sigma'))
    n = float(1000 if request.POST.get('n') is None else request.POST.get('n'))
    n = int(math.floor(n))
    u_n = calc_u(sigma,T,n)
    d_n = 1/u_n
    p_n = calc_p(r,T,u_n,d_n,n)
    p_dash = float(u_n*p_n*math.exp(-1*r*(T/n)))
    a = calc_a(S,K,n,d_n,u_n)
    # print (fact(7))
    n_C = S*calc_sum(a,n,p_dash) - K*math.exp(-1*r*(T))*calc_sum(a,n,p_n)
    n_P = calc_PutOptionPrice(S,K,r,T,n_C)
    return render(request, 'option_first/nStep.html',{'title': 'Rasesh','S': S,'T': T,'K': K,'r': r*100,'sigma': sigma,'n_C':round(n_C,6),'n_P':round(n_P,6),'n':n,'u_n':u_n,'d_n':d_n,'a':a,'p_n':p_n,'p_dash':p_dash})


# 600*445