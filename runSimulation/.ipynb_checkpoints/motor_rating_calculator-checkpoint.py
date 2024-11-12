#!/usr/bin/env python
# coding: utf-8

class MotorRatingCalculator:
    def __init__(self, power_calculator, avg_speed_calculator):
        self.power_calculator = power_calculator
        self.avg_speed_calculator = avg_speed_calculator

    def display_motor_rating(self):
        energy_consumed_kwh = self.power_calculator.calculate_energy_consumed()
        avg_speeds = self.avg_speed_calculator.get_section_average_speeds()

        print(f"Total energy consumed during the run: {energy_consumed_kwh:.3f} kWh")
        print("Average speeds for each section (km/h):")
        for i, speed in enumerate(avg_speeds, start=1):
            print(f"Section {i}: {speed:.2f} km/h")

