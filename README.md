# generallibrary
Random useful code categorized into modules.

This package and 6 other make up [ManderaGeneral](https://github.com/ManderaGeneral).

## Information
| Package                                                            | Ver                                                | Latest Release       | Python                                                                                                                   | Platform        |   Lvl | Todo                                                       | Tests   |
|:-------------------------------------------------------------------|:---------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:-----------------------------------------------------------|:--------|
| [generallibrary](https://github.com/ManderaGeneral/generallibrary) | [2.8.12](https://pypi.org/project/generallibrary/) | 2021-11-29 19:00 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     0 | [5](https://github.com/ManderaGeneral/generallibrary#Todo) | 99.5 %  |

## Contents
<pre>
<a href='#generallibrary'>generallibrary</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todo'>Todo</a>
</pre>

## Installation
| Command                      | <a href='https://pypi.org/project/packaging'>packaging</a>   | <a href='https://pypi.org/project/pyperclip'>pyperclip</a>   | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/tabulate'>tabulate</a>   | <a href='https://pypi.org/project/pytz'>pytz</a>   | <a href='https://pypi.org/project/dill'>dill</a>   |
|:-----------------------------|:-------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------------------|:-----------------------------------------------------------|:---------------------------------------------------|:---------------------------------------------------|
| `pip install generallibrary` | Yes                                                          | Yes                                                          | Yes                                                    | Yes                                                        | Yes                                                | Yes                                                |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/__init__.py#L1'>Module: generallibrary</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Class: AutoInitBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Class: CallTable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: generate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: generate_with_args</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: generate_with_funcs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: set_args</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: set_funcs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Class: CodeLine</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Method: get_lines</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Method: text</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Class: Date</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Method: get_timezone_obj</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Method: now</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Class: EmptyContext</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Class: EnvVar</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Property: value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/types.py#L1'>Class: HierarchyStorer</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Class: Markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: add_code_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: add_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: add_list_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: add_pre_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: add_table_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_all_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_section_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: link</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: wrap_with_tags</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Class: NetworkDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_spouse</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_spouses</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/objinfo.py#L1'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/objinfo.py#L1'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: add_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/parents.py#L1'>Method: check_if_parent_eligible</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: defined_by_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: disconnect</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: doc</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/origin.py#L1'>Method: from_base</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/origin.py#L1'>Method: from_builtin</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/origin.py#L1'>Method: from_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/origin.py#L1'>Method: from_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/origin.py#L1'>Method: from_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: get_definition_line</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: get_origin</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/objinfo.py#L1'>Method: identifier</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: internal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/type.py#L1'>Method: is_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/type.py#L1'>Method: is_function</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/type.py#L1'>Method: is_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/type.py#L1'>Method: is_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/type.py#L1'>Method: is_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/type.py#L1'>Method: is_property</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: print_link_to_obj</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: private</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: protected</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/properties.py#L1'>Method: public</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: remove_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/parents.py#L1'>Method: spawn_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/type.py#L1'>Method: type</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Class: Operators</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: deco_define_comparisons</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Class: PythonVersion</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: version</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Class: Recycle</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: recycle_clear</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: recycle_clear_all</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Class: SigInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: call</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: callableObject</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: class_from_callable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: defaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Method: getIndexFromName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: leadingArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: namesRequired</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: namesWithoutDefaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: namesWithoutPacked</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: packedArgs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: packedArgsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: packedKwargs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: packedKwargsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: parameters</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: positionalArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: positionalOnlyArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: positionalOnlyOppositeArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: positionalOppositeArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: positional_extra</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: unpackedArgs</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Property: unpackedKwargs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Class: SortedList</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Method: add</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Method: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Class: Storable</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: copy_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: load_node</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: save_node</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Class: Timer</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Method: deco</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Method: print</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Method: reset</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Method: seconds</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Class: TreeDiagram</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/diagram.py#L1'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Class: Ver</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Method: bump</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Class: VerInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: caseSensitive</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pathDelimiter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pathRootHasColon</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pathRootIsDelimiter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: positionalArgument</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonAlpha</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonBeta</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonCandidate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonFinal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonMajor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonMicro</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonMinor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonReleaseKeyword</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonReleaseLevel</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonSerial</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonSerialString</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonString</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Property: pythonVersion</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/objinfo.py#L1'>Function: cache_clear</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: calculate</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: ceil</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: clamp</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Class: classproperty</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Function: clipboard_copy</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Function: clipboard_get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: combine</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/text.py#L1'>Function: comma_and_and</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: confineTo</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Function: debug</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: deco_bound_defaults</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: deco_cache</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: deco_cast_parameters</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: deco_extend</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: deco_propagate_while</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: defaults</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: depth</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: dict_insert</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: doubleRectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: exclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: extend_list_in_dict</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: flatten</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: floor</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/types.py#L1'>Function: getBaseClassNames</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/types.py#L1'>Function: getBaseClasses</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Function: get_definition_line</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: get_free_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: get_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Function: get_installed_packages</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: get_items</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: get_launch_options</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Function: get_origin</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: get_rows</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: get_values</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/object.py#L1'>Function: getsize</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/types.py#L1'>Function: hasMethod</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/objinfo/objinfo.py#L1'>Function: hook</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: import_module</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: inclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: initBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: inrange</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: is_iterable</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: iter_first_value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: join_with_str</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/text.py#L1'>Function: match</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/versions.py#L1'>Function: package_is_installed</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: pivot_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/text.py#L1'>Function: plur_sing</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Function: print_link</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/code.py#L1'>Function: print_link_to_obj</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: rectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: remove_duplicates</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/text.py#L1'>Function: replace</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/values.py#L1'>Function: sign</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/time.py#L1'>Function: sleep</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: split_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/types.py#L1'>Function: strToDynamicType</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: subtract_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: terminal</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/types.py#L1'>Function: typeChecker</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: unique_obj_in_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/iterables.py#L1'>Function: update_dict_in_dict</a>
└─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/78e5714/generallibrary/functions.py#L1'>Function: wrapper_transfer</a>
</pre>

## Todo
| Module                                                                                                                      | Message                                                                                                                                                           |
|:----------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L1'>versions.py</a>        | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L17'>Use Ver in each part of VerInfo.</a>                        |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/test/test_time.py#L1'>test_time.py</a> | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/test/test_time.py#L33'>Fix time casting to wrong day when past midnight.</a> |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L1'>objinfo.py</a>  | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L19'>Recycle ObjInfo.</a>                                 |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L1'>functions.py</a>      | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L37'>Remove classproperty once 3.8 is no longer supported.</a>  |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L1'>diagram.py</a>          | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L256'>[UnitTest] for Class: Storable</a>                          |

<sup>
Generated 2021-11-29 19:00 CET for commit <a href='https://github.com/ManderaGeneral/generallibrary/commit/78e5714'>78e5714</a>.
</sup>
