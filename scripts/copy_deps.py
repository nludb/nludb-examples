"""Copies the standard files from `/base` to each of the example projects."""

import shutil
import os
from os.path import join, isfile
from os import listdir
BASE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

def copy_files(src_dir, dest):
  dest_dir = os.path.join(BASE, 'examples', dest)
  onlyfiles = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
  for file in onlyfiles:
    print(join(dest_dir, file))
    shutil.copyfile(join(src_dir, file),join(dest_dir, file))

def copy_base(dest):
  src_dir = os.path.join(BASE, 'base', 'all')
  copy_files(src_dir, dest)

def copy_app(dest):
  copy_base(dest)
  src_dir = os.path.join(BASE, 'base', 'apps')
  copy_files(src_dir, dest)

def copy_plugin(dest):
  copy_base(dest)
  src_dir = os.path.join(BASE, 'base', 'plugins')
  copy_files(src_dir, dest)

def copy_notebooks(dest):
  copy_base(dest)
  src_dir = os.path.join(BASE, 'base', 'notebooks')
  copy_files(src_dir, dest)


if __name__ == '__main__':
  copy_app('apps/hello-world')
  copy_app('apps/qa-bot')
  copy_plugin('plugins/converter')
  copy_plugin('plugins/embedder')
  copy_plugin('plugins/importer')
  copy_plugin('plugins/parser')
  copy_plugin('notebooks/jupyter-playground')
