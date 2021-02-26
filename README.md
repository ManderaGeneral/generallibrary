# generallibrary
Random useful code categorized into modules.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                            | Ver                                             | Latest Release       | Python                                                                                                                   | Platform        |   Lvl | Todo                                                       | Tests   |
|:-------------------------------------------------------------------|:------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:-----------------------------------------------------------|:--------|
| [generallibrary](https://github.com/ManderaGeneral/generallibrary) | [2.8](https://pypi.org/project/generallibrary/) | 2021-02-26 15:47 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     0 | [4](https://github.com/ManderaGeneral/generallibrary#Todo) | 88.7 %  |

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
<a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/__init__.py#L1'>Module: generallibrary</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L530'>Class: AutoInitBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L397'>Class: CallTable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L443'>Method: generate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L447'>Method: generate_with_args</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L451'>Method: generate_with_funcs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L410'>Method: set_args</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L405'>Method: set_funcs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L28'>Class: CodeLine</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L138'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L269'>Method: copy_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L244'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L204'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L153'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L312'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L113'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L40'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L173'>Method: get_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L342'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L219'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L193'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L388'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L327'>Method: get_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L183'>Method: get_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L357'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L265'>Method: load_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L147'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L255'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L262'>Method: save_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L123'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L283'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L54'>Method: text</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L394'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L388'>Class: EmptyContext</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L134'>Class: EnvVar</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L146'>Property: value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/types.py#L185'>Class: HierarchyStorer</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L478'>Class: Markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L138'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L540'>Method: add_code_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L509'>Method: add_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L535'>Method: add_list_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L546'>Method: add_pre_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L526'>Method: add_table_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L269'>Method: copy_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L244'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L204'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L515'>Method: get_all_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L153'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L312'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L113'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L173'>Method: get_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L342'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L219'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L193'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L388'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L327'>Method: get_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L502'>Method: get_section_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L183'>Method: get_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L357'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L485'>Method: link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L265'>Method: load_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L147'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L255'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L262'>Method: save_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L123'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L283'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L394'>Method: view</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L551'>Method: wrap_with_tags</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L442'>Class: NetworkDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L138'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L269'>Method: copy_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L244'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L204'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L153'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L312'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L113'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L173'>Method: get_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L342'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L219'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L193'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L163'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L327'>Method: get_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L183'>Method: get_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L357'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L463'>Method: get_spouse</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L450'>Method: get_spouses</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L265'>Method: load_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L147'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L255'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L262'>Method: save_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L123'>Method: set_index</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L283'>Method: set_parent</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/objinfo.py#L13'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/objinfo.py#L13'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L138'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/parents.py#L80'>Method: check_if_parent_eligible</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L269'>Method: copy_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L244'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L99'>Method: doc</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L46'>Method: file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/children.py#L11'>Method: filters_check</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/origin.py#L25'>Method: from_base</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/origin.py#L19'>Method: from_builtin</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/origin.py#L33'>Method: from_class</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/origin.py#L39'>Method: from_instance</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L204'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/children.py#L18'>Method: get_attrs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L153'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L312'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L77'>Method: get_definition_line</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L113'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L85'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L173'>Method: get_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L342'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L219'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L193'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L71'>Method: get_origin</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L388'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L327'>Method: get_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L183'>Method: get_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L357'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/objinfo.py#L35'>Method: identifier</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L17'>Method: internal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/type.py#L34'>Method: is_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/type.py#L28'>Method: is_function</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/type.py#L50'>Method: is_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/type.py#L59'>Method: is_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/type.py#L22'>Method: is_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/type.py#L44'>Method: is_property</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L265'>Method: load_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L468'>Method: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/objinfo.py#L41'>Method: nice_repr</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L61'>Method: print_link_to_obj</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L25'>Method: private</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L32'>Method: protected</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/properties.py#L10'>Method: public</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L147'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/objinfo.py#L31'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L262'>Method: save_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L123'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L283'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/type.py#L8'>Method: type</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L394'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L302'>Class: Operators</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L313'>Method: deco_define_comparisons</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L209'>Class: PythonVersion</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L215'>Property: version</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L28'>Class: SigInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L231'>Method: call</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L51'>Property: callableObject</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L55'>Method: class_from_callable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L144'>Property: defaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L186'>Method: getIndexFromName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L112'>Property: leadingArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L92'>Property: names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L102'>Property: namesRequired</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L97'>Property: namesWithoutDefaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L107'>Property: namesWithoutPacked</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L193'>Property: packedArgs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L130'>Property: packedArgsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L198'>Property: packedKwargs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L137'>Property: packedKwargsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L87'>Property: parameters</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L170'>Property: positionalArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L154'>Property: positionalOnlyArgNames</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L163'>Property: positionalOnlyOppositeArgNames</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L178'>Property: positionalOppositeArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L78'>Property: positional_extra</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L203'>Property: unpackedArgs</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L214'>Property: unpackedKwargs</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L3'>Class: SortedList</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L30'>Method: add</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L47'>Method: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/time.py#L7'>Class: Timer</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/time.py#L26'>Method: print</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/time.py#L15'>Method: reset</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/time.py#L22'>Method: seconds</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L381'>Class: TreeDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L138'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L269'>Method: copy_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L244'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L204'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L153'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L312'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L113'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L173'>Method: get_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L342'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L219'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L193'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L388'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L327'>Method: get_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L183'>Method: get_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L357'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L265'>Method: load_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L147'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L255'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L262'>Method: save_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L123'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L283'>Method: set_parent</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L394'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L15'>Class: Ver</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L21'>Method: bump</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L197'>Class: VerInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L161'>Property: caseSensitive</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L63'>Property: java</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L53'>Property: linux</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L58'>Property: mac</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L68'>Property: os</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L175'>Property: pathDelimiter</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L189'>Property: pathRootHasColon</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L182'>Property: pathRootIsDelimiter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L168'>Property: positionalArgument</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L123'>Property: pythonAlpha</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L128'>Property: pythonBeta</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L133'>Property: pythonCandidate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L138'>Property: pythonFinal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L92'>Property: pythonMajor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L102'>Property: pythonMicro</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L97'>Property: pythonMinor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L143'>Property: pythonReleaseKeyword</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L107'>Property: pythonReleaseLevel</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L113'>Property: pythonSerial</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L118'>Property: pythonSerialString</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L148'>Property: pythonString</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L153'>Property: pythonVersion</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L48'>Property: windows</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L256'>Function: calculate</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L23'>Function: ceil</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L28'>Function: clamp</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L15'>Class: classproperty</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L10'>Function: clipboard_copy</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L23'>Function: clipboard_get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L266'>Function: combine</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/text.py#L3'>Function: comma_and_and</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L105'>Function: confineTo</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/time.py#L40'>Function: current_datetime</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/time.py#L45'>Function: current_datetime_formatted</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L63'>Function: debug</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L9'>Function: deco_cache</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L340'>Function: deco_cast_parameters</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L358'>Function: deco_default_self_args</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L377'>Function: deco_extend</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L465'>Function: deco_propagate_while</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L281'>Function: defaults</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L89'>Function: depth</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L85'>Function: doubleRectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L238'>Function: exclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L120'>Function: extend_list_in_dict</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L18'>Function: floor</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L165'>Function: get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/types.py#L162'>Function: getBaseClassNames</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/types.py#L132'>Function: getBaseClasses</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L135'>Function: get_definition_line</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L144'>Function: get_free_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L180'>Function: get_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L227'>Function: get_installed_packages</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L76'>Function: get_items</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L165'>Function: get_launch_options</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L91'>Function: get_origin</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L205'>Function: get_rows</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L68'>Function: get_values</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/object.py#L8'>Function: getsize</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/types.py#L174'>Function: hasMethod</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/objinfo.py#L57'>Function: hook</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L243'>Function: inclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L483'>Function: initBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L59'>Function: inrange</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L84'>Function: is_iterable</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L104'>Function: iter_first_value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L115'>Function: join_with_str</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L232'>Function: package_is_installed</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L291'>Function: pivot_list</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/text.py#L15'>Function: plur_sing</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L112'>Function: print_link</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/code.py#L126'>Function: print_link_to_obj</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L73'>Function: rectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L260'>Function: remove_duplicates</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/values.py#L42'>Function: sign</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/time.py#L33'>Function: sleep</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L280'>Function: split_list</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/types.py#L5'>Function: strToDynamicType</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/types.py#L104'>Function: typeChecker</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L248'>Function: unique_obj_in_list</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/iterables.py#L132'>Function: update_dict_in_dict</a>
└─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/functions.py#L456'>Function: wrapper_transfer</a> <b>(Untested)</b>
</pre>

## Todo
| Module                                                                                                                      | Message                                                                                                                                                                 |
|:----------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L1'>versions.py</a>       | <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/versions.py#L17'>Use Ver in each part of VerInfo.</a>                             |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L1'>diagram.py</a>         | <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L68'>Generalize _deco_cast_to_diagram()</a>                            |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L1'>diagram.py</a>         | <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/diagram.py#L76'>wrapper_transfer for every deco</a>                               |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/objinfo.py#L1'>objinfo.py</a> | <a href='https://github.com/ManderaGeneral/generallibrary/blob/34af811/generallibrary/objinfo/objinfo.py#L17'>Disable save, load and copy of ObjInfo's TreeDiagram.</a> |

<sup>
Generated 2021-02-26 15:48 CET for commit <a href='https://github.com/ManderaGeneral/generallibrary/commit/34af811'>34af811</a>.
</sup>
