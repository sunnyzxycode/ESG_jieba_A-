# main solution function

# import function_risk_frequency as frf
import pandas as pd
from function_physical_risk_frequency import physical_risk_solution_frequency
from function_transport_risk_frequency import transport_risk_solution_frequency
from low_risk import low_risk_solution_frequency
from transaction_risk import transaction_risk_solution_frequency
from hard_risk import hard_risk_solution_frequency



# owner_path = input("pls input index: ")
# # owner_dict_path = r"C:\Users\zxy\OneDrive\桌面\ESG_20241021\物理风险v1.0.txt"
#
# physical_risk_solution_frequency(owner_path)


# 读取Excel表格
df = pd.read_excel(r"C:\Users\zxy\OneDrive\桌面\file_names.xlsx")
print(df)

df['Processed'] = df['Filename'].apply(hard_risk_solution_frequency)

df.to_excel(r"C:\Users\zxy\OneDrive\桌面\hard_risk_solved.xlsx")
