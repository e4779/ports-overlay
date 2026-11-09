--- setup.py.orig	2026-11-10 00:15:53.567192000 +0700
+++ setup.py	2026-11-10 00:15:53.568336000 +0700
@@ -51,7 +51,7 @@
 elif sys.platform == "win32":
     cflags = ["/std:c++17", "/d2FH4-"]
     package_data["ctranslate2"] = ["*.dll"]
-elif sys.platform == "linux":
+elif sys.platform in ("linux", "freebsd"):
     cflags.append("-fPIC")
     ldflags.append("-Wl,-rpath,/usr/local/lib64:/usr/local/lib")
 
