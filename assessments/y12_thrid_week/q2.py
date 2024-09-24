def grade(per):
    if per >= 90:
        return 'A'
    elif per >= 80:
        return 'B'
    elif per >= 70:
        return 'C' 
    elif per >= 60:
        return 'D'
    elif per < 60:
        return 'F'
    #endif
#endfunction

print(grade(int(input())))
