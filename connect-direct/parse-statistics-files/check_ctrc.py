import os
import re

def process_file(file_path, pnum_dict):
    with open(file_path, 'r') as file:
        for line in file:
            if "PNUM=" in line:
                # Extract PNUM
                pnum_start = line.find("PNUM=") + len("PNUM=")
                pnum_end = line.find("|", pnum_start)
                pnum = line[pnum_start:pnum_end]

                star = line[5:26]

                # Create a dict for PNUM, if not exist
                if pnum not in pnum_dict:
                    pnum_dict[pnum] = {"RECI_PSTR": False, "RECI_CTRC": False, "RECI_PRED": False, "STAR": star}

                # define and update RECID
                if "PSTR" in line:
                    pnum_dict[pnum]["RECI_PSTR"] = True
                if "CTRC" in line:
                    pnum_dict[pnum]["RECI_CTRC"] = True
                if "PRED" in line:
                    pnum_dict[pnum]["RECI_PRED"] = True
                

def process_directory(directory_path):
    pnum_dict = {}
    pattern = re.compile(r"S\d{8}\.\d{3}")

    for filename in os.listdir(directory_path):
        if pattern.match(filename):
            file_path = os.path.join(directory_path, filename)
            process_file(file_path, pnum_dict)


    # Print PNUMs and flags
    for pnum, flags in pnum_dict.items():
       if not pnum_dict[pnum]["RECI_CTRC"]:
           print(f"PNUM={pnum}, RECI_PSTR={flags['RECI_PSTR']}, RECI_CTRC={flags['RECI_CTRC']}, RECI_PRED={flags['RECI_PRED']}, STAR={flags['STAR']}")

# Process in current path:
directory_path = '.'
process_directory(directory_path)
