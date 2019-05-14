import pandas as pd

xl01 = pd.read_excel('./10601Jeri.xlsx')
xl01.sort_values(by=['firing_rate'],inplace=True)
xl01.to_excel('./10601JeriSORTED.xlsx')
 
#xl03 = pd.read_excel('./10603Jeri.xlsx')
#xl03.sort_values(by=['firing_rate'], inplace=True)
#xl03.to_excel('./10603JeriSORTED.xlsx')




