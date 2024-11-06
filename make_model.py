import gzip
import shutil
import os

def merge_and_decompress(directory, part_files, gz_output="render.pth.gz", decompressed_output="render.pth"):
    # Ensure directory path is appended correctly
    gz_output_path = os.path.join(directory, gz_output)
    decompressed_output_path = os.path.join(directory, decompressed_output)

    # Step 1: Concatenate files
    with open(gz_output_path, "wb") as outfile:
        for part in part_files:
            part_path = os.path.join(directory, part)  # Prepend directory path
            with open(part_path, "rb") as infile:
                shutil.copyfileobj(infile, outfile)
    
    # Step 2: Decompress the gzipped file
    with gzip.open(gz_output_path, "rb") as f_in:
        with open(decompressed_output_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    print("Files concatenated and decompressed successfully.")
    return decompressed_output_path
directory = "./checkpoint"
part_files = ["render.pth.gz.001", "render.pth.gz.002"]
merge_and_decompress(directory, part_files, gz_output="render.pth.gz", decompressed_output="render.pth")
