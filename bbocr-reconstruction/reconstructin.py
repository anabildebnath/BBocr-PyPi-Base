import time;
import os;

def reconstruct(directory, img_src_save_dir):
    """
    This function reconstructs the image
    Args:
    directory: Directory containing the images
    img_src_save_dir: Directory to save the image
    """
    directory = "image/"  # Replace with your test directory path
    img_src_save_dir = "image/"  # Replace with your image source directory path

    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):

            file_path = directory + "/" + file_name

            print(
                "----------------------------------------------------------------------------"
            )
            print("File name:", file_name)

            start_time = time.time()
            roi = run_inference(
                file_path, file_name, img_src_save_dir
            )
            print(
                "Execution Time for Layout Prediction and Text Recognition:",
                round(time.time() - start_time, 2),
                "seconds",
            )

            start_time = time.time()
            print(roi)
            generate_html(roi, file_name)
            print(
                "Execution Time for Reconstruction:",
                round(time.time() - start_time, 2),
                "seconds",
            )