#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import sys
import os
import cmd
from ovirtcli.shell.actioncmdshell import ActionCmdShell
from ovirtcli.shell.connectcmdshell import ConnectCmdShell
from ovirtcli.shell.config import Config
from ovirtcli.shell.showcmdshell import ShowCmdShell
from ovirtcli.shell.listcmdshell import ListCmdShell
from ovirtcli.shell.updatecmdshell import UpdateCmdShell
from ovirtcli.shell.deletecmdshell import DeleteCmdShell
from ovirtcli.shell.createcmdshell import CreateCmdShell
from ovirtcli.shell.disconnectcmdshell import DisconnectCmdShell

class EngineShell(cmd.Cmd, ConnectCmdShell, ActionCmdShell, \
                  ShowCmdShell, ListCmdShell, UpdateCmdShell, \
                  DeleteCmdShell, CreateCmdShell, DisconnectCmdShell):
    """ovirt-engine-cli command processor."""
    ############################# INIT #################################
    def __init__(self, context, parser, completekey='tab', stdin=None, stdout=None):
        cmd.Cmd.__init__(self, completekey=completekey, stdin=stdin, stdout=stdout)
        ConnectCmdShell.__init__(self, context, parser)
        ActionCmdShell.__init__(self, context, parser)
        ShowCmdShell.__init__(self, context, parser)
        ListCmdShell.__init__(self, context, parser)
        UpdateCmdShell.__init__(self, context, parser)
        DeleteCmdShell.__init__(self, context, parser)
        CreateCmdShell.__init__(self, context, parser)
        DisconnectCmdShell.__init__(self, context, parser)
    ############################# MISC #################################    
    prompt = '[%s shell]# ' % Config.PRODUCT
#    intro = """
#    
#    ##########################
#       Welcome to % s shell
#    ##########################
#    
#    """ % PRODUCT

    doc_header = '%s shell commands:' % Config.PRODUCT
#    misc_header = 'misc_header'
    undoc_header = 'Misc commands:'
    last_output = ''
    ########################### SYSTEM #################################
    def cmdloop(self, intro=None):
        try:
            return cmd.Cmd.cmdloop(self, intro)
        except Exception, e:
            sys.stderr.write('error: %s\n' % str(e))
            return self.cmdloop(intro)

    def emptyline(self):
        print self.prompt

    def onecmd(self, s):
        return cmd.Cmd.onecmd(self, s)

    def onecmd_loop(self, s):
        opts, args = self.parser.parse_args()
        if opts.connect or len(args) == 0:
            self.do_connect(s)
            self.cmdloop()
        else:
            self.cmdloop()

    def precmd(self, line):
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        return cmd.Cmd.postcmd(self, stop, line)
    
    def parseline(self, line):
        ret = cmd.Cmd.parseline(self, line)
        return ret

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line
    
    def do_EOF(self, line):
        return True
    ############################# SHELL #################################
    def do_shell(self, line):
        "Runs a shell command ('!' can be used instead of 'shell' command)."
        output = os.popen(line).read()
        print output
        self.last_output = output

    def do_echo(self, line):
        "Prints the input, replacing '$out' with the output of the last shell command"
        if self.last_output:
            print line.replace('$out', self.last_output)
        elif line:
            print line
        else: print self.prompt
    #####################################################################