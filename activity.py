from sklearn import tree
import csv

if __name__ == "__main__":
    X = []
    Y = []

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data_count = 0
        for row in csv_reader:
            isBig = row[0] == "big"
            isFar = row[1] == "far"
            isHabitable = row[2] == "yes"
            count = int(row[3])

            X.append([isBig, isFar, count])
            Y.append([isHabitable])
            data_count += 1
        print(f'Processed {data_count} data.')

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    while(True):
        isBig = input("Is it Big?[Y/n]: ").lower() == "y"
        isFar = input("Is it Far?[Y/n]: ").lower() == "y"
        count = int(input("how many count?: "))
        ans = clf.predict([[isBig, isFar, count]])[0]
        if (ans):
            print("The planet is habitable")
        else:
            print("The planet is NOT habitable")
        # tree.plot_tree(clf)

        print()
        if (input("Predict again?[Y/n]").lower() != "y"):
            break