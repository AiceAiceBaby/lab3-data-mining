from tabulate import tabulate

if __name__ == "__main__":
    print("ITERATION 1")
    print("M1 = 4")
    print("M2 = 11")
    print()
    data1 = [
                [2, 2, 9, 'C1'],
                [4, 0, 7, 'C1'],
                [10, 6, 1, 'C2'],
                [12, 8, 1, 'C2'],
                [3, 1, 8, 'C1'],
                [20, 16, 9, 'C2'],
                [30, 26, 19, 'C2'],
                [11, 7, 0, 'C2'],
                [25, 21, 14, 'C2'],
            ]
    print (tabulate(data1, headers=["Datapoint", "D1", "D2", "Cluster"]))

    print()
    print("ITERATION 2")
    print("M1 = (2+3+4)/3= 3")
    print("M2 = (10+12+20+30+11+25)/6= 18")
    print()

    data2 = [
                [2, 1, 16, 'C1'],
                [4, 1, 14, 'C1'],
                [3, 0, 15, 'C1'],
                [10, 7, 8, 'C1'],
                [12, 9, 6, 'C2'],
                [20, 17, 2, 'C2'],
                [30, 27, 12, 'C2'],
                [11, 8, 7, 'C2'],
                [25, 22, 7, 'C2'],
            ]
    print (tabulate(data2, headers=["Datapoint", "D1", "D2", "Cluster"]))

    print()
    print("ITERATION 3")
    print("M1 = (2+3+4+10)/4= 4.75")
    print("M2 = (12+20+30+11+25)/5= 19.6")
    print()

    data3 = [
                [2, 2.75, 17.6, 'C1'],
                [4, 0.75, 15.6, 'C1'],
                [3, 1.76, 16.6, 'C1'],
                [10, 5.25, 9.6, 'C1'],
                [12, 7.25, 7.6, 'C1'],
                [20, 15.25, 0.4, 'C2'],
                [30, 25.25, 10.4, 'C2'],
                [11, 6.25, 8.6, 'C1'],
                [25, 20.25, 5.4, 'C2'],
            ]
    print (tabulate(data3, headers=["Datapoint", "D1", "D2", "Cluster"]))