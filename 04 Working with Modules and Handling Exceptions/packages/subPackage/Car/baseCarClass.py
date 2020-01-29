#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Represent gas and electric cars."""
class Car():
    """A simple attempt to model a car."""
    
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0
        
    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")
        
    def drive(self):
        """Simulate driving."""
        print("The car is moving.")
        
    def update_fuel_level(self, new_level):
        """Update the fuel level."""
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")
            
    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel.")
        else:
            print("The tank won't hold that much.")


# In[ ]:




