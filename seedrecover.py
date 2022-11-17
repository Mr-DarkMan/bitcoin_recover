# If you find this program helpful, please consider a small
# donation to the developer at the following Bitcoin address:
#
#           bc1qpx6jucg6z50tlc8xcdf6gruss848jyawn52yea
#
#                      Thank You!

# PYTHON_ARGCOMPLETE_OK - enables optional bash tab completion

from __future__ import print_function

from btcrecover import btcrseed
import sys, multiprocessing

if __name__ == "__main__":

    print("Starting", btcrseed.full_version())
    btcrseed.register_autodetecting_wallets()
    mnemonic_sentence = btcrseed.main(sys.argv[1:])

    if mnemonic_sentence:
        if not btcrseed.tk_root:  # if the GUI is not being used
            btcrseed.print("Seed found:", mnemonic_sentence)  # never dies from printing Unicode

        # print this if there's any chance of Unicode-related display issues
        if any(ord(c) > 126 for c in mnemonic_sentence):
            print("HTML encoded seed:", mnemonic_sentence.encode("ascii", "xmlcharrefreplace"))

        if btcrseed.tk_root:      # if the GUI is being used
            btcrseed.show_mnemonic_gui(mnemonic_sentence)

        retval = 0

    elif mnemonic_sentence is None:
        retval = 1  # An error occurred or Ctrl-C was pressed inside btcrseed.main()

    else:
        retval = 0  # "Seed not found" has already been printed to the console in btcrseed.main()

    # Wait for any remaining child processes to exit cleanly (to avoid error messages from gc)
    for process in multiprocessing.active_children():
        process.join(1.0)

    sys.exit(retval)
