# generallibrary 2.5.14
Random useful code categorized into modules.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                            | Version                                            | Latest Release       | Python                                                                                                                   | Platform        |
|:-------------------------------------------------------------------|:---------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|
| [generallibrary](https://github.com/ManderaGeneral/generallibrary) | [2.5.14](https://pypi.org/project/generallibrary/) | 2021-02-04 17:13 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |

## Contents
<pre>
<a href='#generallibrary-2.5.14'>generallibrary 2.5.14</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todo-(23x)'>Todo (23x)</a>
</pre>

## Installation
| Command                      | <a href='https://pypi.org/project/packaging'>packaging</a>   | <a href='https://pypi.org/project/pyperclip'>pyperclip</a>   | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/tabulate'>tabulate</a>   | <a href='https://pypi.org/project/pytz'>pytz</a>   |
|:-----------------------------|:-------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------------------|:-----------------------------------------------------------|:---------------------------------------------------|
| `pip install generallibrary` | Yes                                                          | Yes                                                          | Yes                                                    | Yes                                                        | Yes                                                |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/__init__.py#L1'>Module: generallibrary</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L399'>Class: CallTable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L445'>Method: generate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L449'>Method: generate_with_args</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L453'>Method: generate_with_funcs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L412'>Method: set_args</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L407'>Method: set_funcs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/code.py#L31'>Class: CodeLine</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L259'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L431'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L236'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L353'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L311'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L337'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L347'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L331'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L343'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L395'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/code.py#L43'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L387'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L322'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L391'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L371'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L232'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L228'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L227'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L233'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L231'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L230'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L229'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L234'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L415'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L306'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L477'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L408'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L400'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L269'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/code.py#L57'>Method: text</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L435'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L390'>Class: EmptyContext</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/values.py#L108'>Class: EnvVar</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/types_.py#L183'>Class: HierarchyStorer</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L496'>Class: Markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L259'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L552'>Method: add_code_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L532'>Method: add_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L566'>Method: add_list_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L572'>Method: add_pre_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L557'>Method: add_table_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L541'>Method: all_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L431'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L236'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L353'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L311'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L337'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L347'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L331'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L343'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L395'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L387'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L322'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L391'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L371'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L232'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L228'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L227'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L233'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L231'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L230'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L229'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L234'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L507'>Method: link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L415'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L306'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L477'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L408'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L525'>Method: section_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L400'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L269'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L435'>Method: view</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L577'>Method: wrap_with_tags</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L128'>Class: NetworkDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L138'>Method: get_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L154'>Method: get_links</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L160'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L90'>Method: get_nodes_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L97'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L118'>Method: get_ordered_flat</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L166'>Method: get_routes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L145'>Method: link</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L121'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/objinfo.py#L14'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/objinfo.py#L14'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L259'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/parents.py#L69'>Method: check_if_parent_eligible</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L431'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L236'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L66'>Method: doc</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/children.py#L11'>Method: filters_check</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/origin.py#L25'>Method: from_base</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/origin.py#L19'>Method: from_builtin</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/origin.py#L33'>Method: from_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/origin.py#L39'>Method: from_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L353'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L311'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/children.py#L18'>Method: get_attrs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L337'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L347'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L331'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L343'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L50'>Method: get_definition_line</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L395'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L58'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L387'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L322'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L391'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L371'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L232'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/parents.py#L7'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L227'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L233'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L231'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/parents.py#L89'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L229'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L234'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/objinfo.py#L40'>Method: identifier</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L13'>Method: internal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/type.py#L33'>Method: is_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/type.py#L27'>Method: is_function</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/type.py#L49'>Method: is_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/type.py#L58'>Method: is_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/type.py#L21'>Method: is_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/type.py#L43'>Method: is_property</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L415'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L35'>Method: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/objinfo.py#L46'>Method: nice_repr</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L41'>Method: print_link_to_obj</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L21'>Method: private</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L28'>Method: protected</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/properties.py#L6'>Method: public</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L306'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/objinfo.py#L36'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L408'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L400'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L269'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/objinfo/type.py#L8'>Method: type</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L435'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L303'>Class: Operators</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L313'>Method: deco_define_comparisons</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/versions.py#L206'>Class: PythonVersion</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L26'>Class: SigInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L232'>Method: call</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L56'>Method: class_from_callable</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L187'>Method: getIndexFromName</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/iterables.py#L3'>Class: SortedList</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/iterables.py#L32'>Method: add</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/iterables.py#L49'>Method: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/time.py#L7'>Class: Timer</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/time.py#L26'>Method: print</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/time.py#L15'>Method: reset</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/time.py#L22'>Method: seconds</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L198'>Class: TreeDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L259'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L431'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L236'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L353'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L311'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L337'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L347'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L331'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L343'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L395'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L387'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L322'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L391'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L371'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L232'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L228'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L227'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L233'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L231'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L230'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L229'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L234'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L415'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L306'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L477'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L408'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L400'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L269'>Method: set_parent</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/diagram.py#L435'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/versions.py#L16'>Class: Ver</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/versions.py#L20'>Method: bump</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/versions.py#L192'>Class: VerInfo</a>
└─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/888bb5b/generallibrary/functions.py#L13'>Class: classproperty</a>
</pre>

## Todo (23x)
| Module             | Message                                                                                   |
|:-------------------|:------------------------------------------------------------------------------------------|
| functions.py       | Add caching for SigInfo's signature methods                                               |
| functions.py       | Test deco\_extend with int and str.                                                        |
| versions.py        | Replace this temporary Ver class with revamped VerInfo split into isolated parts.         |
| diagram.py         | Tests for NetworkDiagram.                                                                 |
| diagram.py         | Storable NetworkDiagram.                                                                  |
| diagram.py         | Moveable NetworkDiagram.                                                                  |
| diagram.py         | Transform Network to and from Tree if possible.                                           |
| diagram.py         | Remove or hide Network route methods.                                                     |
| diagram.py         | Idea: Make TreeDiagram loadable with a generic list of lists for example.                 |
| diagram.py         | Removable keys.                                                                           |
| diagram.py         | Create Markdown tree from markdown text.                                                  |
| diagram.py         | Tests for Markdown.                                                                       |
| diagram.py         | Split line in lines with \n.                                                              |
| types\_.py          | TnD                                                                                       |
| code.py            | Search for old CodeGen and replace.                                                       |
| code.py            | Maybe put (parts of?) this directly in TreeDiagram.                                       |
| code.py            | Refactor link methods to ObjInfo.                                                         |
| subsets\_methods.py | Subset methods for ObjInfo.is\_method().                                                   |
| children.py        | Define TreeDiagram.\_\_iter\_\_ as well, but without generation.                              |
| objinfo.py         | Module tree for ObjInfo.                                                                  |
| objinfo.py         | Another type of diagram for ObjInfo as an object can be an attribute of multiple objects. |
| objinfo.py         | Tests for ObjInfo.                                                                        |
| objinfo.py         | Disable save, load and copy.                                                              |

<sup>
Generated 2021-02-05 12:08 CET for commit <a href='https://github.com/ManderaGeneral/generallibrary/commit/888bb5b'>888bb5b</a>.
</sup>
