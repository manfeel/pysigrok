from sigrok import *
import itertools
import sys

def check(ret, operation):
    if ret != SR_OK:
        print "Error %s (%s): %s." % (
            operation, sr_strerror_name(ret), sr_strerror(ret))
        sys.exit(1)

context_ptr = new_sr_context_ptr_ptr()
check(sr_init(context_ptr), "initializing libsigrok")
context = sr_context_ptr_ptr_value(context_ptr)

driver_list = sr_driver_list()
drivers = []
for i in itertools.count():
    driver = sr_dev_driver_ptr_array_getitem(driver_list, i)
    if driver:
        drivers.append(driver)
    else:
        break

print "Drivers:", str.join(", ", [driver.name for driver in drivers])

print "Devices:"
for driver in drivers:
    check(sr_driver_init(context, driver), "initialising %s" % driver.name)
    device_list = sr_driver_scan(driver, None)
    device_list_item = device_list
    devices = []
    while device_list_item:
        devices.append(gpointer_to_sr_dev_inst_ptr(device_list_item.data))
        device_list_item = device_list_item.next
    g_slist_free(device_list)
    if len(devices) > 0:
        for device in devices:
            print device.vendor, device.model, device.version

check(sr_exit(context), "shutting down libsigrok")

sys.exit(0)
