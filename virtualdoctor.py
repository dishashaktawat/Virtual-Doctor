sym={'low energy':'heart attack','anxiety':['heart attack','mental illness'],'breathing problem':['heart attack','lung disease'],
     'chest pain':['heart attack','lung disease'],'asthma':'lung disease','coughing up blood':'lung disease','constant worry':'mental illness',
     'feeling depressed':'mental illness','sad all the time':'mental illness','tension':'mental illness','fainting':'headache',
     'neck stiffness':'headache','fever':'headache'}
symm=['low enery','anxiety','breathing problem','chest pain','asthma','coughing up blood','constant worry','feeling depressed','sad all the time','tension',
      'fainting','neck stiffness','fever']

disease=['heart attack','lung disease','mental illness','headache']
m=[]
q=int(input('enter your status:1-> For add symptom \n 0-> For exit'))
while(q):
    symp=input('enter patient symptoms')
    r=symp in sym
    if(r==True):
        m.append(symp)
    print(m)
    print('enter 1 to add')
    print('enter 0 to exit')
    add=int(input('add more symptoms'))
    if(add):
        pass
    else:
        break
else:
    q=0
print(m)
print('corresponding disease')
for i in range(0,len(m)):
    for j in range(0,len(symm)):
        if(m[i] in symm[j]):
            d=symm[j]
            print(sym[d])
                
                    

    
