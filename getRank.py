def get_rank (my_word):
    from functools import reduce 
    word_list = list(my_word)
    word_len = len(my_word)-1
    sorted_list = list(sorted(set(word_list)))
    
    count_list = {k: [i for i, j in enumerate(word_list) if j==k] for k in sorted_list}
    real_index = sorted_list.index(word_list[0])
    total_before = 0;
    for item in sorted_list:
        for i in count_list[item]:
            total_before += word_len- i + 1
        total_before -= reduce(lambda x,y: x+y,range(len(count_list[item])))
        if item==word_list[0]:
            break
    return total_before
# To run
value = input()
print(get_rank(value))
