from math import ceil
tax =0

# list of common food and medicines

list_food=['Apples','Avocados', 'Bananas', 'Blueberries', 'Oranges', 'Strawberries', 'Eggs', 'Chicken', 'Lamb', 'Almonds', 'Coconuts', 'Walnut', 'Broccoli', 'Carrots', 'Cauliflower', 'Cucumber', 'Garlic', 'Onions', 'Tomatoes', 'Salmon', 'Shellfish', 'Shrimp', 'Tuna', 'Oats', 'Peanuts', 'Cheese', 'Yogurt', 'Coconut', 'Potatoes', 'Apple', 'chocolates', 'choclate']
medicine_list = ['antibiotic',"cure","drug","medication","pharmaceutical","pills","prescription","remedy","anesthetic","antidote","antiseptic","antitoxin","balm","capsule","dose","elixir","injection","inoculation","liniment","lotion","medicament","ointment","physic","potion","salve","sedative","serum","tablet","tincture","tonic","vaccination","vaccine","biologic","pharmacon"]

#function for tax calculation books, medicine and food
def without_tax(x):
    a=0
    for i in range(0, len(x)):
        if(x[i]==' '):
            a = i
            break
    
    b=x[0:a]
    start =0
    end=len(x)
    start = x.find(' at')
    start+=4
    final_n = float(b)*float(x[start:end])
    tax = float(final_n)
    # print(tax)
    return tax

#function for tax generation of other materials

def with_tax(x):
    a=0
    for i in range(0, len(x)):
        if(x[i]==' '):
            a = i
            break
    
    b=x[0:a]
    start =0
    end=len(x)
    start = x.find(' at')
    start+=4
    final_n = x[start:end]

    tax = float(final_n)*0.1 # 10% tax on other items
    return tax+float(final_n)

#funnction for tax on imported items
    
def imported_tax(x):
    a=0
    for i in range(0, len(x)):
        if(x[i]==' '):
            a = i
            break
    
    b=x[0:a]
    start =0
    end=len(x)
    start = x.find(' at')
    start+=4 
    final_n = x[start:end]

    impo_tax = float(b)* float(final_n)*0.05 # 5% tax on imported items
    return impo_tax

#function for roundof 

def tax_round(taxx):
    roud =20
    return ceil(round(taxx, 2) * roud) / roud

# main function
def sales_tax():
    count=0
    sales_tax =0
    total_tax=0
    food = False
    medicine = False

    # Reading every input in the list.
    for x in list_input:
        # finding price for every input
        srt =0
        end=len(x)
        srt = x.find(' at')
        srt+=4
        value = x[srt:end]


        taxx=0
        #checking items in food_list and medicine_list
        for i in range(0, len(list_food)):
            if list_food[i] in x:
                food = True

        for i in range(0, len(medicine_list)):
            if medicine_list[i] in x:
                medicine = True

        # no tax for these items
        if (('book' in x) or ('food' in x) or ('medicine' in x) or ('chocolates' in x) or ('chocolate' in x) or ('pills' in x) ):
            taxx += without_tax(x)  
        # 10% tax for other items
        else:
            taxx += with_tax(x)
        # 5% tax for imported items
        if 'imported' in x:
            taxx+=imported_tax(x)

        #calculating sales tax....
        sales_tax += taxx - float(value)
        taxx = tax_round(taxx)
        #calculating total tax.......
        total_tax+=taxx
        start = x.find(' at')
        print(x[0:start] + ':' + str(taxx))
    
    # roundof tax and printing...
    sales_tax = tax_round(sales_tax)
    total_tax = tax_round(total_tax)
    print("Sales tax : " + str(sales_tax))
    print("Total tax : " + str(total_tax))

# user input
list_input=['1 book at 12.49 ','1 music CD at 14.99','1 chocolate bar at 0.85 ']

sales_tax()