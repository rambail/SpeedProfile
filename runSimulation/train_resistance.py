#!/usr/bin/env python
# coding: utf-8

class TrainResistance:
    def __init__(self, train_params, speed):
        self.speed = speed
        self.train_params = train_params
        # Additional initialization...
    
    def calculate_davis_resistance(self):
        train_mass = float(self.train_params['Train_mass'])
        static_friction = float(self.train_params['Static_friction'])
        rolling_resistance = float(self.train_params['Rolling_resistance'])
        air_resistance = float(self.train_params['Air_resistance'])
        return (static_friction + rolling_resistance * self.speed + air_resistance * self.speed**2) * train_mass

