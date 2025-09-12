def partitionString(s: str) -> list[str]:
    seen = set()
    segments = []
    seg = ""
    for char in s:
        seg += char
        if seg not in seen:
            seen.add(seg)
            segments.append(seg)
            seg = ""
    
    return segments

print(partitionString(input()))



    


