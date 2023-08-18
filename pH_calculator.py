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

    
    if (isinstance(json_data, list)):
        
        for record in json_data:
                        
            filtered_data.append(record["aqueous phase"])
            

            print(record['aqueous phase']['solutes'])
            

    if (isinstance(json_data, dict)):
        
                
        filtered_data.append(json_data["aqueous phase"])
        
        
        print(json_data["aqueous phase"])



    for record in filtered_data:
        
        if (isinstance(record['pH'], int) or isinstance(record['pH'], float)): 
            
            print(f"pH is present and valid, pH is {record['pH']}.")

            
        else:
            
            print("pH is not int. Here are the solutes:", record['solutes'])
            for solute in record['solutes']:
                if (solute['identity'] == 'HNO3'):
                    print('The pH is', -math.log10(solute['concentration']['quantity']))

        
alpha("testwithoutPh.json")
