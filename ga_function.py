import random

def generatePopulation(n):# 隨機產生初始population，有n個
    
    population = []
    
    for i in range(n):
        
        population.append('%.10f'%(random.uniform(1, 2)))#產生50個0-1間小數10位的數字
        
    for i in range(len(population)):
        
        population[i] = float(population[i]) 
           
    return population

def getfitness(population):
    
    score_list = []  
    
    for i in range(len(population)): # 跑過每一個population
        
        population[i] = float(population[i])
        score = abs((population[i] * population[i]) - 2) #平方-2，最好的fitness是接近0，越大越差
        score_list.append(score)

    return score_list

def select(population, score_list, n): #只要留下前n個
    
    #先把float的population改成str且後面有補0的
    for i in range(len(population)): # 先全部換成str型態
        
        population[i] = '%.10f'%population[i]
        
    for i in range(1, len(score_list)):#泡泡排序，小到大，population依據score排序
        
        for j in range(0, len(score_list) - i):
            
            if score_list[j] > score_list[j+1]:
                
                score_list[j], score_list[j + 1] = score_list[j + 1], score_list[j]
                population[j], population[j + 1] = population[j + 1], population[j] #population排序根據他的score來排，表現好在前面    
    
    new_pop = population[:int(n)] # 留下前n個
    
    return new_pop

def cross(population, n,):
    
    original_population = population #先保留一份原本的population
    new_pop = population #放子帶
    cross_pop = []

    for i in range(len(new_pop)): #把除了自己每一個都交配過
        
        for j in range(len(population)):
            
            if type(new_pop[i]) != str:
                
                new_pop[i] = '%.10f'%population[i]
                
            if type(population[j]) != str:
                
                population[j] = '%.10f'%population[j]
                
            if new_pop[i] != population[j]: #如果不是自己就看要換哪個小東東
                
                for k in range(2, 12):

                    prob = random.uniform(0, 1) #隨機產生一個機率
                    
                    if prob < 0.5:
                        
                        if type(new_pop[i]) != float and type(new_pop[i]) != list:#是str才要轉成福點數統一
                            
                            new_pop[i] = float(new_pop[i])
                            
                        if type(new_pop[i]) == list:
                            
                            new_pop[i] = ''.join(new_pop[i])
                            new_pop[i] = float(new_pop[i])
                            
                        new_pop[i] = '%.10f'%new_pop[i]
                        new_pop[i] = list(new_pop[i])
                        
                        if k == 2:
                            
                            new_pop[i][k] = population[j][11]
                            
                        else:
                            
                            new_pop[i][k] = population[j][k-1]

                    elif prob >= 0.5:
                        
                        if type(new_pop[i]) != float and type(new_pop[i]) != list:#是str才要轉成福點數統一
                            
                            population[i] = float(population[i])
                            
                        if type(new_pop[i]) == list:
                            
                            new_pop[i] = ''.join(new_pop[i])
                            new_pop[i] = float(new_pop[i])
                            
                        new_pop[i] = '%.10f'%new_pop[i]
                        new_pop[i] = list(new_pop[i])
                        
                        if k == 11:
                           
                            new_pop[i][k] = population[j][2]
                            
                        else:
                            
                            new_pop[i][k] = population[j][k+1]

            new_pop[i] = ''.join(new_pop[i])
            cross_pop.append(new_pop[i])

        cross_pop_score = getfitness(cross_pop)
        cross_pop = select(cross_pop, cross_pop_score, n*0.5) # 需要在這邊把部分刪除，不然記憶體會爆掉，設定留前20%
    
    ori_score_list = getfitness(original_population) #原始pop的score list
    ori_result = select(original_population, ori_score_list, n*0.5) # 子代留下n的一半(表現好的)
    cross_pop_score_list = getfitness(cross_pop) #cross完的
    result = select(cross_pop, cross_pop_score_list, n*0.5) # 原始母體也留下n的一半(表現好的)

    for i in range(len(ori_result)):
        
        result.append(ori_result[i]) # 合併
    
    return result

def mutation(population): #做突變

    for i in range(len(population)):
        
        prob = random.uniform(0, 1)#隨機產生一個0~1的機率，大於0.9那個population就要做mutation，不然就略過那個population
        population[i] = str(population[i])
        
        if prob > 0.9:
            
            for j in range(2,12):#從小數點後開始突變
                
                prob = random.uniform(0, 1) #隨機產生一個機率
                
                if prob > 0.5: #如果機率大於0.8，當次的小東東就要被突變的數字換掉
                    
                    population[i] = list(population[i])
                    population[i][j] = random.randrange(0, 10) #產生一個0-9的數字去替代掉原本的數字
                    population[i] = ''.join('%s' %id for id in population[i])

    return population