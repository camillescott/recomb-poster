from __future__ import print_function
import glob
import os

DEP=['poster/flexdashboard-poster.Rmd', 'scripts/render-poster.R']

def task_build_html():


    return {'file_dep': DEP,
            'actions': ['R -f scripts/render-poster.R'],
            'targets': ['output/index.html', 'output/poster.png'],
            'clean': True}

def task_publish():

    cmd_list = ['touch output/.nojekyll',
                'git add output/',
                'git commit  -m "Generated gh-pages for `git log master -1 '\
                '--pretty=short --abbrev-commit`"',
                'git subtree split --prefix output/ -b gh-pages',
                'git push -f origin gh-pages:gh-pages',
                'git branch -D gh-pages']

    return {'task_dep': ['build_html'],
            'file_dep': DEP,
            'actions': cmd_list}

