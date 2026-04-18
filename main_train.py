import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.model_selection import cross_validate,KFold




def train_model():

    train = pd.read_csv('inputs/train.csv')
    y = train.pop('SalePrice')
    y_train = y.iloc[:len(train)]
    y_test = y.iloc[len(train):]



    x_train = pd.read_csv('inputs/x_train_cleaned.csv')
    x_test = pd.read_csv('inputs/test.csv')

    cat_cols = x_test.select_dtypes(include=['str']).columns.tolist()

    encoder = pickle.load(open('outputs/encoder.pkl','rb'))
    encoder.transform(x_test[cat_cols])

    best_params = {'n_estimators': 100, 'max_depth': 16, 'min_impurity_decrease': 0.9, 'min_samples_split': 4}

    rf = RandomForestRegressor(
        **best_params,
        random_state=1412,
        n_jobs=8
    )
    cv = KFold(shuffle=True,n_splits=5,random_state=1412)
    result = cross_validate(
        rf,x_train,y_train,
        scoring='neg_root_mean_squared_error',
        cv = cv,
        return_train_score=True
    )

    print(abs(result['test_score'].mean()))
    print(abs(result['train_score'].mean()))

    rf.fit(x_train,y_train)
    with open('outputs/model.pkl','wb') as f:
        pickle.dump(rf,f)


if __name__ == '__main__':
    train_model()
