import sys, re, string, google;

# Set the license key (must be unique to you)

google.setLicense('$YOUR_API_KEY')

# Get the domain from the user

try: 

	domain = sys.argv[1]

except: 

	print ("Usage: dnscour <domain.tld> \n") 

domain = raw_input('Enter the domain to be searched:\n')

# Create the query 

termkeyword = "inurl:"
query = keyword + domain

#Start the query 

looppotentials = []

for i in [0,10,20,30,40,50,60,70,80,90]: 

# Perform the query five times, taking 10 results each time 

# and putting them into our potentials list 

	data = google.doGoogleSearch(query,start=(i)) 

for result in data.results: 
	potentials.append(result.URL)
	
# Initialize a second list to hold unique, cleaned entries

refined = []

# Do the cleaning work and populate the new list

for i in potentials: 
	i = i.replace('http://','') 
	i = i.replace('https:','') 
	keep = i.split('/') 
	
if keep[0] not in refined: 
	refined.append(keep[0])
	
# Print the contents of the refined list

null = ""

for i in refined: 
	if i is null: 
		refined.remove(i) 
	else: print i
