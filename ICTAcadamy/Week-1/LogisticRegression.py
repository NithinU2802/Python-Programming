import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

breast_cancer = load_breast_cancer()
X = breast_cancer.data
y = breast_cancer.target

feature_names = breast_cancer.feature_names
df = pd.DataFrame(X, columns=feature_names)


model = LogisticRegression()
num_features_to_select = 5  
rfe = RFE(estimator=model, n_features_to_select=num_features_to_select)
rfe.fit(X, y)


selected_features = df.columns[rfe.support_]
feature_ranking = rfe.ranking_

feature_rank_df = pd.DataFrame({'Feature': df.columns, 'Ranking': feature_ranking})

sorted_feature_rank_df = feature_rank_df.sort_values(by='Ranking')

print("Top {} Features:".format(num_features_to_select))
print(sorted_feature_rank_df.head(num_features_to_select))
