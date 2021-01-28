import numpy as np
import pandas as pd

df = pd.read_csv("DSL-StrongPasswordData.csv")

clmns=['sessionIndex',"rep",'H.period', 'UD.period.t', 'H.t', 'UD.t.i', 'H.i', 'UD.i.e', 'H.e',
       'UD.e.five', 'H.five', 'UD.five.Shift.r', 'H.Shift.r', 'UD.Shift.r.o',
       'H.o', 'UD.o.a', 'H.a', 'UD.a.n', 'H.n', 'UD.n.l', 'H.l', 'UD.l.Return',
       'H.Return']

df=df[clmns]
with open('extracted_features_uf.csv', "w") as fu:
    with open('extracted_features_bf.csv', "w") as fb:
        with open('extracted_features_tf.csv', "w") as ft:

            '''
                            unigram
            '''

            df.to_csv(fu, header=True, line_terminator='\n', index=False)

            '''
                            bigram
            '''

            durss=np.array(['period', 't', 'i', 'e', 'five', 'Shift.r','o', 'a', 'n', 'l', 'Return'], dtype="object")
            UDtss=np.array(['period.t', 't.i', 'i.e', 'e.five', 'five.Shift.r', 'Shift.r.o', 'o.a', 'a.n', 'n.l', 'l.Return'], dtype="object")

            durs=np.array(df["H."+durss])
            UDts=np.array(df["UD."+UDtss])

            bdur = durs[:,:-1] + durs[:,1:]
            bUD = UDts[:,:-1] + UDts[:,1:]

            datab=np.copy(bdur)
            for i in range(bUD.shape[1]):
                datab = np.insert(datab,2*i+1,bUD[:,i],1)

            clmns = ["sessionIndex", "rep"]
            for i in range((UDtss.shape[0])-1):
                clmns.append("H." + durss[i] + "+" + durss[i+1])
                clmns.append("UD." + UDtss[i] + "+" + UDtss[i+1])

            clmns.append("H." + durss[-2] + "+" + durss[-1])
            datab=np.concatenate((df[["sessionIndex", "rep"]],datab),axis=1)
            dfb = pd.DataFrame(datab, columns=pd.Series(clmns))
            dfb = dfb.astype({"sessionIndex": int, "rep": int})
            dfb.to_csv(fb, header= True, line_terminator='\n', index=False)

            '''
                            trigram
            '''

            tdur = durs[:, :-2] + durs[:, 1:-1] + durs[:, 2:]
            tUD = UDts[:, :-2] + UDts[:, 1:-1] + UDts[:, 2:]

            datat = np.copy(tdur)
            for i in range(tUD.shape[1]):
                datat = np.insert(datat, 2 * i + 1, tUD[:, i], 1)

            clmns = ["sessionIndex", "rep"]
            for i in range((UDtss.shape[0]) - 2):
                clmns.append("H." + durss[i] + "+" + durss[i + 1] + "+" + durss[i + 2])
                clmns.append("UD." + UDtss[i] + "+" + UDtss[i + 1] + "+" + UDtss[i + 2])
            clmns.append("H." + durss[-3] + "+" + durss[-2] + "+" + durss[-1])

            datat = np.concatenate((df[["sessionIndex", "rep"]], datat), axis=1)
            dft = pd.DataFrame(datat, columns=pd.Series(clmns))
            dft = dft.astype({"sessionIndex": int, "rep": int})
            dft.to_csv(ft, header=True, line_terminator='\n', index=False)