# generallibrary
Random useful code categorized into modules.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                            | Ver                                               | Latest Release        | Python                                                                                                                   | Platform        |   Lvl | Todo                                                       | Tests   |
|:-------------------------------------------------------------------|:--------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:-----------------------------------------------------------|:--------|
| [generallibrary](https://github.com/ManderaGeneral/generallibrary) | [2.8.4](https://pypi.org/project/generallibrary/) | 2021-04-17 12:25 CEST | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     0 | [4](https://github.com/ManderaGeneral/generallibrary#Todo) | 99.5 %  |

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
| Command                      | <a href='https://pypi.org/project/packaging'>packaging</a>   | <a href='https://pypi.org/project/pyperclip'>pyperclip</a>   | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/tabulate'>tabulate</a>   | <a href='https://pypi.org/project/pytz'>pytz</a>   |
|:-----------------------------|:-------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------------------|:-----------------------------------------------------------|:---------------------------------------------------|
| `pip install generallibrary` | Yes                                                          | Yes                                                          | Yes                                                    | Yes                                                        | Yes                                                |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/__init__.py#L1'>Module: generallibrary</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L550'>Class: AutoInitBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L417'>Class: CallTable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L463'>Method: generate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L467'>Method: generate_with_args</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L471'>Method: generate_with_funcs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L430'>Method: set_args</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L425'>Method: set_funcs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L28'>Class: CodeLine</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L46'>Method: get_lines</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L60'>Method: text</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L58'>Class: Date</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L80'>Method: get_timezone_obj</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L84'>Method: now</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L408'>Class: EmptyContext</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L134'>Class: EnvVar</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L146'>Property: value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L185'>Class: HierarchyStorer</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L482'>Class: Markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L550'>Method: add_code_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L519'>Method: add_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L545'>Method: add_list_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L556'>Method: add_pre_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L536'>Method: add_table_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L525'>Method: get_all_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L512'>Method: get_section_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L495'>Method: link</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L561'>Method: wrap_with_tags</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L441'>Class: NetworkDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L464'>Method: get_spouse</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L449'>Method: get_spouses</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L13'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L13'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L123'>Method: add_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/parents.py#L59'>Method: check_if_parent_eligible</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L203'>Method: disconnect</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L113'>Method: doc</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L53'>Method: file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L28'>Method: from_base</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L21'>Method: from_builtin</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L36'>Method: from_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L42'>Method: from_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L49'>Method: from_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L214'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L143'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L304'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L88'>Method: get_definition_line</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L98'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L100'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L169'>Method: get_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L342'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L231'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L195'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L82'>Method: get_origin</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L156'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L323'>Method: get_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L182'>Method: get_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L359'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L56'>Method: identifier</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L18'>Method: internal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L34'>Method: is_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L28'>Method: is_function</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L50'>Method: is_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L59'>Method: is_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L22'>Method: is_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L44'>Method: is_property</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L44'>Method: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L72'>Method: print_link_to_obj</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L27'>Method: private</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L35'>Method: protected</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L10'>Method: public</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L132'>Method: remove_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L108'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L279'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/parents.py#L7'>Method: spawn_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L8'>Method: type</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L393'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L314'>Class: Operators</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L325'>Method: deco_define_comparisons</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L210'>Class: PythonVersion</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L216'>Property: version</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L557'>Class: Recycle</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L592'>Method: recycle_clear</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L597'>Method: recycle_clear_all</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L43'>Class: SigInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L247'>Method: call</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L66'>Property: callableObject</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L70'>Method: class_from_callable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L160'>Property: defaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L202'>Method: getIndexFromName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L128'>Property: leadingArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L108'>Property: names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L118'>Property: namesRequired</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L113'>Property: namesWithoutDefaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L123'>Property: namesWithoutPacked</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L209'>Property: packedArgs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L146'>Property: packedArgsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L214'>Property: packedKwargs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L153'>Property: packedKwargsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L103'>Property: parameters</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L186'>Property: positionalArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L170'>Property: positionalOnlyArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L179'>Property: positionalOnlyOppositeArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L194'>Property: positionalOppositeArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L93'>Property: positional_extra</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L219'>Property: unpackedArgs</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L230'>Property: unpackedKwargs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L5'>Class: SortedList</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L32'>Method: add</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L49'>Method: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L12'>Class: Timer</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L38'>Method: deco</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L31'>Method: print</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L20'>Method: reset</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L27'>Method: seconds</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L386'>Class: TreeDiagram</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L393'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L15'>Class: Ver</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L21'>Method: bump</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L198'>Class: VerInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L162'>Property: caseSensitive</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L176'>Property: pathDelimiter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L190'>Property: pathRootHasColon</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L183'>Property: pathRootIsDelimiter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L169'>Property: positionalArgument</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L124'>Property: pythonAlpha</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L129'>Property: pythonBeta</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L134'>Property: pythonCandidate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L139'>Property: pythonFinal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L93'>Property: pythonMajor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L103'>Property: pythonMicro</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L98'>Property: pythonMinor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L144'>Property: pythonReleaseKeyword</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L108'>Property: pythonReleaseLevel</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L114'>Property: pythonSerial</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L119'>Property: pythonSerialString</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L149'>Property: pythonString</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L154'>Property: pythonVersion</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L109'>Function: cache_clear</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L270'>Function: calculate</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L23'>Function: ceil</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L28'>Function: clamp</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L29'>Class: classproperty</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L10'>Function: clipboard_copy</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L23'>Function: clipboard_get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L293'>Function: combine</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/text.py#L5'>Function: comma_and_and</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L105'>Function: confineTo</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L66'>Function: debug</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L377'>Function: deco_bound_defaults</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L22'>Function: deco_cache</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L347'>Function: deco_cast_parameters</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L397'>Function: deco_extend</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L485'>Function: deco_propagate_while</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L293'>Function: defaults</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L91'>Function: depth</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L85'>Function: doubleRectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L261'>Function: exclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L122'>Function: extend_list_in_dict</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L324'>Function: flatten</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L18'>Function: floor</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L167'>Function: get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L162'>Function: getBaseClassNames</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L132'>Function: getBaseClasses</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L138'>Function: get_definition_line</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L146'>Function: get_free_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L182'>Function: get_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L222'>Function: get_installed_packages</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L78'>Function: get_items</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L166'>Function: get_launch_options</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L94'>Function: get_origin</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L228'>Function: get_rows</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L70'>Function: get_values</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/object.py#L8'>Function: getsize</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L174'>Function: hasMethod</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L82'>Function: hook</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L14'>Function: import_module</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L266'>Function: inclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L502'>Function: initBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L59'>Function: inrange</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L86'>Function: is_iterable</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L106'>Function: iter_first_value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L117'>Function: join_with_str</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/text.py#L38'>Function: match</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L227'>Function: package_is_installed</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L318'>Function: pivot_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/text.py#L17'>Function: plur_sing</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L115'>Function: print_link</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L129'>Function: print_link_to_obj</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L73'>Function: rectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L194'>Function: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L283'>Function: remove_duplicates</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/text.py#L28'>Function: replace</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L42'>Function: sign</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L50'>Function: sleep</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L307'>Function: split_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L5'>Function: strToDynamicType</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L104'>Function: typeChecker</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L271'>Function: unique_obj_in_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L134'>Function: update_dict_in_dict</a>
└─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L476'>Function: wrapper_transfer</a>
</pre>

## Todo
| Module                                                                                                                     | Message                                                                                                                                                          |
|:---------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L1'>objinfo.py</a> | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L18'>Recycle ObjInfo.</a>                                |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L1'>versions.py</a>       | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L17'>Use Ver in each part of VerInfo.</a>                       |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L1'>functions.py</a>     | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L35'>Remove classproperty once 3.8 is no longer supported.</a> |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L1'>functions.py</a>     | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L14'>UnitTest for Function: import_module</a>                  |

<sup>
Generated 2021-04-17 12:25 CEST for commit <a href='https://github.com/ManderaGeneral/generallibrary/commit/75df3da'>75df3da</a>.
</sup>
