#import kitano as kt
from kitano.logging import puts
import kitano.logging as logg

strf = logg.strft

print(strf)

logg.str_date(strf)

puts('testing...',file_log='app.log')
