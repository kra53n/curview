def cur_expand(cur_name, cur_type, course, course_ruble=0):
    cur = {
        "name": cur_name,
        "cur_type": cur_type,
    }

    if cur_type == "cur" or "metal":
        cur["course_ruble"] = course

    if cur_type == "crypto_cur":
        cur["course_dollar"] = course
        cur["course_ruble"] = course * course_ruble

    return cur
