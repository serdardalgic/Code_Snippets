#!/usr/bin/python
# -*- coding: UTF-8 -*-

import difflib
import sys
import shlex
from subprocess import Popen, PIPE

# Write PEP8_IGNORES string as PEP8 rules to be ignored,
# separated with ',' with each other consecutively.
# No space before or after ','
#PEP8_IGNORES = "W292,E132"
PEP8_IGNORES = ""


def run(command, shell=False, splitter=None, stripped=True):
    """
    Run the given command, wait until the command is executed, then,
    if the process is succesful, return the result list. If splittter is
    provided, return splitted result.

    shlex is used for parsing the command. See below link for details.
    http://docs.python.org/2/library/subprocess.html#popen-constructor
    """
    p = Popen(shlex.split(command), shell=shell, stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = p.communicate()
    if not stderr:
        if not splitter:
            if not stripped:
                return stdout
            else:
                return stdout.strip()
        elif stripped:
            return stdout.strip().split(splitter)
        else:
            return stdout.split(splitter)
    else:
        print stderr
        sys.exit(p.returncode)


def get_external_prog(prog):
    """
    Return the external program's path via 'which' UNIX command.
    If not found, print an error message and exit.
    """
    PROG = run('which ' + prog)
    if not PROG:
        print "**************************************************"
        print "%s command not found on the server." % prog
        print "please inform the sysadmins about this situation!"
        print "**************************************************"
        sys.exit(-4)
    return PROG


def get_file_content(fname, commit=""):
    """
    Return fname file's content at the specified commit.
    For the blobs, fname is not given
    """
    if not fname:
        return run('git show %s' % commit, stripped=False)

    return run('git show %s:%s' % (commit, fname), stripped=False)


def get_base_and_commit(fname):
    """
    Return the sha1 for src and dst of the file before the commit
    """
    rv = run("git diff-index HEAD --cached %s" % fname, splitter=" ")
    return rv[2], rv[3]


def get_modified_lines(fname, base, commit):
    """
    Return a list of modified lines from base to commit.
    Inspired from http://stackoverflow.com/a/9506715/566715
    """
    old_content = get_file_content(fname, base)
    new_content = get_file_content(fname, commit)

    d = difflib.Differ()
    diffs = d.compare(old_content.split('\n'), new_content.split('\n'))
    lineNum = 0
    lines = []

    for line in diffs:
    # split off the code
        code = line[:2]
        # if the line is in both files or just b, increment the line number.
        if code in ("  ", "+ "):
            lineNum += 1
        # if this line is only in b, add the line number to lines list.
        if code == "+ ":
            lines.append(lineNum)

    return lines


def pep8(filename, content=None):
    """
    Checks the given file content with pep8.
    run() function is not used here, because of the need
    for p.communicate().
    """
    PEP8 = get_external_prog('pep8')

    if PEP8_IGNORES:
        cmd = PEP8 + " -r --ignore=" + PEP8_IGNORES
    else:
        cmd = PEP8 + " -r"

    if not content:
        cmd = cmd + " " + filename
        return run(cmd)
    else:
        cmd = cmd + " /dev/stdin"
        p = Popen(shlex.split(cmd), stdin=PIPE, stdout=PIPE, stderr=PIPE)
        pep8_output = p.communicate(content)[0]
        return pep8_output.replace("/dev/stdin", filename)


def main():
    """
    main is main
    """
    added_files = run(
        "git diff-index --cached --diff-filter=A HEAD --name-only",
        splitter='\n')
    modif_files = run(
        "git diff-index --cached --diff-filter=M HEAD --name-only",
        splitter='\n')

    #print added_files
    #print modif_files

    pep8_violation = False

    for fname in added_files:
        if fname[-3:] == ".py":
            print "[PEP8] check on newly added file: ", fname
            content = get_file_content(fname)
            pep8_messages = pep8(fname, content)
            if pep8_messages:
                pep8_violation = True
                print pep8_messages

    for fname in modif_files:
        if fname[-3:] == ".py":
            print "[PEP8] check on modified file: ", fname
            content = get_file_content(fname)
            pep8_messages = pep8(fname, content)
            if pep8_messages:
                base, commit = get_base_and_commit(fname)
                modified_lines = get_modified_lines("", base, commit)
                # when splitted with '\n', pep8_messages comes with
                # a '' at the end, skip this.
                for pep8_msg in pep8_messages.split('\n')[:-1]:
                    line_no = pep8_msg.split(":")[1]
                    if int(line_no) in modified_lines:
                        pep8_violation = True
                        print pep8_msg
    #print added_files
    #print modif_files
    if pep8_violation:
        print "******************************************************"
        print "Commit aborted, please fix the related pep8 errors. "
        print "******************************************************"
        sys.exit(-2)

if __name__ == '__main__':
    main()
