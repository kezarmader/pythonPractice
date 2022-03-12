#
# Complete the function below.
#
# The function accepts an INTEGER_ARRAY arr as parameter 
# and is expected to return a TWO_DIMENSIONAL_INTEGER_ARRAY.
#
def main():
    results = get_permutations([1,2,2])
    print(results)

def get_permutations(arr):
    # Write your code here
    results = []
    get_permutations_helper(arr, 0, [], results)
    return results
    
def get_permutations_helper(arr, subProblem, partialSolution, results):
    if subProblem == len(arr):
        results.append(list(partialSolution))
        return
    
    isVisited = {}
    for i in range(subProblem, len(arr)):
        if isVisited.get(partialSolution[i]) == None:
            isVisited[partialSolution[i]] = partialSolution[i]
            partialSolution[i], partialSolution[subProblem] =  partialSolution[subProblem], partialSolution[i]
            get_permutations_helper(arr, subProblem + 1, partialSolution, results)
            partialSolution[i], partialSolution[subProblem] =  partialSolution[subProblem], partialSolution[i]
        else:
            print('av', partialSolution, isVisited)

if __name__ == '__main__':
    main()