filename=input("Enter the file name: ")
fh=open(filename)
track = dict()

for line in fh:
    line = line.strip()
    enrollment = line[:line.find(',')]          #search the first comma
#----------------------------------------------------------------
    lineV1 = line[line.find(',') + 1:]          #desde comma #1 hasta la segunda comma
    name_student = lineV1[:lineV1.find(',')]
#----------------------------------------------------------------
    lineV2 = lineV1[lineV1.find(',')+1:]        #search the second comma
    program = lineV2[:lineV2.find(',')]         #desde la segunda comma hasta la tercera comma
#-------------------------------------
    total_credits = lineV2[lineV2.find(',') + 1:]
#-----------------------------------------------------
    if not (name_student in track):             #CREAR REGISTRO PARA CADA ESTUDIANTE
        track[name_student] = int(total_credits)
    elif enrollment == 'D':                     #LE RESTAMOS LOS CREDITOS AL BALANCE
        track[name_student] -= int(total_credits)
    else:                                       #LE SUMAMOS SU BALANCE
        track[name_student]  += int(total_credits)


for key, value in track.items():
    print(key, track[key])
#print(f"{name_student} {track[name_student]}")
