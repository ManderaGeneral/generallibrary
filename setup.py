from setuptools import setup

setup(
    name = "generallibrary",
    version = "1.1.3",
    description = (""
                   "Fixed Timer again, now using time.time() which is the same os.path.getmtime() uses. "
                   "Random functions to help with native classes."
                   ""),
    py_modules = ["generallibrary"]
)


from generalfile import test

