#!/usr/bin/env python
# coding: utf-8

class AverageSpeedCalculator:
    def __init__(self):
        self.section_avg_speed = []

    def calculate_segment_average_speed(self, segment_distance, segment_time):
        avg_speed = (segment_distance / segment_time) * 18 / 5  # Convert m/s to km/h
        self.section_avg_speed.append(avg_speed)
        return avg_speed

    def get_section_average_speeds(self):
        return self.section_avg_speed


# In[ ]:




