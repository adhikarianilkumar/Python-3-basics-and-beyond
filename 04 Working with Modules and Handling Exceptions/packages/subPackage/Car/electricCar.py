#!/usr/bin/env python
# coding: utf-8

# In[1]:


from .baseCarClass import Car
from .battery import Battery

class ElectricCar(Car, Battery):
    """A simple model of an electric car."""
    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)
        # Attributes specific to electric cars.
        # Battery capacity in kWh.
        self.battery_size = 70
        # Charge level in %.
        self.charge_level = 0
        # Attribute specific to electric cars.
        self.battery = Battery()
        
    def charge(self):
        """Fully charge the vehicle."""
        self.charge_level = 100
        print("The vehicle is fully charged.")
    
    def charge(self):
        """Fully charge the vehicle."""
        self.battery.charge_level = 100
        print("The vehicle is fully charged.")


# In[ ]:




