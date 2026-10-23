--- server.c.orig	2026-10-23 11:30:19.044791000 +0700
+++ server.c	2026-10-23 11:30:19.046231000 +0700
@@ -5,7 +5,7 @@
 
 int resolve(const char *host, unsigned short port, struct addrinfo** addr) {
 	struct addrinfo hints = {
-		.ai_family = AF_UNSPEC,
+		.ai_family = AF_INET,
 		.ai_socktype = SOCK_STREAM,
 		.ai_flags = AI_PASSIVE,
 	};
