from recommonmark.parser import CommonMarkParser

source_parsers = {
	'.md': CommonMarkParser,
}

source_prefix = ['.rst', '.md']
