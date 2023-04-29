import argparse
import sys
from cmd_utils import *



argparser = argparse.ArgumentParser(description="The stupidest content tracker")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True
argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository.")

argsp = argsubparsers.add_parser("cat-file",
                                 help="Provide content of repository objects")
argsp.add_argument("type",
                   metavar="type",
                   choices=["blob", "commit", "tag", "tree"],
                   help="Specify the type")
argsp.add_argument("object",
                   metavar="object",
                   help="The object to display")

argsp = argsubparsers.add_parser(
    "hash-object",
    help="Compute object ID and optionally creates a blob from a file")

argsp.add_argument("-t",
                   metavar="type",
                   dest="type",
                   choices=["blob", "commit", "tag", "tree"],
                   default="blob",
                   help="Specify the type")

argsp.add_argument("-w",
                   dest="write",
                   action="store_true",
                   help="Actually write the object into the database")

argsp.add_argument("path",
                   help="Read object from <file>")



def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    if args.command == "init":
        cmd_init(args)
    elif args.command == "hash-object": 
        cmd_hash_object(args)
    # if   args.command == "add"         : cmd_add(args)
    # elif args.command == "cat-file"    : cmd_cat_file(args)
    # elif args.command == "checkout"    : cmd_checkout(args)
    # elif args.command == "commit"      : cmd_commit(args)
    # elif args.command == "hash-object" : cmd_hash_object(args)
    # elif args.command == "init"        : cmd_init(args)
    # elif args.command == "log"         : cmd_log(args)
    # elif args.command == "ls-files"    : cmd_ls_files(args)
    # elif args.command == "ls-tree"     : cmd_ls_tree(args)
    # elif args.command == "merge"       : cmd_merge(args)
    # elif args.command == "rebase"      : cmd_rebase(args)
    # elif args.command == "rev-parse"   : cmd_rev_parse(args)
    # elif args.command == "rm"          : cmd_rm(args)
    # elif args.command == "show-ref"    : cmd_show_ref(args)
    # elif args.command == "tag"         : cmd_tag(args)


