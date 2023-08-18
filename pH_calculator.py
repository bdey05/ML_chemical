import json
import numpy as np
import math 


def alpha(file_name):

    with open(file_name, "r",  encoding = 'utf-8') as file:

    
        json_data = json.load(file)

    
    filtered_data = []

    
    for record in json_data:

        
        filtered_data.append(record["aqueous phase"])


    # prints a list of associated name-value pairs of all data, within the aqueous phase object
            
    # accessing pH to see if value already provided

    # if pH is missing, checking provided concentration of the strong acid-nitric acid, for pH calculation
         
    pH = filtered_data[1]


    acid_conc = filtered_data [0]


    if isinstance(pH, (int, float)):

            
        pH = np.array("pH", dtype=float)

                        
        return h3o
        
    elif isinstance(acid_conc, (int, float)):
                
        acid_conc = np.array("pH", dtype=float)

        h3o = -math.log10(pH)

        return h3o

        
alpha("all_TPEN_DERIVATIVE_records.json")
