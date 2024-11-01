if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    scores_lst_avg = student_marks[query_name]
    len_scores_avg = len(scores_lst_avg)
    soma = 0
    for i in scores_lst_avg:
        soma += i
    avg_lst = soma/len_scores_avg
    #print("%.2f" % avg_lst)
    print(f'{avg_lst:.2f}')
   
    
    

    
