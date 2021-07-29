
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:20:42 2021

@author: vasavtrehan
"""

# IMPORTING MODULES
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from tkinter import ttk
from tkmacosx import Button
import webbrowser
from PIL import Image, ImageTk
from covid import Covid
from covid_india import states
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# DEFINING WINDOW AND NESSESITIES
root = Tk()
covid = Covid()
root.geometry("858x550")
root.title("Coronavirus")
root.configure(bg="white")
myFont = font.Font(family="Raleway"
    , size=20)
# CANVAS
#canvas = Canvas(root, bg="white", width=600, height=300)
#canvas.grid(columnspan=4, rowspan=4, padx=30)
# LOGO VISIBLE ON THE DOCK/TASKBAR

# LOGO INSIDE THE WINDOW
Logo = ImageTk.PhotoImage(Image.open("covihelplogo.png"))
LogoLabel = Label(image=Logo)
LogoLabel.image = Logo
LogoLabel.grid(column=1, row=0, pady=(30, 10))

# INSTRUCTIONS IMAGE

#instructions = Label(root, text="Choose one of the options below")
#instructions['font'] = myFont
#instructions.grid(column=0, row=1)

# frontpage destroyer
def destroyer():
    LogoLabel.destroy()
    fetch_btn.destroy()
    sim_btn.destroy()
    info_btn.destroy()
    compare_cases_button.destroy()
    technifyed_logo_label.destroy()
# covid-stats
def stats(): 
    destroyer()
    clicked = StringVar()
    clicked.set("Select")
    country = clicked
    def india_state_stats():
        statebtn.destroy()
        countrybtn.destroy()
        click = StringVar()
        click.set("select")
        state_drop = OptionMenu(root, click, "Andaman and Nicobar Islands""Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli and Daman & Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")
        state_drop['font'] = myFont
        state_drop.grid(row=0, column=0)
        def statestatgo():
            yo = messagebox.showinfo("info", "The data shown here is counted from the very first case reported in your area")
            state = click.get()
            v = states.getdata(state)
            Active_cases = v.get("Active")
            Cured = v.get('Cured')
            Deaths = v.get('Death')
            my_tree = ttk.Treeview(root)
            # Define our columns
            my_tree['columns'] = ('Active Cases', 'Cured', 'Deaths')
            # Format our column
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Active Cases", anchor=W, width=120, minwidth=25)
            my_tree.column("Cured", anchor=W, width=120, minwidth=25)
            my_tree.column("Deaths", anchor=W, width=120, minwidth=25)
            # create headings
            my_tree.heading("#0", text="Label", anchor=W)
            my_tree.heading("Active Cases",text="New cases", anchor=W)
            my_tree.heading("Cured",text="Cured", anchor=W)
            my_tree.heading("Deaths",text="New Deaths", anchor=W)
            # add data
            my_tree.insert(parent='', index='end', iid=0, text="", values=(Active_cases, Cured, Deaths))
            my_tree.grid(row=0, column=2)
            data1 = {'data': ['Active','Cured','Deaths'],
            'numbers': [int(Active_cases), int(Cured), int(Deaths)]}
            df1 = DataFrame(data1,columns=['data','numbers'])
            figure1 = plt.Figure(figsize=(4, 7), dpi=100)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, root)
            bar1.get_tk_widget().grid(row=1, column=2)
            df1 = df1[['data','numbers']].groupby('data').sum()
            df1.plot(kind='bar', legend=True, ax=ax1)
            ax1.set_title('Graph')
            root.geometry("858x750")
            technifyed_logo = ImageTk.PhotoImage(Image.open("/Users/abhishektrehan/Desktop/aa.png"))
            technifyed_logo_label = Label(image=technifyed_logo)
            technifyed_logo_label.image = technifyed_logo
            technifyed_logo_label.grid(row=1, column=1, pady=30, padx=10)
        gostatestatbtn = Button(root, text='Go', command=statestatgo)
        gostatestatbtn['font'] = myFont
        gostatestatbtn.grid(row=0, column=1)
    def country_stats():
        root.geometry("400x600")
        statebtn.destroy()
        countrybtn.destroy()
        global country
        drop = OptionMenu(root, clicked,"China","India","US","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico","Japan","Ethiopia","Philippines","Egypt","Vietnam","DR Congo","Turkey","Iran","Germany","Thailand","United Kingdom","France","Italy","Tanzania","South Africa","Myanmar","Kenya","South Korea","Colombia","Spain","Uganda","Argentina","Algeria","Sudan","Ukraine","Iraq","Afghanistan","Poland","Canada","Morocco","Saudi Arabia","Uzbekistan","Peru","Angola","Malaysia","Mozambique","Ghana","Yemen","Nepal","Venezuela","Madagascar","Cameroon","Côte d'Ivoire","North Korea","Australia","Niger","Sri Lanka","Burkina Faso","Mali","Romania","Malawi","Chile","Kazakhstan","Zambia","Guatemala","Ecuador","Syria","Netherlands","Senegal","Cambodia","Chad","Somalia""Zimbabwe","Guinea","Rwanda","Benin","Burundi","Tunisia","Bolivia","Belgium","Haiti","Cuba","South Sudan","Dominican Republic","Czech Republic (Czechia)","Greece","Jordan","Portugal","Azerbaijan","Sweden","Honduras","United Arab Emirates","Hungary","Tajikistan","Belarus","Austria","Papua New Guinea","Serbia","Israel","Switzerland","Togo","Sierra Leone","Laos","Paraguay","Bulgaria","Libya","Lebanon","Nicaragua","Kyrgyzstan","El Salvador","Turkmenistan","Singapore","Denmark","Finland","Congo","Slovakia","Norway","Oman","State of Palestine","Costa Rica","Liberia","Ireland","Central African Republic","New Zealand","Mauritania","Panama","Kuwait","Croatia","Moldova","Georgia","Eritrea","Uruguay","Bosnia and Herzegovina","Mongolia","Armenia","Jamaica","Qatar","Albania","Lithuania","Namibia","Gambia","Botswana","Gabon","Lesotho","North Macedonia","Slovenia","Guinea-Bissau","Latvia","Bahrain","Equatorial Guinea","Trinidad and Tobago","Estonia","Timor-Leste","Mauritius","Cyprus","Eswatini","Djibouti","Fiji""Comoros","Guyana","Bhutan","Solomon Islands","Montenegro","Luxembourg","Suriname","Cabo Verde","Micronesia","Maldives","Malta","Brunei","Belize","Bahamas","Iceland","Vanuatu","Barbados","Sao Tome & Principe","Samoa","Saint Lucia","Kiribati","Grenada","St. Vincent & Grenadines","Tonga","Seychelles","Antigua and Barbuda","Andorra","Dominica","Marshall Islands","Saint Kitts & Nevis","Monaco","Liechtenstein","San Marino","Palau","Tuvalu","Nauru","Holy See",)
        drop['font'] = myFont
        drop.grid(row=0, column=0)
        #headers = [["Total active cases", "New cases", "Total deaths", "Total recovered"]]
        #table = [[total_active_cases, New_cases, Total_deaths, Total_recovered]]
        country_dict = {"Afghanistan":1,"Albania":2,"Algeria":3,"Andorra":4,"Angola":5,"Antigua and Barbuda":6,"Argentina":7,"Armenia":8,"Australia":9,"Austria":10,"Azerbaijan":11,"Bahamas":12,"Bahrain":13,"Bangladesh":14,"Barbados":15,"Belarus":16,"Belgium":17,"Belize":18,"Benin":19,"Bhutan":20,"Bolivia":21,"Bosnia and Herzegovina":22,"Botswana":23,"Brazil":24,"Brunei":25,"Bulgaria":26,"Burkina Faso":27,"Burma":28,"Burundi":29,"Cabo Verde":30,"Cambodia":31,"Cameroon":32,"Canada":33,"Central African Republic":34,"Chad":35,"Chile":36,"China":37,"Colombia":38,"Comoros":39,"Congo (Brazzaville)":40,"Congo (Kinshasa)":41,"Costa Rica":42,"Cote d'Ivoire":43,"Croatia":44,"Cuba":45,"Cyprus":46,"Czechia":47,"Denmark":48,"Diamond Princess":49,"Djibouti":50,"Dominica":51,"Dominican Republic":52,"Ecuador":53,"Egypt":54,"El Salvador":55,"Equatorial Guinea":56,"Eritrea":57,"Estonia":58,"Eswatini":59,"Ethiopia":60,"Fiji":61,"Finland":62,"France":63,"Gabon":64,"Gambia":65,"Georgia":66,"Germany":67,"Ghana":68,"Greece":69,"Grenada":70,"Guatemala":71,"Guinea":72,"Guinea-Bissau":73,"Guyana":74,"Haiti":75,"Holy See":76,"Honduras":77,"Hungary":78,"Iceland":79,"India":80,"Indonesia":81,"Iran":82,"Iraq":83,"Ireland":84,"Israel":85,"Italy":86,"Jamaica":87,"Japan":88,"Jordan":89,"Kazakhstan":90,"Kenya":91,"Korea, South":92,"Kosovo":93,"Kuwait":94,"Kyrgyzstan":95,"Laos":96,"Latvia":97,"Lebanon":98,"Lesotho":99,"Liberia":100,"Libya":101,"Liechtenstein":102,"Lithuania":103,"Luxembourg":104,"MS Zaandam":105,"Madagascar":106,"Malawi":107,"Malaysia":108,"Maldives":109,"Mali":110,"Malta":111,"Marshall Islands":112,"Mauritania":113,"Mauritius":114,"Mexico":115,"Micronesia":116,"Moldova":117,"Monaco":118,"Mongolia":119,"Montenegro":120,"Morocco":121,"Mozambique":122,"Namibia":123,"Nepal":124,"Netherlands":125,"New Zealand":126,"Nicaragua":127,"Niger":128,"Nigeria":129,"North Macedonia":130,"Norway":131,"Oman":132,"Pakistan":133,"Panama":134,"Papua New Guinea":135,"Paraguay":136,"Peru":137,"Philippines":138,"Poland":139,"Portugal":140,"Qatar":141,"Romania":142,"Russia":143,"Rwanda":144,"Saint Kitts and Nevis":145,"Saint Lucia":146,"Saint Vincent and the Grenadines":147,"Samoa":148,"San Marino":149,"Sao Tome and Principe":150,"Saudi Arabia":151,"Senegal":152,"Serbia":153,"Seychelles":154,"Sierra Leone":155,"Singapore":156,"Slovakia":157,"Slovenia":158,"Solomon Islands":159,"Somalia":160,"South Africa":161,"South Sudan":162,"Spain":163,"Sri Lanka":164,"Sudan":165,"Suriname":166,"Sweden":167,"Switzerland":168,"Syria":169,"Taiwan*":170,"Tajikistan":171,"Tanzania":172,"Thailand":173,"Timor-Leste":174,"Togo":175,"Trinidad and Tobago":176,"Tunisia":177,"Turkey":178,"US":179,"Uganda":180,"Ukraine":181,"United Arab Emirates":182,"United Kingdom":183,"Uruguay":184,"Uzbekistan":185,"Vanuatu":186,"Venezuela":187,"Vietnam":188,"West Bank and Gaza":189,"Yemen":190,"Zambia":191,"Zimbabwe":192}
        def gocountry():  
            yo = messagebox.showinfo("info", "The data shown here is counted from the very first case reported in your area")
            country = clicked.get()
            country_id = country_dict.get((country.lower()).capitalize())
            country_cases = covid.get_status_by_country_id(country_id) 
            confirmed = country_cases.get('confirmed')
            active = country_cases.get('active')
            deaths = country_cases.get('deaths')
            recovered = country_cases.get('recovered')  
            if active == "" or None:
                    active = "N/A"
            if confirmed == "" or None:
                confirmed = "N/A"
            if deaths == "" or None:
                deaths = "N/A"
            if recovered == "" or None:
                recovered = "N/A"                              
            my_tree = ttk.Treeview(root, height=1)
                    #Define our columns
            my_tree['columns'] = ('Active Cases', 'Total Deaths', 'Total Recovered', 'Total Cases')
                # Format our column
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Active Cases", anchor=W, width=120, minwidth=25)
            my_tree.column("Total Deaths", anchor=W, width=120, minwidth=25)
            my_tree.column("Total Recovered", anchor=W, width=120, minwidth=25)
            my_tree.column("Total Cases", anchor=W, width=120, minwidth=25)
                    # create headings
            my_tree.heading("#0", text="Label", anchor=W)
            my_tree.heading("Active Cases",text="Active Cases", anchor=W)
            my_tree.heading("Total Deaths",text="Total Deaths", anchor=W)
            my_tree.heading("Total Recovered",text="Total Recovered", anchor=W)
            my_tree.heading("Total Cases",text="Total Cases", anchor=W)
                # add data
            my_tree.insert(parent='', index='end', iid=0, text="", values=(active, deaths,recovered, confirmed))
                # pack to the screen
            root.geometry("858x300")
            my_tree.grid(row=0, column=2)
            data1 = {'data': ['Active','Total','Deaths', "Recovred"],
            'numbers': [int(active), int(confirmed), int(deaths), int(recovered)]}
            df1 = DataFrame(data1,columns=['data','numbers'])
            figure1 = plt.Figure(figsize=(4, 7), dpi=100)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, root)
            bar1.get_tk_widget().grid(row=1, column=2)
            df1 = df1[['data','numbers']].groupby('data').sum()
            df1.plot(kind='bar', legend=True, ax=ax1)
            ax1.set_title('Graph')
            root.geometry("858x770")
            technifyed_logo = ImageTk.PhotoImage(Image.open("/Users/abhishektrehan/Desktop/aa.png"))
            technifyed_logo_label = Label(image=technifyed_logo)
            technifyed_logo_label.image = technifyed_logo
            technifyed_logo_label.grid(row=1, column=1, pady=30, padx=10)
        gocountrybtn = Button(root, text="Go", command=gocountry)
        gocountrybtn['font'] = myFont
        gocountrybtn.grid(row=0, column=1)
    countrybtn = Button(root, text="Choose a Country", command=country_stats)
    countrybtn['font'] = myFont
    countrybtn.grid(row=0, column=0, padx=50, pady=50)
    statebtn = Button(root, text="All states in India", command=india_state_stats)
    statebtn['font']= myFont
    statebtn.grid(row=0, column=1, padx=50, pady=50)

def compare_cases():
    destroyer()
    clicked = StringVar()
    clicked.set("Select")
    clicked1 = StringVar()
    clicked1.set("Select")
    drop = OptionMenu(root, clicked,"China","India","US","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico","Japan","Ethiopia","Philippines","Egypt","Vietnam","DR Congo","Turkey","Iran","Germany","Thailand","United Kingdom","France","Italy","Tanzania","South Africa","Myanmar","Kenya","South Korea","Colombia","Spain","Uganda","Argentina","Algeria","Sudan","Ukraine","Iraq","Afghanistan","Poland","Canada","Morocco","Saudi Arabia","Uzbekistan","Peru","Angola","Malaysia","Mozambique","Ghana","Yemen","Nepal","Venezuela","Madagascar","Cameroon","Côte d'Ivoire","North Korea","Australia","Niger","Sri Lanka","Burkina Faso","Mali","Romania","Malawi","Chile","Kazakhstan","Zambia","Guatemala","Ecuador","Syria","Netherlands","Senegal","Cambodia","Chad","Somalia""Zimbabwe","Guinea","Rwanda","Benin","Burundi","Tunisia","Bolivia","Belgium","Haiti","Cuba","South Sudan","Dominican Republic","Czech Republic (Czechia)","Greece","Jordan","Portugal","Azerbaijan","Sweden","Honduras","United Arab Emirates","Hungary","Tajikistan","Belarus","Austria","Papua New Guinea","Serbia","Israel","Switzerland","Togo","Sierra Leone","Laos","Paraguay","Bulgaria","Libya","Lebanon","Nicaragua","Kyrgyzstan","El Salvador","Turkmenistan","Singapore","Denmark","Finland","Congo","Slovakia","Norway","Oman","State of Palestine","Costa Rica","Liberia","Ireland","Central African Republic","New Zealand","Mauritania","Panama","Kuwait","Croatia","Moldova","Georgia","Eritrea","Uruguay","Bosnia and Herzegovina","Mongolia","Armenia","Jamaica","Qatar","Albania","Lithuania","Namibia","Gambia","Botswana","Gabon","Lesotho","North Macedonia","Slovenia","Guinea-Bissau","Latvia","Bahrain","Equatorial Guinea","Trinidad and Tobago","Estonia","Timor-Leste","Mauritius","Cyprus","Eswatini","Djibouti","Fiji""Comoros","Guyana","Bhutan","Solomon Islands","Montenegro","Luxembourg","Suriname","Cabo Verde","Micronesia","Maldives","Malta","Brunei","Belize","Bahamas","Iceland","Vanuatu","Barbados","Sao Tome & Principe","Samoa","Saint Lucia","Kiribati","Grenada","St. Vincent & Grenadines","Tonga","Seychelles","Antigua and Barbuda","Andorra","Dominica","Marshall Islands","Saint Kitts & Nevis","Monaco","Liechtenstein","San Marino","Palau","Tuvalu","Nauru","Holy See",)
    drop['font'] = myFont
    drop.grid(row=0, column=0, pady=20, padx=20)
    drop1 = OptionMenu(root, clicked1,"China","India","US","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico","Japan","Ethiopia","Philippines","Egypt","Vietnam","DR Congo","Turkey","Iran","Germany","Thailand","United Kingdom","France","Italy","Tanzania","South Africa","Myanmar","Kenya","South Korea","Colombia","Spain","Uganda","Argentina","Algeria","Sudan","Ukraine","Iraq","Afghanistan","Poland","Canada","Morocco","Saudi Arabia","Uzbekistan","Peru","Angola","Malaysia","Mozambique","Ghana","Yemen","Nepal","Venezuela","Madagascar","Cameroon","Côte d'Ivoire","North Korea","Australia","Niger","Sri Lanka","Burkina Faso","Mali","Romania","Malawi","Chile","Kazakhstan","Zambia","Guatemala","Ecuador","Syria","Netherlands","Senegal","Cambodia","Chad","Somalia""Zimbabwe","Guinea","Rwanda","Benin","Burundi","Tunisia","Bolivia","Belgium","Haiti","Cuba","South Sudan","Dominican Republic","Czech Republic (Czechia)","Greece","Jordan","Portugal","Azerbaijan","Sweden","Honduras","United Arab Emirates","Hungary","Tajikistan","Belarus","Austria","Papua New Guinea","Serbia","Israel","Switzerland","Togo","Sierra Leone","Laos","Paraguay","Bulgaria","Libya","Lebanon","Nicaragua","Kyrgyzstan","El Salvador","Turkmenistan","Singapore","Denmark","Finland","Congo","Slovakia","Norway","Oman","State of Palestine","Costa Rica","Liberia","Ireland","Central African Republic","New Zealand","Mauritania","Panama","Kuwait","Croatia","Moldova","Georgia","Eritrea","Uruguay","Bosnia and Herzegovina","Mongolia","Armenia","Jamaica","Qatar","Albania","Lithuania","Namibia","Gambia","Botswana","Gabon","Lesotho","North Macedonia","Slovenia","Guinea-Bissau","Latvia","Bahrain","Equatorial Guinea","Trinidad and Tobago","Estonia","Timor-Leste","Mauritius","Cyprus","Eswatini","Djibouti","Fiji""Comoros","Guyana","Bhutan","Solomon Islands","Montenegro","Luxembourg","Suriname","Cabo Verde","Micronesia","Maldives","Malta","Brunei","Belize","Bahamas","Iceland","Vanuatu","Barbados","Sao Tome & Principe","Samoa","Saint Lucia","Kiribati","Grenada","St. Vincent & Grenadines","Tonga","Seychelles","Antigua and Barbuda","Andorra","Dominica","Marshall Islands","Saint Kitts & Nevis","Monaco","Liechtenstein","San Marino","Palau","Tuvalu","Nauru","Holy See",)
    drop1['font'] = myFont
    drop1.grid(row=0, column=1, pady=20, padx=20)
    def compare_cases_go():
        country1 = clicked.get()
        country2= clicked1.get()
        country_dict = {"Afghanistan":1,"Albania":2,"Algeria":3,"Andorra":4,"Angola":5,"Antigua and Barbuda":6,"Argentina":7,"Armenia":8,"Australia":9,"Austria":10,"Azerbaijan":11,"Bahamas":12,"Bahrain":13,"Bangladesh":14,"Barbados":15,"Belarus":16,"Belgium":17,"Belize":18,"Benin":19,"Bhutan":20,"Bolivia":21,"Bosnia and Herzegovina":22,"Botswana":23,"Brazil":24,"Brunei":25,"Bulgaria":26,"Burkina Faso":27,"Burma":28,"Burundi":29,"Cabo Verde":30,"Cambodia":31,"Cameroon":32,"Canada":33,"Central African Republic":34,"Chad":35,"Chile":36,"China":37,"Colombia":38,"Comoros":39,"Congo (Brazzaville)":40,"Congo (Kinshasa)":41,"Costa Rica":42,"Cote d'Ivoire":43,"Croatia":44,"Cuba":45,"Cyprus":46,"Czechia":47,"Denmark":48,"Diamond Princess":49,"Djibouti":50,"Dominica":51,"Dominican Republic":52,"Ecuador":53,"Egypt":54,"El Salvador":55,"Equatorial Guinea":56,"Eritrea":57,"Estonia":58,"Eswatini":59,"Ethiopia":60,"Fiji":61,"Finland":62,"France":63,"Gabon":64,"Gambia":65,"Georgia":66,"Germany":67,"Ghana":68,"Greece":69,"Grenada":70,"Guatemala":71,"Guinea":72,"Guinea-Bissau":73,"Guyana":74,"Haiti":75,"Holy See":76,"Honduras":77,"Hungary":78,"Iceland":79,"India":80,"Indonesia":81,"Iran":82,"Iraq":83,"Ireland":84,"Israel":85,"Italy":86,"Jamaica":87,"Japan":88,"Jordan":89,"Kazakhstan":90,"Kenya":91,"Korea, South":92,"Kosovo":93,"Kuwait":94,"Kyrgyzstan":95,"Laos":96,"Latvia":97,"Lebanon":98,"Lesotho":99,"Liberia":100,"Libya":101,"Liechtenstein":102,"Lithuania":103,"Luxembourg":104,"MS Zaandam":105,"Madagascar":106,"Malawi":107,"Malaysia":108,"Maldives":109,"Mali":110,"Malta":111,"Marshall Islands":112,"Mauritania":113,"Mauritius":114,"Mexico":115,"Micronesia":116,"Moldova":117,"Monaco":118,"Mongolia":119,"Montenegro":120,"Morocco":121,"Mozambique":122,"Namibia":123,"Nepal":124,"Netherlands":125,"New Zealand":126,"Nicaragua":127,"Niger":128,"Nigeria":129,"North Macedonia":130,"Norway":131,"Oman":132,"Pakistan":133,"Panama":134,"Papua New Guinea":135,"Paraguay":136,"Peru":137,"Philippines":138,"Poland":139,"Portugal":140,"Qatar":141,"Romania":142,"Russia":143,"Rwanda":144,"Saint Kitts and Nevis":145,"Saint Lucia":146,"Saint Vincent and the Grenadines":147,"Samoa":148,"San Marino":149,"Sao Tome and Principe":150,"Saudi Arabia":151,"Senegal":152,"Serbia":153,"Seychelles":154,"Sierra Leone":155,"Singapore":156,"Slovakia":157,"Slovenia":158,"Solomon Islands":159,"Somalia":160,"South Africa":161,"South Sudan":162,"Spain":163,"Sri Lanka":164,"Sudan":165,"Suriname":166,"Sweden":167,"Switzerland":168,"Syria":169,"Taiwan*":170,"Tajikistan":171,"Tanzania":172,"Thailand":173,"Timor-Leste":174,"Togo":175,"Trinidad and Tobago":176,"Tunisia":177,"Turkey":178,"US":179,"Uganda":180,"Ukraine":181,"United Arab Emirates":182,"United Kingdom":183,"Uruguay":184,"Uzbekistan":185,"Vanuatu":186,"Venezuela":187,"Vietnam":188,"West Bank and Gaza":189,"Yemen":190,"Zambia":191,"Zimbabwe":192}
        # table1 data
        yo = messagebox.showinfo("info", "The data shown here is counted from the very first case reported in your area")
        country1_id = country_dict.get((country1.lower()).capitalize())
        country1_cases = covid.get_status_by_country_id(country1_id) 
        confirmed1 = country1_cases.get('confirmed')
        active1 = country1_cases.get('active')
        deaths1 = country1_cases.get('deaths')
        recovered1 = country1_cases.get('recovered') 
        # table1 formation
        my_tree = ttk.Treeview(root, height=1)
        #Define our columns
        my_tree['columns'] = ('Active Cases', 'Total Deaths', 'Total Recovered', 'Total Cases')
        # Format our column
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Active Cases", anchor=W, width=120, minwidth=25)
        my_tree.column("Total Deaths", anchor=W, width=120, minwidth=25)
        my_tree.column("Total Recovered", anchor=W, width=120, minwidth=25)
        my_tree.column("Total Cases", anchor=W, width=120, minwidth=25)
        # create headings
        my_tree.heading("#0", text="Label", anchor=W)
        my_tree.heading("Active Cases",text="Active Cases", anchor=W)
        my_tree.heading("Total Deaths",text="Total Deaths", anchor=W)
        my_tree.heading("Total Recovered",text="Total Recovered", anchor=W)
        my_tree.heading("Total Cases",text="Total Cases", anchor=W)
        # add data
        my_tree.insert(parent='', index='end', iid=0, text="", values=(active1, deaths1, recovered1, confirmed1))
        # grid to the screen
        my_tree.grid(row=1, column=0)
       
        # country 2
        country2_id = country_dict.get((country2.lower()).capitalize())
        country2_cases = covid.get_status_by_country_id(country2_id) 
        confirmed2 = country2_cases.get('confirmed')
        active2 = country2_cases.get('active')
        deaths2 = country2_cases.get('deaths')
        recovered2 = country2_cases.get('recovered') 
        # table1 formation
        my_tree = ttk.Treeview(root, height=1)
        #Define our columns
        my_tree['columns'] = ('Active Cases', 'Total Deaths', 'Total Recovered', 'Total Cases')
        # Format our column
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Active Cases", anchor=W, width=120, minwidth=25)
        my_tree.column("Total Deaths", anchor=W, width=120, minwidth=25)
        my_tree.column("Total Recovered", anchor=W, width=120, minwidth=25)
        my_tree.column("Total Cases", anchor=W, width=120, minwidth=25)
        # create headings
        my_tree.heading("#0", text="Label", anchor=W)
        my_tree.heading("Active Cases",text="Active Cases", anchor=W)
        my_tree.heading("Total Deaths",text="Total Deaths", anchor=W)
        my_tree.heading("Total Recovered",text="Total Recovered", anchor=W)
        my_tree.heading("Total Cases",text="Total Cases", anchor=W)
        # add data
        my_tree.insert(parent='', index='end', iid=0, text="", values=(active2, deaths2, recovered2, confirmed2))
        # grid to the screen
        drop1.destroy()
        drop2 = OptionMenu(root, clicked1,"China","India","US","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico","Japan","Ethiopia","Philippines","Egypt","Vietnam","DR Congo","Turkey","Iran","Germany","Thailand","United Kingdom","France","Italy","Tanzania","South Africa","Myanmar","Kenya","South Korea","Colombia","Spain","Uganda","Argentina","Algeria","Sudan","Ukraine","Iraq","Afghanistan","Poland","Canada","Morocco","Saudi Arabia","Uzbekistan","Peru","Angola","Malaysia","Mozambique","Ghana","Yemen","Nepal","Venezuela","Madagascar","Cameroon","Côte d'Ivoire","North Korea","Australia","Niger","Sri Lanka","Burkina Faso","Mali","Romania","Malawi","Chile","Kazakhstan","Zambia","Guatemala","Ecuador","Syria","Netherlands","Senegal","Cambodia","Chad","Somalia""Zimbabwe","Guinea","Rwanda","Benin","Burundi","Tunisia","Bolivia","Belgium","Haiti","Cuba","South Sudan","Dominican Republic","Czech Republic (Czechia)","Greece","Jordan","Portugal","Azerbaijan","Sweden","Honduras","United Arab Emirates","Hungary","Tajikistan","Belarus","Austria","Papua New Guinea","Serbia","Israel","Switzerland","Togo","Sierra Leone","Laos","Paraguay","Bulgaria","Libya","Lebanon","Nicaragua","Kyrgyzstan","El Salvador","Turkmenistan","Singapore","Denmark","Finland","Congo","Slovakia","Norway","Oman","State of Palestine","Costa Rica","Liberia","Ireland","Central African Republic","New Zealand","Mauritania","Panama","Kuwait","Croatia","Moldova","Georgia","Eritrea","Uruguay","Bosnia and Herzegovina","Mongolia","Armenia","Jamaica","Qatar","Albania","Lithuania","Namibia","Gambia","Botswana","Gabon","Lesotho","North Macedonia","Slovenia","Guinea-Bissau","Latvia","Bahrain","Equatorial Guinea","Trinidad and Tobago","Estonia","Timor-Leste","Mauritius","Cyprus","Eswatini","Djibouti","Fiji""Comoros","Guyana","Bhutan","Solomon Islands","Montenegro","Luxembourg","Suriname","Cabo Verde","Micronesia","Maldives","Malta","Brunei","Belize","Bahamas","Iceland","Vanuatu","Barbados","Sao Tome & Principe","Samoa","Saint Lucia","Kiribati","Grenada","St. Vincent & Grenadines","Tonga","Seychelles","Antigua and Barbuda","Andorra","Dominica","Marshall Islands","Saint Kitts & Nevis","Monaco","Liechtenstein","San Marino","Palau","Tuvalu","Nauru","Holy See",)
        drop2['font'] = myFont
        drop2.grid(row=2, column=0, pady=20, padx=20)
        my_tree.grid(row=3, column=0)
        
        #graph-double bar chart
        c1 = str(country1)
        c2 = str(country2)
        data1 = {'data': ['Active','Total','Deaths', "Recovred"],
        c1 : [int(active1), int(confirmed1), int(deaths1), int(recovered1)],
        c2 :[int(active2), int(confirmed2), int(deaths2), int(recovered2)]}
        df1 = DataFrame(data1,columns=['data',c1, c2])
        figure1 = plt.Figure(figsize=(4, 7), dpi=70)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().grid(row=4, column=0)
        df1 = df1[['data', c1, c2]].groupby('data').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Comparison of Countries')
        compare_cases_go_button2 = Button(root, text="Go", command=compare_cases_go)
        compare_cases_go_button2['font'] = myFont
        compare_cases_go_button2.grid(row=5, column=0)
        compare_cases_go_button.destroy()
        root.geometry("500x950")
    compare_cases_go_button = Button(root, text="Go", command=compare_cases_go)
    compare_cases_go_button['font'] = myFont
    compare_cases_go_button.grid(row=0, column=2)       






GREY = (0.78, 0.78, 0.78)  # uninfected
RED = (0.96, 0.15, 0.15)   # infected
GREEN = (0, 0.86, 0.03)    # recovered
BLACK = (0, 0, 0)          # dead

COVID19_PARAMS = {
    "r0": 2.28,
    "incubation": 5,
    "percent_mild": 0.8,
    "mild_recovery": (7, 14),
    "percent_severe": 0.2,
    "severe_recovery": (21, 42),
    "severe_death": (14, 56),
    "fatality_rate": 0.034,
    "serial_interval": 7
}


class Virus():
    def __init__(self, params):
        # create plot
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111, projection="polar")
        self.axes.grid(False)
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])
        self.axes.set_ylim(0, 1)

        # create annotations
        self.day_text = self.axes.annotate(
            "Day 0", xy=[np.pi / 2, 1], ha="center", va="bottom")
        self.infected_text = self.axes.annotate(
            "Infected: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=RED)
        self.deaths_text = self.axes.annotate(
            "\nDeaths: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=BLACK)
        self.recovered_text = self.axes.annotate(
            "\n\nRecovered: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=GREEN)

        # create member variables
        self.day = 0
        self.total_num_infected = 0
        self.num_currently_infected = 0
        self.num_recovered = 0
        self.num_deaths = 0
        self.r0 = params["r0"]
        self.percent_mild = params["percent_mild"]
        self.percent_severe = params["percent_severe"]
        self.fatality_rate = params["fatality_rate"]
        self.serial_interval = params["serial_interval"]

        self.mild_fast = params["incubation"] + params["mild_recovery"][0]
        self.mild_slow = params["incubation"] + params["mild_recovery"][1]
        self.severe_fast = params["incubation"] + params["severe_recovery"][0]
        self.severe_slow = params["incubation"] + params["severe_recovery"][1]
        self.death_fast = params["incubation"] + params["severe_death"][0]
        self.death_slow = params["incubation"] + params["severe_death"][1]

        self.mild = {i: {"thetas": [], "rs": []} for i in range(self.mild_fast, 365)}
        self.severe = {
            "recovery": {i: {"thetas": [], "rs": []} for i in range(self.severe_fast, 365)},
            "death": {i: {"thetas": [], "rs": []} for i in range(self.death_fast, 365)}
        }

        self.exposed_before = 0
        self.exposed_after = 1

        self.initial_population()


    def initial_population(self):
        population = 4500
        self.num_currently_infected = 1
        self.total_num_infected = 1
        indices = np.arange(0, population) + 0.5
        self.thetas = np.pi * (1 + 5**0.5) * indices
        self.rs = np.sqrt(indices / population)
        self.plot = self.axes.scatter(self.thetas, self.rs, s=5, color=GREY)
        # patient zero
        self.axes.scatter(self.thetas[0], self.rs[0], s=5, color=RED)
        self.mild[self.mild_fast]["thetas"].append(self.thetas[0])
        self.mild[self.mild_fast]["rs"].append(self.rs[0])


    def spread_virus(self, i):
        self.exposed_before = self.exposed_after
        if self.day % self.serial_interval == 0 and self.exposed_before < 4500:
            self.num_new_infected = round(self.r0 * self.total_num_infected)
            self.exposed_after += round(self.num_new_infected * 1.1)
            if self.exposed_after > 4500:
                self.num_new_infected = round((4500 - self.exposed_before) * 0.9)
                self.exposed_after = 4500
            self.num_currently_infected += self.num_new_infected
            self.total_num_infected += self.num_new_infected
            self.new_infected_indices = list(
                np.random.choice(
                    range(self.exposed_before, self.exposed_after),
                    self.num_new_infected,
                    replace=False))
            thetas = [self.thetas[i] for i in self.new_infected_indices]
            rs = [self.rs[i] for i in self.new_infected_indices]
            self.anim.event_source.stop()
            if len(self.new_infected_indices) > 24:
                size_list = round(len(self.new_infected_indices) / 24)
                theta_chunks = list(self.chunks(thetas, size_list))
                r_chunks = list(self.chunks(rs, size_list))
                self.anim2 = ani.FuncAnimation(
                    self.fig,
                    self.one_by_one,
                    interval=50,
                    frames=len(theta_chunks),
                    fargs=(theta_chunks, r_chunks, RED))
            else:
                self.anim2 = ani.FuncAnimation(
                    self.fig,
                    self.one_by_one,
                    interval=50,
                    frames=len(thetas),
                    fargs=(thetas, rs, RED))
            self.assign_symptoms()

        self.day += 1

        self.update_status()
        self.update_text()


    def one_by_one(self, i, thetas, rs, color):
        self.axes.scatter(thetas[i], rs[i], s=5, color=color)
        if i == (len(thetas) - 1):
            self.anim2.event_source.stop()
            self.anim.event_source.start()


    def chunks(self, a_list, n):
        for i in range(0, len(a_list), n):
            yield a_list[i:i + n]


    def assign_symptoms(self):
        num_mild = round(self.percent_mild * self.num_new_infected)
        num_severe = round(self.percent_severe * self.num_new_infected)
        # choose random subset of newly infected to have mild symptoms
        self.mild_indices = np.random.choice(self.new_infected_indices, num_mild, replace=False)
        # assign the rest severe symptoms, either resulting in recovery or death
        remaining_indices = [i for i in self.new_infected_indices if i not in self.mild_indices]
        percent_severe_recovery = 1 - (self.fatality_rate / self.percent_severe)
        num_severe_recovery = round(percent_severe_recovery * num_severe)
        self.severe_indices = []
        self.death_indices = []
        if remaining_indices:
            self.severe_indices = np.random.choice(remaining_indices, num_severe_recovery, replace=False)
            self.death_indices = [i for i in remaining_indices if i not in self.severe_indices]

        # assign recovery/death day
        low = self.day + self.mild_fast
        high = self.day + self.mild_slow
        for mild in self.mild_indices:
            recovery_day = np.random.randint(low, high)
            mild_theta = self.thetas[mild]
            mild_r = self.rs[mild]
            self.mild[recovery_day]["thetas"].append(mild_theta)
            self.mild[recovery_day]["rs"].append(mild_r)
        low = self.day + self.severe_fast
        high = self.day + self.severe_slow
        for recovery in self.severe_indices:
            recovery_day = np.random.randint(low, high)
            recovery_theta = self.thetas[recovery]
            recovery_r = self.rs[recovery]
            self.severe["recovery"][recovery_day]["thetas"].append(recovery_theta)
            self.severe["recovery"][recovery_day]["rs"].append(recovery_r)
        low = self.day + self.death_fast
        high = self.day + self.death_slow
        for death in self.death_indices:
            death_day = np.random.randint(low, high)
            death_theta = self.thetas[death]
            death_r = self.rs[death]
            self.severe["death"][death_day]["thetas"].append(death_theta)
            self.severe["death"][death_day]["rs"].append(death_r)


    def update_status(self):
        if self.day >= self.mild_fast:
            mild_thetas = self.mild[self.day]["thetas"]
            mild_rs = self.mild[self.day]["rs"]
            self.axes.scatter(mild_thetas, mild_rs, s=5, color=GREEN)
            self.num_recovered += len(mild_thetas)
            self.num_currently_infected -= len(mild_thetas)
        if self.day >= self.severe_fast:
            rec_thetas = self.severe["recovery"][self.day]["thetas"]
            rec_rs = self.severe["recovery"][self.day]["rs"]
            self.axes.scatter(rec_thetas, rec_rs, s=5, color=GREEN)
            self.num_recovered += len(rec_thetas)
            self.num_currently_infected -= len(rec_thetas)
        if self.day >= self.death_fast:
            death_thetas = self.severe["death"][self.day]["thetas"]
            death_rs = self.severe["death"][self.day]["rs"]
            self.axes.scatter(death_thetas, death_rs, s=5, color=BLACK)
            self.num_deaths += len(death_thetas)
            self.num_currently_infected -= len(death_thetas)


    def update_text(self):
        self.day_text.set_text("Day {}".format(self.day))
        self.infected_text.set_text("Infected: {}".format(self.num_currently_infected))
        self.deaths_text.set_text("\nDeaths: {}".format(self.num_deaths))
        self.recovered_text.set_text("\n\nRecovered: {}".format(self.num_recovered))


    def gen(self):
        while self.num_deaths + self.num_recovered < self.total_num_infected:
            yield


    def animate(self):
        self.anim = ani.FuncAnimation(
            self.fig,
            self.spread_virus,
            frames=self.gen,
            repeat=True)

def main():
    coronavirus = Virus(COVID19_PARAMS)
    coronavirus.animate()
    plt.show()
def simulate_run():
    if __name__ == "__main__":
        data_info = messagebox.askokcancel("Info", "This chart does not use any specific data of a particular area. We have made this to show the pace of coronavirus infection. This is just for representational purposes.")
        if data_info == True:
            root.update()
            main()
        else:
            pass
def Covid_info_WHO():
    webbrowser.open_new_tab("https://www.technifyed.com/2021/05/24/covid-19-basics/")
# fetch button
fetch_btn = Button(root, text=" LIVE COVID-19 STATS", command=stats, relief=SUNKEN, bg='red',fg='white', borderless=1)
fetch_btn['font'] = myFont
fetch_btn.grid(row=2, column=0, pady=(20, 40), padx=(20, 10))
# simulate button
sim_btn = Button(root, text="SIMULATE CORONAVIRUS",command=simulate_run, relief=SUNKEN, bg='red',fg='white', borderless=1)
sim_btn['font'] = myFont
sim_btn.grid(row=2, column=1, pady=(20, 40), padx=(20, 10))
# covid-19 information button (WHO)
info_btn = Button(root, text="    COVID-19 INFO    ", command=Covid_info_WHO, relief=SUNKEN, bg='red',fg='white', borderless=1)
info_btn['font'] = myFont
info_btn.grid(row=2, column=2, pady=(20, 40), padx=(20, 10))
# comapre button
compare_cases_button = Button(root, text="COMPARE 2 COUNTRIES", command=compare_cases, relief=SUNKEN, bg='red', fg='white', borderless=1)
compare_cases_button['font'] = myFont
compare_cases_button.grid(row=3, column=1, pady=(20, 40), padx=(20, 10))
# technifyed logo
#LogoLabel = Label(image=Logo)
#LogoLabel.image = Logo
technifyed_logo = ImageTk.PhotoImage(Image.open("technifyed_logo.png"))
technifyed_logo_label = Label(image=technifyed_logo)
technifyed_logo_label.image = technifyed_logo
technifyed_logo_label.grid(row=4, column=1, pady=30, padx=10)

root.mainloop()
