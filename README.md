# generallibrary
Random useful code categorized into modules.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                            | Ver                                             | Latest Release       | Python                                                                                                                   | Platform        | Todo                                                       |   Lvl | Tests   |
|:-------------------------------------------------------------------|:------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|:-----------------------------------------------------------|------:|:--------|
| [generallibrary](https://github.com/ManderaGeneral/generallibrary) | [2.7](https://pypi.org/project/generallibrary/) | 2021-02-09 15:48 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu | [7](https://github.com/ManderaGeneral/generallibrary#Todo) |     0 | 86.1 %  |

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
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/object.py#L81'>Class: AutoInitBases</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L396'>Class: CallTable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L442'>Method: generate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L446'>Method: generate_with_args</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L450'>Method: generate_with_funcs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L409'>Method: set_args</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L404'>Method: set_funcs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L31'>Class: CodeLine</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L275'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L445'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L260'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L365'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L323'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L349'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L359'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L343'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L355'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L407'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L41'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L399'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L334'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L403'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L383'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L251'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L250'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L256'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L254'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L255'>Method: hook_new_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L253'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L252'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L257'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L430'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L318'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L491'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L422'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L414'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L281'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L55'>Method: text</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L449'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L387'>Class: EmptyContext</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L132'>Class: EnvVar</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L144'>Property: value</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L183'>Class: HierarchyStorer</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L509'>Class: Markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L275'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L571'>Method: add_code_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L540'>Method: add_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L566'>Method: add_list_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L577'>Method: add_pre_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L557'>Method: add_table_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L445'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L260'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L365'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L546'>Method: get_all_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L323'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L349'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L359'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L343'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L355'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L407'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L399'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L334'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L403'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L533'>Method: get_section_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L383'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L251'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L250'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L256'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L254'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L255'>Method: hook_new_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L253'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L252'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L257'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L516'>Method: link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L430'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L318'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L491'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L422'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L414'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L281'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L449'>Method: view</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L582'>Method: wrap_with_tags</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L152'>Class: NetworkDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L70'>Class: Link</a> <b>(Untested)</b>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L80'>Method: check_direction</a> <b>(Untested)</b>
│  │  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L76'>Method: other_node</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L10'>Class: Route</a> <b>(Untested)</b>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L14'>Method: get_links</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L24'>Method: is_circular</a> <b>(Untested)</b>
│  │  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L28'>Method: is_uturn</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L37'>Class: RouteGrp</a> <b>(Untested)</b>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L59'>Method: get_active_links</a> <b>(Untested)</b>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L65'>Method: get_connected_nodes</a> <b>(Untested)</b>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L53'>Method: get_links</a>
│  │  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L47'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L161'>Method: get_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L179'>Method: get_links</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L185'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L90'>Method: get_nodes_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L97'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L127'>Method: get_ordered_flat</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L118'>Method: get_ordered_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L191'>Method: get_routes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L168'>Method: link</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L133'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L14'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L14'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L275'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/parents.py#L71'>Method: check_if_parent_eligible</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L445'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L260'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L91'>Method: doc</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L44'>Method: file</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/children.py#L11'>Method: filters_check</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L25'>Method: from_base</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L19'>Method: from_builtin</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L33'>Method: from_class</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/origin.py#L39'>Method: from_instance</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L365'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L323'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/children.py#L18'>Method: get_attrs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L349'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L359'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L343'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L355'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L75'>Method: get_definition_line</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L407'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L83'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L399'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L69'>Method: get_origin</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L334'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L403'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L383'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/parents.py#L7'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L250'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L256'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L254'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L255'>Method: hook_new_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/parents.py#L97'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L252'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L257'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L38'>Method: identifier</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L15'>Method: internal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L33'>Method: is_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L27'>Method: is_function</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L49'>Method: is_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L58'>Method: is_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L21'>Method: is_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L43'>Method: is_property</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L430'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L466'>Method: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L44'>Method: nice_repr</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L59'>Method: print_link_to_obj</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L23'>Method: private</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L30'>Method: protected</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/properties.py#L8'>Method: public</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L318'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L34'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L422'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L414'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L281'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/type.py#L8'>Method: type</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L449'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L301'>Class: Operators</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L312'>Method: deco_define_comparisons</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L211'>Class: PythonVersion</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L217'>Property: version</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L27'>Class: SigInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L230'>Method: call</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L50'>Property: callableObject</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L54'>Method: class_from_callable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L143'>Property: defaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L185'>Method: getIndexFromName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L111'>Property: leadingArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L91'>Property: names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L101'>Property: namesRequired</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L96'>Property: namesWithoutDefaults</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L106'>Property: namesWithoutPacked</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L192'>Property: packedArgs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L129'>Property: packedArgsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L197'>Property: packedKwargs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L136'>Property: packedKwargsName</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L86'>Property: parameters</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L169'>Property: positionalArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L153'>Property: positionalOnlyArgNames</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L162'>Property: positionalOnlyOppositeArgNames</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L177'>Property: positionalOppositeArgNames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L77'>Property: positional_extra</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L202'>Property: unpackedArgs</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L213'>Property: unpackedKwargs</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L3'>Class: SortedList</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L32'>Method: add</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L49'>Method: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L7'>Class: Timer</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L26'>Method: print</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L15'>Method: reset</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L22'>Method: seconds</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L223'>Class: TreeDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L275'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L445'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L260'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L365'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L323'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L349'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L359'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L343'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L355'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L407'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L399'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L334'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L403'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L383'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L251'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L250'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L256'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L254'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L255'>Method: hook_new_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L253'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L252'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L257'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L430'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L318'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L491'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L422'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L414'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L281'>Method: set_parent</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L449'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L15'>Class: Ver</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L21'>Method: bump</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L197'>Class: VerInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L161'>Property: caseSensitive</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L63'>Property: java</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L53'>Property: linux</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L58'>Property: mac</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L68'>Property: os</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L175'>Property: pathDelimiter</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L189'>Property: pathRootHasColon</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L182'>Property: pathRootIsDelimiter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L168'>Property: positionalArgument</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L123'>Property: pythonAlpha</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L128'>Property: pythonBeta</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L133'>Property: pythonCandidate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L138'>Property: pythonFinal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L92'>Property: pythonMajor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L102'>Property: pythonMicro</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L97'>Property: pythonMinor</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L143'>Property: pythonReleaseKeyword</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L107'>Property: pythonReleaseLevel</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L113'>Property: pythonSerial</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L118'>Property: pythonSerialString</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L148'>Property: pythonString</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L153'>Property: pythonVersion</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L48'>Property: windows</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L197'>Function: addToDictInDict</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L179'>Function: extend_list_in_dict</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L255'>Function: calculate</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L21'>Function: ceil</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L26'>Function: clamp</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L14'>Class: classproperty</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L12'>Function: clipboard_copy</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L25'>Function: clipboard_get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L346'>Function: combine</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/text.py#L3'>Function: comma_and_and</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L103'>Function: confineTo</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L40'>Function: current_datetime</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L45'>Function: current_datetime_formatted</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L64'>Function: debug</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L8'>Function: deco_cache</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L339'>Function: deco_cast_parameters</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L357'>Function: deco_default_self_args</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L376'>Function: deco_extend</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L464'>Function: deco_propagate_while</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L280'>Function: defaults</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L117'>Function: depth</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L131'>Function: dictFirstValue</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L243'>Function: get_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L83'>Function: doubleRectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L304'>Function: exclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L16'>Function: floor</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L62'>Function: get</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L160'>Function: getBaseClassNames</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L130'>Function: getBaseClasses</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L214'>Function: get_free_index</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L77'>Function: getIterable</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L269'>Function: get_rows</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L136'>Function: get_definition_line</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L228'>Function: get_installed_packages</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L163'>Function: get_launch_options</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L142'>Function: get_lines</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L92'>Function: get_origin</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/object.py#L8'>Function: getsize</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L172'>Function: hasMethod</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L313'>Function: inclusive</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/object.py#L35'>Function: initBases</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L57'>Function: inrange</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L108'>Function: isIterable</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L146'>Function: iterFirstValue</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L164'>Function: joinWithStr</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L232'>Function: package_is_installed</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/text.py#L15'>Function: plur_sing</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L113'>Function: print_link</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/code.py#L127'>Function: print_link_to_obj</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L71'>Function: rectify</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L340'>Function: remove_duplicates</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/values.py#L40'>Function: sign</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/time.py#L33'>Function: sleep</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L3'>Function: strToDynamicType</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/types.py#L102'>Function: typeChecker</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/iterables.py#L322'>Function: unique_obj_in_list</a>
└─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/functions.py#L455'>Function: wrapper_transfer</a> <b>(Untested)</b>
</pre>

## Todo
| Module                                                                                                                     | Message                                                                                                                                                                |
|:---------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/randomtesting.py#L1'>randomtesting.py</a>            | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/randomtesting.py#L15'>Generalize _traverse_depth()</a>                                           |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/randomtesting.py#L1'>randomtesting.py</a>            | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/randomtesting.py#L62'>Generalize _deco_cast_to_diagram()</a>                                     |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/randomtesting.py#L1'>randomtesting.py</a>            | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/randomtesting.py#L70'>wrapper_transfer for every deco</a>                                        |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L1'>diagram.py</a>         | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L154'>Storable and moveable NetworkDiagram.</a>                        |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L1'>diagram.py</a>         | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/diagram.py#L155'>Transform Network to and from Tree if possible.</a>              |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L1'>versions.py</a>       | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/versions.py#L17'>Use Ver in each part of VerInfo.</a>                             |
| <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L1'>objinfo.py</a> | <a href='https://github.com/ManderaGeneral/generallibrary/blob/master/generallibrary/objinfo/objinfo.py#L18'>Disable save, load and copy of ObjInfo's TreeDiagram.</a> |

<sup>
Generated 2021-02-19 10:32 CET for commit <a href='https://github.com/ManderaGeneral/generallibrary/commit/master'>master</a>.
</sup>
