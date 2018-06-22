from sys import argv


if __name__ == '__main__':
    '''
        Verify number of columns for each line in csv if less than arg
        del the line.
    '''
    if len(argv) < 4:
        print(argv[0], 'ficIn nbColumns ficOut')
        exit()

    fileIn = argv[1]
    nbArgs = int(argv[2])
    fileOut = argv[3]


    with open(fileIn, 'r') as f:
        with open(fileOut, 'w') as fOut:
            content = f.readlines()
            for line in content:
                t = line.split(';')
                if len(t) < 6:
                    continue
                fOut.write(line)
