import streamlit as st 
import pickle
import pandas as pd

print('Successfully executed ')

model = pickle.load(open('model.pkl', 'rb'))



def main():
    #Setting Application title
    st.title('Vehicle Insurance Claim Fraud Prediction App')
    html_temp = """
    <div style="background-color:Blue;padding:20px">
    <h2 style="color:white;text-align:center;">Streamlit Vehicle Insurance Claim Fraud Prediction  </h2>
    </div>
    """

    #Setting Application description
   
    st.markdown(html_temp, unsafe_allow_html=True)

    #Setting Application sidebar default
    
     
   
    st.info("Input data below")
    #Based on our optimal features selection
    #st.subheader("Demographic data")
    TypeOfIncident = st.selectbox('What is the type of incident:', ('Multi-vehicle Collision', 'Single Vehicle Collision','Parked Car','Vehicle Theft'))
    TypeOfCollission = st.selectbox('What is the collission type:', ('Side Collision', 'Rear Collision', 'Front Collision', 'Unknown'))
    SeverityOfIncident=st.selectbox('Severity of the incident:', ('Total Loss', 'Minor Damage', 'Major Damage', 'Trivial Damage'))
    AuthoritiesContacted = st.selectbox('Authorities contacted:', ('Police', 'Other', 'Fire', 'Ambulance', 'None'))
    #st.subheader("Payment data")
    IncidentTime = st.slider('Select time of the incident', min_value=0, max_value=24, value=0)
    NumberOfVehicles = st.selectbox('Number of Vehicles', (1,2,3,4))
    PropertyDamage = st.selectbox('Property Damage', ('Unknown', 'YES', 'NO'))
    BodilyInjuries = st.selectbox('Bodily Injuries',(0,1,2))
    Witnesses = st.selectbox('Number of Witness', (0,1,2,3))
    PoliceReport = st.selectbox('Whether reported to police:',('Unknown', 'YES', 'NO'))
    #st.subheader("Services signed up for")
    AmountOfVehicleDamage = st.number_input('Amount of vehicle damage:',min_value=0, max_value=10000, value=0)
    InsuredGender = st.selectbox('Insured gender:', ('MALE', 'FEMALE'))
    InsuredEducationLevel = st.selectbox("Insured Education Level:", ('JD', 'High School', 'Masters', 'MD', 'Associate', 'College',
       'PhD'))
    InsuredOccupation = st.selectbox("Select the occupation:",('armed-forces', 'tech-support', 'exec-managerial', 'adm-clerical',
       'handlers-cleaners', 'craft-repair', 'prof-specialty',
       'other-service', 'priv-house-serv', 'protective-serv',
       'farming-fishing', 'sales', 'transport-moving',
       'machine-op-inspct'))
    CapitalGains = st.number_input('Capital Gains:',min_value=0, max_value=200000, value=0)
    CapitalLoss=st.number_input('Capital Gains:',min_value=-200000, max_value=0, value=0)
    CustomerLoyaltyPeriod = st.number_input('Customer Loyalty Period:',min_value=0, max_value=500, value=0)
    InsurancePolicyState = st.selectbox("Insurance Policy State", ('State1', 'State3', 'State2'))
    Policy_CombinedSingleLimit = st.selectbox("Policy Combined Single Limit:", ('100/300', '500/1000', '250/500', '250/1000', '500/300', '500/500',
       '100/500', '250/300', '100/1000'))
    Policy_Deductible = st.number_input('Policy Deductible:',min_value=500, max_value=2000, value=500)
    PolicyAnnualPremium = st.number_input('Policy Annual Premium:',min_value=100, max_value=2500, value=100)
    UmbrellaLimit = st.number_input('Umbrella Limit:',min_value=-1000000, max_value=1000000, value=0)
    InsuredRelationship = st.selectbox("Insured Relationship:", ('not-in-family', 'wife', 'own-child', 'unmarried', 'husband',
       'other-relative'))
    VehicleMake = st.selectbox("Select Vehicle Make", ('Audi', 'Volkswagen', 'Toyota', 'Mercedes', 'Suburu', 'Saab',
       'Nissan', 'Ford', 'Accura', 'Dodge', 'Honda', 'Chevrolet', 'Jeep',
       'BMW'))
    VehicleModel = st.selectbox("Select Vehicle Model", ('A5', 'Jetta', 'CRV', 'C300', 'Passat', '92x', 'Ultima', 'Fusion',
       'Impreza', '93', 'Highlander', 'X5', 'Accord', 'Corolla',
       'Forrestor', 'F150', 'Pathfinder', 'Neon', 'Tahoe', 'Wrangler',
       'A3', 'RSX', 'Malibu', 'E400', 'Legacy', '95', 'Grand Cherokee',
       'Escape', 'Civic', 'Silverado', 'RAM', 'Camry', 'M5', '3 Series',
       'ML350', 'Maxima', 'MDX', 'X6', 'TL'))
    VehicleYOM=st.number_input('Vehicle Year of Manufacturing:',min_value=1995, max_value=2023, value=2000)

    data = {
            'TypeOfIncident': TypeOfIncident,
            'TypeOfCollission' : TypeOfCollission,
            'SeverityOfIncident' : SeverityOfIncident,
            'AuthoritiesContacted' : AuthoritiesContacted,
            'IncidentTime' : IncidentTime ,
            'NumberOfVehicles' : NumberOfVehicles,
            'PropertyDamage' : PropertyDamage,
            'BodilyInjuries' : BodilyInjuries,
            'Witnesses' : Witnesses,
            'PoliceReport' : PoliceReport,
            'AmountOfVehicleDamage' : AmountOfVehicleDamage,
            'InsuredGender' : InsuredGender,
            'InsuredEducationLevel' : InsuredEducationLevel,
            'InsuredOccupation' : InsuredOccupation,
            'CapitalGains' : CapitalGains,
            'CapitalLoss' : CapitalLoss,
            'CustomerLoyaltyPeriod': CustomerLoyaltyPeriod,
            'InsurancePolicyState': InsurancePolicyState,
            'Policy_CombinedSingleLimit' : Policy_CombinedSingleLimit,
            'Policy_Deductible' : Policy_Deductible,
            'PolicyAnnualPremium' : PolicyAnnualPremium,         
            'UmbrellaLimit' : UmbrellaLimit,
            'InsuredRelationship' : InsuredRelationship,
            'VehicleMake' : VehicleMake,
            'VehicleModel' : VehicleModel,
            'VehicleYOM' : VehicleYOM
            }
    features_df = pd.DataFrame.from_dict([data])
    #st.markdown("<h3></h3>", unsafe_allow_html=True)
    #st.write('Overview of input is shown below')
    #st.markdown("<h3></h3>", unsafe_allow_html=True)
    #st.dataframe(features_df)
    #Preprocess inputs
    col_names = pickle.load(open('cat_col.pkl', 'rb'))
    print(col_names)
    for col in col_names:
        
        #features_df[col]=features_df[col].astype('category')
        name=col+'.pkl'
        
        enc=pickle.load(open(name, 'rb'))
        
        features_df[col]=enc.transform(features_df[col])

    prediction = model.predict(features_df)
    if st.button('Predict'):
        if prediction == 1:
            st.warning('Yes, its a fraud.')
        else:
            st.success('No, its not a fraud.')



   
if __name__ == '__main__':
        main()