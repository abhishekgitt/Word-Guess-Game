def show_joined(some_list):
    joined_list = ''.join(some_list)
    print(joined_list)

def check_dash_list(before_list,after_list):
    firs_list = ''.join(before_list)
    second_list = ''.join(after_list)
    if firs_list == second_list:
        return 0