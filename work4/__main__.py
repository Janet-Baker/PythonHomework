if __name__ == '__main__':
    input1 = input()
    TelDict = {'mayun': '13309283335',
               'zhaolong': '18989227822',
               'zhangmin': '13382398921',
               'Gorge': '19833824743',
               'Jordan': '18807317878',
               'Curry': '15093488129',
               'Wade': '19282937665'}
    print(TelDict.get(input1, "not found"))
