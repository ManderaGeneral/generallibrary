# generallibrary
Random useful code categorized into modules.

[![workflow Actions Status](https://github.com/ManderaGeneral/generallibrary/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/generallibrary/actions)
![GitHub last commit](https://img.shields.io/github/last-commit/ManderaGeneral/generallibrary)
[![PyPI version shields.io](https://img.shields.io/pypi/v/generallibrary.svg)](https://pypi.org/project/generallibrary/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/generallibrary.svg)](https://pypi.python.org/pypi/generallibrary/)
[![Generic badge](https://img.shields.io/badge/platforms-windows%20%7C%20ubuntu-blue.svg)](https://shields.io/)

## Contents
<pre>
<a href='#generallibrary'>generallibrary</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todos'>Todos</a>
</pre>

## Installation
| Command                      | <a href='https://pypi.org/project/packaging'>packaging</a>   | <a href='https://pypi.org/project/pyperclip'>pyperclip</a>   | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/tabulate'>tabulate</a>   | <a href='https://pypi.org/project/pytz'>pytz</a>   |
|:-----------------------------|:-------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------------------|:-----------------------------------------------------------|:---------------------------------------------------|
| `pip install generallibrary` | Yes                                                          | Yes                                                          | Yes                                                    | Yes                                                        | Yes                                                |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/__init__.py#L1'>Module: generallibrary</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L398'>Class: CallTable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L444'>Method: generate</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L448'>Method: generate_with_args</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L452'>Method: generate_with_funcs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L411'>Method: set_args</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L406'>Method: set_funcs</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/code.py#L30'>Class: CodeLine</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L251'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L423'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L228'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L345'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L303'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L329'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L339'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L323'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L335'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L387'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/code.py#L43'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L379'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L314'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L383'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L363'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L224'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L220'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L219'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L225'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L223'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L222'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L221'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L226'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L407'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L298'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L469'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L400'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L392'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L261'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/code.py#L57'>Method: text</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L427'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L389'>Class: EmptyContext</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/values.py#L108'>Class: EnvVar</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/types_.py#L183'>Class: HierarchyStorer</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L487'>Class: Markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L251'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L544'>Method: add_code_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L524'>Method: add_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L554'>Method: add_list_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L560'>Method: add_pre_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L549'>Method: add_table_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L533'>Method: all_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L423'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L228'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L345'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L303'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L329'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L339'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L323'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L335'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L387'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L379'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L314'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L383'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L363'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L224'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L220'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L219'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L225'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L223'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L222'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L221'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L226'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L499'>Method: link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L407'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L298'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L469'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L400'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L517'>Method: section_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L392'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L261'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L427'>Method: view</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L565'>Method: wrap_with_tags</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L121'>Class: NetworkDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L130'>Method: get_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L146'>Method: get_links</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L152'>Method: get_nodes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L90'>Method: get_ordered</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L111'>Method: get_ordered_flat</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L158'>Method: get_routes</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L137'>Method: link</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L114'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/objinfo.py#L13'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/objinfo.py#L13'>Class: ObjInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L251'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/parents.py#L69'>Method: check_if_parent_eligible</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L423'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L228'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L66'>Method: doc</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/children.py#L11'>Method: filters_check</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/origin.py#L25'>Method: from_base</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/origin.py#L19'>Method: from_builtin</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/origin.py#L33'>Method: from_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/origin.py#L39'>Method: from_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L345'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L303'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/children.py#L18'>Method: get_attrs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L329'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L339'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L323'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L335'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L50'>Method: get_definition_line</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L387'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L58'>Method: get_lines</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L379'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L314'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L383'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L363'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L224'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/parents.py#L7'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L219'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L225'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L223'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/parents.py#L89'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L221'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L226'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/objinfo.py#L40'>Method: identifier</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L13'>Method: internal</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/type.py#L33'>Method: is_class</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/type.py#L27'>Method: is_function</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/type.py#L49'>Method: is_instance</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/type.py#L58'>Method: is_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/type.py#L21'>Method: is_module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/type.py#L43'>Method: is_property</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L407'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L35'>Method: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/objinfo.py#L46'>Method: nice_repr</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L41'>Method: print_link_to_obj</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L21'>Method: private</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L28'>Method: protected</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/properties.py#L6'>Method: public</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L298'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/objinfo.py#L36'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L400'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L392'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L261'>Method: set_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/objinfo/type.py#L8'>Method: type</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L427'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L302'>Class: Operators</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L312'>Method: deco_define_comparisons</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/versions.py#L205'>Class: PythonVersion</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L25'>Class: SigInfo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L231'>Method: call</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L55'>Method: class_from_callable</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L186'>Method: getIndexFromName</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/iterables.py#L3'>Class: SortedList</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/iterables.py#L32'>Method: add</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/iterables.py#L49'>Method: remove</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/time.py#L7'>Class: Timer</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/time.py#L26'>Method: print</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/time.py#L15'>Method: reset</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/time.py#L22'>Method: seconds</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L189'>Class: TreeDiagram</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L251'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L423'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L228'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L345'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L303'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L329'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L339'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L323'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L335'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L387'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L379'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L314'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L383'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L363'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L224'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L220'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L219'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L225'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L223'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L222'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L221'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L226'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L407'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L298'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L469'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L400'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L392'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L261'>Method: set_parent</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/diagram.py#L427'>Method: view</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/versions.py#L16'>Class: Ver</a>
│  └─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/versions.py#L20'>Method: bump</a>
├─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/versions.py#L191'>Class: VerInfo</a>
└─ <a href='https://github.com/ManderaGeneral/generallibrary/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generallibrary/functions.py#L12'>Class: classproperty</a>
</pre>

## Todos
| Module             | Message                                                                                   |
|:-------------------|:------------------------------------------------------------------------------------------|
| functions.py       | Add caching for SigInfo's signature methods                                               |
| functions.py       | Test deco\_extend with int and str.                                                        |
| versions.py        | Replace this temporary Ver class with revamped VerInfo split into isolated parts.         |
| diagram.py         | Tests for NetworkDiagram.                                                                 |
| diagram.py         | Storable NetworkDiagram.                                                                  |
| diagram.py         | Moveable NetworkDiagram.                                                                  |
| diagram.py         | Transform Network to and from Tree if possible.                                           |
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
Generated 2021-01-29 11:42 CET for commit <a href='https://github.com/ManderaGeneral/generallibrary/commit/6c7dd3ca1e5eb1e618167b802c89216d93798623'>6c7dd3ca1e5eb1e618167b802c89216d93798623</a>.
</sup>
