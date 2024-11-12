#!/usr/bin/env python
# coding: utf-8

import numpy as np

class PowerConsumptionCalculator:
    def __init__(self, mass, regen_efficiency):
        self.mass = mass
        self.regen_efficiency = regen_efficiency
        self.power_log = []

    def log_power_during_acceleration(self, speed, acceleration):
        force = self.mass * 1000 * acceleration  # Force in Newtons
        power = force * speed  # Power in Watts
        self.power_log.append(power)

    def log_power_during_braking(self, speed, braking_deceleration):
        force = self.mass * 1000 * braking_deceleration  # Force in Newtons
        power = force * speed  # Power in Watts
        self.power_log.append(-power * self.regen_efficiency)  # Regenerated power

    def calculate_energy_consumed(self):
        energy_consumed_joules = np.trapezoid(self.power_log, dx=1)  # Integration over time
        energy_consumed_kwh = energy_consumed_joules / 3_600_000  # Convert to kWh
        return energy_consumed_kwh

