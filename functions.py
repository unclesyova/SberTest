



def dict_to_str(dictionary):
    
    inversed_dict = {}
    for key, value in dictionary.items():
       for val in value:
           inversed_dict[val] = key
    sorted_by_key = sorted(inversed_dict.items(), key=lambda x: x[0])
    result = "".join(list(zip(*sorted_by_key))[1])  

    return result 
