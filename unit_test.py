import merged_catalog
import csv

# Test CAse 1 (All the correct csv passed and output should be as per expectation)

company_A=merged_catalog.merge('barcodea','cataloga')
company_B=merged_catalog.merge('barcodeb','catalogb')
print("test case 1 sucessfully completed  //////////////////////")

# Test case 2 (wrong barcode csv format is passed for company B, It will ask to correct the format)
print("Starting Test case 2")
company_A=merged_catalog.merge('barcodea','cataloga')
company_B=merged_catalog.merge('barcode_missing','catalogb')
print("Test case 2 ended /////////////////////////////////")


# Test case 3 (catalog file is having missing decsription in csv, It will ask to correct the format)
print("Starting Test case 3")
company_A=merged_catalog.merge('barcodea','missing_description')
company_B=merged_catalog.merge('barcodeb','missing_description')
print("test case3 ended //////////////////////////////////////")


#Test case 4 (passing wrong csv format for barcode and catalog)
print("Starting Test case 4")
company_A=merged_catalog.merge('barcode_missing','missing_description')
company_B=merged_catalog.merge('barcodeb','missing_description')
print("test case 4 ended //////////////////////////////////////")

