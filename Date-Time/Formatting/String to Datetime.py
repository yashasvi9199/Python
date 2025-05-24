from datetime import datetime

# Date string in dd/mm/YYYY HH:MM:SS
str = "12/05/2020 19:32:11"

# Conversion
dt = datetime.strptime(str, "%d/%m/%Y %H:%M:%S")
# dt = datetime.strptime(str, "%m/%d/%Y %M:%S:%H")          can be re-arranged as per wish
print(dt)