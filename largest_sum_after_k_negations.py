class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        count = 0;
        my_list = A
        new_list = []
        j = 0
        
        for index, item in enumerate(my_list):
            print(index, item)
            if j < K:
                smallest = min(my_list)
                #my_list.remove(smallest)
                print("smallest = "+str(smallest))
                smallest *= -1
                print("smallest = "+str(smallest))
                new_list.append(smallest)
                j += 1
            else:
                new_list.append(item)  
        print("new_list = "+str(new_list))
        print("sum(new_list) = "+str(sum(new_list)))
        return sum(new_list) 