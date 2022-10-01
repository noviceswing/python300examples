# 合并排序数组

class Solution:
    def mergeSortArray(self, A, B):
        i, j =0, 0
        c = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                c.append(A[i])
                i += 1
            else:
                c.append(B[j])
                j += 1
        while i < len(A):
            c.append(A[i])
            i += 1
        
        while j < len(B):
            c.append(B[j])
            j += 1

        return c

if __name__ == '__main__':
    A = [1,4,5]
    B = [2,5,6]
    solution = Solution()
    print(solution.mergeSortArray(A,B))