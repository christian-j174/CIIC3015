def main():
    x1 = float(input("Enter the x1 point: "))
    x2 = float(input("Enter the x2 point: "))
    y1 = float(input("Enter the y1 point: "))
    y2 = float(input("Enter the y2 point: "))
    slope = (y2 - y1) / (x2 - x1)
    slope = round(slope, 2)

    fh = open('file_points.txt', 'w')
    fh.write( str(x1) + '\n' )
    fh.write( str(x2) + '\n')
    fh.write( str(y1) + '\n' )
    fh.write( str(y2) + '\n' )
    fh.write(str(f"The slope is: {slope}"))
    fh.close()
    return str(slope)



result = main()

print("The slope:", result)