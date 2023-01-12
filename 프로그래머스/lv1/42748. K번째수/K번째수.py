def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        slice_list = array[commands[i][0]-1:commands[i][1]]
        sorted_list = sorted(slice_list)
        answer.append(sorted_list[commands[i][2]-1])
    return answer