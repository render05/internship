# import pandas as pd
# df2 = pd.DataFrame({'A':[1,2,3,4,5],'B':[12,13,14,15,16]})
# df1 = pd.DataFrame({'A':[11,22,33,44],'B':[121,133,145,155]},index =[1,2,3,4])
# print(df1)
# print(df2)
# print("\n Addition\n",df1+df2)
# import pandas as pd

# df2 = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': ["a11", "b22", "55c", "d33", "e43"],
#     'C': ["a", "b", "c", "d", "e"]
# })

# df1 = pd.DataFrame({
#     'A': [6, 7, 9, 11, 8],
#     'B': ["a11", "b32", "55c", "d34", "e43"],
#     'C': ["ab", "bc", "cd", "de", "ef"]
# },
# index =[1,2,3,4,5])
# print(df1)
# print()
# print(df2)
# res=pd.concat([df1,df2],keys=['x','y'])
# print(res)
# import pandas as pd

# df2 = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': ["a11", "b22", "55c", "d33", "e43"],
#     'C': ["a", "b", "c", "d", "e"]
# })

# df1 = pd.DataFrame({
#     'A': [6, 7, 9, 11, 8],
#     'B': ["a11", "b32", "55c", "d34", "e43"],
#     'C': ["ab", "bc", "cd", "de", "ef"]
# },
# index =[1,2,3,4,5])
# print(df1)
# print()
# print(df2)
# # res=pd.concat([df1,df2],ignore_index= True)
# res=pd.concat([df1,df2],axis =1)
# print(res)

import pandas as pd 
df2 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ["a11", "b22", "55c", "d33", "e43"],
    'C': ["a", "b", "c", "d", "e"]
})

df1 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ["a11", "b32", "55c", "d34", "e43"],
    'C': ["ab", "bc", "c", "d", "ef"]
},
index =[1,2,3,4,5])
# res = df2.merge(df1,on='A')
# res = df2.merge(df1,on=['A','C'])
# res = df2.merge(df1,on='A',how = 'left')
# res = df2.merge(df1,on='A',how = 'outer')
res = df2.merge(df1,on='A',how = 'inner')
print(res)

