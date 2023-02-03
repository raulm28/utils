from tabula import read_pdf
import pandas as pd
pd.set_option('display.max_rows',150000)
pd.set_option('display.max_columns',20)
pd.set_option('display.width', 10000)
df = read_pdf("/Users/molinar1/Downloads/Informatica-DataClasses.pdf",pages='all',lattice=True, multiple_tables=True)

# df[1].columns = ['Critical Capabilities','Adaptive','Alation','Alex Solutions','ASG','Collibra','Data Advantage Group','data.world','erwin','Global IDs','IBM','Infogix','Informatica','Oracle','SAP','Smartlogic','Semantic Web Company','Syniti']
# df[1][['Adaptive','Alation','Alex Solutions','ASG','Collibra','Data Advantage Group','data.world','erwin','Global IDs','IBM','Infogix','Informatica','Oracle','SAP','Smartlogic','Semantic Web Company','Syniti']]= df[1][['Adaptive','Alation','Alex Solutions','ASG','Collibra','Data Advantage Group','data.world','erwin','Global IDs','IBM','Infogix','Informatica','Oracle','SAP','Smartlogic','Semantic Web Company','Syniti']].replace(to_replace='[^\\d.\\d]{0,10}',value='', regex=True)
#
# df[3].columns = ['Use Cases','Adaptive','Alation','Alex Solutions','ASG','Collibra','Data Advantage Group','data.world','erwin','Global IDs','IBM','Infogix','Informatica','Oracle','SAP','Smartlogic','Semantic Web Company','Syniti']
# df[3][['Adaptive','Alation','Alex Solutions','ASG','Collibra','Data Advantage Group','data.world','erwin','Global IDs','IBM','Infogix','Informatica','Oracle','SAP','Smartlogic','Semantic Web Company','Syniti']]= df[1][['Adaptive','Alation','Alex Solutions','ASG','Collibra','Data Advantage Group','data.world','erwin','Global IDs','IBM','Infogix','Informatica','Oracle','SAP','Smartlogic','Semantic Web Company','Syniti']].replace(to_replace='[^\\d.\\d]{0,10}',value='', regex=True)
#
#
# print(df[1][['Critical Capabilities','Collibra','Informatica']])
# print(df[3][['Use Cases','Collibra','Informatica']].iloc[:-1,:])
# new = pd.concat(df,ignore_index=True)
# # print(new)
# writer = pd.ExcelWriter('ICD10CM-Neoplasm-P-2021.xlsx', engine='openpyxl')
# new.to_excel(writer,sheet_name='Data',index=False)
# writer.save()