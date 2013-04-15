%module(package="sigrok") libsigrok
%include "cpointer.i"
%include "carrays.i"

%{
#include "libsigrok/libsigrok.h"
#include "libsigrok/proto.h"
#include "libsigrok/version.h"
%}

typedef struct _GSList GSList;

struct _GSList
{
  gpointer data;
  GSList *next;
};

void g_slist_free(GSList *list);

%include "libsigrok/libsigrok.h"
#undef SR_API
#define SR_API
%ignore sr_config_info_name_get;
%include "libsigrok/proto.h"
%include "libsigrok/version.h"

%pointer_functions(struct sr_context *, sr_context_ptr_ptr);
%array_functions(struct sr_dev_driver *, sr_dev_driver_ptr_array);
%pointer_cast(gpointer, struct sr_dev_inst *, gpointer_to_sr_dev_inst_ptr);
