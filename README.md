
[![PyPI version shields.io](https://img.shields.io/pypi/v/generallibrary.svg)](https://pypi.org/project/generallibrary/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/generallibrary.svg)](https://pypi.python.org/pypi/generallibrary/)
[![Generic badge](https://img.shields.io/badge/platforms-Windows%20|%20Ubuntu%20|%20MacOS-blue.svg)](https://shields.io/)
[![workflow Actions Status](https://github.com/ManderaGeneral/generallibrary/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/generallibrary/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/generallibrary.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/generallibrary/alerts/)

# Package: generallibrary
Random useful code categorized into modules.

## Installation
```
pip install generallibrary
```

## Attributes of module generallibrary
| Module    | Name                                                    | Type     | Attributes   | Explanation                                                                                   |
|:----------|:--------------------------------------------------------|:---------|:-------------|:----------------------------------------------------------------------------------------------|
| code      | [CodeGen](#Attributes-of-class-CodeGen)                 | class    | 4            | Tool to help with printing code line by line.                                                 |
| code      | args_to_attrs                                           | function |              | Print code for a dunder init method to store all arguments as attributes.                     |
| code      | attributes_to_markdown                                    | function |              | Convert attributes of a given obj to a readme string recursively.                             |
| code      | clipboard_copy                                          | function |              | Copy a string to clipboard.                                                                   |
| code      | clipboard_get                                           | function |              | Get clipboard string.                                                                         |
| code      | debug                                                   | function |              | Easily call eval() on an arbitrary amount of evaluation strings.                              |
| code      | print_link                                              | function |              | Print a link in PyCharm to a line in file.                                                    |
| code      | print_link_to_obj                                       | function |              | Print a link in PyCharm to a module, function, class, method or property.                     |
| diagram   | [TreeDiagram](#Attributes-of-class-TreeDiagram)         | class    | 18           | Saveable tree diagram with optional storage.                                                  |
| functions | EmptyContext                                            | class    |              | Class for an empty context manager.                                                           |
| functions | [Operators](#Attributes-of-class-Operators)             | class    | 2            | Automatic operator definitions for classes.                                                   |
| functions | [SigInfo](#Attributes-of-class-SigInfo)                 | class    | 21           | Handles a callable along with it's parameters.                                                |
| functions | calculate                                               | function |              | Automatically fills variables of a formula in a string then evaluates it.                     |
| functions | classproperty                                           | class    |              | Just like @property but for a class method.                                                   |
| functions | deco_cache                                              | function |              | Enable caching for a method or function.                                                      |
| functions | deco_cast_parameters                                    | function |              | Decorator to make sure `path` parameter is a Path.                                            |
| functions | deco_default_self_args                                  | function |              | As an alternative to setting each and every parameter's default value to `None` for a method. |
| functions | defaults                                                | function |              | Set default values of a given dictionary, option to overwrite None values.                    |
| iterables | [SortedList](#Attributes-of-class-SortedList)           | class    | 2            | Controls a sorted list in ascending order.                                                    |
| iterables | addToDictInDict                                         | function |              | Add a key-value argument to a dict inside a dict, automatically creates dict.                 |
| iterables | addToListInDict                                         | function |              | Add a value to a list inside a dictionary, automatically creates list.                        |
| iterables | combine                                                 | function |              | Create a list of dicts containing every unique combination from given object (Can be tuples). |
| iterables | depth                                                   | function |              | Get depth of an object by recursively checking the first value.                               |
| iterables | dictFirstValue                                          | function |              | Get first 'random' value of a dictionary or None.                                             |
| iterables | exclusive                                               | function |              | Returns a new dictionary without keys.                                                        |
| iterables | getFreeIndex                                            | function |              | Get the first free integer index of dictionary starting at 0.                                 |
| iterables | getIterable                                             | function |              | Returns the iterable values of a tuple, list or dict. Otherwise `False`.                      |
| iterables | getRows                                                 | function |              | Get rows as lists in list from a tuple, list or dict (where it discards keys).                |
| iterables | inclusive                                               | function |              | Returns a new dictionary without keys not in keys.                                            |
| iterables | isIterable                                              | function |              | See if an obj is a tuple, list or dict.                                                       |
| iterables | iterFirstValue                                          | function |              | Get first 'random' value of an iterable or None.                                              |
| iterables | joinWithStr                                             | function |              | Like str.join() but it casts the values to strings first, also takes dict.                    |
| iterables | remove_duplicates                                       | function |              | Remove all duplicates in a list.                                                              |
| iterables | uniqueObjInList                                         | function |              | Controls whether a unique object should be present in a list.                                 |
| object    | attributes                                              | function |              | Get attributes from a Module or Class with a lot of optional flags for filtering.             |
| object    | getsize                                                 | function |              | Get a sum of sizes from an object and it's members in bytes.                                  |
| object    | initBases                                               | function |              | Decorator function for class to automatically initalize all inherited classes.                |
| time      | [Timer](#Attributes-of-class-Timer)                     | class    | 3            | Callable class to easily time things and print.                                               |
| time      | sleep                                                   | function |              | Normal sleep function from time package.                                                      |
| types     | [HierarchyStorer](#Attributes-of-class-HierarchyStorer) | class    | 1            | A metaclass that automatically stores references to all inheriters.                           |
| types     | getBaseClassNames                                       | function |              | Get all base classes from an object's class.                                                  |
| types     | getBaseClasses                                          | function |              | Get all base classes from an object's class.                                                  |
| types     | hasMethod                                               | function |              | Return whether an object has a specific callabale attribute.                                  |
| types     | strToDynamicType                                        | function |              | Try to convert a string to bool, None, int or float.                                          |
| types     | typeChecker                                             | function |              | Check type(s) of an object.                                                                   |
| values    | clamp                                                   | function |              | Return clamped value between minimum and maximum.                                             |
| values    | confineTo                                               | function |              | Confine this value, but unlike clamp it subtracts diff * n to create an 'infinite' effect.    |
| values    | doubleRectify                                           | function |              | Return 0 if it's between min and max, otherwise it returns difference from edge of range.     |
| values    | inrange                                                 | function |              | Return whether value is between minimum and maximum.                                          |
| values    | rectify                                                 | function |              | Return 0 if it's below threshold, otherwise difference.                                       |
| values    | sign                                                    | function |              | Get sign value based on threshold that defaults to 0.                                         |
| versions  | [VerInfo](#Attributes-of-class-VerInfo)                 | class    | 23           | Get version info regarding current Python, OS and conditional functionalities.                |
| versions  | get_installed_packages                                  | function |              | Get a list of all installed packages as strings.                                              |
| versions  | package_is_installed                                    | function |              | Returns whether a package is installed.                                                       |


#### Attributes of class CodeGen
| Module   | Name     | Type     | Explanation                                                                  |
|:---------|:---------|:---------|:-----------------------------------------------------------------------------|
|          | indent   | variable | Variable of type 'str'.                                                      |
| code     | add      | method   | Add a new line.                                                              |
| code     | generate | method   | Generate a list of formatted code lines by iterating stored _Line instances. |
| code     | print    | method   | Generate and print copyable code.                                            |


#### Attributes of class HierarchyStorer
| Module   | Name   | Type     | Explanation                           |
|:---------|:-------|:---------|:--------------------------------------|
|          | mro    | variable | Variable of type 'method_descriptor'. |


#### Attributes of class Operators
| Module    | Name                    | Type     | Explanation                                      |
|:----------|:------------------------|:---------|:-------------------------------------------------|
|           | comparisons             | variable | Variable of type 'dict'.                         |
| functions | deco_define_comparisons | method   | Define all comparision operators for this class. |


#### Attributes of class SigInfo
| Module    | Name                           | Type     | Explanation                                                                                   |
|:----------|:-------------------------------|:---------|:----------------------------------------------------------------------------------------------|
| functions | callableObject                 | property | Propertize to protect but still have public.                                                  |
| functions | class_from_callable            | method   | Return class that owns given method, or given callable from initiating SigInfo.               |
| functions | defaults                       | property | Get dict of default values.                                                                   |
| functions | getIndexFromName               | method   | Get index from name if name exists, else None.                                                |
| functions | leadingArgNames                | property | Get names leading args that don't have default value.                                         |
| functions | names                          | property | Get list of parameter names.                                                                  |
| functions | namesRequired                  | property | Get list of parameter that have to be defined, i.e. non-packed without default value.         |
| functions | namesWithoutDefaults           | property | Get list of parameter names except those ones that have a default value.                      |
| functions | namesWithoutPacked             | property | Get list of parameter names except *args or **kwargs.                                         |
| functions | packedArgs                     | property | Return a list of values in packed args parameter, empty list if there are no packed args.     |
| functions | packedArgsName                 | property | Get name of packed *args or None.                                                             |
| functions | packedKwargs                   | property | Return a dict of values in packed kwargs parameter, empty dict if there are no packed kwargs. |
| functions | packedKwargsName               | property | Get name of packed *kwargs or None.                                                           |
| functions | parameters                     | property | Get list of inspect parameter objects.                                                        |
| functions | positionalArgNames             | property | Get list of parameter names that CAN take a positional argument.                              |
| functions | positionalOnlyArgNames         | property | Get list of parameter names that can ONLY take a positional argument.                         |
| functions | positionalOnlyOppositeArgNames | property | Get list of parameter names that CAN take a keyword argument.                                 |
| functions | positionalOppositeArgNames     | property | Get list of parameter names that can ONLY take a keyword argument.                            |
| functions | positional_extra               | property | Get a list of the positional parameter names, including self or cls.                          |
| functions | unpackedArgs                   | property | Extract a list of all positional ONLY parameters for callable.                                |
| functions | unpackedKwargs                 | property | Extract a dict of key words that callable can take.                                           |


#### Attributes of class SortedList
| Module    | Name   | Type   | Explanation                      |
|:----------|:-------|:-------|:---------------------------------|
| iterables | add    | method | Add objects to sorted list.      |
| iterables | remove | method | Remove objects from sorted list. |


#### Attributes of class Timer
| Module   | Name    | Type   | Explanation                                          |
|:---------|:--------|:-------|:-----------------------------------------------------|
| time     | print   | method | Print seconds passed.                                |
| time     | reset   | method | Reset and start timer.                               |
| time     | seconds | method | Get seconds passed since timer started or was reset. |


#### Attributes of class TreeDiagram
| Module   | Name               | Type     | Explanation                                                           |
|:---------|:-------------------|:---------|:----------------------------------------------------------------------|
|          | data_keys          | variable | Variable of type 'list'.                                              |
| diagram  | all_parents        | method   | Get a list of all parents recursively.                                |
| diagram  | copy_to            | method   | Copy this Node along with it's children by using save and load.       |
| diagram  | data_keys_add      | method   | Define what attributes to keep track of automatically in __setattr__. |
| diagram  | get_children       | method   | Get a list of all children this Node has.                             |
| diagram  | get_parent         | method   | Get this Node's parent.                                               |
| diagram  | hook_add_child     | method   | New child hook.                                                       |
| diagram  | hook_create_post   | method   | Post-creation hook.                                                   |
| diagram  | hook_create_pre    | method   | Pre-creation hook.                                                    |
| diagram  | hook_lose_child    | method   | Lost child hook.                                                      |
| diagram  | hook_lose_parent   | method   | Lost parent hook.                                                     |
| diagram  | hook_new_parent    | method   | New parent hook.                                                      |
| diagram  | hook_remove        | method   | Remove hook.                                                          |
| diagram  | hook_set_attribute | method   | Attribute set hook.                                                   |
| diagram  | load               | method   | Create a new Tree from a dictionary save.                             |
| diagram  | remove             | method   | Remove this Node.                                                     |
| diagram  | save               | method   | Recursively save by returning a new dictionary.                       |
| diagram  | set_parent         | method   | Set a new parent for this Node.                                       |


#### Attributes of class VerInfo
| Module   | Name                 | Type     | Explanation                                                                                  |
|:---------|:---------------------|:---------|:---------------------------------------------------------------------------------------------|
| versions | caseSensitive        | property | Get whether current OS is case sensitive.                                                    |
| versions | java                 | property | Get whether running on Java.                                                                 |
| versions | linux                | property | Get whether running on Linux.                                                                |
| versions | mac                  | property | Get whether running on Mac.                                                                  |
| versions | os                   | property | Return name of running operating system.                                                     |
| versions | pathDelimiter        | property | Get current OS's path delimiter.                                                             |
| versions | pathRootHasColon     | property | Get whether current OS defines path root with a colon in the first part.                     |
| versions | pathRootIsDelimiter  | property | Get whether current OS defines path root as a starting delimiter.                            |
| versions | positionalArgument   | property | Get whether current python version supports positional arguments.                            |
| versions | pythonAlpha          | property | Return whether release level is 'alpha'.                                                     |
| versions | pythonBeta           | property | Return whether release level is 'beta'.                                                      |
| versions | pythonCandidate      | property | Return whether release level is 'candidate'.                                                 |
| versions | pythonFinal          | property | Return whether release level is 'final'.                                                     |
| versions | pythonMajor          | property | Return first digit of python version.                                                        |
| versions | pythonMicro          | property | Return third digit of python version.                                                        |
| versions | pythonMinor          | property | Return second digit of python version.                                                       |
| versions | pythonReleaseKeyword | property | Return keyword for release level such as 'a', 'b', 'rc' or '' for final.                     |
| versions | pythonReleaseLevel   | property | Return release level of python version.                                                      |
| versions | pythonSerial         | property | Return serial number of python version. I think it's only used for non-final release levels. |
| versions | pythonSerialString   | property | Return serial number of python version as a string, should be empty if it's 0.               |
| versions | pythonString         | property | Return python version as '3.8.5' or '3.8.5a4' if alpha release 4.                            |
| versions | pythonVersion        | property | Returns a PythonVersion object that can be used to compare directly to an int, float or str. |
| versions | windows              | property | Get whether running on Windows.                                                              |

## Usage example
```python
from generallibrary import clamp
print(clamp(-3.2, -1, 1))
# >>> -1
```

## Releases
#### generallibrary 2.1
 * Added properties to `VerInfo()` for conditional functionalities
     * caseSensitive
     * positionalArgument
     * pathDelimiter
     * pathRootIsDelimiter
     * pathRootHasColon

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

[Go to installation](#Installation)