sent_message = "Hi there, this is a secret message"
unsent_message = "This message has been unsent."
try:
	file = open("test1.txt", "r+")
	file.write(sent_message)
finally:
	file.close()
with open("test1.txt","r+") as file:
	original_content = file.read()
	file.seek(0)
	file.truncate(len(unsent_message))
	file.write(unsent_message)
	

import csv

# Data to be written to the CSV file
data_to_write = [
  ['Name', 'Age', 'Grade'],
  ['Alice', 25, 'A'],
  ['Bob', 22, 'B'],
  ['Charlie', 28, 'A+']
]

# Open the CSV file in 'read' mode
with open('output.csv', 'w', newline='') as file:
  # Create a CSV reader object
  csv_writer = csv.writer(file)
  csv_writer.writerows(data_to_write)
#with open('output.csv', 'r') as file:
	#csv_reader = csv.reader(file)
	#for row in csv_reader:
		#print(row)

#use csv.reader
with open('Bestseller - Sheet1.csv', 'r') as file:
	csv_reader = csv.reader(file)
	header = next(csv_reader)
	index_sales = header.index('sales in millions')
	index_books = header.index('Book')
	max_sales = 0
	book = ""
	for row in csv_reader:
		sales = float(row[index_sales])
		if sales > max_sales:
			max_sales = sales
			book = row[index_books]
	print(f'{book} has the highest sales {max_sales} in millions.')

#use csv.DictReader
max_sales = 0
book = ""
with open('Bestseller - Sheet1.csv', 'r') as file:
	csv_reader = csv.DictReader(file)
	for row in csv_reader:
		sales = float(row['sales in millions'])
		if sales > max_sales:
			max_sales = sales
			book = row['Book']
	
print(f'{book} has the highest sales {max_sales} in millions.')



new_data = [
	['Book', 'Author', 'Sales in Millions'],
	['Hallucinations', 'Oliver Sacks', 'NA'], 
	['The Gene', 'Siddartha Murkherjee', 'NA']
]

with open('bestseller_info.csv', 'w', newline = '') as file:
	csv_writer = csv.writer(file)
	csv_writer.writerows(new_data)
	

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
try:
	with open('packing_list.csv', 'r') as file:
		csv_reader = csv.reader(file)
		for row in csv_reader:
			print(row)
except FileNotFoundError:
	print('Packing list file not found. Creating a new one')
	with open('packing_list.csv', 'w',  newline = '') as file:
		csv_writer = csv.writer(file)
		csv_writer.writerows(data)




		
	

		
		

	

	
		
		




	


	


