from sigrok import *
import sys

sr_ctx = new_sr_context_pointer();

ret = sr_init(sr_ctx)
if ret != SR_OK:
    print "Error initializing libsigrok (%s): %s." % (
        sr_strerror_name(ret), sr_strerror(ret))
    sys.exit(1)

ret = sr_exit(sr_context_pointer_value(sr_ctx))
if ret != SR_OK:
    print "Error shutting down libsigrok (%s): %s." % (
        sr_strerror_name(ret), sr_strerror(ret))
    sys.exit(1)

sys.exit(0)
