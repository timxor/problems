# problem type: geometric problem

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height) == 2:
            return min(height) * min(height)
        
        if len(height) == 3:
            return min(height) * max(height)
        
        # max
        head = max(height)
        head_i = height.index(head)
        height.remove(head)
        
        tail_one = max(height)
        t1i = height.index(tail_one)
        height.remove(tail_one)
        
        tail_two = max(height)
        t2i = height.index(tail_two)
        height.remove(tail_two)
        
        print("head = "+str(head))
        print("tail_one = "+str(tail_one))
        print("tail_two = "+str(tail_two))
        
        candiate_one = abs(t1i - head_i)
        c1_literal = t1i
        candiate_two = abs(t2i - head_i)
        c2_literal = t2i
        
        print("c1 = " + str(candiate_one))
        print("c2 = " + str(candiate_two))
        
        delta_size = 0
        
        delta_size = max(candiate_one, candiate_two)
        print("delta_size = " + str(delta_size))
        
        literal_second = 0
        if candiate_one == max(candiate_one, candiate_two):
            literal_second = c1_literal
        else:
            literal_second = c2_literal
        
        print("literal_second = " + str(literal_second))
        min_length = min(head, literal_second)
        print("min_length = " + str(min_length))
        
        final = min_length * min_length
        print("final = " + str(final))
        return final
    
    
    
        '''
        
        
        --
        input:[1,2,4,3]
        expected:4
        actual:9
        --
        input:[2,3,10,5,7,8,9]
        expected: 36
        --
        input:[1,8,6,2,5,4,8,3,7]
        expected:49
        actual:25 --> 36
        --
        
        
        
        
        '''
    
    
    
    
        
#         if candiate_two > candiate_one:
#             container_min_size = min(head, candiate_two)
#             if len(height) % 2 == 0:
#                 container_min_size += 2
#             else:
#                 container_min_size += 1
#         else:
#             container_min_size = min(head, candiate_one) + 1
        
#         print("container_min_size = " + str(container_min_size))
#         result = container_min_size * container_min_size
#         print(result)
#         return result
        
        # input_size = len(height) -1
        # red_head, red_tail = 0, 0
        # i, j = 0, len(height) -1
        
#         while i < j:
#             # locate max delta, for i & j, save them
            
#             i, j = i+1, j-1
        
        
        # of red, use smaller
        #smaller_red = min()
        
        # for index, item in enumerate(height):
        #     print(index, item)
        
        
        #return 9
