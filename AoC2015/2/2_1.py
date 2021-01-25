#WORKINPROGRESS

input = open('input.txt', 'r+')
lines = input.readlines()

dimensions = [0, 0, 0]
l = w = h = 0
prior_char_index = char_index = 0
paper = totpaper = slack = 0

for line in lines:

    for char in line:
        
        if char == 'x' or (char_index + 1) == (len(line)):

            if l == 0:
                l = int(line[prior_char_index:char_index])
                prior_char_index = char_index + 1

            elif w == 0:
                w = int(line[prior_char_index:char_index])
                prior_char_index = char_index + 1

            elif h == 0:
                h = int(line[prior_char_index:char_index])
                prior_char_index = char_index + 1

        char_index += 1

    #print(str(l) + ' ' + str(w) + ' ' + str(h))
    dimensions[0] = l * w
    dimensions[1] = w * h
    dimensions[2] = l * h
    #print(dimensions)
    dimensions.sort()
    slack = dimensions[0]  

    for i in range(0, len(dimensions)):
        dimensions[i] = dimensions[i] * 2
        paper = paper + dimensions[i]

    #print(paper)
    totpaper = totpaper + paper + slack
    #print(slack)
    #print(paper)
    #print(totpaper)
    
    for i in range(0, len(dimensions)):
        dimensions[i] = 0
    paper = slack = 0
    l = w = h = 0
    char_index = prior_char_index = 0

print(totpaper)
