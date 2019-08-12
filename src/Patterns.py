# Contains a whole lot of lists I guess
patterns = {
    "test": ["3.1", "6", "sin(x)", "-sin(x)", "-4sin(x)", "4sin(x)", "8sin(x)",
             "-8sin(x)", "cos(x)", "-cos(x)", "50sin(x)", "-50sin(x)"],
    "wiggle": ["4sin(1/2x)", "-2sin(1/2x)", "6sin(1/2x)", "-6sin(1/2x)",
               "-2sin(1/2x)", "2sin(1/2x)", "2cos(1/2x)", "-2cos(1/2x)"],
    "eyes": ["3tan(x)", "-3tan(x)", "8cos(1/3x)", "-8cos(1/3x)",
             "4cos(1/3x)", "-4cos(1/3x)", "sin(1/3x)", "-sin(1/3x)"],
    "fingers": ["tan(1/3x)", "tan(-1/3x)", "tan(1/4x)", "tan(-1/4x)",
                "3tan(1/3x)", "-3tan(1/3x)", "3tan(1/4x)", "-3tan(1/4x)",
                "3tan(1/4x)", "-3tan(1/4x)", "2sin(1/2x)", "-2sin(1/2x)"],
    "city": ["15sin(2x)", "-15sin(2x)", "4cos(x)", "-4cos(x)",
             "10sin(1/2x)", "-10sin(1/2x)", "tan(x)", "-tan(x)"],
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
              "100sin(1/2x)", "100cos(1/2x)"]
}
# Contains the x y multipliers for each list because I'm lazy

mults = {
    "test": 6,
    "wiggle": 35,
    "eyes": 20,
    "fingers": 90,
    "city": 17,
    "chunk": 3
}