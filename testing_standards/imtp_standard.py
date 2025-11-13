from .athlete import Athlete
import math

class IMTP_Calculations:

    def __init__(self, athlete, target_knee_angle_deg=135, quadriceps_offset=7):
        
        self.athlete = athlete
        self.target_knee_angle = target_knee_angle_deg
        self.quadriceps_offset = quadriceps_offset
        self.alfa_angle_rad = math.radians(target_knee_angle_deg)

        self.ankle_offset = (athlete.foot_length/2) - athlete.heel_ankle_length
        
        self.beta_angle_rad = math.atan((2*self.quadriceps_offset)/athlete.thigh_length)
        self.l1 = math.sqrt((athlete.thigh_length/2)**2 + self.quadriceps_offset**2)
        self.omega_angle_rad = self.alfa_angle_rad + self.beta_angle_rad
        self.l2 = math.sqrt(self.l1**2 + athlete.shin_length**2 - (2 * self.l1 * athlete.shin_length * math.cos(self.omega_angle_rad)))
        self.h = math.sqrt(self.l2**2 - self.ankle_offset**2)

        self.gamma_angle_rad = math.acos((self.l1**2 + athlete.trunk_length**2 - athlete.arm_length**2) / (2 * self.l1 * athlete.trunk_length))
        self.delta_angle_rad = self.gamma_angle_rad + self.beta_angle_rad

        self.theta_angle_rad = math.asin(self.h / self.l2)
        self.lambda_angle_rad = math.acos((self.athlete.shin_length**2 + self.l2**2 - self.l1**2) / (2 * self.athlete.shin_length * self.l2))  
        self.epsilon_angle_rad = self.theta_angle_rad - self.lambda_angle_rad


    def bar_height(self):

        bar_height = self.h + self.athlete.ankle_height

        return bar_height
    

    def ankle_angle_OG(self):
        A = self.l1
        S = self.athlete.shin_length
        O2 = self.ankle_offset
        H = self.h

        K1 = A**2 + S**2 + O2**2 - 2*A*S * math.cos(self.omega_angle_rad) - H**2
        K2 = 2 * H
        K3 = 2*S - 2*A * math.cos(self.omega_angle_rad)

        a = K3**2 - K2**2
        b = -2 * K1 * K2
        c = (K3**2 * O2**2) - K1**2

        D = b**2 - 4*a*c

        H1_a = (-b + math.sqrt(D)) / (2*a)
        H1_b = (-b - math.sqrt(D)) / (2*a)
        
        if 0 < H1_a < H:
            H1 = H1_a
        elif 0 < H1_b < H:
            H1 = H1_b
             
        epsilon_rad = math.atan(H1 / O2)
        epsilon_deg = math.degrees(epsilon_rad)
        ankle_angle = epsilon_deg

        return ankle_angle
    

    def segment_angles(self):

        ankle_angle = math.degrees(self.epsilon_angle_rad)
        knee_angle = math.degrees(self.alfa_angle_rad)
        hip_angle = math.degrees(self.delta_angle_rad)

        angles = {
            'ankle': ankle_angle,
            'knee': knee_angle,
            'hip': hip_angle
        }

        return angles
    

    def segment_inclination(self):
        
        shin_incline = self.epsilon_angle_rad
        thigh_incline = shin_incline + (math.radians(180) - self.alfa_angle_rad)
        trunk_incline = thigh_incline - (math.radians(180) - self.delta_angle_rad)

        return shin_incline, thigh_incline, trunk_incline


    def acromion_position(self):

        shin_incline, thigh_incline, trunk_incline = self.segment_inclination()
        
        final_positon = - self.ankle_offset

        knee_projection = math.cos(shin_incline) * self.athlete.shin_length
        final_positon += knee_projection

        hip_projection = math.cos(thigh_incline) * self.athlete.thigh_length
        final_positon += hip_projection

        shoulder_projection = math.cos(trunk_incline) * self.athlete.trunk_length
        final_positon += shoulder_projection

        return final_positon

