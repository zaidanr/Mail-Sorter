# -- MADE SOLELY FOR EDUCATIONAL PURPOSE, AUTHOR NOT RESPONSIBLE FOR ANY ILLEGAL USE OR DAMAGE CAUSED BY THIS CODE. -- # 
# 
# Author : github.com/zaidanr

import os.path
import csv
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input mail list ex: mail_list.txt. ")
parser.add_argument("--output", help="Output file ex: sorted_mail.csv. ")
args = parser.parse_args()

mail_list = args.input      # Input file
output_file = args.output   # Output file
domains_row = []            # The CSV header fields
domain_dict = {}            # Main dictionary to classify mail domain
addresses_column = []       # The CSV data column

try: 
    if os.path.exists(mail_list):

        start_time = time.time()

        # Open the mail list file
        email = open('mail_list.txt', 'r')    

        # Function to sort the header fields (row)
        def row_sort(e):
            return len(domain_dict[e])
        
        # Function to append .csv to output file
        def outfile_validator(outfile):
            if  not outfile.endswith(".csv"):
                return outfile + ".csv"
            else: return outfile

        # Creating dictionary to classify the mail domain
        for address in email:
            address = address.rstrip()
            domain = address.split('@')[1].rstrip()
            if domain not in domain_dict:
                domain_dict.update({domain: [address]})
            elif domain in domain_dict:
                domain_dict[domain].append(address)

        #calculate highest index
        highest_index = 0
        highest_index_var = "" 
        for i in domain_dict:
            domains_row.append(i)   #Appending each domain found in main dictionary to be used as CSV header fields
            if (len(domain_dict[i]) > highest_index): 
                highest_index = len(domain_dict[i])
                highest_index_var = i

        # Sort the domains_row
        domains_row.sort(reverse=True, key=row_sort)

        # Create main column based on highest_index & highest_index_var
        for i in domain_dict[highest_index_var]:
            counter = 0
            addresses_column.insert(counter, [i])
            counter += 1

        # Insert data to main column
        for i in domain_dict:
            counter = 0
            if (i != highest_index_var):
                for j in domain_dict[i]:
                    addresses_column[counter].append(j)
                    counter += 1

        # address_column normalization
        for i in range(len(addresses_column)):
            if (len(addresses_column[i]) < len(addresses_column[0])):
                for j in range(len(addresses_column[0]) - len(addresses_column[i])):
                    addresses_column[i].append(" ")

        # Close the email file
        email.close()

        # Write to csv
        csvfile = open(outfile_validator(output_file), "w+")
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(domains_row)
        csvwriter.writerows(addresses_column)
        csvfile.close()

        print("Time elapsed: " + str(time.time() - start_time) + " seconds")
    else: 
        print ("Input file not exist")
except:
    print ('Usage : python3 sorter.py -h')
