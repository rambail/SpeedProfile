#!/usr/bin/env python
# coding: utf-8

class MotorRatingCalculator:
    def __init__(self, train_params):
        self.train_params = train_params
        self.train_mass = float(self.train_params['Train_mass'])
        self.starting_resistance = float(self.train_params['Starting_resistance'])
        self.mc_mass = float(self.train_params['Mc_mass'])
        self.tc_mass = float(self.train_params['Tc_mass'])
        self.inertia_mass_m = float(self.train_params['Inertia_mass_m'])
        self.inertia_mass_t = float(self.train_params['Inertia_mass_t'])
        self.acceleration = float(self.train_params['Acceleration'])
        self.switch_speed = float(self.train_params['Switch_speed']) * 1000 / 3600
        self.motor_nos = float(self.train_params['Motor_nos'])

    def display_motor_rating(self):
        te_start = self.train_mass * self.starting_resistance / 1000 # Starting Effort in kN
        te_rolling = (self.train_mass + 
                      self.mc_mass * self.inertia_mass_m * 2 + 
                     self.tc_mass * self.inertia_mass_t) * self.acceleration # Moving Effort
        te_total = te_start + te_rolling # Total Effort
        te_motor = te_total / self.motor_nos # Effort per Motor
        motor_rating = te_motor * self.switch_speed  # Motor Rating
        return motor_rating

   

