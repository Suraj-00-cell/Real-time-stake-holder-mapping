import pandas as pd
import numpy as np
from upload import browse_file
import pandas as pd
import numpy as np
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
from upload import browse_file
A = []
B = []

def column_input_for_stat_and_whole():
    n = int(input("*****For how many column you want the output"))
    print('''*****Enter the column names for which you want the graph or stats or excel file********
                                format - Enter column one ---> Press Enter enter second column etc''')
    
    for i in range(n):
        name = input("enter column name")
        A.append(name)
    
    return A

def column_and_cat_input():
    main_column = input("*******Enter the main column for which you want the grouping**********")
    B.append(main_column)
    n = int(input("*****For how many column you want the output"))
    print('''*****Enter the column names for which you want the graph or stats or excel file********
                                format - Enter column one ---> Press Enter enter second column etc''')
    for i in range(n):
        name = input("enter column name")
        A.append(name) 

    return B,A


def statistics():

    #df = pd.read_excel("HH.xlsx")  
    df = browse_file()

    list = column_input_for_stat_and_whole()


    
    #list=["Ward_No","Residence","Ownership","House_Type","Status","Religion","Category","Social_class","Electrified","Mobile","Cooking_Fuel","DW_Source","DW_Availability","TLT_Availability","WW_Disposed","Garbage","TB_Last_3YR","Malaria_Last_3YR","Dengue_Last_3YR","PH","CP","Heart_Attack","Delivery_Last_3Yr","MM","CM","Main_Occupation_01","Main_Occupation_02","Agriculture_then_land_owned (in Acre)","Cultivation_Land (in Acre)","Crop_Taken","Irrigation_Facility","Pump(in HP)","No_of_Month_Pump_Used","Pump_Usage_Hours/day","Source","Distance_Source_To_Use (in meter)","Annual_Income_Agriculture (in INR)","Month_Receiving_Money_Agriculture","Quantity_Agriculture_Sold (in Tonn)","No_Cow","No_Bullocks","No_Sheep","No_Goat","No_Poultry","Dependency_Livestock","Livestock_Income_Monthly (In INR)","Job_Card_MGNREGS","Employment_MGNREGS","Govt_Employee","Room_Type","No_Windows","No_Roof_Opening","No_TV","TV_Usage/Day_(hours)","No_Ref","Ref_Usage/Day_(hours)","No_Fan","Fan_Usage/Day_(hours)","No_Water_Heater","No_Mixer","No_CFL","CFL_Usage/Day_(hours)","No_Mobile","No_Shop","No_Tailoring","No_Water_Pump","No_Bank_Accounts","Bank_Name","Service","Loan_Taken","Electricity_Bill_(INR/Month)","Load_Shedding_Hrs","Water_Cost_INR/Month","Migrated_Seasonally","No_of_Months_MS","Who_MS","MS_Since_Year"]

    j = 0

    writer = pd.ExcelWriter("output_stats.xlsx", engine='xlsxwriter')

    for i in list:
        column_description = df[i].describe()    
        # Print the description
        sheet1 = "sheet" + str(j)
        j+=1
        column_description.to_excel(writer, sheet_name=sheet1)
        
    writer.save()   


def categorical_visual():

    #df = pd.read_excel("HH.xlsx")  
    df = browse_file()
    f_list , list = column_and_cat_input()
    #f_list = ["Ward_No"]
    #list=["Residence","Ownership","House_Type","Status","Religion","Category","Social_class","Electrified","Mobile","Cooking_Fuel","DW_Source","DW_Availability","TLT_Availability","WW_Disposed","Garbage","TB_Last_3YR","Malaria_Last_3YR","Dengue_Last_3YR","PH","CP","Heart_Attack","Delivery_Last_3Yr","MM","CM","Main_Occupation_01","Main_Occupation_02","Agriculture_then_land_owned (in Acre)","Cultivation_Land (in Acre)","Crop_Taken","Irrigation_Facility","Pump(in HP)","No_of_Month_Pump_Used","Pump_Usage_Hours/day","Source","Distance_Source_To_Use (in meter)","Annual_Income_Agriculture (in INR)","Month_Receiving_Money_Agriculture","Quantity_Agriculture_Sold (in Tonn)","No_Cow","No_Bullocks","No_Sheep","No_Goat","No_Poultry","Dependency_Livestock","Livestock_Income_Monthly (In INR)","Job_Card_MGNREGS","Employment_MGNREGS","Govt_Employee","Room_Type","No_Windows","No_Roof_Opening","No_TV","TV_Usage/Day_(hours)","No_Ref","Ref_Usage/Day_(hours)","No_Fan","Fan_Usage/Day_(hours)","No_Water_Heater","No_Mixer","No_CFL","CFL_Usage/Day_(hours)","No_Mobile","No_Shop","No_Tailoring","No_Water_Pump","No_Bank_Accounts","Bank_Name","Service","Loan_Taken","Electricity_Bill_(INR/Month)","Load_Shedding_Hrs","Water_Cost_INR/Month","Migrated_Seasonally","No_of_Months_MS","Who_MS","MS_Since_Year"]


    # Save the plot to a folder path
    folder_path = input("enter the path") # Specify the folder path here
    

    for i in list:
        # Calculate the percentage of each status within each ward
        status_counts = df.groupby([f_list[0], i]).size()
        status_perc = status_counts.groupby(level=0).apply(lambda x: x / float(x.sum()) * 100)

        # Pivot the data to create a new DataFrame with status categories as columns
        status_df = status_perc.unstack(i)

        # Plot the stacked bar chart
        status_df.plot(kind='bar', edgecolor='black')

        # Set the plot title and labels with Times New Roman font
        title_text = str(i) + ' Distribution'
        title_font = {'fontname': 'Times New Roman', 'fontsize': 16, 'fontweight': 'bold'}

        # Add black border to the plot title
        title_text_obj = plt.title(title_text, **title_font)
        title_text_obj.set_path_effects([path_effects.Stroke(foreground='black'), path_effects.Normal()])

        # Set the plot title and labels with bold font weight
        plt.ylabel('Percentage', fontsize=16, fontweight='bold' , fontname='Times New Roman')

        # Set legend font size and position
        plt.legend(fontsize=12, loc='upper right')

        plt.xticks(fontsize=16, fontname='Times New Roman')
        plt.yticks(fontsize=16, fontname='Times New Roman')
        

        # Specify the file name here
        #file_name = str(i) + ".png"
        #file_path = folder_path + '/' + file_name

        #plt.savefig(file_path)
        plt.show()


def full_visual():

    #df = pd.read_excel("HH.xlsx")  
    df = browse_file()
    list = column_input_for_stat_and_whole()
    
    #list=["Residence","Ownership","House_Type","Status","Religion","Category","Social_class","Electrified","Mobile","Cooking_Fuel","DW_Source","DW_Availability","TLT_Availability","WW_Disposed","Garbage","TB_Last_3YR","Malaria_Last_3YR","Dengue_Last_3YR","PH","CP","Heart_Attack","Delivery_Last_3Yr","MM","CM","Main_Occupation_01","Main_Occupation_02","Agriculture_then_land_owned (in Acre)","Cultivation_Land (in Acre)","Crop_Taken","Irrigation_Facility","Pump(in HP)","No_of_Month_Pump_Used","Pump_Usage_Hours/day","Source","Distance_Source_To_Use (in meter)","Annual_Income_Agriculture (in INR)","Month_Receiving_Money_Agriculture","Quantity_Agriculture_Sold (in Tonn)","No_Cow","No_Bullocks","No_Sheep","No_Goat","No_Poultry","Dependency_Livestock","Livestock_Income_Monthly (In INR)","Job_Card_MGNREGS","Employment_MGNREGS","Govt_Employee","Room_Type","No_Windows","No_Roof_Opening","No_TV","TV_Usage/Day_(hours)","No_Ref","Ref_Usage/Day_(hours)","No_Fan","Fan_Usage/Day_(hours)","No_Water_Heater","No_Mixer","No_CFL","CFL_Usage/Day_(hours)","No_Mobile","No_Shop","No_Tailoring","No_Water_Pump","No_Bank_Accounts","Bank_Name","Service","Loan_Taken","Electricity_Bill_(INR/Month)","Load_Shedding_Hrs","Water_Cost_INR/Month","Migrated_Seasonally","No_of_Months_MS","Who_MS","MS_Since_Year"]
    #list=["Residence","Ownership","House_Type"]

    # Save the plot to a folder path
    folder_path = input("enter the path") # Specify the folder path here

    for i in list:

        # Calculate the percentage
        counts = df[i].value_counts()
        perc = counts / counts.sum() * 100

        # Create a bar chart for the percentage of each house type
        a =  perc.plot(kind='bar', color='grey' , edgecolor='black')

        # Set the plot title and labels with Times New Roman font
        title_text = i + ' Distribution in Village'
        title_font = {'fontname': 'Times New Roman', 'fontsize': 20, 'fontweight': 'bold'}

        # Add black border to the plot title
        title_text_obj = plt.title(title_text, **title_font)
        title_text_obj.set_path_effects([path_effects.Stroke(foreground='black'), path_effects.Normal()])

        # Set the plot title and labels with bold font weight
        plt.ylabel('Percentage', fontsize=16, fontweight='bold' , fontname='Times New Roman')

    
        # Customize x-axis tick labels
        plt.xticks(rotation=0, fontsize=16, fontname='Times New Roman')
        plt.yticks(fontsize=16, fontname='Times New Roman' , )

        
        # Display the percentage values on top of each bar
        for i, v in enumerate(perc):
            a.text(i, v, f"{v:.1f}%", ha='center', va='bottom', fontweight='bold')

    
        
        # Specify the file name here
        file_name = str(i) + ".png"
        file_path = folder_path + '/' + file_name


    
        #plt.savefig(file_path)


        # Display the chart
        plt.show()

def whole_save():

    #df = pd.read_excel("HH.xlsx")  
    df = browse_file()
    #f_list = ["Ward_No"]
    #list=["Residence","Ownership","House_Type","Status","Religion","Category","Social_class","Electrified","Mobile","Cooking_Fuel","DW_Source","DW_Availability","TLT_Availability","WW_Disposed","Garbage","TB_Last_3YR","Malaria_Last_3YR","Dengue_Last_3YR","PH","CP","Heart_Attack","Delivery_Last_3Yr","MM","CM","Main_Occupation_01","Main_Occupation_02","Agriculture_then_land_owned (in Acre)","Cultivation_Land (in Acre)","Crop_Taken","Irrigation_Facility","Pump(in HP)","No_of_Month_Pump_Used","Pump_Usage_Hours/day","Source","Distance_Source_To_Use (in meter)","Annual_Income_Agriculture (in INR)","Month_Receiving_Money_Agriculture","Quantity_Agriculture_Sold (in Tonn)","No_Cow","No_Bullocks","No_Sheep","No_Goat","No_Poultry","Dependency_Livestock","Livestock_Income_Monthly (In INR)","Job_Card_MGNREGS","Employment_MGNREGS","Govt_Employee","Room_Type","No_Windows","No_Roof_Opening","No_TV","TV_Usage/Day_(hours)","No_Ref","Ref_Usage/Day_(hours)","No_Fan","Fan_Usage/Day_(hours)","No_Water_Heater","No_Mixer","No_CFL","CFL_Usage/Day_(hours)","No_Mobile","No_Shop","No_Tailoring","No_Water_Pump","No_Bank_Accounts","Bank_Name","Service","Loan_Taken","Electricity_Bill_(INR/Month)","Load_Shedding_Hrs","Water_Cost_INR/Month","Migrated_Seasonally","No_of_Months_MS","Who_MS","MS_Since_Year"]

    f_list , list = column_and_cat_input()

    # Create an Excel writer object
    writer = pd.ExcelWriter('full_village_wise_data.xlsx', engine='xlsxwriter')


    j=0


    for i in list:

        # Calculate the percentage of each house type

        df.groupby([f_list[0], i])
        df1 = df[i].value_counts()
        df2 = df1 / df1.sum() * 100
    
        #for i in range(len(list)):
        sheet1 = "sheet_count" + str(j)
        sheet2 = "sheet_percentage" + str(j)
        j+=1
        df1.to_excel(writer, sheet_name=sheet1)
        df2.to_excel(writer, sheet_name=sheet2)

    writer.save()  


def category_save():
    #df = pd.read_excel("HH.xlsx")  
    df = browse_file()

    j=0

    f_list , list = column_and_cat_input()
    #f_list = ["Ward_No"]
    #list=["Residence","Ownership","House_Type","Status","Religion","Category","Social_class","Electrified","Mobile","Cooking_Fuel","DW_Source","DW_Availability","TLT_Availability","WW_Disposed","Garbage","TB_Last_3YR","Malaria_Last_3YR","Dengue_Last_3YR","PH","CP","Heart_Attack","Delivery_Last_3Yr","MM","CM","Main_Occupation_01","Main_Occupation_02","Agriculture_then_land_owned (in Acre)","Cultivation_Land (in Acre)","Crop_Taken","Irrigation_Facility","Pump(in HP)","No_of_Month_Pump_Used","Pump_Usage_Hours/day","Source","Distance_Source_To_Use (in meter)","Annual_Income_Agriculture (in INR)","Month_Receiving_Money_Agriculture","Quantity_Agriculture_Sold (in Tonn)","No_Cow","No_Bullocks","No_Sheep","No_Goat","No_Poultry","Dependency_Livestock","Livestock_Income_Monthly (In INR)","Job_Card_MGNREGS","Employment_MGNREGS","Govt_Employee","Room_Type","No_Windows","No_Roof_Opening","No_TV","TV_Usage/Day_(hours)","No_Ref","Ref_Usage/Day_(hours)","No_Fan","Fan_Usage/Day_(hours)","No_Water_Heater","No_Mixer","No_CFL","CFL_Usage/Day_(hours)","No_Mobile","No_Shop","No_Tailoring","No_Water_Pump","No_Bank_Accounts","Bank_Name","Service","Loan_Taken","Electricity_Bill_(INR/Month)","Load_Shedding_Hrs","Water_Cost_INR/Month","Migrated_Seasonally","No_of_Months_MS","Who_MS","MS_Since_Year"]

    writer = pd.ExcelWriter("output_file.xlsx", engine='xlsxwriter')
    for i in list:
        p = i
        # Calculate the percentage of each status within each ward
        df1 = df.groupby([f_list[0],i]).size()

        df2 = df1.groupby(level=0).apply(lambda x: x / float(x.sum()) * 100)

    
        #for i in range(len(list)):
        sheet1 = "sheet_count" + str(j)
        sheet2 = "sheet_percentage" + str(j)
        j+=1
        df1.to_excel(writer, sheet_name=sheet1)
        df2.to_excel(writer, sheet_name=sheet2)

    writer.save()  



        


