import sys
from sklearn.linear_model import perceptron
from sklearn.model_selection import train_test_split
import pandas as pd

words = []    # The word, correct label and pronunciation
data = []     # Training examples, e.g. feature vectors
labels = []   # Correct labels

for line in open('pronunciation_data.tsv').readlines():
    row = line.strip().split('\t')
    vec = []
    for i in row[3].split(','):
            vec.append(int(i))
    data.append(vec)
    labels.append(int(row[0]))
    words.append((row[1], row[2], int(row[0])))


net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(data,labels)

result = net.predict(data)

total = 0
correct = 0
for i in range(0, len(words)):
	if result[i] == words[i][2]:
		print('+', result[i], words[i])
		correct = correct + 1
	else:
		print('-', result[i], words[i])
	total = total + 1
print(correct/total)


#разобьем файл на train_data и test_data
pr_df = pd.read_table('pronunciation_data.tsv', sep = "\t", names = ["label", "word", "transcription", "vector"])

train_df, test_df = train_test_split(pr_df, test_size = 0.20)

train_data, test_data = [], []
train_labels, test_labels = [], []
train_words, test_words = [], []


for n, line in enumerate(train_df["label"]):
    train_vec = []
    for i in train_df["vector"].iloc[n].split(','):
            train_vec.append(int(i))
    train_data.append(train_vec)
    train_labels.append(int(train_df["label"].iloc[n]))
    train_words.append((train_df["word"].iloc[n], train_df["transcription"].iloc[n], int(train_df["label"].iloc[n])))

for n, line in enumerate(test_df["label"]):
    test_vec = []
    for i in test_df["vector"].iloc[n].split(','):
        test_vec.append(int(i))
    test_data.append(test_vec)
    test_labels.append(int(test_df["label"].iloc[n]))
    test_words.append((test_df["word"].iloc[n], test_df["transcription"].iloc[n], int(test_df["label"].iloc[n])))

net_1 = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net_1.fit(train_data, train_labels)

result_1 = net_1.predict(test_data)

total_1 = 0
correct_1 = 0
for i in range(0, len(test_words)):
    if result_1[i] == test_words[i][2]:
        print('+', result_1[i], test_words[i])
        correct_1 = correct_1 + 1
    else:
        print('-', result_1[i], test_words[i])
    total_1 = total_1 + 1
print(correct_1/total_1)
