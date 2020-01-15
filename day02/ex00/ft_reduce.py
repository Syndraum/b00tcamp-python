def ft_reduce(function_to_apply, list_of_inputs):
    res = list_of_inputs[0]
    for inputs in [list_of_inputs[1]]:
        res = function_to_apply(res, inputs)
    return res
