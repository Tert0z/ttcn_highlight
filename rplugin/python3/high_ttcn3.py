import pynvim
import re

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

    def __init__(self, nvim):
        self.nvim = nvim
        tags_file = open("/home/tert0z/tags")
        self.tags = [[i.strip() for i in t.split("\t")]for t in tags_file.readlines()]

    @pynvim.function('TestFunction')
    def testfunction(self, filename):
        file = open(filename[0], "r").readlines()

        target_files = self._get_imported_files(file)
        target_files.append(filename[0])
        self.nvim.out_write(str(target_files))
        for tag in self.tags:
            if tag[1] in target_files:
                self.nvim.command("syn keyword ttcn3_"+self.mappings[tag[3].strip()] + " " + tag[0])
        self.nvim.out_write("\n")

    def _get_imported_files(self, file_content):
        result = []
        for line in file_content:
             import_match = self.module_import_regex.search(line)
             if import_match :
                 try:
                     tag = next(t for t in self.tags if t[0] == import_match.group(1))
                     result.append(tag[1])
                 except:
                     pass
        return result


