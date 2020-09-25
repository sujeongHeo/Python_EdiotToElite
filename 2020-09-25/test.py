from random import random
def random_arr (n):
    result = {}
    arrSize = int(n) * 2 + 1
    while(len(result) != arrSize):
        gen_num =int(random() * 100) * 2 -100 # 0 ~ 100
        if gen_num in result:
            continue
        else:
            result[gen_num] = (gen_num)
            
    print("result is : ", result)
    # print("result size is : ", len(result))
    result = list(result)
    print("list result : ",result)
    return result

get_num = input()
random_arr(get_num)

# var names = ["Mike","Matt","Nancy","Adam","Jenny","Nancy","Carl"];
# var uniq = names.reduce(function(a,b){
#     console.log(a, '여기는 뭐야 ??');
#     console.log(b, "여기는 뭐야 ??");
#     console.log(a.indexOf(b), "여기는 뭐야??");
#     if (a.indexOf(b) < 0 ) a.push(b);
#     return a;
# },[]);

# console.log(uniq, names) // [ 'Mike', 'Matt', 'Nancy', 'Adam', 'Jenny', 'Carl' ]


# for javascript we can use Math.floor(Math.random() * 100)
# const array = ['a', 1, 2, 'a', 'a', 3];

#1 : 'Set'
#2 .while (i < 10) {
#   text += "The number is " + i;
#   i++;
# }
# var dict = {};

# var names = ["Mike","Matt","Nancy","Adam","Jenny","Nancy","Carl"];

# var uniq = names.reduce(function(a,b){
# 	if (a.indexOf(b) < 0 ) a.push(b);
# 	return a;
#   },[]);

# console.log(uniq, names) // [ 'Mike', 'Matt', 'Nancy', 'Adam', 'Jenny', 'Carl' ]

# // 한 줄로 표현
# return names.reduce(function(a,b){if(a.indexOf(b)<0)a.push(b);return a;},[])


    

