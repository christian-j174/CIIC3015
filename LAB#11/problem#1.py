def main():
    """Write the numbers from 1 trough 10
    to a file named numbers.txt"""
    fhandle = open('numbers.txt','a')
    for number in range(1,11):
        fhandle.write(str(number))
    fhandle.close()


if __name__ == '__main__':
    main()