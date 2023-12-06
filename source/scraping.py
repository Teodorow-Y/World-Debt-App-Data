import re
import requests

#----------------- GETTING DATA FROM WEB ----------------#   
# To get information
website = 'https://datosmacro.expansion.com/deuda'
result = requests.get(website)
content = result.text


# To work data to Shimoku
country_dic, nd = {},{}
country, deuda_total, deuda_per_capita, deuda_PIB = [],[],[],[] 


#----------------- FILTER DATA WEB ----------------# 
# Filter to Data Country

patron = r'https://datosmacro.expansion.com/deuda/[\w-]*'
repeat_machine = re.findall(patron, str(content))

def filter_request_country():
    sin_repeat = list(repeat_machine)
    for i in sin_repeat:
        machine= i.replace('https://datosmacro.expansion.com/deuda/',"")
        country.append(machine)
    country.pop(0)

# Filter to Data Deuda
patron_deuda = r'numero eur" data-value="[\w-]*'
repeat_deuda = re.findall(patron_deuda, str(content))

def filter_request_deuda():
    sin_repeat = list(repeat_deuda)
    clean_machine = []
    for i in sin_repeat:
        machine= i.replace('numero eur" data-value="','')
        clean_machine.append(machine)
    for i,value in enumerate(clean_machine):
        if i % 2 == 0:
            deuda_total.append(eval(value))
        else:
            deuda_per_capita.append(eval(value))


# Filter to Data PIB
patron_PIB = r'numero" data-value="[.\w -]*'
repeat_PIB = re.findall(patron_PIB, str(content))

def filter_request_PIB():
    sin_repeat = list(repeat_PIB)
    for i in sin_repeat:
        machine= i.replace('numero" data-value="','')        
        deuda_PIB.append(eval(machine))





#----------------- Tag to Score ----------------# 
# Tag to Level Scoring

def evaluating(i):    
    if int(deuda_PIB[i]) < 50:
        return 'Low'
    elif int(deuda_PIB[i]) < 80:
        return 'Medium'
    else: 
        return 'Critical'


#----------------- ADDING DICT TO SHIMOKU ----------------# 
# DICT TO: TABLE 

def adding_to_dict():
    lista_retorno = []
    for i in range(25):   #len(country) ------ TO GET ALL COUNTRIES :
        country_dic['Country'] = country[i]
        country_dic['Deuda_total'] = deuda_total[i]
        country_dic['Deuda_Per_Capita'] = deuda_per_capita[i]
        country_dic['Deuda_PIB'] = deuda_PIB[i]
        country_dic['level'] = evaluating(i)
        lista_retorno.append(dict(country_dic))    
    return lista_retorno

# DICT TO: TREE

def seccionador():         
    total_pib_deuda, sum_low, sum_mid, sum_cri = 0, 0, 0, 0
    child_low, child_mid, child_cri, main_low, main_mid, main_cri ={}, {}, {}, {}, {}, {}
    master_low, master_mid, master_cri = [],[],[]    
    
    for i in range(70):  #len(deuda_PIB)  ----- TO GET ALL COUNTRIES:

        #Prepare Dicts
        total_pib_deuda += deuda_PIB[i]
        if evaluating(i) == 'Low':
            sum_low += int(deuda_PIB[i])
            child_low['name'] = country[i]
            child_low['value'] = deuda_PIB[i]
            master_low.append(dict(child_low))
        elif evaluating(i) == 'Medium':
            sum_mid += int(deuda_PIB[i])
            child_mid['name'] = country[i]
            child_mid['value'] = deuda_PIB[i]
            master_mid.append(dict(child_mid))
        elif evaluating(i) == 'Critical':
            sum_cri += int(deuda_PIB[i])
            child_cri['name'] = country[i]
            child_cri['value'] = deuda_PIB[i]
            master_cri.append(dict(child_cri))
    
    # Main Dicts
        # Main LOW
    main_low['name'] = 'Master Low'
    main_low['value'] = sum_low
    main_low['children'] = master_low
        # Main MID  
    main_mid['name'] = 'Master Mid'
    main_mid['value'] = sum_mid
    main_mid['children'] = master_mid
        # Main CRITICAL
    main_cri['name'] = 'Master Critical'
    main_cri['value'] = sum_cri
    main_cri['children'] = master_cri
    main_list = [main_cri, main_mid, main_low]

    #CHILDREN
    nd['name'] = 'root'
    nd['value'] = total_pib_deuda
    nd['children'] = main_list

    
#----------------- EXECUTE TASKS ----------------# 
filter_request_country()
filter_request_deuda()
filter_request_PIB()
seccionador()
 