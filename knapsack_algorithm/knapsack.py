# grocerydata.csv dataset 
# the weight can not be dividable
# it's a order dataset of users

import csv 
import mergesort

def extractCSV(csv_file,delimiter=','):

    csvdata = []
    
    with open(csv_file,'r') as csv_file_reader:

        csv_extractor = csv.DictReader(csv_file_reader,delimiter=delimiter)

        for data in csv_extractor:

            csvdata.append({"key":data['key'],"weight":float(data['weight']),"profit":int(data['profit'])})

    return csvdata 


def knapsack(csvlist,bagweight):
    
    profitweightratio = []
    bag = []
    # ratio of p/w (profit/weight)
    for x in csvlist:

        ratio = x['profit'] / x['weight']
        profitweightratio.append({"key":x['key'],"ratio":ratio,"weight":x['weight']})

    #once you have the ratio 
    # next is sort the data 
    sorted_profitweightratio = mergesort.mergesort(profitweightratio,0,len(profitweightratio) - 1)    
    
    maxbagweight = 0.0
    i = 0

    while maxbagweight <= float(bagweight):
        
        try:
           # need to check those data should i add in the bag or not 
           future_maxbagweight = maxbagweight + sorted_profitweightratio[i]['weight']

           if future_maxbagweight < float(bagweight):

              bag.append(sorted_profitweightratio[i])
              maxbagweight = future_maxbagweight

           i = i + 1

        except IndexError:

            break   


    return bag  


if __name__ == "__main__":
    
    bagweight = 5 # 5 kg upto carry 
    csvdata =  extractCSV('grocerydata.csv',',')
    bag = knapsack(csvdata,bagweight)
    print("bag",bag)
