--- ggml/src/ggml-vulkan/ggml-vulkan-comm.cpp.orig
+++ ggml/src/ggml-vulkan/ggml-vulkan-comm.cpp
@@ -1,3 +1,8 @@
+// FreeBSD compat: _XOPEN_SOURCE=600 hides F_DUPFD_CLOEXEC (POSIX-2008)
+#ifndef F_DUPFD_CLOEXEC
+#define F_DUPFD_CLOEXEC 17
+#endif
+
 #include "ggml-vulkan-common.h"
 
 #if !defined(_WIN32)
