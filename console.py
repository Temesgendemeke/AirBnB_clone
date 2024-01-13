#!/usr/bin/python3
from cmd import Cmd
from models.base_model import BaseModel
import sys
class HBNBCommand(Cmd):
    prompt = "(hbnb) "
    def do_quit(self, line):
        return True
    def help_quit(self):
        print ('Quit command to exit the program\n')
    def emptyline(self):
        pass
    def do_create(self, class_name):
        if class_name:
            if class_name in globals():
                basemodel_instance = BaseModel()
                
            else:
                print("** class doesn't exist **")

        elif not class_name:
            print ("** class name missing **")
    def do_show(self, class_name):
        if class_name:
            if class_name in globals():
                basemodel_instance = BaseModel()
            elif class_name.id is None:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

        elif not class_name:
            print ("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()