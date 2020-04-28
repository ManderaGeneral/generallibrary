from generallibrary import *
import pandas as pd



# test.TypesTest()

df = pd.DataFrame({
    "a": {"color": "red", "value": 5},
    "b": {"color": "red", "value": 2}
})

# print(df.dtypes)

# print(typeChecker({"abc": [True]}, dict, list, bool))

# print(dict.__name__)

timer = Timer()
time.sleep(1)
print(timer.seconds())

print(time.time())


