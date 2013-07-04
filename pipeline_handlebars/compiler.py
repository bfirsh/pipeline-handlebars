from django.conf import settings
from pipeline.compilers import SubProcessCompiler


class HandlebarsCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('.html') or filename.endswith('.hbs')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled
        command = "%s %s -f %s" % (
            settings.PIPELINE_HANDLEBARS_BINARY,
            infile,
            outfile
            )
        return self.execute_command(command)

