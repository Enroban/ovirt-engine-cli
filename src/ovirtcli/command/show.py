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


from ovirtcli.command.command import OvirtCommand
from ovirtcli.utils.typehelper import TypeHelper


class ShowCommand(OvirtCommand):

    name = 'show'
    description = 'show one object'
    args_check = lambda self, x: len(x) > 0
    valid_options = [ ('*', str) ]
    SHOW_ALL_KEY = '--showall'

    helptext = """\
        == Usage ==
    
        show <type> <id> [object identifiers]

        == Description ==

        Retrieve an object and display information about it. The following
        arguments are required:

          * type        The type of object to retrieve
          * id          The object identifier

        Objects can be identified by their name and by their unique id.

        == Supported Help formats ==

        - This help will show all available attribute options for showing 
          resource
          
          * format      - help show type
          * example     - help show vm

        == Available Types ==

        The <type> parameter must be one of the following.

          $types

        == Object Identifiers ==

        Some objects can only exist inside other objects. For example, a disk
        can only exist in the content of a virtual machine. In this case, one
        or more object identifier opties needs to be provided to identify the
        containing object.

        An object identifier is an option of the form '--<type>id <id>'. This
        would identify an object with type <type> and id <id>. See the
        examples section below for a few examples.

        == Examples ==

        - This example shows information about the virtual machine "myvm"

          $ show vm myvm

        - This example shows all information about the virtual machine "myvm"
          including empty properties

          $ show vm myvm --showall

        - This example shows information about the nic named 'nic1' of the 
          virtual machine "myvm"

          $ show nic nic1 --vmid myvm

        == Return values ==

        This command will exit with one of the following statuses. To see the
        exit status of the last command, type 'status'.

          $statuses
        """

    helptext1 = """\
        == Usage ==

        - show <type>
            
        - show <type> <id> [object identifiers]

        == Description ==

        Shows an object by type '$type'. See 'help show' for generic
        help on showing objects.

        == Attribute Options ==

        The following options are available for objects with type '$type':

          $options

        == Return values ==

        This command will exit with one of the following statuses. To see the
        exit status of the last command, type 'status'.

          $statuses
        """

    def execute(self):
        """Execute "show"."""
        args = self.arguments
        opts = self.options

        if not (TypeHelper.isKnownType(args[0])):
            self.error('no such type: %s' % args[0])

        if len(args) < 2 and len(opts) == 0:
            self.error('%s identifier required.' % args[0])

        obj = self.get_object(typ=args[0],
                              obj_id=args[1] if len(args) > 1 else None,
                              base=self.resolve_base(opts),
                              opts=opts)

        if not (obj):
            self.error('no such %s %s' % (args[0], args[1]))

        self.context.formatter.format(self.context,
                                      obj,
                                      show_all=True if opts and opts.has_key(ShowCommand.SHOW_ALL_KEY) else False)

    def show_help(self):
        """Show help for "show"."""
        self.check_connection()
        args = self.arguments
        opts = self.options

        subst = {}

        types = self.get_singular_types(method='get')
        subst['types'] = self.format_map(types)

        statuses = self.get_statuses()
        subst['statuses'] = self.format_list(statuses)

        if len(args) == 1 and self.is_supported_type(types.keys(), args[0]):
            helptext = self.helptext1
            params_list = self.get_options(method='get',
                                           resource=TypeHelper.to_singular(args[0]),
                                           sub_resource=self.resolve_base(opts))
            subst['options'] = self.format_list(params_list)
            subst['type'] = args[0]
        elif len(args) == 2 and self.is_supported_type(types.keys(), args[0]):
            helptext = self.helptext1

            subst['type'] = args[0]
            subst['id'] = args[1]
            base = self.resolve_base(opts)
            obj = self.get_object(args[0], args[1], base)
            if obj is None:
                self.error('no such %s: %s' % (args[0], args[1]))

            params_list = self.get_options(method='get',
                                           resource=obj,
                                           sub_resource=base)
            subst['options'] = self.format_list(params_list)

        else:
            helptext = self.helptext
            if len(args) == 1: self.is_supported_type(types.keys(), args[0])


        helptext = self.format_help(helptext, subst)
        stdout = self.context.terminal.stdout
        stdout.write(helptext)

