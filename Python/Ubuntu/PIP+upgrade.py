
# coding: utf-8

# # Pip Upgrade

# In[1]:

import pip
from subprocess import call


# In[ ]:

for dist in pip.get_installed_distributions():
    call("pip install --upgrade "+dist.project_name, shell=True)

