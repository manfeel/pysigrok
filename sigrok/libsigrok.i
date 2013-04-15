%module(package="sigrok") libsigrok
%include "cpointer.i"

%{
#include "libsigrok/libsigrok.h"
#include "libsigrok/proto.h"
#include "libsigrok/version.h"
%}


%include "libsigrok/libsigrok.h"
#undef SR_API
#define SR_API
%ignore sr_config_info_name_get;
%include "libsigrok/proto.h"
%include "libsigrok/version.h"

%pointer_functions(struct sr_context *, sr_context_pointer);
