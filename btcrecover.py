# If you find this program helpful, please consider a small
# donation to the developer at the following Bitcoin address:
#
#           bc1qpx6jucg6z50tlc8xcdf6gruss848jyawn52yea
#
#                      Thank You!

# PYTHON_ARGCOMPLETE_OK - enables optional bash tab completion

from __future__ import print_function

from btcrecover import btcrpass
import sys, multiprocessing

if __name__ == "__main__":

    print("Starting", btcrpass.full_version(),
          file=sys.stderr if any(a.startswith("--listp") for a in sys.argv[1:]) else sys.stdout)  # --listpass
    btcrpass.parse_arguments(sys.argv[1:])
    (password_found, not_found_msg) = btcrpass.main()

    if isinstance(password_found, basestring):
        btcrpass.safe_print("Password found: '" + password_found + "'")
        if any(ord(c) < 32 or ord(c) > 126 for c in password_found):
            print("HTML encoded:   '" + password_found.encode("ascii", "xmlcharrefreplace") + "'")
        retval = 0

    elif not_found_msg:
        print(not_found_msg, file=sys.stderr if btcrpass.args.listpass else sys.stdout)
        retval = 0

    else:
        retval = 1  # An error occurred or Ctrl-C was pressed

    # Wait for any remaining child processes to exit cleanly (to avoid error messages from gc)
    for process in multiprocessing.active_children():
        process.join(1.0)

    sys.exit(retval)
