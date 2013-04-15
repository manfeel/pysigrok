from sigrok import *
import itertools
import sys

sr_ctx = new_sr_context_ptr_ptr()

ret = sr_init(sr_ctx)
if ret != SR_OK:
    print "Error initializing libsigrok (%s): %s." % (
        sr_strerror_name(ret), sr_strerror(ret))
    sys.exit(1)

driver_list = sr_driver_list()
drivers = []
for i in itertools.count():
    driver = sr_dev_driver_ptr_array_getitem(driver_list, i)
    if driver:
        drivers.append(driver)
    else:
        break

print "Drivers:", str.join(", ", [driver.name for driver in drivers])

ret = sr_exit(sr_context_ptr_ptr_value(sr_ctx))
if ret != SR_OK:
    print "Error shutting down libsigrok (%s): %s." % (
        sr_strerror_name(ret), sr_strerror(ret))
    sys.exit(1)

sys.exit(0)
