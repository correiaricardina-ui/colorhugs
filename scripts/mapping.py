# Region -> area, per avatar. Areas:
# LH Learning Hub · BG Brain Gym · IW My Inner World · KD Kids Draw
# CC Color & Create · MC My ColorHugs · CM Community
MAP = {
 "gato":      {"LH":[1,3],"BG":[10,11,12,13],"IW":[4],"KD":[8,9],"CC":[2],"MC":[5],"CM":[6,7]},
 "coelho":    {"LH":[1,3,14,15],"BG":[5,6,12,13],"IW":[4],"KD":[9,11],"CC":[2],"MC":[10],"CM":[7,8]},
 "urso":      {"LH":[1,13],"BG":[8,9,11,12],"IW":[3],"KD":[6,7],"CC":[2],"MC":[10],"CM":[4,5]},
 "raposa":    {"LH":[1,2,15],"BG":[11,12,13,14],"IW":[5],"KD":[8,9],"CC":[3],"MC":[4,10],"CM":[6,7]},
 "dino":      {"LH":[1],"BG":[9,10,11,12,13,14,15],"IW":[3],"KD":[5,6],"CC":[2],"MC":[4,16],"CM":[7,8]},
 "robot":     {"LH":[1,3],"BG":[22,23,25,28],"IW":[4],"KD":[9,10,11,12,14,15,21,24,26],
               "CC":[2],"MC":[13,20,27],"CM":[5,6,7,8,16,17,18,19]},
 "borboleta": {"LH":[1],"BG":[18,19,24,25],"IW":[7],"KD":[2,3,8,9,14,15,20,21],
               "CC":[4,5,10,11,16,17,22,23],"MC":[6],"CM":[12,13]},
 "carro":     {"LH":[2],"BG":[7,8],"IW":[4,9,10,11],"KD":[12,13,14,15],"CC":[1],
               "MC":[3,5],"CM":[6,16,17,18,19]},
 "casa":      {"LH":[4,7],"BG":[9,11],"IW":[12,26,27,29,30,31],
               "KD":[13,14,15,16,17,18,19,20,21,22,23,24],"CC":[1,3],"MC":[2],
               "CM":[5,6,8,10,25,28]},
 "foguetao":  {"LH":[10],"BG":[4],"IW":[9,12],"KD":[5,6],"CC":[1,2],"MC":[7,8,11],"CM":[3]},
# Penguin and kite were withdrawn: the penguin's wings share one sealed region
# with its head and back, and the kite has no back feature, so neither could
# expose seven meaningful groups. See D-079.
}

AREA_COLOUR = {
 "LH":(126,177,235),  # Learning Hub
 "BG":(244,166,201),  # Brain Gym
 "IW":(186,166,230),  # My Inner World
 "KD":(247,176,124),  # Kids Draw for Kids
 "CC":(140,206,163),  # Color & Create
 "MC":(245,206,124),  # My ColorHugs
 "CM":(240,152,163),  # Community
}
AREA_ORDER = ["LH","BG","IW","KD","CC","MC","CM"]
