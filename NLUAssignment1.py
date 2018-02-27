import re
import math

            
            
        
    
def get_freq(x,y):
    s1=' '.join(x)
    s2=' '.join(y)
    n=len(re.findall(s1,s2))
    return n
    

def N_gram(x,N):
      m=len(x)
      s=[]
      for i in range(m):
           if len(x[i:i+N])==N:
               s.append(x[i:i+N])
      return s        	


def get_probability(x,N,L=0):
    m=len(x)
    d1={};d2={}
    m2=N-1
    count=0
    for i in range(m):
        S=' '.join(x[i])
        g=re.findall(r'\b\w+\b',S)
        g.insert(len(g),'</s>')
        g.insert(0,'<s>')
        a=N_gram(g,N)
        m1=len(a)
        if N>=2:
            for j in range(m1):
                s1=' '.join(a[j])
                s1=s1.lower()
                a2=a[j][0:m2]
                s2=' '.join(a2)
                s2=s2.lower()
                if s2!='<s>':
                    if s1 not in d1:
                        d1[s1]=get_freq(a[j],g)
                    else:
                        d1[s1]=d1[s1]+get_freq(a[j],g)
                    if s2 not in d2:
                        d2[s2]=get_freq(a2,g)
                    else:
                        d2[s2]=d2[s2]+get_freq(a2,g)
                    f1=d1[s1];f2=d2[s2]
                    d1[s1]=(float(f1)/f2)
        else:
             for j in range(m1):
                 s1=' '.join(a[j])
                 s1=s1.lower()
                 if s1!='<s>':
                     if s1 not in d1:
                         d1[s1]=get_freq(a[j],g)
                     else:
                         d1[s1]=d1[s1]+get_freq(a[j],g)
                     count=count+d1[s1]
    #Laplace Smoothing for unigram
    if N==1:
        for k,v in d1.items():
            d1[k]=float(v)/count
        count=count+len(d1)
    return [d1,count]

             
         

            
def perplexity(y,d,N,L1):
    #y is test data


    PP=0
    m=len(y)
    count=0
    for i in range(m):
        S=' '.join(y[i])
        g=re.findall(r'\b\w+\b',S)
        count=count+len(g)
        g.insert(len(g),'</s>')
        g.insert(0,'<s>')
        a=N_gram(g,N)
        L1count=0
        m1=len(a)
        for j in range(m1):
            s3=' '.join(a[j])
            s3=s3.lower()
            if s3 in d:
                PP=PP+math.log(d[s3])
#                count=count+1
            else:
                n1=len(a[j])
                for k in range(1,n1-1):
                    Z=a[j][k:n1]
                    lenZ=len(Z)
                    s4=' '.join(Z)
                    s4=s4.lower()
                    if s4 in d:
                        PP=PP+math.log(d[s4])
                        L1count=L1count+1
#                        count=count+1
                        break
                    if s4 not in d and lenZ==1:
                        PP=PP+math.log( float(1)/L1)
#                        count=count+1
    print(count)
    PP=math.exp(-PP/count)    
    return PP
       
            
             
        
        
        
        
    
			
			
		
