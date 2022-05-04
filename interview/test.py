nlst = []
while True:
    try:
        nlst.append(int(input()))
    except:
        count = 0
        positive = []
        for i in nlst:
            if i < 0:
                count += 1
            else:
                positive.append(i)
        print(count)
        if sum(positive):
            print('{:.1f}'.format(sum(positive)/len(positive)))
        else:
            print(0.0)

# num_list = []
# while True:

#     try:
        
#         num_list.append(int(input()))
#     except:
#         print(num_list)
        # over_list, down_list = [], []
#         for i in num_list:
#             if i < 0:
#                 down_list.append(i)
#             else:
#                 over_list.append(i)
#         print(len(down_list))
#         if len(over_list) > 0:
#             print(round(sum(over_list) /len(over_list), 1))
#         else:
#             print(0.0)
#         break
