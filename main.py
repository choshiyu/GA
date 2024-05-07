from ga_function import generatePopulation, getfitness, cross, select, mutation
'''
# 二分逼近法先找到標準答案
def half_interval(x,precise):
    p = pow(10,precise)
    x *= p
    if x > p:
        low = p
        high = x
    else:
        low = 0
        high = p
    while(high - low > 1):
        mid = (high + low) // 2
        if (mid * mid // p) > x:
            high = mid
        else:
            low = mid
    s = str(low)
    res = s[0] + '.'
    for i in range(1,len(s)):
        res += s[i]
    return res
print(half_interval(2,10))'''
# ans --> 1.4142135624

if __name__ == '__main__':

    sum_appro = 0
    error_sum = 0
    count = 0
    n = 200 # population群的數目
    max_iter = 10 # 最多跑幾次
    
    population = generatePopulation(n)#先產生初始母體(產生隨機數字)
    
    while (count < max_iter):
        
        scorelist = getfitness(population)#population算分數，會得到一個分數的list
        population = select(population, scorelist, n)#population做選擇
        count += 1
        print('iteration:', count, '/best:', population[0], '/best score(least error):', min(scorelist))
        sum_appro += float(population[0])
        error_sum += min(scorelist) #把每次的error累計起來
        population = cross(population, n)#population交配
        population = mutation(population)#population突變
        
    print('population size:', n)
    print('max iteration set to:', max_iter)
    print('iteration times:', count)
    print('average error:', error_sum / count)
    print('average approximation', sum_appro / count)