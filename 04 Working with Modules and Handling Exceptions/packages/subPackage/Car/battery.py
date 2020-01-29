#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Battery():
    """A battery for an electric car."""
    def __init__(self, size=70):
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %.
        self.size = size
        self.charge_level = 0
    
    def get_range(self):
        """Return the battery's range."""
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270


# In[ ]:




