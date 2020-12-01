#Email extractor

import re

str= "ADGITM, NEW DELHIFC-26, SHASTRI PARK, DELHI hello@gmail.com github098@outlook.com – 110 053 contact@adgitmdelhi.ac.in +91(11) 49905900-99, 32526261-64 http:/www.adgitmdelhi.ac.in"

email = re.findall(r"[0-9a-zA-Z._%]+@[0-9a-zA-Z._%]+[.][a-zA-Z.0-9]+", str )

print(email)
