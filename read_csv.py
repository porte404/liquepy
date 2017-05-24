import pandas as pd
#import arcpy

input_path = "D:/D--Temp/Porter/"
#arcpy.env.workspace = input_path

input_layers = "test_explor.csv"

#------------------------#
# INPUT LAYER FORMATTING #
#------------------------#
#
#0: OBJECT_ID 
#1: EXPLOR_ID
#2: UNIT_ID  
#3: DEPTH
#4: USCS_CLASS
#5: WET_DRY
#6: N_VAL

df = pd.read_csv(input_path + input_layers, index_col=['OBJECT_ID','EXPLOR_ID'])


dt1 = df.iloc[df.index.get_level_values(1) == 2]
#for r in dt1.itertuples():
#    print(r)
dt2 = df.loc[df.index(1)]
print(dt2)

#print(df.index.get_level_values(1).idxmax())

def iterate_df_rows(df):
        dt1 = df.iloc[df.index.get_level_values(1) == 2]
        for row in df.itertuples():
            pass

class borehole():
     def __init__(self, UNIT_ID, DEPTH, USCS_CLASS, WET_DRY, N_VAL):
         pass
     def __str__(self):
         return "Exploration {} at {}' depth.".format(EXPLOR_ID=1,DEPTH=15)
     def __repr__(self):
         return "{}()".format(self.__class__.__name__)
     
     
class liquefied(borehole):
    pass

#iterate_df_rows(df)
    
#------------------------#
# INPUT LAYER FORMATTING #
#------------------------#
#
#