from sklearn.metrics import precision_score, recall_score, confusion_matrix

x=[1,0,0,1,1]
y=[0,1,0,1,0]

precision=precision_score(x,y)
recall=recall_score(x,y)

print("Precision API : ",precision);
print("Recall API : ",recall);

mat=confusion_matrix(x,y)

true_negative=mat[0,0]
true_positive=mat[1,1]
false_negative=mat[0,1]
false_positive=mat[1,0]

precision=true_positive/(true_positive+false_positive)
recall=true_positive/(true_positive+false_negative)

print("Precision Confusion Matrix : ",precision);
print("Recall Confusion Matrix : ",recall);
