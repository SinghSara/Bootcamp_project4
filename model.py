import pandas as pd
import os
import numpy as np
from sklearn import preprocessing
import pickle
from  sklearn.metrics import accuracy_score
from sklearn.tree  import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler

df_claim=pd.read_csv("C:\\Users\\singh\\OneDrive\\Documents\\Bootcamp\\Problem Statement 4\\Bootcamp_project4\\\Train Data\\Train_Claim.csv")

df_demographics=pd.read_csv("C:\\Users\\singh\\OneDrive\\Documents\\Bootcamp\\Problem Statement 4\\Bootcamp_project4\\Train Data\\Train_Demographics.csv")

df_policy=pd.read_csv("C:\\Users\\singh\\OneDrive\\Documents\\Bootcamp\\Problem Statement 4\\Bootcamp_project4\\Train Data\\Train_Policy.csv")

df_vehicle=pd.read_csv("C:\\Users\\singh\\OneDrive\\Documents\\Bootcamp\\Problem Statement 4\\Bootcamp_project4\\Train Data\\Train_Vehicle.csv")

df_target=pd.read_csv("C:\\Users\\singh\\OneDrive\\Documents\\Bootcamp\\Problem Statement 4\\Bootcamp_project4\\Train Data\\Traindata_with_Target.csv")
df_vehicle=df_vehicle.pivot(index='CustomerID', columns='VehicleAttribute', values='VehicleAttributeDetails').reset_index()

df=df_claim.merge(df_demographics,on='CustomerID',how='left')

df=df.merge(df_policy,on='CustomerID',how='left')

df=df.merge(df_vehicle,on='CustomerID',how='left')

df=df.merge(df_target,on='CustomerID',how='left')


df.loc[df["PropertyDamage"] == "?", "PropertyDamage"] = 'Unknown'
 

##replacing missing vehicle make with the mode of related model 
for i in df.index:
    if df['VehicleMake'][i]=='???':
        model=df['VehicleModel'][i]
        
        make=df[df['VehicleModel']==model]['VehicleMake'].mode()
        
        df['VehicleMake'][i]=make[0]

## replacing missing value with 0
df.loc[df['Witnesses']=='MISSINGVALUE','Witnesses']='0'

df['Witnesses']=df['Witnesses'].astype('int64')

df['InsuredGender']=df['InsuredGender'].fillna(df['InsuredGender'].mode())


df.loc[df["PoliceReport"] == "?", "PoliceReport"] = 'Unknown'



df.loc[df["TypeOfCollission"] == "?", "TypeOfCollission"] = 'Unknown'


df['AuthoritiesContacted']=df['AuthoritiesContacted'].fillna('None')

## impute AmountOfTotalClaim value 

amt_median=df[df['AmountOfTotalClaim']!="MISSEDDATA"]['AmountOfTotalClaim'].median()
#df['AmountOfTotalClaim']=df['AmountOfTotalClaim'].fillna(df['AmountOfTotalClaim'].median())
df.loc[df["AmountOfTotalClaim"] == "MISSEDDATA", "AmountOfTotalClaim"] = amt_median
df['AmountOfTotalClaim']=df['AmountOfTotalClaim'].astype('float64')

premium_amt_mean=df[df['PolicyAnnualPremium']>=0]['PolicyAnnualPremium'].mean()
#df[df['PolicyAnnualPremium']<0]['PolicyAnnualPremium']=premium_amt_mean
df.loc[df["PolicyAnnualPremium"] < 0, "PolicyAnnualPremium"]=premium_amt_mean

time_median=df[df['IncidentTime']>=0]['IncidentTime'].median()
df.loc[df["IncidentTime"] < 0, "IncidentTime"]=time_median

df.drop(['Country','CustomerID','VehicleID'],axis=1,inplace=True)
df['VehicleYOM']=df['VehicleYOM'].astype('int')

df_new=df.drop(['AmountOfTotalClaim','AmountOfPropertyClaim','InsuredAge','AmountOfInjuryClaim','DateOfPolicyCoverage','DateOfIncident','InsuredZipCode','IncidentState', 'IncidentCity',
       'IncidentAddress','InsuredHobbies','InsurancePolicyNumber'],axis=1)

string_col=df_new.select_dtypes(include=['category','object']).columns

numeric_col=df_new.select_dtypes(include=['int32','int64','float64']).columns

for col in string_col:          
    label_encoder = preprocessing.LabelEncoder()
    
    df_new[col]=label_encoder.fit_transform(df_new[col])
    #df[col]=df[col].astype('category')
    filename=col+".pkl"
    pickle.dump(label_encoder, open(filename,'wb'))
string_col=list(string_col)
string_col.remove('ReportedFraud')

pickle.dump(string_col, open('cat_col.pkl','wb'))
scaling_columns=[ 'AmountOfVehicleDamage', 'CapitalGains',
       'CapitalLoss', 'CustomerLoyaltyPeriod', 'Policy_Deductible',
       'PolicyAnnualPremium', 'UmbrellaLimit']

for col in scaling_columns:
    minmax = MinMaxScaler()
    df_new[col]=minmax.fit_transform(df_new[[col]])

X,Y=df_new.loc[:, ~df_new.columns.isin(['ReportedFraud'])],df_new.loc[:, df_new.columns.isin(['ReportedFraud'])]

dtc = DecisionTreeClassifier()
dtc.fit(X, Y)

y_pred = dtc.predict(X)

print(accuracy_score(Y, y_pred))
print(X.columns)
pickle.dump(dtc, open('model.pkl','wb'))



