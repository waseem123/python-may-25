def sorting(data, ascending=True):
    if ascending == True:
        data.sort()
    else:
        data.sort(reverse=True)
    return data
