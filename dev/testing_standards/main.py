from testing_standards.imtp_standard import IMTP_Calculations
from testing_standards.athlete import Athlete


foot_length = 28.0
heel_ankle_length = 5
ankle_height = 9.0
shin_length = 44
thigh_length = 43
trunk_length = 59.0
arm_length = 71.0


me = Athlete(foot_length, heel_ankle_length, ankle_height, shin_length, thigh_length, trunk_length, arm_length)

imtp = IMTP_Calculations(me)

bar_height = imtp.bar_height()
angles = imtp.segment_angles()
acromion_position = imtp.acromion_position()


print(f'Výška osy: {bar_height}')
print(f'Úhel v kotníku: {angles['ankle']:.0f}')
print(f'Úhel v koleni: {angles['knee']:.0f}')
print(f'Úhel v kyčli: {angles['hip']:.0f}')
print(f'Pozice ramen: {acromion_position:.1f}')


