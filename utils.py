from datetime import datetime, timedelta

# sublords_combination = [
#     [
#         {"sublord": "Ketu", "start": "00.00.00", "end": "00.46.40"},
#         {"sublord": "Shukra", "start": "46.40.40", "end": "03.00.00"},
#         {"sublord": "Ravi", "start": "03.00.00", "end": "03.40.00"},
#         {"sublord": "Chandra", "start": "03.40.00", "end": "04.46.40"},
#         {"sublord": "Mangal", "start": "04.46.40", "end": "05.33.20"},
#         {"sublord": "Rahu", "start": "07.33.20", "end": "09.20.00"},
#         {"sublord": "Guru", "start": "07.33.20", "end": "09.20.00"},
#         {"sublord": "Shani", "start": "09.20.00", "end": "11.26.40"},
#         {"sublord": "Buddha", "start": "11.26.40", "end": "13.20.00"},
#     ],
#     [
#         {"sublord": "Shukra", "start": "13.20.00", "end": "15.33.20"},
#         {"sublord": "Ravi", "start": "15.33.20", "end": "16.13.20"},
#         {"sublord": "Chandra", "start": "16.13.20", "end": "17.20.00"},
#         {"sublord": "Mangal", "start": "17.20.00", "end": "18.06.40"},
#         {"sublord": "Rahu", "start": "18.06.40", "end": "20.06.40"},
#         {"sublord": "Guru", "start": "20.06.40", "end": "21.53.20"},
#         {"sublord": "Shani", "start": "21.53.20", "end": "24.00.00"},
#         {"sublord": "Buddha", "start": "24.00.00", "end": "25.53.20"},
#         {"sublord": "Ketu", "start": "25.53.20", "end": "26.40.00"},
#     ],
#     [
#         {"sublord": "Ravi", "start": "26.40.00", "end": "27.20.00"},
#         {"sublord": "Chandra", "start": "27.20.00", "end": "28.26.40"},
#         {"sublord": "Mangal", "start": "28.26.40", "end": "29.13.20"},
#         {"sublord": "Rahu", "start": "19.13.20", "end": "30.00.00"},
#     ],
#     [
#         {"sublord": "Buddha", "start": "00.00.00", "end": "01.53.20"},
#         {"sublord": "Ketu", "start": "01.53.20", "end": "02.40.00"},
#         {"sublord": "Shukra", "start": "02.40.00", "end": "04.53.20"},
#         {"sublord": "Ravi", "start": "04.53.20", "end": "05.33.20"},
#         {"sublord": "Chandra", "start": "05.33.20", "end": "06.40.00"},
#     ],
#     [
#         {"sublord": "Rahu", "start": "06.40.00", "end": "08.40.00"},
#         {"sublord": "Guru", "start": "08.40.00", "end": "10.26.40"},
#         {"sublord": "Shani", "start": "10.26.40", "end": "12.33.20"},
#         {"sublord": "Buddha", "start": "12.33.20", "end": "14.26.40"},
#         {"sublord": "Ketu", "start": "14.26.40", "end": "15.13.20"},
#         {"sublord": "Shukra", "start": "15.13.20", "end": "17.26.40"},
#         {"sublord": "Ravi", "start": "17.26.40", "end": "18.06.40"},
#         {"sublord": "Chandra", "start": "18.06.40", "end": "19.13.20"},
#         {"sublord": "Mangal", "start": "19.13.20", "end": "20.00.00"},
#     ],
#     [
#         {"sublord": "Guru", "start": "20.00.00", "end": "21.46.40"},
#         {"sublord": "Shani", "start": "21.46.40", "end": "23.53.20"},
#         {"sublord": "Buddha", "start": "23.53.20", "end": "25.46.40"},
#         {"sublord": "Ketu", "start": "25.46.40", "end": "26.33.20"},
#         {"sublord": "Shukra", "start": "26.33.20", "end": "28.46.40"},
#         {"sublord": "Ravi", "start": "28.46.40", "end": "29.26.40"},
#         {"sublord": "Chandra", "start": "29.26.40", "end": "30.00.00"},
#     ],
#     [
#         {"sublord": "Rahu", "start": "00.00.00", "end": "01.13.20"},
#         {"sublord": "Guru", "start": "01.13.20", "end": "03.00.00"},
#         {"sublord": "Shani", "start": "03.00.00", "end": "05.06.00"},
#         {"sublord": "Buddha", "start": "05.06.00", "end": "07.00.00"},
#         {"sublord": "Ketu", "start": "07.00.00", "end": "07.46.00"},
#         {"sublord": "Shukra", "start": "07.46.00", "end": "10.00.00"},
#     ],
#     [
#         {"sublord": "Chandra", "start": "10.00.00", "end": "11.06.40"},
#         {"sublord": "Mangal", "start": "11.06.40", "end": "11.53.20"},
#         {"sublord": "Rahu", "start": "11.53.20", "end": "13.53.20"},
#         {"sublord": "Guru", "start": "13.53.20", "end": "15.40.00"},
#         {"sublord": "Shani", "start": "15.40.00", "end": "17.46.40"},
#         {"sublord": "Buddha", "start": "17.46.40", "end": "19.40.00"},
#         {"sublord": "Ketu", "start": "19.40.00", "end": "20.26.40"},
#         {"sublord": "Shukra", "start": "20.26.40", "end": "22.40.00"},
#         {"sublord": "Ravi", "start": "22.40.00", "end": "23.20.00"},
#     ],
#     [
#         {"sublord": "Mangal", "start": "23.20.00", "end": "24.06.40"},
#         {"sublord": "Rahu", "start": "24.06.40", "end": "26.06.40"},
#         {"sublord": "Guru", "start": "26.06.40", "end": "27.53.20"},
#         {"sublord": "Shani", "start": "27.53.20", "end": "30.00.00"},
#     ],
#     [
#         {"sublord": "Chandra", "start": "00.00.00", "end": "00.33.00"},
#         {"sublord": "Mangal", "start": "00.33.00", "end": "01.20.00"},
#         {"sublord": "Rahu", "start": "01.20.00", "end": "03.20.00"},
#     ],
#     [
#         {"sublord": "Shani", "start": "03.20.00", "end": "05.26.40"},
#         {"sublord": "Buddha", "start": "05.26.40", "end": "07.20.00"},
#         {"sublord": "Ketu", "start": "07.20.00", "end": "08.06.40"},
#         {"sublord": "Shukra", "start": "08.06.40", "end": "10.20.00"},
#         {"sublord": "Ravi", "start": "10.20.00", "end": "11.00.00"},
#         {"sublord": "Chandra", "start": "11.00.00", "end": "12.06.40"},
#         {"sublord": "Mangal", "start": "12.06.40", "end": "12.53.20"},
#         {"sublord": "Rahu", "start": "12.53.20", "end": "14.53.20"},
#         {"sublord": "Guru", "start": "14.53.20", "end": "16.40.00"},
#     ],
#     [
#         {"sublord": "Buddha", "start": "16.40.00", "end": "18.33.20"},
#         {"sublord": "Ketu", "start": "18.33.20", "end": "19.20.00"},
#         {"sublord": "Shukra", "start": "19.20.00", "end": "21.33.20"},
#         {"sublord": "Ravi", "start": "21.33.20", "end": "22.13.20"},
#         {"sublord": "Chandra", "start": "22.13.20", "end": "23.20.00"},
#         {"sublord": "Mangal", "start": "23.20.00", "end": "24.06.40"},
#         {"sublord": "Rahu", "start": "24.06.40", "end": "26.06.40"},
#         {"sublord": "Guru", "start": "26.06.40", "end": "27.53.20"},
#         {"sublord": "Shani", "start": "27.53.20", "end": "30.00.00"},
#     ],
# ]

sublords_combination = [
    [
        {"sublord": "Ketu", "start": "00.00.00", "end": "00.46.40", "duration": 1.22},
        {"sublord": "Shukra", "start": "46.40.40", "end": "03.00.00", "duration": 3.38},
        {"sublord": "Ravi", "start": "03.00.00", "end": "03.40.00", "duration": 1.11},
        {
            "sublord": "Chandra",
            "start": "03.40.00",
            "end": "04.46.40",
            "duration": 1.45,
        },
        {"sublord": "Mangal", "start": "04.46.40", "end": "05.33.20", "duration": 1.17},
        {"sublord": "Rahu", "start": "07.33.20", "end": "09.20.00", "duration": 3.13},
        {"sublord": "Guru", "start": "07.33.20", "end": "09.20.00", "duration": 2.33},
        {"sublord": "Shani", "start": "09.20.00", "end": "11.26.40", "duration": 3.24},
        {"sublord": "Buddha", "start": "11.26.40", "end": "13.20.00", "duration": 2.35},
    ],
    [
        {"sublord": "Shukra", "start": "13.20.00", "end": "15.33.20", "duration": 3.22},
        {"sublord": "Ravi", "start": "15.33.20", "end": "16.13.20", "duration": 1.06},
        {"sublord": "Chandra", "start": "16.13.20", "end": "17.20.00", "duration": 1.5},
        {"sublord": "Mangal", "start": "17.20.00", "end": "18.06.40", "duration": 1.19},
        {"sublord": "Rahu", "start": "18.06.40", "end": "20.06.40", "duration": 3.27},
        {"sublord": "Guru", "start": "20.06.40", "end": "21.53.20", "duration": 3.05},
        {"sublord": "Shani", "start": "21.53.20", "end": "24.00.00", "duration": 3.38},
        {"sublord": "Buddha", "start": "24.00.00", "end": "25.53.20", "duration": 3.17},
        {"sublord": "Ketu", "start": "25.53.20", "end": "26.40.00", "duration": 1.22},
    ],
    [
        {"sublord": "Ravi", "start": "26.40.00", "end": "27.20.00", "duration": 1.09},
        {
            "sublord": "Chandra",
            "start": "27.20.00",
            "end": "28.26.40",
            "duration": 2.02,
        },
        {"sublord": "Mangal", "start": "28.26.40", "end": "29.13.20", "duration": 1.22},
        {"sublord": "Rahu", "start": "19.13.20", "end": "30.00.00", "duration": 1.21},
    ],
    [
        {"sublord": "Buddha", "start": "00.00.00", "end": "01.53.20", "duration": 3.13},
        {"sublord": "Ketu", "start": "01.53.20", "end": "02.40.00", "duration": 1.24},
        {"sublord": "Shukra", "start": "02.40.00", "end": "04.53.20", "duration": 3.37},
        {"sublord": "Ravi", "start": "04.53.20", "end": "05.33.20", "duration": 1.45},
        {
            "sublord": "Chandra",
            "start": "05.33.20",
            "end": "06.40.00",
            "duration": 2.01,
        },
    ],
    [
        {"sublord": "Rahu", "start": "06.40.00", "end": "08.40.00", "duration": 3.27},
        {"sublord": "Guru", "start": "08.40.00", "end": "10.26.40", "duration": 3.12},
        {"sublord": "Shani", "start": "10.26.40", "end": "12.33.20", "duration": 3.39},
        {"sublord": "Buddha", "start": "12.33.20", "end": "14.26.40", "duration": 3.26},
        {"sublord": "Ketu", "start": "14.26.40", "end": "15.13.20", "duration": 1.15},
        {"sublord": "Shukra", "start": "15.13.20", "end": "17.26.40", "duration": 4.03},
        {"sublord": "Ravi", "start": "17.26.40", "end": "18.06.40", "duration": 1.12},
        {
            "sublord": "Chandra",
            "start": "18.06.40",
            "end": "19.13.20",
            "duration": 2.04,
        },
        {"sublord": "Mangal", "start": "19.13.20", "end": "20.00.00", "duration": 1.25},
    ],
    [
        {"sublord": "Guru", "start": "20.00.00", "end": "21.46.40", "duration": 3.15},
        {"sublord": "Shani", "start": "21.46.40", "end": "23.53.20", "duration": 3.53},
        {"sublord": "Buddha", "start": "23.53.20", "end": "25.46.40", "duration": 3.29},
        {"sublord": "Ketu", "start": "25.46.40", "end": "26.33.20", "duration": 1.27},
        {"sublord": "Shukra", "start": "26.33.20", "end": "28.46.40", "duration": 4.06},
        {"sublord": "Ravi", "start": "28.46.40", "end": "29.26.40", "duration": 1.14},
        {
            "sublord": "Chandra",
            "start": "29.26.40",
            "end": "30.00.00",
            "duration": 1.03,
        },
    ],
    [
        {"sublord": "Rahu", "start": "00.00.00", "end": "01.13.20", "duration": 2.07},
        {"sublord": "Guru", "start": "01.13.20", "end": "03.00.00", "duration": 3.05},
        {"sublord": "Shani", "start": "03.00.00", "end": "05.06.00", "duration": 3.31},
        {"sublord": "Buddha", "start": "05.06.00", "end": "07.00.00", "duration": 3.18},
        {"sublord": "Ketu", "start": "07.00.00", "end": "07.46.00", "duration": 1.22},
        {"sublord": "Shukra", "start": "07.46.00", "end": "10.00.00", "duration": 3.54},
    ],
    [
        {
            "sublord": "Chandra",
            "start": "10.00.00",
            "end": "11.06.40",
            "duration": 1.54,
        },
        {"sublord": "Mangal", "start": "11.06.40", "end": "11.53.20", "duration": 1.22},
        {"sublord": "Rahu", "start": "11.53.20", "end": "13.53.20", "duration": 3.31},
        {"sublord": "Guru", "start": "13.53.20", "end": "15.40.00", "duration": 3.08},
        {"sublord": "Shani", "start": "15.40.00", "end": "17.46.40", "duration": 3.42},
        {"sublord": "Buddha", "start": "17.46.40", "end": "19.40.00", "duration": 3.21},
        {"sublord": "Ketu", "start": "19.40.00", "end": "20.26.40", "duration": 1.22},
        {"sublord": "Shukra", "start": "20.26.40", "end": "22.40.00", "duration": 4.01},
        {"sublord": "Ravi", "start": "22.40.00", "end": "23.20.00", "duration": 1.07},
    ],
    [
        {"sublord": "Mangal", "start": "23.20.00", "end": "24.06.40", "duration": 1.22},
        {"sublord": "Rahu", "start": "24.06.40", "end": "26.06.40", "duration": 3.33},
        {"sublord": "Guru", "start": "26.06.40", "end": "27.53.20", "duration": 3.51},
        {"sublord": "Shani", "start": "27.53.20", "end": "30.00.00", "duration": 3.46},
    ],
    [
        {
            "sublord": "Chandra",
            "start": "00.00.00",
            "end": "00.33.00",
            "duration": 1.02,
        },
        {"sublord": "Mangal", "start": "00.33.00", "end": "01.20.00", "duration": 1.28},
        {"sublord": "Rahu", "start": "01.20.00", "end": "03.20.00", "duration": 3.43},
    ],
    [
        {"sublord": "Shani", "start": "03.20.00", "end": "05.26.40", "duration": 3.59},
        {"sublord": "Buddha", "start": "05.26.40", "end": "07.20.00", "duration": 3.34},
        {"sublord": "Ketu", "start": "07.20.00", "end": "08.06.40", "duration": 1.26},
        {"sublord": "Shukra", "start": "08.06.40", "end": "10.20.00", "duration": 4.14},
        {"sublord": "Ravi", "start": "10.20.00", "end": "11.00.00", "duration": 1.16},
        {
            "sublord": "Chandra",
            "start": "11.00.00",
            "end": "12.06.40",
            "duration": 2.05,
        },
        {"sublord": "Mangal", "start": "12.06.40", "end": "12.53.20", "duration": 1.3},
        {"sublord": "Rahu", "start": "12.53.20", "end": "14.53.20", "duration": 3.49},
        {"sublord": "Guru", "start": "14.53.20", "end": "16.40.00", "duration": 3.25},
    ],
    [
        {"sublord": "Buddha", "start": "16.40.00", "end": "18.33.20", "duration": 3.25},
        {"sublord": "Ketu", "start": "18.33.20", "end": "19.20.00", "duration": 1.21},
        {"sublord": "Shukra", "start": "19.20.00", "end": "21.33.20", "duration": 4.16},
        {"sublord": "Ravi", "start": "21.33.20", "end": "22.13.20", "duration": 1.13},
        {
            "sublord": "Chandra",
            "start": "22.13.20",
            "end": "23.20.00",
            "duration": 2.09,
        },
        {"sublord": "Mangal", "start": "23.20.00", "end": "24.06.40", "duration": 1.13},
        {"sublord": "Rahu", "start": "24.06.40", "end": "26.06.40", "duration": 3.32},
        {"sublord": "Guru", "start": "26.06.40", "end": "27.53.20", "duration": 3.34},
        {"sublord": "Shani", "start": "27.53.20", "end": "30.00.00", "duration": 4.08},
    ],
]

# Corrected list of Rashis
rashis = [
    "Mesha",
    "Vrishabha",
    "Mithuna",
    "Karka",
    "Simha",
    "Kanya",
    "Tula",
    "Vrishchika",
    "Dhanu",
    "Makara",
    "Kumbha",
    "Meena",
]

# Corrected list of Nakshatras
nakshatras = [
    "Ashwini",
    "Bharani",
    "Krittika",
    "Rohini",
    "Mrigashira",
    "Ardra",
    "Punarvasu",
    "Pushya",
    "Ashlesha",
    "Magha",
    "Purva Phalguni",
    "Uttara Phalguni",
    "Hasta",
    "Chitra",
    "Swati",
    "Vishakha",
    "Anuradha",
    "Jyeshtha",
    "Mula",
    "Purva Ashadha",
    "Uttara Ashadha",
    "Shravana",
    "Dhanishta",
    "Shatabhisha",
    "Purva Bhadrapada",
    "Uttara Bhadrapada",
    "Revati",
]

final_combinations = [
    {"Rashi": "Mesha", "Nakshatra": "Ashwini", "Sublord": sublords_combination[0]},
    {"Rashi": "Mesha", "Nakshatra": "Bharani", "Sublord": sublords_combination[1]},
    {"Rashi": "Mesha", "Nakshatra": "Krittika", "Sublord": sublords_combination[2]},
    {"Rashi": "Simha", "Nakshatra": "Magha", "Sublord": sublords_combination[0]},
    {
        "Rashi": "Simha",
        "Nakshatra": "Purva Phalguni",
        "Sublord": sublords_combination[1],
    },
    {
        "Rashi": "Simha",
        "Nakshatra": "Uttara Phalguni",
        "Sublord": sublords_combination[2],
    },
    {"Rashi": "Dhanu", "Nakshatra": "Mula", "Sublord": sublords_combination[0]},
    {
        "Rashi": "Dhanu",
        "Nakshatra": "Purva Ashadha",
        "Sublord": sublords_combination[1],
    },
    {
        "Rashi": "Dhanu",
        "Nakshatra": "Uttara Ashadha",
        "Sublord": sublords_combination[2],
    },
    {"Rashi": "Mithuna", "Nakshatra": "Mrigashira", "Sublord": sublords_combination[3]},
    {"Rashi": "Mithuna", "Nakshatra": "Ardra", "Sublord": sublords_combination[4]},
    {"Rashi": "Mithuna", "Nakshatra": "Punarvasu", "Sublord": sublords_combination[5]},
    {"Rashi": "Tula", "Nakshatra": "Chitra", "Sublord": sublords_combination[3]},
    {"Rashi": "Tula", "Nakshatra": "Swati", "Sublord": sublords_combination[4]},
    {"Rashi": "Tula", "Nakshatra": "Vishakha", "Sublord": sublords_combination[5]},
    {"Rashi": "Kumbha", "Nakshatra": "Dhanishta", "Sublord": sublords_combination[3]},
    {"Rashi": "Kumbha", "Nakshatra": "Shatabhisha", "Sublord": sublords_combination[4]},
    {
        "Rashi": "Kumbha",
        "Nakshatra": "Purva Bhadrapada",
        "Sublord": sublords_combination[5],
    },
    {"Rashi": "Vrishabha", "Nakshatra": "Krithika", "Sublord": sublords_combination[6]},
    {"Rashi": "Vrishabha", "Nakshatra": "Rohini", "Sublord": sublords_combination[7]},
    {
        "Rashi": "Vrishabha",
        "Nakshatra": "Mrigashira",
        "Sublord": sublords_combination[8],
    },
    {
        "Rashi": "Kanaya",
        "Nakshatra": "Uttara Phalguni",
        "Sublord": sublords_combination[6],
    },
    {"Rashi": "Kanaya", "Nakshatra": "Hasta", "Sublord": sublords_combination[7]},
    {"Rashi": "Kanaya", "Nakshatra": "Chitra", "Sublord": sublords_combination[8]},
    {
        "Rashi": "Makara",
        "Nakshatra": "Uttara Ashadha",
        "Sublord": sublords_combination[6],
    },
    {"Rashi": "Makara", "Nakshatra": "Shravana", "Sublord": sublords_combination[7]},
    {"Rashi": "Makara", "Nakshatra": "Dhanishta", "Sublord": sublords_combination[8]},
    {"Rashi": "Karka", "Nakshatra": "Punarvasu", "Sublord": sublords_combination[9]},
    {"Rashi": "Karka", "Nakshatra": "Pushya", "Sublord": sublords_combination[10]},
    {"Rashi": "Karka", "Nakshatra": "Ashlesha", "Sublord": sublords_combination[11]},
    {
        "Rashi": "Vrishchika",
        "Nakshatra": "Vishakha",
        "Sublord": sublords_combination[9],
    },
    {
        "Rashi": "Vrishchika",
        "Nakshatra": "Anuradha",
        "Sublord": sublords_combination[10],
    },
    {
        "Rashi": "Vrishchika",
        "Nakshatra": "Jyeshtha",
        "Sublord": sublords_combination[11],
    },
    {
        "Rashi": "Meena",
        "Nakshatra": "Purva Bhadrapada",
        "Sublord": sublords_combination[9],
    },
    {
        "Rashi": "Meena",
        "Nakshatra": "Uttara Bhadrapada",
        "Sublord": sublords_combination[10],
    },
    {"Rashi": "Meena", "Nakshatra": "Revati", "Sublord": sublords_combination[11]},
]

get_sublord = lambda rashi, nakshatra: [
    i["Sublord"]
    for i in final_combinations
    if i["Rashi"] == rashi and i["Nakshatra"] == nakshatra
][0]

import json, requests


def get_nakshatra_timings(datetime):
    api_key = "N5SkRG5RNS4r8evnyqRqq7YRB3OUt49Y5IkO9Si9"
    year = datetime.year
    month = datetime.month
    day = datetime.day
    hour = datetime.hour
    minute = datetime.minute
    second = datetime.second

    url = "https://json.freeastrologyapi.com/nakshatra-durations"

    payload = json.dumps(
        {
            "year": year,
            "month": month,
            "date": day,
            "hours": hour,
            "minutes": minute,
            "seconds": second,
            "latitude": 18.5204,
            "longitude": 73.8567,
            "timezone": 5.5,
            "config": {"observation_point": "topocentric", "ayanamsha": "lahiri"},
        }
    )
    headers = {"Content-Type": "application/json", "x-api-key": api_key}

    response = requests.request("POST", url, headers=headers, data=payload)

    output = json.loads(response.text)["output"]

    return output


def get_sublords_timings(nakshatra_start_timing, combination):
    try:
        start_time = nakshatra_start_timing

        # Convert phase durations to timedelta
        def hours_minutes_to_timedelta(hours_minutes):
            hours = int(hours_minutes)
            minutes = (hours_minutes - hours) * 60
            return timedelta(hours=hours, minutes=minutes)

        # Calculate the exact timings for each phase
        phases = [di["duration"] for di in combination]
        phase_names = [di["sublord"] for di in combination]
        phase_timings = []
        current_time = start_time
        for phase in phases:
            phase_duration = hours_minutes_to_timedelta(phase)
            end_time = current_time + phase_duration
            phase_timings.append((current_time, end_time))
            current_time = end_time

        output = []
        # Output the timings for each phase
        for i, (start, end) in enumerate(phase_timings):
            output.append(
                {
                    "name": phase_names[i],
                    "start": start.strftime("%Y-%m-%d %I:%M:%S %p"),
                    "end": end.strftime("%Y-%m-%d %I:%M:%S %p"),
                }
            )

        return output
        # print(
        #     f"{phase_names[i]}: {start.strftime('%I:%M:%S %p')} to {end.strftime('%I:%M:%S %p')}"
        # )
    except Exception as e:
        print("error in get sublords timings ,", e)
