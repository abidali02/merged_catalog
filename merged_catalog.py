import csv


#defining function to open csv files and merge into one list

def merge(barcode,catalog):
    
    #defining variable format_checker to increase the count if any formatting issue found in csv
    format_checker=0

    #opening the csv barcode and adding the data in the list (barcode_list)
    
    with open(barcode+'.csv', 'r') as code_file:
            code=csv.reader(code_file)
            barcode_list=list(code)

            #checking the format of the csv is correct or not
            if barcode_list[0] !=['SupplierID', 'SKU', 'Barcode']:
                format_checker=format_checker+1
                print(str(barcode) + " csv format is not correct. Please use this format:- SupplierID, SKU, Barcode")

    #opening the csv catalog and adding the data in the list (catalog_list)
            
    with open(catalog+'.csv', 'r') as cat_file:
            cat=csv.reader(cat_file)
            catalog_list=list(cat)

            #checking the format of the csv is correct or not
            
            if catalog_list[0] !=['SKU', 'Description']:
                format_checker=format_checker+1
                print(str(catalog) + " csv format is not correct. Please use this format:- SKU, Description")



    #defining a temporary array to store merged value from barcode list and catalog list   
    temp_arr=[]
    if (format_checker==0):
    #looping through barcode list and catalog list and merging these two list create superset of each company
        for row_catalog_list in catalog_list[1:]:
                for row_in_barcode in barcode_list:
                    
                    if row_catalog_list[0]==row_in_barcode[1]:
                        row_in_barcode.append(row_catalog_list[1])
                        temp_arr.append(row_in_barcode)

    return(temp_arr,format_checker)




a,format_checker_a=merge('barcodea','cataloga') #barcodea and cataloga is the input csv name for the company A
b,format_checker_b=merge('barcodeb','catalogb') #barcodeb and catalogb is the input csv name for the company B

#checking if format of csv is fine then entering the block to merge 2 csv

if (format_checker_a==0 and format_checker_b==0):
    print("Format of CSV is correct, starting the merge process for catalog")

    final_arr=[] #this array is to store all the data of super set catalog
    hold_description=[] # to hold the value of description which is added in the merged list
    hold_sku=[] #to hold the value of the sku which is added in the merged list

    #looping through each row in merged list of A and B
    
    for linea in a:
        for lineb in b:
            #checking if the element of A and B are same
            if linea[2]==lineb[2]:

                #checking if that element is already added in the final_arr
                
                if linea[3] not in hold_description:
                    hold_description.append(linea[3]) #adding description of that row in hold_description
                    hold_sku.append(linea[1]) #adding sku of that row in hold_sku
                    linea.append("A") #appending supplier name in the list
                    final_arr.append(linea) #appending th row in final_arr
                    if linea[3] != lineb[3]: #checking if the description in both A and B company is same or not. if not then adding the description of B company also in hold_description
                        hold_description.append(lineb[3])

        
                  
        if linea[1] not in hold_sku: #adding the value from Company A which is not common to company
            hold_sku.append(linea[1])
            linea.append("A")
            final_arr.append(linea)
            
            
    for lineb in b: #adding the value from Company A which is not common to company
        if lineb[3] not in hold_description:
            hold_sku.append(lineb[1])
            hold_description.append(lineb[3])
            lineb.append("B")
            final_arr.append(lineb)

    #as final_arr contains some extr columns which is not required in final csv
    #defining output_arr which will only contain the required column for output csv (SKU, Description, Initial source company)

    output_arr=[]

    with open("output.csv", "w", newline='') as new_file:
        wr = csv.writer(new_file)
        ls=["SKU","Description","Source"]
        wr.writerow(ls)
        for line_final in final_arr:
            csv_arr=[]
            csv_arr.extend([line_final[1],line_final[3],line_final[4]])
            wr.writerow(csv_arr)
            output_arr.append(csv_arr)
            
        print("output file is generated with merged catalog")


else:
    print("exiting application because of csv issue")


