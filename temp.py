base_path="."

import os
from IPython.display import clear_output

def auto_install():
    global base_path

    # Remove existing 'DH_live' folder if it exists
    dh_live_path = os.path.join(base_path, "DH_live")
    if os.path.exists(dh_live_path):
        os.system(f"rm -rf {dh_live_path}")
    
    # Clone the repository
    os.system(f"git clone https://github.com/kleinlee/DH_live.git {dh_live_path}")
    
    # Concatenate parts of the checkpoint file (assuming they're in the right place)
    checkpoint_path = os.path.join(dh_live_path, "checkpoint")
    render_files = [
        os.path.join(checkpoint_path, "render.pth.gz.001"),
        os.path.join(checkpoint_path, "render.pth.gz.002")
    ]
    os.system(f"cat {' '.join(render_files)} > {os.path.join(checkpoint_path, 'render.pth.gz')}")
    
    # Decompress the gzipped file
    os.system(f"gzip -d -c {os.path.join(checkpoint_path, 'render.pth.gz')} > {os.path.join(checkpoint_path, 'render.pth')}")
    
    # Clear output (for Jupyter or IPython environments)
    clear_output()

# Run the installation process
auto_install()



import os
import re 
import uuid 
import shutil
import uuid 
import click
import gradio as gr

def clean_file_name(file_path):
    # Get the base file name and extension
    file_name = os.path.basename(file_path)
    file_name, file_extension = os.path.splitext(file_name)

    # Replace non-alphanumeric characters with an underscore
    cleaned = re.sub(r'[^a-zA-Z\d]+', '_', file_name)

    # Remove any multiple underscores
    clean_file_name = re.sub(r'_+', '_', cleaned).strip('_')

    # Generate a random UUID for uniqueness
    random_uuid = uuid.uuid4().hex[:6]

    # Combine cleaned file name with the original extension
    clean_file_path = os.path.join(os.path.dirname(file_path), clean_file_name + f"_{random_uuid}" + file_extension)

    return clean_file_path

def run_lipsync_process(video_path, audio_path):
    """
    Run the entire lip-sync process:
    1. Extract keypoints from the video
    2. Find the folder created by keypoint extraction
    3. Run the lip-sync demo
    4. Return the output path of the generated video
    """
    global base_path
    # Define folder paths
    vid_folder = os.path.join(base_path, "DH_live","video_data")
    result_folder = os.path.join(base_path,"DH_live","result")
    
    # Create the result folder if it doesn't exist
    os.makedirs(result_folder, exist_ok=True)

    # Define the output path
    output_path = os.path.join(result_folder, os.path.basename(video_path))

    def list_folders(path):
        """Return a list of directories (folders) within the specified path."""
        try:
            return [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]
        except OSError as e:
            print(f"Error listing folders in {path}: {e}")
            return []

    def find_new_folder(old_folders):
        """Return the first new folder found in vid_folder."""
        try:
            new_folders = list_folders(vid_folder)
            for folder in new_folders:
                if folder not in old_folders:
                    return os.path.join(vid_folder, folder)
        except Exception as e:
            print(f"Error finding new folder: {e}")
        return None

    def run_command(command):
        """Execute a shell command and return True if it succeeded, else False."""
        try:
            return os.system(command) == 0
        except Exception as e:
            print(f"Error running command '{command}': {e}")
            return False

    # Step 1: Record the initial folder list in vid_folder
    initial_folders = list_folders(vid_folder)

    # Step 2: Extract keypoints from the video
    keypoint_command = f"python {base_path}/DH_live/data_preparation.py {video_path}"
    print(f"Input Video Save at: {video_path}")
    print(f"Input Audio Save at: {audio_path}")
    print("Extracting lip keypoints from the video.")
    if run_command(keypoint_command):
        # Step 3: Find the new folder created by keypoint extraction
        video_folder = find_new_folder(initial_folders)
        print(f"Successfully generated keypoint_rotate.pkl from the video.")
        if video_folder:
            # Step 4: Run the lip-sync demo with the extracted video folder
            print(f"Lip sync started.")
            lipsync_command = f"python {base_path}/DH_live/demo.py {video_folder} {audio_path} {output_path}"
            if run_command(lipsync_command):
                print(f"Lip sync ended.")
                # Step 5: Check if output file was created successfully
                if os.path.exists(output_path):
                    print(f"Lip-sync completed successfully. Output saved at: {output_path}")
                    return output_path  # Return the path of the saved output
                else:
                    print("Failed to generate output file. Output path does not exist.")
            else:
                print("Lip-sync process failed. Command execution failed.")
                print(f"Command: {lipsync_command}")
        else:
            print("No new folder found after keypoint extraction.")
    else:
        print("Failed to extract keypoints from video.")
        print(f"Command: {keypoint_command}")
    
    return None  # Return None if the process failed at any step


# Example usage
# video_path = "/content/video.mp4"
# audio_path = "/content/video.WAV"
# output_video = run_lipsync_process(video_path, audio_path)


def gradio_call(input_video, input_audio):
    """
    Handle the lip-sync process and launch the Gradio interface with the command-line options.
    """
    upload_video = clean_file_name(f"{base_path}/DH_live/video_data/{os.path.basename(input_video)}")
    upload_audio = clean_file_name(f"{base_path}/DH_live/video_data/{os.path.basename(input_audio)}")
    
    shutil.copy(input_video, upload_video)
    shutil.copy(input_audio, upload_audio)
    
    # Run lip-sync process
    lip_sync_video = run_lipsync_process(upload_video, upload_audio)
    
    # Return the lip-sync video path for downloading
    return lip_sync_video

@click.command()
@click.option("--debug", is_flag=True, default=False, help="Enable debug mode.")
@click.option("--share", is_flag=True, default=False, help="Enable sharing of the interface.")
def main(debug, share):
    # Example inputs for Gradio interface
    demo_examples = [[f"{base_path}/video_data/demo.mp4", f"{base_path}/video_data/audio0.wav"]]

    # Define Gradio inputs and outputs
    gradio_inputs = [
        gr.File(label="Upload Video", type="filepath"),
        gr.File(label="Upload Audio", type="filepath")
    ]

    gradio_outputs = [gr.File(label="Download LipSync Video", show_label=True)]

    # Define and configure the Gradio interface
    demo = gr.Interface(fn=gradio_call, inputs=gradio_inputs, outputs=gradio_outputs,
                        title="DH_live LipSync Base Model",examples=demo_examples)

    demo.queue().launch(allowed_paths=[f"{base_path}/result"],debug=debug, share=share)

if __name__ == "__main__":
    main()

