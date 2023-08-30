import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

driver_dict = pickle.load(open('dictionary/driver_dict','rb'))
constructor_dict = pickle.load(open('dictionary/constructor_dict','rb'))
clf = pickle.load(open('raoforest.pkl','rb'))

data = pd.read_csv("cleaned_data.csv")

y_dict = {1:'Podium Finish',
          2:'Points Finish',
          3:'No Points Finish'        
        }

le_d = LabelEncoder()
le_d.fit(data[['driver']])

le_c = LabelEncoder()
le_c.fit(data[['constructor']])

le_gp = LabelEncoder()
le_gp.fit(data[['GP_name']] )

grid_position_mapping = {'Pole': 1, 'P2': 2, 'P3': 3, 'P4': 4, 'P5': 5, 'P6': 6, 'P7': 7, 'P8': 8, 'P9': 9, 'P10': 10}

def pred(driver, constructor, grid_position, circuit):
    encoded_grid_position = grid_position_mapping.get(grid_position, 0)
    
    gp = le_gp.fit_transform([circuit]).max()
    quali_pos = encoded_grid_position
    constructor_enc = le_c.transform([constructor]).max()
    driver_enc = le_d.transform([driver]).max()
    driver_confidence = driver_dict[driver].max()
    constructor_relaiablity = constructor_dict[constructor].max()
    prediction = clf.predict([[gp,quali_pos,constructor_enc,driver_enc,driver_confidence,constructor_relaiablity]]).max()
    print(prediction)

    return y_dict[prediction]

# Example usage
#print(pred('Max Verstappen', 'Red Bull', 'P2', 'Silverstone Circuit'))
