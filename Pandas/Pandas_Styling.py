#pandas styling exercises at w3resource.com
#use jupyter notebook
#Create a dataframe of ten rows, four columns with random values. Write a Pandas program to highlight\
#the negative numbers red and positive numbers black
'''import pandas as pd
import numpy as np
np.random.seed(24)  
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
#print(df)   
def pos_neg_colors(val):
    colors = 'red' if val<0 else 'black'
    return 'color: %s'%colors
df.style.applymap(pos_neg_colors)'''

#Create a dataframe of ten rows, four columns with random values. Convert some values to nan values.\
#Write a Pandas program which will highlight the nan values.
'''import pandas as pd
import numpy as np
import jinja2 
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[0,2] = np.nan
df.iloc[4,1] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
#print(df)   
def pos_neg_colors(val):
    colors = 'red' if val<0 else 'black'
    return "color: %s"%colors
df.style.highlight_null(null_color='red')'''

#Create a dataframe of ten rows, four columns with random values. Write a Pandas program to highlight the maximum value in each column
'''import jinja2;import pandas as pd;import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)   
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[4,1] = np.nan
df.iloc[9,4] = np.nan
#print(df)
def highlight_max(x):
    is_max = x == x.max()
    return ['background-color: green' if i else '' for i in is_max]
df.style.apply(highlight_max,subset=pd.IndexSlice[:,['B','C','D','E']])'''

#Create a dataframe of ten rows, four columns with random values. Write a Pandas program to highlight the minimum value in each column. 
'''import jinja2
import numpy as np; import pandas as pd
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[4,1] = np.nan
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
print(df)
def high_min(val):
    is_min = val == val.min()
    return ['background-color: red' if i else '' for i in is_min]
df.style.apply(high_min,subset=pd.IndexSlice[:,['B','C','D','E']])'''

#Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to highlight the maximum value in last two columns
'''import pandas as pd; import jinja2
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[4,1] = np.nan
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
#print(df)   
def high_max(val):
    is_max = val == val.max()
    return['background-color: green' if x else '' for x in is_max]
df.style.apply(high_max,subset=pd.IndexSlice[:,['D','E']])'''

#Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to set dataframe background Color black and font color yellow
'''import jinja2
import pandas as pd;import numpy as np
np.random.seed(24)#
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[4,1] = np.nan
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
#print(df)
df.style.set_properties(**{'background-color':'black','font-color':'yellow'})'''

# Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to highlight dataframe's specific columns
'''import jinja2; import pandas as pd; import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[4,1] = np.nan
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
#print(df)   
df.style.set_properties(**{'background-color':'grey'},subset=pd.IndexSlice[:,['B','C']])'''

#Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to highlight dataframe's specific columns with different colors
'''import pandas as pd; import numpy as np; import jinja2
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[4,1] = np.nan
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
#print(df)   
def back_colors(x):
    df = x.copy()
    df.loc[:,:] = 'background-color: red'
    df[['B','C','E']] = 'background-color: grey'
    return df
df.style.apply(back_colors,axis=None)'''

#Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to display the dataframe in table style
'''import jinja2; import pandas as pd; import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[4,1] = np.nan
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
#print(df)   
th_props = [('font-size','12px'),('text-align','center'),('font-weight','bold'),('color','6d6d6d'),\
        ('backgroud-color','#f7ffff'))]
td_props = [('font-size','12px')]
stl = [dict(selector='th',props=th_props),dict(selector='td',props=td_props)]
print(df.style.set_table_styles(stl))'''

#Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to highlight the entire row in Yellow where a specific column value is greater than 0.5
'''import jinja2; import pandas as pd; import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
#print(df)   
def greater_than_val(x):
    if x.C > 0.5:
        return['background-color: yellow']*5
    return ['background-color: white']*5
df.style.apply(greater_than_val,axis=1) '''

#Create a dataframe of ten rows, four columns with random values.\
# Write a Pandas program to display the dataframe in Heatmap style
'''import jinja2; import pandas as pd; import numpy as np
import seaborn as sb
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
print(df)  
c = sb.light_palette('red',as_cmap=True)
df.style.background_gradient(c,cmap='viridis') '''

#Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to make a gradient color mapping on a specified column
'''import jinja2;
import pandas as pd;
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
#print(df)  
df.style.background_gradient(subset=pd.IndexSlice[:,['C']])'''

#Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to make a gradient color on all the values of the said dataframe
'''import pandas as pd
import numpy as np
import jinja2
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
#print(df)
df.style.background_gradient(subset=pd.IndexSlice[:,['A','B','C','D','E']])'''

#Create a dataframe of ten rows, four columns with random values. Write a Pandas program to display\
# the dataframe in table style and border around the table and not around the rows
'''import pandas as pd; import jinja2
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[4,1] = np.nan
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
#print(df)
df.style.set_table_styles([{'selector':'','props':[('border','5px solid #7a7')]}])'''

#Create a dataframe of ten rows, four columns with random values. \
#Write a Pandas program to display bar charts in dataframe on specified columns
'''import pandas as pd; import jinja2
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A':np.linspace(1,10,10)})
df = pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],axis=1)
df.iloc[4,1] = np.nan
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[9,4] = np.nan
#print(df)
df.style.bar(subset=pd.IndexSlice[:,['B','C']],color='#d65f5f')'''

