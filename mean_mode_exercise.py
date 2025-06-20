import pandas as pd
df = pd.read_csv("NIFTY 50-06-06-2024-to-06-06-2025.csv",parse_dates=["Date "])
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Shares Trade','Turnover (₹ Cr)']
# print(df.columns)
# print(df)

df["% Change"] = (df["Close"].pct_change()*100).round(2).fillna(0)
# print(df.head(10))


#c mean change 
df["Mean chnage"] = (df['% Change'].mean()).round(3)
# print(df.head(10))


# print(len(df))

# df = df.iloc[:len(df)//10]
# print(df)

# df['Cluster'] = df.index // 10
# print(df)

positive_mean = df[df['% Change']>0]["% Change"].mean()
negative_mean = df[df["% Change"]<0]["% Change"].mean()



length_of_positive_changes = len(df[df["% Change"]>=0])
length_of_negative_changes = len(df[df["% Change"]<0])

positive_df =df[df["% Change"]>=0]
negative_df = df[df["% Change"]<0]

positive_mean = positive_df["% Change"].mean().round(2)
negative_mean = negative_df["% Change"].mean().round(2)

positive_median = positive_df["% Change"].median()
negative_median = negative_df["% Change"].median()

positive_std = positive_df["% Change"].std()
negative_std = negative_df["% Change"].std()



print(f"total positive changes days are: {length_of_positive_changes}")
print(f"total negative changes days are: {length_of_negative_changes}")

df["+mean"] = positive_mean
df["-mean"] = negative_mean

df["+median"] = positive_median
df["-median"] = negative_median

df["+std"] = positive_std.round(2)
df["-std"] = negative_std.round(2)


# print(f"positive_mean is :{positive_mean}")
# print(f"negative_mean is :{negative_mean}")

# print(f"negative_mode is : {negative_mode}")
# print(f"positive_mode is : {positive_mode}")

# print(df.head(10))

## calculating breaches
lower_bound = negative_std - negative_mean*3
upperbound = positive_std + positive_mean*3

print(lower_bound,upperbound)

upper_breached = positive_df[positive_df["% Change"]>upperbound]
print(upper_breached.count()/positive_df.count()*100)