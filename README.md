# merged_catalog


1. this code is written in python3

2. this code will take input as csv files

3. this can take up to 3 csv files for each company.

4. CSV file name is named as below
	'barcodea','cataloga' are the name of barcode and catalogue csv file respectively for company A
	'barcodeb','catalogb' are the name of barcode and catalogie csv file respectively for company B

	
5. It is assumed that input files are kept under resource folder under the code folder (code directory/resource), code and output file will be stored in the same folder.
	if you need to change input file or output file folder then thant can be easily done by just giving folder path.
	

6. It is merging the csvs for each company and making super set of each comapny

7. these super set of each comapy are compared and created a new csv file.

8. This code has 2 main block. 
	A. merging all the CSV file of each company to create a super set.
	B. Comparing the super set of each company to create merged catalog

9. This code unit test is also works.
	It is first checking the format of the inout file. If the format of the input file will not be correct it will give output as " csv format is not correct so exiting the code"
	If the format of csv is correct it will print CSV format is correct and will go into next block.
	If required it can write super set of each file to csv as part of unit testing.

10. The logic block can also be run as part of unit testing. Just need to pass superset of each companies.

11. unit_test is code written for different test case scenario.
	Test case 1 is having all valid inputs and output will be sucessfully genrated
	Test case2,3,4 are having some of the data missing in the csv so output is not generated.

12 No data from supplier files are needed so we havent used the supplier file.