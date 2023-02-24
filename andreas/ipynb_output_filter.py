#! /usr/bin/env python

import sys
import nbformat

json_in = nbformat.read(sys.stdin, nbformat.NO_CONVERT)

nb_version = json_in["nbformat"]


if nb_version == 4:
    try: 
        json_in.metadata.language_info.pop("version", None)
    except AttributeError:
        pass
        
    for cell in json_in.cells:
        if "outputs" in cell:
            cell.outputs = []
        if "execution_count" in cell:
            cell.execution_count = None
elif nb_version == 3:
    for sheet in json_in.worksheets:
        for cell in sheet.cells:
            if "outputs" in cell:
                cell.outputs = []
            if "prompt_number" in cell:
                cell.prompt_number = None
else:
    sys.exit("Unknown nbformat " + str(nb_version))

    
nbformat.write(json_in, sys.stdout, nbformat.NO_CONVERT)
