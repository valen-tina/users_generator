# users_generator

##Python dockerized script
Python script to generate csv file with users. Its dockerized and accepting amount of users to generate.
CSV has fields ['streetNumber', 'streetName', 'zipcode', 'state', 'name', 'email', 'phone']

Script is using https://github.com/EthanRBrown/rrad address base.

#To run container:
Run following command:
`./run.sh`

Script will ask for amount to generate and will create `randomAddresses.csv` file in same directory.