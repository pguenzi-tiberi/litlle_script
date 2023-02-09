#!/usr/bin/env python3

import argparse
import os
import sys
import time
import shutil
from Bio import SeqIO

def run() :
    parser = argparse.ArgumentParser(
        prog="gff_builder_trinotate",
        description="\n\n A little program to make a gff from trinotate report and other files ",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=True,
    )

    mandatory_args = parser.add_argument_group("Mandatory arguments")

    # Mandatory arguments

    # Trinotate report
    
    mandatory_args.add_argument(
        "--fasta_file",
        "-i",
        action="store",
        dest="fasta_file",
        help="FASTA file of the genome which will be integrated into a kraken2 database",
        default="",
        required=True,
    )

    mandatory_args.add_argument(
        "--tax_id",
        "-t",
        action="store",
        dest="tax_id",
        help="NCBI taxonomy ID of the organism",
        default="",
        required=True,
    )
   
    args = parser.parse_args()
    actual_path = os.getcwd()

    global_start = time.perf_counter()
    file_finished = open("fasta_modified.fa", "w+")
    for seq_record in SeqIO.parse(args.fasta_file, "fasta"):
        seq_record_modified=">"+seq_record.id+"|kraken:taxid|"+args.tax_id
        file_finished.write(str(seq_record_modified)+"\n")
        file_finished.write(str(seq_record.seq)+"\n")

    print(
        f"\n Total running time : {float(time.perf_counter() - global_start)} seconds"
    )



if __name__ == '__main__':
    run()