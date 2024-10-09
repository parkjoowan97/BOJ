def solution(s):
    number = list(s.split(" "))
    new_num = []
    for num in number:
        new_num.append(int(num))
    maximum,minimum = str(max(new_num)), str(min(new_num))
    answer = minimum + " " + maximum
     
    return answer