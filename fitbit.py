def sortBinaryNumbers(bitArrays):
    # Write your code here
    maxBitNum = 0
    # 1) convertim in binar
    for bits in bitArrays:
        max1 = max(bits)
        if maxBitNum < max1:
            maxBitNum = max1

    binaryArr = {}

    for i in range(len(bitArrays)):
        binaryNum = ['0'] * (maxBitNum + 1)
        for bit in bitArrays[i]:
            binaryNum[(maxBitNum) - bit] = '1'
        binaryNum = ''.join(binaryNum)
        binaryArr[i] = int(binaryNum, 2)

    binaryArr = sorted(binaryArr.items(), key=lambda keyVal: keyVal[1], reverse=True)

    result = []
    for tpl in binaryArr:
        result.append(tpl[0])
    return result

bitArrays = [ [0,1,2], [3,1,0] ]

sortBinaryNumbers(bitArrays)

