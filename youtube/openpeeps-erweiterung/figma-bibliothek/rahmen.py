# Rahmen (x, y, w, h) der Figma-Symbole auf der Seite "Symbols" (aus get_metadata, 30.09.2026)
R = {}
def reihe(prefix, w, h, eintraege):
    for name, x, y in eintraege: R[prefix + name] = (x, y, w, h)
reihe("a person/", 0, 0, [])
R["a person/bust"] = (5438, 0, 1136, 1533); R["a person/sitting"] = (5438, 1653, 1647, 2500); R["a person/standing"] = (5438, 4273, 1179, 3291)
reihe("accessories/", 392, 138, [("Eyepatch",13890,5021),("Glasses",13890,5279),("Glasses 2",13890,5537),("Glasses 3",13890,5795),("Glasses 4",13890,6053),
    ("Glasses 5",14402,5021),("Glasses 5_2",14402,5279),("Sunglasses",14402,5537),("Sunglasses 2",14402,5795)])
reihe("body/", 818, 733, [("Blazer Black Tee",7625,0),("Button Shirt 1",7625,853),("Button Shirt 2",7625,1706),("Coffee",7625,2559),("Device",7625,3412),
    ("Dress",8563,0),("Explaining",8563,853),("Gaming",8563,1706),("Gym Shirt",8563,2559),("Hoodie",8563,3412),
    ("jacket",9501,0),("jacket-polka-dots",9501,853),("Killer",9501,1706),("Macbook",9501,2559),("Paper",9501,3412),
    ("Pointing Up",10439,0),("Polo and Sweater",10439,853),("Shirt and Coat",10439,1706),("Sporty Tee",10439,2559),("Striped Pocket Tee",10439,3412),
    ("Striped Tee",11377,0),("Sweater",11377,853),("Sweater Dots",11377,1706),("Tee 1",11377,2559),("Tee 2",11377,3412),
    ("Tee Arms Crossed",12315,0),("Tee Selena",12315,853),("Thunder T-Shirt",12315,1706),("Turtleneck",12315,2559),("Whatever",12315,3412)])
reihe("face/", 289, 293, [("Angry with Fang",13933,0),("Awe",13933,413),("Blank",13933,826),("Calm",13933,1239),("Cheeky",13933,1652),
    ("Concerned",14342,0),("Concerned Fear",14342,413),("Contempt",14342,826),("Cute",14342,1239),("Cyclops",14342,1652),
    ("Driven",14751,0),("Eating Happy",14751,413),("Explaining",14751,826),("Eyes Closed",14751,1239),("Fear",14751,1652),
    ("Hectic",15160,0),("Loving Grin 1",15160,413),("Loving Grin 2",15160,826),("Monster",15160,1239),("Old",15160,1652),
    ("Rage",15569,0),("Serious",15569,413),("Smile",15569,826),("Smile Big",15569,1239),("Smile LOL",15569,1652),
    ("Smile Teeth Gap",15978,0),("Solemn",15978,413),("Suspicious",15978,826),("Tired",15978,1239),("Very Angry",15978,1652),
    ("With_Mask/Cheers",13928,2061),("With_Mask/Calm",14342,2052),("With_Mask/Smile",14750,2061)])
reihe("facial-hair/", 280, 230, [("Chin",13932,2760),("Full",13932,3110),("Full 2",13932,3460),("Full 3",13932,3810),("Full 4",13932,4160),
    ("Goatee 1",14332,2760),("Goatee 2",14332,3110),("Moustache 1",14332,3460),("Moustache 2",14332,3810),("Moustache 3",14332,4160),
    ("Moustache 4",14732,2760),("Moustache 5",14732,3110),("Moustache 6",14732,3460),("Moustache 7",14732,3810),("Moustache 8",14732,4160),("Moustache 9",15132,2760)])
reihe("head/", 474, 567, [("Afro",16933,0),("Bangs",16933,687),("Bangs 2",16933,1374),("Bantu Knots",16933,2061),("Bear",16933,2748),
    ("Bun",17526,0),("Bun_2",17526,687),("Bun 2",17526,1374),("Buns",17526,2061),("Cornrows",17526,2748),
    ("Cornrows 2",18119,0),("Dreads 1",18119,687),("Dreads 2",18119,1374),("Flat Top",18119,2061),("Flat Top Long",18119,2748),
    ("Gray Bun",18713,0),("Gray Medium",18713,687),("Gray Short",18713,1374),("hat-beanie",18713,2061),("hat-hip",18713,2748),
    ("Hijab",19306,0),("Long",19306,687),("Long Afro",19306,1374),("Long Bangs",19306,2061),("Long Curly",19306,2748),
    ("Medium 1",19899,0),("Medium 2",19899,687),("Medium 3",19899,1374),("Medium Bangs",19899,2061),("Medium Bangs 2",19899,2748),
    ("Medium Bangs 3",20492,0),("Medium Straight",20492,687),("Mohawk",20492,1374),("Mohawk 2",20492,2061),("No Hair 1",20492,2748),
    ("No Hair 2",21085,0),("No Hair 3",21085,687),("Pomp",21085,1374),("Shaved 1",21085,2061),("Shaved 2",21085,2748),
    ("Shaved 3",21678,0),("Short 1",21678,687),("doctor-nurse-2",38162,3052),("doctor-nurse-2_2",38771,3052),("doctor-nurse-3",37528,3052),
    ("Short 2",21678,1374),("Short 3",21678,2061),("Short 4",21678,2748),("Short 4_2",22271,0),("Short 5",22271,687),
    ("Turban",22271,1374),("Twists",22271,2061),("Twists 2",22271,2748)])
reihe("pose/sitting/", 1534, 1856, [("bike",24089,0),("closed_legs-1",23322,5132),("closed_legs-2",23322,7108),("crossed_legs",23322,9084),
    ("hands_back-1",23322,11060),("hands_back-2",24976,3156),("mid-1",24976,5132),("mid-2",24976,7108),("one_leg_up-1",24976,9084),
    ("one_leg_up-2",24976,11060),("wheelchair",23322,3156)])
reihe("pose/standing/", 1645, 2500, [("blazer-1",27598,0),("blazer-2",27598,2620),("blazer-3",27598,5240),("blazer-4",27598,7860),
    ("crossed_arms-1",29363,0),("crossed_arms-2",29363,2620),("easing-1",29363,5240),("easing-2",29363,7860),("pointing_finger-1",29363,10480),
    ("pointing_finger-2",31128,0),("polka_dots",31128,2620),("resting-1",31128,5240),("resting-2",31128,7860),("robot_dance-1",31128,10480),
    ("robot_dance-2",32893,0),("robot_dance-3",32893,2620),("shirt-1",32893,5240),("shirt-2",32893,7860),("shirt-3",32893,10480),
    ("doctor-nurse-03",36880,-61),("doctor-nurse-02",40410,-61),("doctor-nurse-01",38645,-61),("shirt-4",34658,0),
    ("walking-1",34658,2620),("walking-2",34658,5240),("walking-3",34658,7860)])
reihe("mask/", 397, 228, [("medical mask",36880,3030),("respirator",36880,3336)])
