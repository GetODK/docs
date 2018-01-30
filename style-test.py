import os
import re
import glob
import click
import shutil
import importlib
import proselint
from blessings import Terminal

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# variables to hold error and warning count
err_cnt = 0
warn_cnt = 0

# for generating colored output
os.environ["TERM"] = "linux"
os.environ["TERMINFO"]= "/etc/terminfo"
t = Terminal()

def add_checks():      
    """Add checks to proselint."""
    src ='./style-guide'       
    dest = os.path.dirname(proselint.__file__)
    dest_prc = dest + '/.proselintrc'
    dest = dest + '/checks/style-guide'

    # remove style-guide folder
    if os.path.exists(dest):
        shutil.rmtree(dest)

    # copy over style-guide folder to checks
    shutil.copytree(src, dest)

    with open("style-test.txt", "r") as file:
        tests = file.readlines()

    with open(dest_prc, "r") as in_file:
        buf = in_file.readlines()

    pos = len(buf)-2

    # find first occurence of style-guide checks in proselintrc
    for index, line in enumerate(buf):
        if line.startswith("        \"style-guide."):
            pos = index
            break      

    # copy over new checks to proselintrc from style-text.txt
    with open(dest_prc, "w") as out_file:
        for index, line in enumerate(buf):
            if index == pos-1 and not line.endswith(",\n"):
                line = line[0:line.rfind("\n")] + ",\n"
            if index < pos:
                out_file.write(line)
        for test in tests:
            out_file.write(test)                
        out_file.write("    }\n")
        out_file.write("}")


def remove_lines(text):
    """Remove ignored lines  and directive blocks from text."""
    directive_list = [".. image::", ".. figure::", ".. video::", ".. code::",
                      ".. code-block::", ".. csv-table::", ".. toctree::",]
    index = 0
    length = len(text)
    while index<len(text):
        # remove ignored lines
        if "startignore" in text[index]:
            while index < length and "endignore" not in text[index]:
                text[index] = "ignore_line\n"
                index = index+1
        # remove directive blocks
        if index < length and any(word in text[index] for word in directive_list):
            indent = len(text[index]) - len(text[index].lstrip())
            text[index] = "ignore_line\n"
            index = index + 1
            if index < length:
                space_cnt = len(text[index]) - len(text[index].lstrip())
            while index < length and (space_cnt > indent or text[index] == '\n'):
                if not text[index].isspace():
                    text[index] = "ignore_line\n"
                index = index + 1
                if index < length:
                    space_cnt = len(text[index]) - len(text[index].lstrip())
            index = index - 1        
        index = index+1 
    
    return text            


def get_line(filename, row, col):
    """Get specific line from file."""
    lines = open(filename, 'r').readlines() 

    for index,line in enumerate(lines):
        if index==row-1:
            if line.isspace():
                line = lines[index+1]
            st_col = max(0, col-15)
            en_col = min(col+15, len(line))
            text = "..." + line[st_col:en_col].rstrip() + "..."
            break
    
    return text


def temp_file(text):
    """Create a temporary file to write the text lines.""" 
    f= open("temp.txt","w+")
    for line in text:
        f.write(line)
    text = open("temp.txt", "r")
    os.remove("temp.txt")
    return text    


def get_errlist():
    """Returns a list of fixable errors to fail the build."""
    list_errors = [
                   "style-guide.check-curlyquote", "style-guide.uk-us",
                   "spelling.able_atable", "spelling.able_ible", 
                   "spelling.athletes", "spelling.em_im_en_in", 
                   "spelling.er_or", "spelling.in_un", 
                   "spelling.misc", "misc.capitalization", 
                   "misc.inferior_superior", "misc.many_a", 
                   "misc.phrasal_adjectives", "nonwords.misc",
                 ]  
    return list_errors


def exclude_checks():
    """Removes the checks which are to be excluded."""
    list_exclude = [
                     "typography.symbols", "weasel_words.very",
                  ]
    dest = os.path.dirname(proselint.__file__)
    dest_prc = dest + '/.proselintrc'

    with open(dest_prc, "r") as in_file:
        buf = in_file.readlines()

    # remove excluded checks
    for index, line in enumerate(buf):
        if any(word in line for word in list_exclude):
            buf[index] = line.replace('true','false')  

    with open(dest_prc, "w") as out_file:
        for index, line in enumerate(buf):
            out_file.write(line)


def get_paths(paths):
    """Return a list of files to run the checks on."""
    file_path = os.path.realpath(__file__)

    # find path for all .rst files
    search_path = file_path[0:file_path.rfind('/')]

    # Make a list of paths to check for
    path_list = []

    # Add paths if provided by user
    if paths:
        search_path = search_path + "/"
        path_list = [search_path + path for path in paths]

    # Add all rst files if specific paths not provided by user
    else:
        for filename in glob.glob(os.path.join(search_path, '*.rst')):
            path_list.append(filename)       
    
    return path_list


def run_checks(paths, fix):
    """Run checks on the docs."""
    global t
    path_list = get_paths(paths) 
    list_errors = get_errlist()
    errors = []

    for filename in path_list:
        shortname = filename[filename.rfind('/')+1:]

        print(t.cyan("Testing %s ..." %shortname)) 
        
        # read the file 
        with open(filename, "r") as file:
            text = file.readlines()

        # remove ignored lines
        text = remove_lines(text)
        
        # Import extra check module from style-guide 
        extra = importlib.import_module('style-guide.extra', None)

        # run checks for quotes, curly quotes, section labels
        errors = extra.check(temp_file(text))

        # lint the text for other tests
        errors = errors + proselint.tools.lint(temp_file(text))

        # sort the errors according to line and column 
        errors = sorted(errors, key=lambda e: (e[2], e[3]))

        if not fix:
            disp_checks(errors, shortname)
        
        # prepare a list for fixing errors
        if fix:
            fix_list = []
            for e in errors:
                check = e[0]
                line = e[2] + 1
                col = e[3] + 1
                extent = e[6]
                replace = e[8]

                # Prepare a list of fixable errors 
                # Don't set errors for style-guide as they might be examples
                if check in list_errors and "style-guide.rst" not in filename:
                    fix_list += [(check, line, col, extent, replace)]

            # call fix_err function to fix the errors
            cnt = len(fix_list)
            if cnt:
                print(t.red("Found %d errors" %cnt))
                print(t.red("Fixing errors"))
                fix_err(fix_list, filename) 
            else:
                print(t.yellow("Found no errors!"))           
    
    # Display total errors and warning count
    if not fix:
        disp_cnt()


def disp_checks(errors, filename):
    """Display errors and warnings."""
    global err_cnt
    global warn_cnt
    global t
    list_errors = get_errlist()

    for e in errors:        
        # e[0]=check
        if e[0] in list_errors and "style-guide.rst" not in filename:
            severity = "error"
        else:
            severity = "warning" 
        # e[2]+1=line, e[3]+1=col
        line1 = "%s | line: %d | col: %d" %(filename, e[2]+1, e[3]+1)
        # get line from file where  e[2]+1=line, e[3]+1=col
        line2 = get_line(filename,e[2]+1,e[3]+1)
        # e[1]=error_message
        line3 = e[1]
        # e[0]=check
        line4 = "%s | %s" %(e[0], severity)
        print(t.blue(line1))
        print(line2)
        if severity is "warning":
            print(t.yellow(line3))
            warn_cnt += 1
        else:
            print(t.red(line3))
            err_cnt += 1
        print(t.white(line4)) 
        print("\n")   
    

def disp_cnt():
    """Display error and warning count."""
    global err_cnt
    global warn_cnt
    global t

    print(t.yellow("Found %d warnings" %warn_cnt))
    print(t.red("Found %d errors") %err_cnt)
    if err_cnt:
        raise Exception("Style-guide testing failed! Fix the errors")


def fix_err(fix_list, filename):
    """Remove the fixable errors.""" 
    buf = open(filename, 'r').readlines()

    for e in fix_list:      
        for index,line in enumerate(buf):
            # e[1]=line
            if index == e[1]-1:
                # e[0]=check
                if e[0] == "style-guide.check-curlyquote":
                    line = re.sub('“','"',line)
                    line = re.sub('”','"',line)
                else:  
                    # e[2]=col, e[3]=extent  
                    word = line[e[2]-1:e[2]+e[3]-2]
                    # e[4]=replacement
                    line = re.sub(word, e[4], line)
                buf[index] = line    
        
    with open(filename, "w") as out_file:
        for line in buf:
            out_file.write(line)


@click.command(context_settings = CONTEXT_SETTINGS)
@click.option('--fix', '-f', is_flag = True, help = "Removes the fixable errors")
@click.argument('paths', nargs = -1, type = click.Path())
def style_test(paths = None, fix = None):
    """A CLI for style guide testing"""

    # add custom style-guide checks to proselint
    add_checks()

    # Remove the excluded checks
    exclude_checks()
    
    # run the checks on docs
    run_checks(paths, fix)
    

if __name__ == '__main__':
    style_test()
