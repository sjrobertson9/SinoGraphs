# Contains a whole lot of lists I guess
patterns = {
    "test": ["sin(x-8/2)+1/2", "sin(x)", "sin(x+8/2)-5", "sin(x)-5"],
    "eyes": ["3tan(x)", "-3tan(x)", "8cos(1/3x)", "-8cos(1/3x)",
             "4cos(1/3x)", "-4cos(1/3x)", "sin(1/3x)", "-sin(1/3x)"],
    "fingers": ["tan(1/3x)", "tan(-1/3x)", "tan(1/4x)", "tan(-1/4x)",
                "3tan(1/3x)", "-3tan(1/3x)", "3tan(1/4x)", "-3tan(1/4x)",
                "3tan(1/4x)", "-3tan(1/4x)", "2sin(1/2x)", "-2sin(1/2x)"],
    "city": ["15sin(1/2x+5)", "-15sin(1/2x+5)", "12sin(1/2x)+3", "-12sin(1/2x)+3",
             "4cos(x)", "-4cos(x)",
             "5cos(x)", "-5cos(x)", "6cos(x)", "-6cos(x)",
             "7cos(x)", "-7cos(x)", "8cos(x)", "-8cos(x)",
             "12sin(1/2x)", "-12sin(1/2x)", "14sin(1/2x)", "-14sin(1/2x)",
             "10sin(1/2x)", "-10sin(1/2x)"],
    "chunk": ["sin(1/2x)", "cos(1/2x)", "5sin(1/2x)", "5cos(1/2x)",
              "10sin(1/2x)", "10cos(1/2x)", "15sin(1/2x)", "15cos(1/2x)",
              "20sin(1/2x)", "20cos(1/2x)", "25sin(1/2x)", "25cos(1/2x)",
              "30sin(1/2x)", "30cos(1/2x)", "35sin(1/2x)", "35cos(1/2x)",
              "40sin(1/2x)", "40cos(1/2x)", "45sin(1/2x)", "45cos(1/2x)",
              "50sin(1/2x)", "50cos(1/2x)", "55sin(1/2x)", "55cos(1/2x)",
              "60sin(1/2x)", "60cos(1/2x)", "65sin(1/2x)", "65cos(1/2x)",
              "70sin(1/2x)", "70cos(1/2x)", "75sin(1/2x)", "75cos(1/2x)",
              "80sin(1/2x)", "80cos(1/2x)", "85sin(1/2x)", "85cos(1/2x)",
              "90sin(1/2x)", "90cos(1/2x)", "95sin(1/2x)", "95cos(1/2x)",
              "100sin(1/2x)", "100cos(1/2x)"],
    "bloop": ["sin(1/2x)", "-sin(1/2x)", "5sin(1/2x)", "-5sin(1/2x)",
              "10sin(1/2x)", "-10sin(1/2x)", "15sin(1/2x)", "-15sin(1/2x)",
              "20sin(1/2x)", "-20sin(1/2x)", "25sin(1/2x)", "-25sin(1/2x)",
              "30sin(1/2x)", "-30sin(1/2x)", "35sin(1/2x)", "-35sin(1/2x)",
              "40sin(1/2x)", "-40sin(1/2x)", "45sin(1/2x)", "-45sin(1/2x)",
              "50sin(1/2x)", "-50sin(1/2x)", "55sin(1/2x)", "-55sin(1/2x)",
              "60sin(1/2x)", "-60sin(1/2x)", "65sin(1/2x)", "-65sin(1/2x)",
              "70sin(1/2x)", "-70sin(1/2x)", "75sin(1/2x)", "-75sin(1/2x)",
              "80sin(1/2x)", "-80sin(1/2x)", "85sin(1/2x)", "-85sin(1/2x)",
              "90sin(1/2x)", "-90sin(1/2x)", "95sin(1/2x)", "-95sin(1/2x)",
              "100sin(1/2x)", "-100sin(1/2x)"],
    "wamp":  ["tan(1/2x)", "-tan(1/2x)", "5tan(1/2x)", "-5tan(1/2x)",
              "10tan(1/2x)", "-10tan(1/2x)", "15tan(1/2x)", "-15tan(1/2x)",
              "20tan(1/2x)", "-20tan(1/2x)", "25tan(1/2x)", "-25tan(1/2x)",
              "30tan(1/2x)", "-30tan(1/2x)", "35tan(1/2x)", "-35tan(1/2x)",
              "40tan(1/2x)", "-40tan(1/2x)", "45tan(1/2x)", "-45tan(1/2x)",
              "50tan(1/2x)", "-50tan(1/2x)", "55tan(1/2x)", "-55tan(1/2x)",
              "60tan(1/2x)", "-60tan(1/2x)", "65tan(1/2x)", "-65tan(1/2x)",
              "70tan(1/2x)", "-70tan(1/2x)", "75tan(1/2x)", "-75tan(1/2x)",
              "80tan(1/2x)", "-80tan(1/2x)", "85tan(1/2x)", "-85tan(1/2x)",
              "90tan(1/2x)", "-90tan(1/2x)", "95tan(1/2x)", "-95tan(1/2x)",
              "100tan(1/2x)", "-100tan(1/2x)", "105tan(1/2x)", "-105tan(1/2x)",
              "110tan(1/2x)", "-110tan(1/2x)", "115tan(1/2x)", "-115tan(1/2x)",
              "120tan(1/2x)", "-120tan(1/2x)", "125tan(1/2x)", "-125tan(1/2x)",
              "130tan(1/2x)", "-130tan(1/2x)", "135tan(1/2x)", "-135tan(1/2x)",
              "140tan(1/2x)", "-140tan(1/2x)", "145tan(1/2x)", "-145tan(1/2x)",
              # "150tan(1/2x)", "-150tan(1/2x)", "155tan(1/2x)", "-155tan(1/2x)",
              "160tan(1/2x)", "-160tan(1/2x)", "165tan(1/2x)", "-165tan(1/2x)",
              # "170tan(1/2x)", "-170tan(1/2x)", "175tan(1/2x)", "-175tan(1/2x)",
              "180tan(1/2x)", "-180tan(1/2x)", "185tan(1/2x)", "-185tan(1/2x)",
              # "190tan(1/2x)", "-190tan(1/2x)", "195tan(1/2x)", "-195tan(1/2x)",
              "200tan(1/2x)", "-200tan(1/2x)", "205tan(1/2x)", "-205tan(1/2x)",
              # "210tan(1/2x)", "-210tan(1/2x)", "215tan(1/2x)", "-215tan(1/2x)",
              "220tan(1/2x)", "-220tan(1/2x)", "225tan(1/2x)", "-225tan(1/2x)"],
    "lejetset": ["3tan(x)", "-3tan(x)", "6tan(x)", "-6tan(x)", "9tan(x)", "-9tan(x)",
                 "12tan(x)", "-12tan(x)", "15tan(x)", "-15tan(x)", "18tan(x)",
                 "-18tan(x)", "21tan(x)", "-21tan(x)", "24tan(x)", "-24tan(x)",
                 "27tan(x)", "-27tan(x)", "30tan(x)", "-30tan(x)", "33tan(x)",
                 "-33tan(x)"]
}
# Contains the x y multipliers for each list because I'm lazy

mults = {
    "test": 6,
    "wiggle": 35,
    "eyes": 20,
    "fingers": 90,
    "city": 17,
    "chunk": 3,
    "bloop": 3,
    "wamp": 1,
    "lejetset": 1
}

# Colors?????

colors = {
    "red": ["maroon", "darkorange", "mistyrose", "chocolate", "tomato",
            "coral", "darksalmon", "sienna"],
    "blue": ["skyblue", "slategrey", "teal", "paleturquoise", "royalblue",
             "lavender", "lightsteelblue", "cornflowerblue"]
}


