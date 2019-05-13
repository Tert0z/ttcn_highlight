import pynvim
import re
import os

@pynvim.plugin
class TestPlugin(object):
    mappings ={
            'M': "module",
            't': "type",
            'c': "const",
            'd': "template",
            'f': "function",
            's': "signature",
            'C': "testcase",
            'a': "altstep",
            'G': "group",
            'P': "modulepar",
            'v': "var",
            'T': "timer",
            'p': "port",
            'm': "member",
            'e': "enum",
        }

    module_import_regex = re.compile('import\s+from\s+(\w*)')
    module_from_file_regex = re.compile("\/(\w*)\.ttcn3")

    def __init__(self, nvim):
        self.nvim = nvim
        tags_file = open(os.path.abspath("./tags"))
        self.tags = {}
        for t in tags_file.readlines():
            tag = [i.strip() for i in t.split("\t")]
            module = self.module_from_file_regex.search(tag[1]).group(1)
            if module in self.tags:
                self.tags[module].append(tag)
            else:
                self.tags[module] = [tag]

    @pynvim.function('HighlightTtcn')
    def highlight_ttcn(self, filename):
        file = open(filename[0], "r").readlines()
        target_files = self._get_imported_modules(file)

        module = self.module_from_file_regex.search(filename[0]).group(1)
        target_files.append(module)

        for f in target_files:
            if f in self.tags:
                for tag in self.tags[f]:
                    self.nvim.command("syn keyword ttcn3_"+self.mappings[tag[3].strip()] + " " + tag[0])

    def _get_imported_modules(self, file_content):
        result = []
        for line in file_content:
             import_match = self.module_import_regex.search(line)
             if import_match :
                 result.append(import_match.group(1))
        return result


