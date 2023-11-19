import graphviz 
import pandas as pd
import numpy as np
from pyrsistent import m
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn import tree
from re import X
from matplotlib import axis, pyplot as plt
from sklearn.tree import _tree



# Firsts things first! Read the file
def readFile():
    df = pd.read_csv('data.csv',sep=';', names=['age', 'sex', 'cp', 'rbp', 'sc', 'fbs', 'rer', 'maxhra', 'exia', 'oldp', 'slope', 'majorv','thal', 'target'])
 
    print(df)
    return df 

def hello():
    msg = 'Here we are! Its time to analyze a heart disease data set and develop a Decision Tree for it.'  \
        + '\nLets do this! Below you can see the data set. A special thanks to Machine learning Repository for the contribution.' \
        + '\nYou can see more about it in https://archive.ics.uci.edu/ml/datasets/statlog+(heart)\n' \
        + '\nSome definitions given:\n' \
        + '\nAccording to https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118 : Heart disease describes a range of conditions that affect your heart.\n '\
        + '\nHeart diseases include: Blood vessel disease: such as coronary artery disease (CAD) , Heart rhythm problems (arrhythmias) , Heart valve disease , Disease of the heart muscle and Heart infection.\n '\
    
    print(msg)

#we find the correlation on target between other attributes
def correlation(df):
    target_corr = df.corr()['target'].abs()
    print(target_corr)
    #heartDisease_df.columns  = ['age', 'sex', 'cp', 'rbp', 'sc', 'fbs', 'rer', 'maxhra', 'exia', 'oldp', 'slope', 'majorv','thal']
    print('Correlation on target: ')
    Array_corr = target_corr.to_numpy()
    print(Array_corr)
    corr = df.corr().abs()
    
    plt.figure(figsize=(20,12))
    sns.set_context('notebook' , font_scale= 1.3)
    sns.heatmap(corr, cmap="Reds", annot=True)
    plt.show()
    print(corr)
    return Array_corr,target_corr

def remove(array,corr,df):
    j=-1
    for i in array:
        j = j + 1
        if(i< 0.02):        
            thesis = j
    if (thesis == 0):
        head = "age"
    elif (thesis == 1):
        head = "sex"
    elif (thesis == 2):
        head = "cp"
    elif (thesis == 3):
        head = "rbp"
    elif (thesis == 4):
        head = "sc"
    elif (thesis == 5):
        head = "fbs"
    elif (thesis == 6):
        head = "rer"
    elif (thesis == 7):
        head = "maxhra"
    elif (thesis == 8):
        head = "exia"
    elif (thesis == 9):
        head = "oldp"
    elif (thesis == 10):
        head = "slope"
    elif (thesis == 11):
        head = "majorv"
    elif (thesis == 12):
        head = "thal"
    df =  df.drop([head], axis=1)
    print('NEW DATAFRAME AFTER PROCCESS')
    print(df)
    return df

#def boxPlot(df):
#df_

#fig, axs = plt.subplots(1, 2, figsize=(16,5))
#axs = axs.flatten() 

    # iterate through each column in df_num and plot
#for i, col_name in enumerate(df_num):
          #sns.boxplot(x="target", y=col_name, data=df, ax=axs[i])
          #axs[i].set_xlabel("target", weight = 'bold')
         # axs[i].set_ylabel(f"{col_name}", weight='bold')
#plt.show()
#print("Box plots are ready!")

   
def imbalanceDf(df):
    
    diff = df[df['target'] == 1]['target'].value_counts().to_numpy()[0] - df[df['target'] == 2]['target'].value_counts().to_numpy()[0] 
    
    if(diff < 100):
        print('The Dataset is balanced') 
    else:
         print('The Dataset is imbalanced')
        

def splitDf(df):
    print(df)
    x = df.drop(['target'], axis=1)
    y = df['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state= 124)
    print (x_train)
    print("--------------------------------------------------------------")
    print (y_train)
    print("--------------------------------------------------------------")
    print (x_test)
    print("--------------------------------------------------------------")
    print (y_test)
    print("--------------------------------------------------------------")

    return  y_train, y_test


def balanceSplitDf(df):
    X = df.drop(['target'], axis=1).to_numpy()
    y = df['target'].to_numpy()
    feature_names = df.drop(['target'], axis=1).columns
    labels = df['target'].unique()
    stratSplit = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=124)
    stratSplit.get_n_splits(X, y)
    print(stratSplit.get_n_splits(X, y))
    print(stratSplit)
    # train_index, test_index = stratSplit.split(X, y)
    # print(train_index)
    for train_index, test_index in stratSplit.split(X, y):
        print("TRAIN:", train_index)
        print("TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
    return   X_train,  y_train,  X_test, y_test, feature_names, labels

def targetAnalogyCheck(y_train, y_test, arg):

    if( arg == 'unbalanced' ):
        trainAnalogy_1 = y_train[y_train == 1].value_counts()
        trainAnalogy_2 = y_train[y_train == 2].value_counts()

        testAnalogy_1 = y_test[y_test == 1].value_counts()
        testAnalogy_2 = y_test[y_test == 2].value_counts()

        print("Train target analogy: ")
        print(trainAnalogy_1)
        print(trainAnalogy_2)

        diff_train = trainAnalogy_1.to_numpy()[0] - trainAnalogy_2.to_numpy()[0]
        sum_train = trainAnalogy_1.to_numpy()[0] + trainAnalogy_2.to_numpy()[0]

        diff_test = testAnalogy_1.to_numpy()[0] - trainAnalogy_2.to_numpy()[0]
        sum_test = testAnalogy_1.to_numpy()[0] + trainAnalogy_2.to_numpy()[0]

        print("Percentage")
        print(diff_train/sum_train)

        print("Percentage")
        print( diff_test/sum_test)
    

        print("Test target analogy: ")
        print(testAnalogy_1)
        print(testAnalogy_2)
    
    elif (arg == "balanced"):

        print(y_train)
        print(y_test)
        k=0
        l=0
        for i in y_train:

            if(i == 1):
                k = k+1 
        for j in y_test:
            if(j == 1):
                l = l+1 
        
        k_ = y_train.size - k
        l_ = y_test.size - l

        print("Train analogy percentage:")
        print((k-k_)/y_train.size)
        print("Test analogy percentage:")
        print((l-l_)/y_test.size)

def originalAnalogy(df):
    y = df['target'].to_numpy()

    k=0
    for i in y:
        if(i == 1):
             k = k + 1       
    k_ = y.size - k 

    print("Original analogy percentage: ")
    print((k-k_)/y.size)

def decisionTree(x_train, y_train, df):

    feature_names = df.drop(['target'], axis=1).columns
    labels = df['target']
    clf = tree.DecisionTreeClassifier(max_depth = 4)
    clf.fit(x_train, y_train)

    dot_data = tree.export_graphviz(clf, out_file=None, 
                        feature_names=feature_names,
                        class_names=['1' , '2'],
                        filled=True,
                        rounded=True,
                        special_characters=True) 

    graph = graphviz.Source(dot_data) 
    graph.render("heart-disease_dep6__") 
    # plt.figure(figsize=(20,10), facecolor ='k')
    # a =tree.plot_tree(clf)             
    # plt.show()
    print("Decision Tree Plotted")
    text_representation = tree.export_text(clf)
    print(text_representation)
    rules = get_rules(clf, feature_names, ['1' , '2'])
    for r in rules:
        print(r)

def get_rules(tree, feature_names, class_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    paths = []
    path = []
    
    def recurse(node, path, paths):
        
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            p1, p2 = list(path), list(path)
            p1 += [f"({name} <= {np.round(threshold, 3)})"]
            recurse(tree_.children_left[node], p1, paths)
            p2 += [f"({name} > {np.round(threshold, 3)})"]
            recurse(tree_.children_right[node], p2, paths)
        else:
            path += [(tree_.value[node], tree_.n_node_samples[node])]
            paths += [path]
            
    recurse(0, path, paths)

    # sort by samples count
    samples_count = [p[-1][1] for p in paths]
    ii = list(np.argsort(samples_count))
    paths = [paths[i] for i in reversed(ii)]
    
    rules = []
    for path in paths:
        rule = "if "
        
        for p in path[:-1]:
            if rule != "if ":
                rule += " and "
            rule += str(p)
        rule += " then "
        if class_names is None:
            rule += "response: "+str(np.round(path[-1][0][0][0],3))
        else:
            classes = path[-1][0][0]
            l = np.argmax(classes)
            rule += f"class: {class_names[l]} (proba: {np.round(100.0*classes[l]/np.sum(classes),2)}%)"
        rule += f" | based on {path[-1][1]:,} samples"
        rules += [rule]
        
    return rules
    
if __name__ == '__main__' : 
    
    hello()

    heartDisease_df = readFile()

    print("--------------Lets begin the analysis--------------")

    Array_corr,target_corr = correlation(heartDisease_df)

    heartDisease_df = remove(Array_corr, target_corr, heartDisease_df) 

    imbalanceDf(heartDisease_df)

    originalAnalogy(heartDisease_df)

    #boxplot(heartDisease_df)
    y_train, y_test = splitDf(heartDisease_df)

    X_train,  Y_train,  X_test, Y_test, feature_names, labels = balanceSplitDf(heartDisease_df)

    targetAnalogyCheck(y_train, y_test, "unbalanced")

    targetAnalogyCheck(Y_train, Y_test, "balanced")   

    decisionTree(X_train, Y_train, heartDisease_df)

    
    