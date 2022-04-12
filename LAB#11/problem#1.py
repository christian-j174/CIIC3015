def main():
    """Write the numbers from 1 trough 10
    to a file named numbers.txt"""
    fhandle = open('numbers.txt','w')
    for number in range(1,10):
        fhandle.write(str(number) + '\n')
    fhandle.close()



if __name__ == '__main__':
    main()