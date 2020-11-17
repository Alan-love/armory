from arm.logicnode.arm_nodes import *

class ArrayShiftNode(ArmLogicTreeNode):
    """Removes the first element of the given array.

    @see [Haxe API](https://api.haxe.org/Array.html#shift)"""
    bl_idname = 'LNArrayShiftNode'
    bl_label = 'Array Shift'
    arm_version = 1

    def init(self, context):
        super(ArrayShiftNode, self).init(context)
        self.add_input('ArmNodeSocketArray', 'Array')

        self.add_output('NodeSocketShader', 'Value')
