#!/usr/bin/python 
import sys
import os
import commands
import shutil


def execute_command(cmd):
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)
  print output

def remove_add_packages(project_name, packages):
  execute_command('cd ' + project_name + ' && meteor remove autopublish')
  execute_command('cd ' + project_name + ' && meteor remove insecure')
  execute_command('cd ' + project_name + ' && mrt add iron-router')
  for package in packages:
    execute_command('cd ' + project_name + ' && mrt add ' + package)

def clean_and_mkdirs(project_name):
  project_dir = os.path.abspath('.')
  os.mkdir(os.path.join(project_dir, project_name + '/server'))
  os.remove(os.path.join(project_dir, project_name + '/' + project_name + '.html'))
  os.remove(os.path.join(project_dir, project_name + '/' + project_name + '.css'))
  os.remove(os.path.join(project_dir, project_name + '/' + project_name + '.js'))
  shutil.copytree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'client'), os.path.join(project_dir, project_name + '/client'))
  
def create_project(project_name, mrt_packages):
  print 'creating project ', project_name, ' with packages ', mrt_packages
  execute_command('meteor create ' + project_name)

def main():
  args = sys.argv[1:]
  if len(args) < 1:
    print "error: must specify project name"
    sys.exit(1)

  project_name = args[0]
  del args[0]

  mrt_packages = []
  if args:
    for package in args:
      if package != 'iron-router':
        mrt_packages.append(package)
      else: 
        print 'iron-router is installed by default'


  print "path: ", os.path.join(os.path.dirname(os.path.realpath(__file__)), 'client')
  create_project(project_name, mrt_packages)
  clean_and_mkdirs(project_name)
  remove_add_packages(project_name, mrt_packages)



if __name__ == '__main__':
  main()