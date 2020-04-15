# I try to learn a new module right here.
from datetime import datetime
import pytz
# use the pytZ module to get time.

Toronto = datetime.now(pytz.timezone("America/Toronto")) # This is the timezone and city name.
print(Toronto.strftime("%H:%M:%S"))
