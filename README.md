# Package: generallibrary
Random useful code categorized into modules.

## Installation
```
pip install generallibrary
```

## Features
| Module    | Name                 | Explanation                                                                                   |
|:----------|:---------------------|:----------------------------------------------------------------------------------------------|
| code      | debug                | Easily call eval() on an arbitrary amount of evaluation strings.                              |
| code      | getLocalFeaturesAsMD | Convert local callable objects that don't start with `_` to a markdown table for a README.    |
| functions | Operators            | Automatic operator definitions for classes.                                                   |
| functions | SigInfo              | Handles a callable along with it's parameters.                                                |
| functions | calculate            | Automatically fills variables of a formula in a string then evaluates it.                     |
| functions | defaults             | Set default values of a given dictionary, option to overwrite None values.                    |
| iterables | SortedList           | Controls a sorted list in ascending order.                                                    |
| iterables | addToDictInDict      | Add a key-value argument to a dict inside a dict, automatically creates dict.                 |
| iterables | addToListInDict      | Add a value to a list inside a dictionary, automatically creates list.                        |
| iterables | combine              | Create a list of dicts containing every unique combination from given object (Can be tuples). |
| iterables | depth                | Get depth of an object by recursively checking the first value.                               |
| iterables | dictFirstValue       | Get first 'random' value of a dictionary or None.                                             |
| iterables | exclusive            | Returns a new dictionary without keys.                                                        |
| iterables | getFreeIndex         | Get the first free integer index of dictionary starting at 0.                                 |
| iterables | getIterable          | Returns the iterable values of a tuple, list or dict. Otherwise `False`.                      |
| iterables | getRows              | Get rows as lists in list from a tuple, list or dict (where it discards keys).                |
| iterables | inclusive            | Returns a new dictionary without keys not in keys.                                            |
| iterables | isIterable           | See if an obj is a tuple, list or dict.                                                       |
| iterables | iterFirstValue       | Get first 'random' value of an iterable or None.                                              |
| iterables | joinWithStr          | Like str.join() but it casts the values to strings first, also takes dict.                    |
| iterables | uniqueObjInList      | Controls whether a unique object should be present in a list or not.                          |
| object    | attributes           | Get all attributes of an object that don't start with `__`, as a dictionary.                  |
| object    | getClassFromMethod   | Retrieve class object from a method object.                                                   |
| object    | getsize              | Get a sum of sizes from an object and it's members in bytes.                                  |
| object    | initBases            | Decorator function for class to automatically initalize all inherited classes.                |
| time      | Timer                | Callable class to easily time things and print.                                               |
| time      | sleep                | Normal sleep function from time package.                                                      |
| types     | getBaseClassNames    | Get all base classes from an object's class as lowered names.                                 |
| types     | getBaseClasses       | Get all base classes from an object's class.                                                  |
| types     | hasMethod            | Return whether an object has a specific callabale attribute.                                  |
| types     | strToDynamicType     | Try to convert a string to bool, None, int or float.                                          |
| types     | typeChecker          | Check type(s) of an object.                                                                   |
| values    | clamp                | Return clamped value between minimum and maximum.                                             |
| values    | confineTo            | Confine this value, but unlike clamp it subtracts diff * n to create an 'infinite' effect.    |
| values    | doubleRectify        | Return 0 if it's between min and max, otherwise it returns difference from edge of range.     |
| values    | inrange              | Return whether value is between minimum and maximum.                                          |
| values    | rectify              | Return 0 if it's below threshold, otherwise difference.                                       |
| values    | sign                 | Get sign value based on threshold that defaults to 0.                                         |
| versions  | VerInfo              | Get version info regarding running Python and OS.                                             |

## Usage example
```python
from generallibrary.values import clamp
print(clamp(-3.2, -1, 1))
# >>> -1
```

## Releases
#### generallibrary 2.0
 * Put all features inside `__init__.py` to make importing easier
 * Added Operators
 * Added VerInfo
 * Added SigInfo
 * Changed addToListInDict to allow *args and returns entire dict
 * Added addToDictInDict
 * Added initCaller decorator
 * Added includeObject parameter to getBaseClasses
 * Added includeDefaulted parameter to getSignatureNames
 * Added combine
 * Added uniqueObjInList

## Todo
 * Redo iterables.py, namely getIterable() and isIterable(), it's a mess
 * Handle local and pre-releases for versions.VerInfo
 * Make SigInfo's callableObject changeable and store all variables when setting them
 * DuckTyping class for versions.py
 * PackageVersion class for versions.py
 * Change getLocalFeaturesAsMD to allow cls or even obj and also *args.