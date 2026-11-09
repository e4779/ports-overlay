--- setup.py.orig
+++ setup.py
@@ -22,7 +22,7 @@
         "Forum": "https://community.libretranslate.com/c/argos-translate/5",
     },
     python_requires=">=3.5",
-    packages=find_packages(),
+    packages=find_packages(exclude=["tests", "tests.*"]),
     install_requires=required_packages,
     entry_points={
         "console_scripts": [
