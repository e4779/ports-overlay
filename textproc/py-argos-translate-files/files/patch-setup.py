--- setup.py.orig	2026-11-10 00:31:15.036504000 +0700
+++ setup.py	2026-11-10 00:31:15.037399000 +0700
@@ -15,6 +15,6 @@
     author="S. Thuret",
     author_email="contact@sebastien-thuret.fr",
     url="https://github.com/LibreTranslate/argos-translate-files",
-    packages=find_packages(),
+    packages=find_packages(exclude=["tests", "tests.*"]),
     install_requires=required_packages,
 )
