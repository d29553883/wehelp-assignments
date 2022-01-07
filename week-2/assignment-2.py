def calculate(min,max):
    sum_number = 0
    for i in range(min,max+1):
        sum_number += i
    print(sum_number) 

calculate(1,3)
calculate(4,8)




data = {
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}


def avg(data):
    a= data["employees"]
    salary_total=0
    for key in a:
        salary_total+=key['salary']
    salary_total = salary_total/(len(a))
    print(salary_total) 


avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
})



def maxProduct(nums):
    x = []
    for i in nums:
        for j in nums:
            if i!=j:
                x.append(i*j)
            else:
                continue
    print(max(x))



maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0]) 



def twoSum(nums, target):    
    dict = {};                        
    list = [];
    for x in range(len(nums)):
        targetTemp = nums[x];                       
        key = target - targetTemp;
        if(key in dict):
            list.append(dict[key]);
            list.append(x);
            return list
        else:
            dict[targetTemp] = x

result=twoSum([2, 11, 7, 15], 9)
print(result)

def maxZeros(nums):
    max_count = 0
    count = 0
    for i in nums: 
        if i == 0:
            count = count + 1   
        else:
            max_count = max((count,max_count))
            count = 0
    max_count = max((count,max_count))
    print(max_count)


maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])



