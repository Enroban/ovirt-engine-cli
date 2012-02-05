
# parser_tab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x06\xd3OxVqV)\xe4\xf4s\xa4yX\x94\xa8'
    
_lr_action_items = {'GT':([2,3,9,10,11,12,13,17,18,19,20,21,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,45,46,47,],[-6,-37,-10,-8,-37,-7,-11,-9,23,-37,-12,-13,23,-22,-21,-14,-15,-17,-18,-19,-37,-20,-32,-33,-26,-25,-23,-27,-24,-16,]),'WORD':([0,1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,19,22,23,26,27,35,52,],[2,-35,-6,9,-5,-1,-36,2,-10,-8,9,-7,-11,-34,-2,-9,32,-4,37,37,37,32,-3,]),'STRING':([2,3,9,10,11,12,13,17,19,23,26,27,35,],[-6,13,-10,-8,13,-7,-11,-9,33,38,38,38,33,]),'HEREDOC':([2,3,9,10,11,12,13,17,18,19,20,21,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,51,],[-6,-37,-10,-8,-37,-7,-11,-9,-37,-37,-12,-13,-37,-22,-21,-14,-15,-17,-18,-19,-37,-20,-32,-33,-26,-25,49,-23,-29,-27,-24,-16,-28,]),'=':([19,],[35,]),'NEWLINE':([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,],[1,-35,-6,-37,-5,-1,15,1,-10,-8,-37,-7,-11,1,-34,-2,-9,-37,-37,-12,-13,-4,-37,-22,-21,-14,-15,-17,-18,-19,-37,-20,-32,-33,-26,-25,-37,-23,-29,-27,-24,-16,1,-30,-31,-28,-3,]),'LT':([2,3,9,10,11,12,13,17,18,19,20,21,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,45,46,47,],[-6,-37,-10,-8,-37,-7,-11,-9,27,-37,-12,-13,27,-22,-21,-14,-15,-17,-18,-19,-37,-20,-32,-33,-26,-25,-23,-27,-24,-16,]),'NUMBER':([19,35,],[34,34,]),'PIPE':([2,3,9,10,11,12,13,17,18,19,20,21,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,45,46,47,],[-6,-37,-10,-8,-37,-7,-11,-9,-37,-37,-12,-13,42,-22,-21,-14,-15,-17,-18,-19,-37,-20,-32,-33,-26,-25,-23,-27,-24,-16,]),'BANG':([0,1,4,6,7,8,15,16,22,52,],[5,-35,-5,-1,-36,5,-34,-2,-4,-3,]),'SHELL':([5,42,],[14,51,]),'OPTION':([2,3,9,10,11,12,13,17,18,19,20,21,30,31,32,33,34,35,36,47,],[-6,-37,-10,-8,19,-7,-11,-9,19,-37,-12,-13,-14,-15,-17,-18,-19,-37,-20,-16,]),'MARKER':([24,],[40,]),'LTLT':([2,3,9,10,11,12,13,17,18,19,20,21,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,45,46,47,],[-6,-37,-10,-8,-37,-7,-11,-9,24,-37,-12,-13,24,-22,-21,-14,-15,-17,-18,-19,-37,-20,-32,-33,-26,-25,-23,-27,-24,-16,]),';':([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,],[7,-35,-6,-37,-5,-1,-36,7,-10,-8,-37,-7,-11,7,-34,-2,-9,-37,-37,-12,-13,-4,-37,-22,-21,-14,-15,-17,-18,-19,-37,-20,-32,-33,-26,-25,-37,-23,-29,-27,-24,-16,7,-30,-31,-28,-3,]),'GTGT':([2,3,9,10,11,12,13,17,18,19,20,21,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,45,46,47,],[-6,-37,-10,-8,-37,-7,-11,-9,26,-37,-12,-13,26,-22,-21,-14,-15,-17,-18,-19,-37,-20,-32,-33,-26,-25,-23,-27,-24,-16,]),'$end':([1,4,6,7,8,15,16,22,52,],[-35,-5,-1,-36,0,-34,-2,-4,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'option_value':([19,35,],[31,47,]),'name':([0,8,],[3,3,]),'redirections':([18,],[25,]),'heredoc':([41,],[48,]),'argument':([3,11,],[10,17,]),'eol':([0,8,14,48,],[4,4,22,52,]),'option_list':([11,],[18,]),'command':([0,8,],[6,16,]),'argument_list':([3,],[11,]),'file':([23,26,27,],[39,45,46,]),'pipeline':([25,],[41,]),'main':([0,],[8,]),'redirection':([18,25,],[28,43,]),'empty':([3,11,18,19,25,35,41,],[12,20,29,36,44,36,50,]),'option':([11,18,],[21,30,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> command','main',1,'p_main','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',115),
  ('main -> main command','main',2,'p_main','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',116),
  ('command -> name argument_list option_list redirections pipeline heredoc eol','command',7,'p_command','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',126),
  ('command -> BANG SHELL eol','command',3,'p_command','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',127),
  ('command -> eol','command',1,'p_command','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',128),
  ('name -> WORD','name',1,'p_name','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',143),
  ('argument_list -> empty','argument_list',1,'p_argument_list','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',147),
  ('argument_list -> argument','argument_list',1,'p_argument_list','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',148),
  ('argument_list -> argument_list argument','argument_list',2,'p_argument_list','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',149),
  ('argument -> WORD','argument',1,'p_argument','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',160),
  ('argument -> STRING','argument',1,'p_argument','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',161),
  ('option_list -> empty','option_list',1,'p_option_list','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',166),
  ('option_list -> option','option_list',1,'p_option_list','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',167),
  ('option_list -> option_list option','option_list',2,'p_option_list','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',168),
  ('option -> OPTION option_value','option',2,'p_option','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',180),
  ('option -> OPTION = option_value','option',3,'p_option','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',181),
  ('option_value -> WORD','option_value',1,'p_option_value','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',189),
  ('option_value -> STRING','option_value',1,'p_option_value','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',190),
  ('option_value -> NUMBER','option_value',1,'p_option_value','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',191),
  ('option_value -> empty','option_value',1,'p_option_value','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',192),
  ('redirections -> empty','redirections',1,'p_redirections','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',197),
  ('redirections -> redirection','redirections',1,'p_redirections','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',198),
  ('redirections -> redirections redirection','redirections',2,'p_redirections','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',199),
  ('redirection -> LT file','redirection',2,'p_redirection','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',210),
  ('redirection -> LTLT MARKER','redirection',2,'p_redirection','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',211),
  ('redirection -> GT file','redirection',2,'p_redirection','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',212),
  ('redirection -> GTGT file','redirection',2,'p_redirection','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',213),
  ('pipeline -> PIPE SHELL','pipeline',2,'p_pipeline','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',218),
  ('pipeline -> empty','pipeline',1,'p_pipeline','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',219),
  ('heredoc -> HEREDOC','heredoc',1,'p_heredoc','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',225),
  ('heredoc -> empty','heredoc',1,'p_heredoc','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',226),
  ('file -> WORD','file',1,'p_file','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',231),
  ('file -> STRING','file',1,'p_file','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',232),
  ('eol -> ; NEWLINE','eol',2,'p_eol','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',237),
  ('eol -> NEWLINE','eol',1,'p_eol','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',238),
  ('eol -> ;','eol',1,'p_eol','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',239),
  ('empty -> <empty>','empty',0,'p_empty','/home/mpastern/Coding/ovirt/ovirt-engine-cli/src/cli/parser.py',244),
]
