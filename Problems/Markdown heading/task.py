def heading(header, hashes=0):
    pre_header = ""
    for x in range(0, hashes):
        pre_header += "#"
        if x < 5:
            x += 1
        else:
            break
    if pre_header == "":
        pre_header = "#"
    return pre_header + " " + header

