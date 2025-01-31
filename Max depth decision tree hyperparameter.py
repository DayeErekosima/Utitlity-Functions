import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def max_depth_error(md, x_train, x_test, y_train, y_test):
    '''Function tunes the max depth of the decision tree classifier and return the accuracy at different depths
    '''
    model = DecisionTreeClassifier(max_depth= md, random_state=42)
    model.fit(x_train, y_train)
    train_acc = model.score(x_train, y_train) * 100
    test_acc = model.score(x_test, y_test)  * 100
    return {'Max Depth': md, 'Training Accuracy': train_acc, 'Test Accuracy': test_acc}

accuracy_df = pd.DataFrame([max_depth_error(md) for md in range(1,21)])
accuracy_df