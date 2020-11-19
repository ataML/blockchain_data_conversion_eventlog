import json
import os
import collections
import re


#the extract function is used from: 
#https://hackersandslackers.com/extract-data-from-complex-json-python/

#fields contains the keys in json file which will be extracted
fields = ["timestamp","tx_id","mspid"]



#csv_path is the path to the output file, in which the extracted data is written in csv format
csv_path ="data_two_proc.csv"

file_dir="data"


def scan_files(path):
    
    case_id=1
    
    with open(csv_path,"w") as f:
       
        #writing the header for csv  
        i = 0
        for i in range(len(fields)):
            f.write(fields[i] + ";")
        i+=1
      #  f.write(fields[i]+"\n")
        f.write("activity_name;case_id\n")
        f.close()
    dir_dict={}
    
    
    #all files in the directory are scanned, then the name, and extension of each file is extracted,
    #a dictionary is created in which keys are the index of each file, and the values are DirEntry of files
    #finaly in ordered_directory_dict all files are sorted based on their indecies
    for file_path in os.scandir(path):
        
        if file_path.is_file():
            base_name= os.path.basename(file_path)
            name, extension = os.path.splitext(base_name)

            if(extension ==".json"):
                dir_dict[int(name)]= file_path
    ordered_directory_dict=collections.OrderedDict(sorted(dir_dict.items()))
        
   
    #looping through all json files 
    for _ , file_path in ordered_directory_dict.items():
        
 
        file_values=[]
    
        #reading one file
        with open(file_path) as json_file:
            
            json_data = json.load(json_file)
            

            for field in fields:
                
                field_values=[]
                res = json_extract(json_data,field)

                for item in res:
                    field_values.append(item)
                file_values.append(field_values)
                
            #we list get all keys which named "key"
            #within these keys we extract the function names
            function_names=[]
            keys= json_extract(json_data,"key")
            
            
            
            for name in keys:
                
                if "functionname" in name:
                 #   print("HHHH ")
                 #   print(name)
                    #we store function names in the form function_XXX,
                    #so we split the name by "_" to get the actual function name
                    function_names.append(name.split("_")[1])
        #    print(function_names)   
            file_values.append(function_names)
            json_file.close()

        case_id=csv_write(fields,file_values,csv_path,case_id)
                
            

def csv_write(fields, data,path,case_id):
    
   # print("len is ::   ")
   # print(data[1])
    
    count=0
    with open(path,"a") as f:
        
        i = 0

        
        for i in range(len(data[0])):

            for j in range(len(data)):
                                    
                if (i < len(data[j])):
                    f.write("\"%s\"" % data[j][i])
                    
                    if(data[j][i]=="createCar"):
                        case_id+=1
                        count=1
                else:
                    f.write("\"\"")
                if(j < len(data)-1):
                    f.write(";")
            f.write(";")
            f.write(str(case_id))
            f.write("\n")
        
      #  i+=1
      #  f.write("%s\n" % data[i])
        if(count == 0):
            case_id+=1
        
        f.close()
        return case_id
    
    
def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


scan_files(file_dir)