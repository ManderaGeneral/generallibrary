# generallibrary
Random useful code categorized into modules.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                            | Ver                                               | Latest Release       | Python                                                                                                                   | Platform        |   Lvl | Todo                                                       | Tests   |
|:-------------------------------------------------------------------|:--------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:-----------------------------------------------------------|:--------|
| [generallibrary](https://github.com/ManderaGeneral/generallibrary) | [2.8.7](https://pypi.org/project/generallibrary/) | 2021-11-03 10:46 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     0 | [4](https://github.com/ManderaGeneral/generallibrary#Todo) | 99.5 %  |

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
<a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/__init__.py#L1'>Module: generallibrary</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L558'>Class: AutoInitBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L424'>Class: CallTable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L470'>Method: generate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L474'>Method: generate_with_args</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L478'>Method: generate_with_funcs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L437'>Method: set_args</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L432'>Method: set_funcs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L28'>Class: CodeLine</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L46'>Method: get_lines</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L60'>Method: text</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L58'>Class: Date</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L80'>Method: get_timezone_obj</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L84'>Method: now</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L415'>Class: EmptyContext</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L139'>Class: EnvVar</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L151'>Property: value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/types.py#L185'>Class: HierarchyStorer</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L600'>Class: Markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L668'>Method: add_code_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L637'>Method: add_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L663'>Method: add_list_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L674'>Method: add_pre_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L654'>Method: add_table_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L643'>Method: get_all_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L630'>Method: get_section_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L613'>Method: link</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L679'>Method: wrap_with_tags</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L559'>Class: NetworkDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L582'>Method: get_spouse</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L567'>Method: get_spouses</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/objinfo.py#L14'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/objinfo.py#L14'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L125'>Method: add_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/parents.py#L59'>Method: check_if_parent_eligible</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L139'>Method: defined_by_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L205'>Method: disconnect</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L114'>Method: doc</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L54'>Method: file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/origin.py#L28'>Method: from_base</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/origin.py#L21'>Method: from_builtin</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/origin.py#L36'>Method: from_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/origin.py#L51'>Method: from_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/origin.py#L58'>Method: from_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L216'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L145'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L422'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L89'>Method: get_definition_line</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L100'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L101'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L171'>Method: get_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L460'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L233'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L197'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L83'>Method: get_origin</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L158'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L441'>Method: get_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L184'>Method: get_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L477'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/objinfo.py#L57'>Method: identifier</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L19'>Method: internal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/type.py#L34'>Method: is_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/type.py#L28'>Method: is_function</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/type.py#L50'>Method: is_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/type.py#L59'>Method: is_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/type.py#L22'>Method: is_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/type.py#L44'>Method: is_property</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L45'>Method: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L73'>Method: print_link_to_obj</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L28'>Method: private</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L36'>Method: protected</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/properties.py#L11'>Method: public</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L134'>Method: remove_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L110'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L397'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/parents.py#L7'>Method: spawn_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/type.py#L8'>Method: type</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L511'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L317'>Class: Operators</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L328'>Method: deco_define_comparisons</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L210'>Class: PythonVersion</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L216'>Property: version</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L565'>Class: Recycle</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L601'>Method: recycle_clear</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L606'>Method: recycle_clear_all</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L45'>Class: SigInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L249'>Method: call</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L68'>Property: callableObject</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L72'>Method: class_from_callable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L162'>Property: defaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L204'>Method: getIndexFromName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L130'>Property: leadingArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L110'>Property: names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L120'>Property: namesRequired</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L115'>Property: namesWithoutDefaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L125'>Property: namesWithoutPacked</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L211'>Property: packedArgs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L148'>Property: packedArgsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L216'>Property: packedKwargs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L155'>Property: packedKwargsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L105'>Property: parameters</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L188'>Property: positionalArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L172'>Property: positionalOnlyArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L181'>Property: positionalOnlyOppositeArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L196'>Property: positionalOppositeArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L95'>Property: positional_extra</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L221'>Property: unpackedArgs</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L232'>Property: unpackedKwargs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L5'>Class: SortedList</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L32'>Method: add</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L49'>Method: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L256'>Class: Storable</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L266'>Method: copy_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L261'>Method: load_node</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L258'>Method: save_node</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L12'>Class: Timer</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L38'>Method: deco</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L31'>Method: print</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L20'>Method: reset</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L27'>Method: seconds</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L504'>Class: TreeDiagram</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/diagram.py#L511'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L15'>Class: Ver</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L21'>Method: bump</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L198'>Class: VerInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L162'>Property: caseSensitive</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L176'>Property: pathDelimiter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L190'>Property: pathRootHasColon</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L183'>Property: pathRootIsDelimiter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L169'>Property: positionalArgument</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L124'>Property: pythonAlpha</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L129'>Property: pythonBeta</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L134'>Property: pythonCandidate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L139'>Property: pythonFinal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L93'>Property: pythonMajor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L103'>Property: pythonMicro</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L98'>Property: pythonMinor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L144'>Property: pythonReleaseKeyword</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L108'>Property: pythonReleaseLevel</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L114'>Property: pythonSerial</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L119'>Property: pythonSerialString</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L149'>Property: pythonString</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L154'>Property: pythonVersion</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/objinfo.py#L116'>Function: cache_clear</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L273'>Function: calculate</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L23'>Function: ceil</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L28'>Function: clamp</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L31'>Class: classproperty</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L10'>Function: clipboard_copy</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L23'>Function: clipboard_get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L291'>Function: combine</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/text.py#L5'>Function: comma_and_and</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L110'>Function: confineTo</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L66'>Function: debug</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L384'>Function: deco_bound_defaults</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L24'>Function: deco_cache</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L350'>Function: deco_cast_parameters</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L404'>Function: deco_extend</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L492'>Function: deco_propagate_while</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L296'>Function: defaults</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L91'>Function: depth</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L334'>Function: dict_insert</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L85'>Function: doubleRectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L261'>Function: exclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L122'>Function: extend_list_in_dict</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L319'>Function: flatten</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L18'>Function: floor</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L167'>Function: get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/types.py#L162'>Function: getBaseClassNames</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/types.py#L132'>Function: getBaseClasses</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L143'>Function: get_definition_line</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L146'>Function: get_free_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L182'>Function: get_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L222'>Function: get_installed_packages</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L78'>Function: get_items</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L171'>Function: get_launch_options</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L98'>Function: get_origin</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L228'>Function: get_rows</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L70'>Function: get_values</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/object.py#L8'>Function: getsize</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/types.py#L174'>Function: hasMethod</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/objinfo/objinfo.py#L83'>Function: hook</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L16'>Function: import_module</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L266'>Function: inclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L509'>Function: initBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L59'>Function: inrange</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L86'>Function: is_iterable</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L106'>Function: iter_first_value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L117'>Function: join_with_str</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/text.py#L38'>Function: match</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/versions.py#L227'>Function: package_is_installed</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L314'>Function: pivot_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/text.py#L17'>Function: plur_sing</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L119'>Function: print_link</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/code.py#L134'>Function: print_link_to_obj</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L73'>Function: rectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L194'>Function: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L282'>Function: remove_duplicates</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/text.py#L28'>Function: replace</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/values.py#L42'>Function: sign</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/time.py#L50'>Function: sleep</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L304'>Function: split_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/types.py#L5'>Function: strToDynamicType</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L326'>Function: subtract_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L611'>Function: terminal</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/types.py#L104'>Function: typeChecker</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L271'>Function: unique_obj_in_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/iterables.py#L134'>Function: update_dict_in_dict</a>
└─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/f2ec73e/generallibrary/functions.py#L483'>Function: wrapper_transfer</a>
</pre>

## Todo
| Module                                                                                                                     | Message                                                                                                                                                          |
|:---------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L1'>versions.py</a>       | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L17'>Use Ver in each part of VerInfo.</a>                       |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L1'>functions.py</a>     | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L37'>Remove classproperty once 3.8 is no longer supported.</a> |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L1'>objinfo.py</a> | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L19'>Recycle ObjInfo.</a>                                |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L1'>diagram.py</a>         | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L256'>[UnitTest] for Class: Storable</a>                         |

<sup>
Generated 2021-11-03 10:46 CET for commit <a href='https://github.com/ManderaGeneral/generallibrary/commit/f2ec73e'>f2ec73e</a>.
</sup>
