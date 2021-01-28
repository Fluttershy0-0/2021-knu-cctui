import numpy as np
import pandas as pd
df = pd.read_csv("maliuk_data.csv")
clmns=['H.period', 'UD.period.t', 'H.t', 'UD.t.i', 'H.i', 'UD.i.e', 'H.e',
       'UD.e.five', 'H.five', 'UD.five.Shift.r', 'H.Shift.r', 'UD.Shift.r.o',
       'H.o', 'UD.o.a', 'H.a', 'UD.a.n', 'H.n', 'UD.n.l', 'H.l', 'UD.l.Return',
       'H.Return']


def extractFeatures(df, clmns, unimb, n):
    features = pd.DataFrame({'subject':np.array([],dtype=str),
                             'sessionIndex': np.array([],dtype=int),
                             'rep' : np.array([],dtype=int),
                             'letter' : np.array([],dtype=str)})
    for i in range(unimb*n):
        features["f{}".format(i+1)]=np.array([],dtype=float)

    for i in range(df.shape[0]):

        for j in range(0,len(clmns)-unimb*n,unimb):
            row = {"subject": df.iloc[i]["subject"],
                   'sessionIndex' : df.iloc[i]["sessionIndex"],
                   'rep': df.iloc[i]["rep"],
                   'letter' : clmns[j][2:]}
            for k in range(unimb*n):
                row["f{}".format(k+1)] = df[clmns].iloc[i, j+k]
            features = features.append(row, ignore_index=True)
    return features


with open('maliuk_unigram_features.csv', "w") as fu:
    with open('maliuk_bigram_features.csv', "w") as fb:
        with open('maliuk_trigram_features.csv', "w") as ft:
            dfu = extractFeatures(df, clmns, 2, 1)
            dfu.to_csv(fu,header= True, line_terminator='\n', index=False)
            dfb = extractFeatures(df, clmns, 2, 2)
            dfb.to_csv(fb, header=True, line_terminator='\n', index=False)
            dft = extractFeatures(df, clmns, 2, 3)
            dft.to_csv(ft, header=True, line_terminator='\n', index=False)