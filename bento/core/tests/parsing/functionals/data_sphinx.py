ref = {'author': 'Georg Brandl',
 'author_email': 'georg@python.org',
 'classifiers': None,
 'data_files': {'gendata_sphinx': {'files': ['texinputs/Makefile',
                                             'texinputs/fncychap.sty',
                                             'texinputs/howto.cls',
                                             'texinputs/manual.cls',
                                             'texinputs/python.ist',
                                             'texinputs/sphinx.sty',
                                             'texinputs/tabulary.sty',
                                             'themes/basic/defindex.html',
                                             'themes/basic/genindex-single.html',
                                             'themes/basic/genindex-split.html',
                                             'themes/basic/genindex.html',
                                             'themes/basic/layout.html',
                                             'themes/basic/modindex.html',
                                             'themes/basic/opensearch.xml',
                                             'themes/basic/page.html',
                                             'themes/basic/search.html',
                                             'themes/basic/theme.conf',
                                             'themes/basic/changes/frameset.html',
                                             'themes/basic/changes/rstsource.html',
                                             'themes/basic/changes/versionchanges.html',
                                             'themes/basic/static/basic.css',
                                             'themes/basic/static/doctools.js',
                                             'themes/basic/static/file.png',
                                             'themes/basic/static/jquery.js',
                                             'themes/basic/static/minus.png',
                                             'themes/basic/static/plus.png',
                                             'themes/basic/static/searchtools.js',
                                             'themes/default/theme.conf',
                                             'themes/default/static/default.css_t',
                                             'themes/sphinxdoc/layout.html',
                                             'themes/sphinxdoc/theme.conf',
                                             'themes/sphinxdoc/static/contents.png',
                                             'themes/sphinxdoc/static/navigation.png',
                                             'themes/sphinxdoc/static/sphinxdoc.css',
                                             'themes/traditional/theme.conf',
                                             'themes/traditional/static/traditional.css'],
                                   'name': 'gendata_sphinx',
                                   'source_dir': 'sphinx',
                                   'target_dir': '$gendatadir/sphinx'},
                'gendata_sphinx_ext_autosummary': {'files': ['templates/module'],
                                                   'name': 'gendata_sphinx_ext_autosummary',
                                                   'source_dir': 'sphinx/ext/autosummary',
                                                   'target_dir': '$gendatadir/sphinx/ext/autosummary'},
                'gendata_sphinx_locale': {'files': ['sphinx.pot',
                                                    'cs/LC_MESSAGES/sphinx.js',
                                                    'cs/LC_MESSAGES/sphinx.mo',
                                                    'cs/LC_MESSAGES/sphinx.po',
                                                    'de/LC_MESSAGES/sphinx.js',
                                                    'de/LC_MESSAGES/sphinx.mo',
                                                    'de/LC_MESSAGES/sphinx.po',
                                                    'es/LC_MESSAGES/sphinx.js',
                                                    'es/LC_MESSAGES/sphinx.mo',
                                                    'es/LC_MESSAGES/sphinx.po',
                                                    'fi/LC_MESSAGES/sphinx.js',
                                                    'fi/LC_MESSAGES/sphinx.mo',
                                                    'fi/LC_MESSAGES/sphinx.po',
                                                    'fr/LC_MESSAGES/sphinx.js',
                                                    'fr/LC_MESSAGES/sphinx.mo',
                                                    'fr/LC_MESSAGES/sphinx.po',
                                                    'it/LC_MESSAGES/sphinx.js',
                                                    'it/LC_MESSAGES/sphinx.mo',
                                                    'it/LC_MESSAGES/sphinx.po',
                                                    'ja/LC_MESSAGES/sphinx.js',
                                                    'ja/LC_MESSAGES/sphinx.mo',
                                                    'ja/LC_MESSAGES/sphinx.po',
                                                    'nl/LC_MESSAGES/sphinx.js',
                                                    'nl/LC_MESSAGES/sphinx.mo',
                                                    'nl/LC_MESSAGES/sphinx.po',
                                                    'pl/LC_MESSAGES/sphinx.js',
                                                    'pl/LC_MESSAGES/sphinx.mo',
                                                    'pl/LC_MESSAGES/sphinx.po',
                                                    'pt_BR/LC_MESSAGES/sphinx.js',
                                                    'pt_BR/LC_MESSAGES/sphinx.mo',
                                                    'pt_BR/LC_MESSAGES/sphinx.po',
                                                    'ru/LC_MESSAGES/sphinx.js',
                                                    'ru/LC_MESSAGES/sphinx.mo',
                                                    'ru/LC_MESSAGES/sphinx.po',
                                                    'sl/LC_MESSAGES/sphinx.js',
                                                    'sl/LC_MESSAGES/sphinx.mo',
                                                    'sl/LC_MESSAGES/sphinx.po',
                                                    'uk_UA/LC_MESSAGES/sphinx.js',
                                                    'uk_UA/LC_MESSAGES/sphinx.mo',
                                                    'uk_UA/LC_MESSAGES/sphinx.po',
                                                    'zh_TW/LC_MESSAGES/sphinx.js',
                                                    'zh_TW/LC_MESSAGES/sphinx.mo',
                                                    'zh_TW/LC_MESSAGES/sphinx.po'],
                                          'name': 'gendata_sphinx_locale',
                                          'source_dir': 'sphinx/locale',
                                          'target_dir': '$gendatadir/sphinx/locale'},
                'gendata_sphinx_pycode': {'files': ['Grammar.txt'],
                                          'name': 'gendata_sphinx_pycode',
                                          'source_dir': 'sphinx/pycode',
                                          'target_dir': '$gendatadir/sphinx/pycode'}},
 'description': 'Sphinx is a tool that makes it easy to create intelligent and beautiful\ndocumentation for Python projects (or other documents consisting of\nmultiple reStructuredText sources), written by Georg Brandl.\nIt was originally created to translate the new Python documentation,\nbut has now been cleaned up in the hope that it will be useful to many\nother projects.\n\nSphinx uses reStructuredText as its markup language, and many of its strengths\ncome from the power and straightforwardness of reStructuredText and its\nparsing and translating suite, the Docutils.\n\nAlthough it is still under constant development, the following features\nare already present, work fine and can be seen "in action" in the Python docs:\n\n* Output formats: HTML (including Windows HTML Help), plain text and LaTeX,\n  for printable PDF versions\n* Extensive cross-references: semantic markup and automatic links\n  for functions, classes, glossary terms and similar pieces of information\n* Hierarchical structure: easy definition of a document tree, with automatic\n  links to siblings, parents and children\n* Automatic indices: general index as well as a module index\n* Code handling: automatic highlighting using the Pygments highlighter\n* Various extensions are available, e.g. for automatic testing of snippets\n  and inclusion of appropriately formatted docstrings.\n\nA development egg can be found `here\n<http://bitbucket.org/birkenfeld/sphinx/get/tip.gz#egg=Sphinx-dev>`_.',
 'download_url': 'http://pypi.python.org/pypi/Sphinx',
 'executables': {'sphinx-autogen': {'function': 'main',
                                    'module': 'sphinx.ext.autosummary.generate',
                                    'name': 'sphinx-autogen'},
                 'sphinx-build': {'function': 'main',
                                  'module': 'sphinx',
                                  'name': 'sphinx-build'},
                 'sphinx-quickstart': {'function': 'main',
                                       'module': 'sphinx.quickstart',
                                       'name': 'sphinx-quickstart'}},
 'extra_source_files': ['AUTHORS',
                        'CHANGES',
                        'EXAMPLES',
                        'LICENSE',
                        'Makefile',
                        'README',
                        'TODO',
                        'babel.cfg',
                        'doc/Makefile',
                        'doc/_static/sphinx.png',
                        'doc/_templates/index.html',
                        'doc/_templates/indexsidebar.html',
                        'doc/_templates/layout.html',
                        'doc/builders.rst',
                        'doc/changes.rst',
                        'doc/concepts.rst',
                        'doc/conf.py',
                        'doc/config.rst',
                        'doc/contents.rst',
                        'doc/examples.rst',
                        'doc/ext/appapi.rst',
                        'doc/ext/autodoc.rst',
                        'doc/ext/autosummary.rst',
                        'doc/ext/builderapi.rst',
                        'doc/ext/coverage.rst',
                        'doc/ext/doctest.rst',
                        'doc/ext/graphviz.rst',
                        'doc/ext/ifconfig.rst',
                        'doc/ext/inheritance.rst',
                        'doc/ext/intersphinx.rst',
                        'doc/ext/math.rst',
                        'doc/ext/refcounting.rst',
                        'doc/ext/todo.rst',
                        'doc/ext/tutorial.rst',
                        'doc/extensions.rst',
                        'doc/faq.rst',
                        'doc/glossary.rst',
                        'doc/intro.rst',
                        'doc/markup/code.rst',
                        'doc/markup/desc.rst',
                        'doc/markup/index.rst',
                        'doc/markup/inline.rst',
                        'doc/markup/misc.rst',
                        'doc/markup/para.rst',
                        'doc/rest.rst',
                        'doc/sphinx-build.1',
                        'doc/sphinx-quickstart.1',
                        'doc/templating.rst',
                        'doc/theming.rst',
                        'ez_setup.py',
                        'setup.cfg',
                        'setup.py',
                        'sphinx-autogen.py',
                        'sphinx-build.py',
                        'sphinx-quickstart.py',
                        'tests/coverage.py',
                        'tests/etree13/ElementPath.py',
                        'tests/etree13/ElementTree.py',
                        'tests/etree13/HTMLTreeBuilder.py',
                        'tests/etree13/__init__.py',
                        'tests/path.py',
                        'tests/root/Makefile',
                        'tests/root/_static/README',
                        'tests/root/_templates/layout.html',
                        'tests/root/autodoc.txt',
                        'tests/root/autosummary.txt',
                        'tests/root/bom.txt',
                        'tests/root/conf.py',
                        'tests/root/contents.txt',
                        'tests/root/desc.txt',
                        'tests/root/ext.py',
                        'tests/root/images.txt',
                        'tests/root/img.gif',
                        'tests/root/img.pdf',
                        'tests/root/img.png',
                        'tests/root/includes.txt',
                        'tests/root/literal.inc',
                        'tests/root/markup.txt',
                        'tests/root/math.txt',
                        'tests/root/rimg.png',
                        'tests/root/special/api.h',
                        'tests/root/special/code.py',
                        'tests/root/subdir/images.txt',
                        'tests/root/subdir/img.png',
                        'tests/root/subdir/include.inc',
                        'tests/root/subdir/includes.txt',
                        'tests/root/subdir/simg.png',
                        'tests/root/svgimg.pdf',
                        'tests/root/svgimg.svg',
                        'tests/root/testtheme/layout.html',
                        'tests/root/testtheme/static/staticimg.png',
                        'tests/root/testtheme/static/statictmpl.html_t',
                        'tests/root/testtheme/theme.conf',
                        'tests/root/wrongenc.inc',
                        'tests/root/ziptheme.zip',
                        'tests/run.py',
                        'tests/test_application.py',
                        'tests/test_autodoc.py',
                        'tests/test_build.py',
                        'tests/test_config.py',
                        'tests/test_coverage.py',
                        'tests/test_env.py',
                        'tests/test_highlighting.py',
                        'tests/test_i18n.py',
                        'tests/test_markup.py',
                        'tests/test_quickstart.py',
                        'tests/test_search.py',
                        'tests/test_theming.py',
                        'tests/util.py',
                        'utils/check_sources.py',
                        'utils/pylintrc',
                        'utils/reindent.py'],
 'libraries': {'default': {'install_requires': ['Pygments>=0.8',
                                                'Jinja2>=2.1',
                                                'docutils>=0.4'],
                           'name': 'default',
                           'packages': ['sphinx',
                                        'sphinx.builders',
                                        'sphinx.directives',
                                        'sphinx.ext',
                                        'sphinx.ext.autosummary',
                                        'sphinx.locale',
                                        'sphinx.pycode',
                                        'sphinx.pycode.pgen2',
                                        'sphinx.util',
                                        'sphinx.writers']}},
 'license': 'BSD',
 'maintainer': 'Georg Brandl',
 'maintainer_email': 'georg@python.org',
 'name': 'Sphinx',
 'path_options': {'gendatadir': {'default': '$sitedir',
                                 'description': 'Directory for dataFiles obtained from distutils conversion',
                                 'name': 'gendatadir'}},
 'platforms': ['any'],
 'summary': 'Python documentation generator',
 'url': 'http://sphinx.pocoo.org/',
 'version': '0.6.3'}
