import os
import json

def convert_bbox(x1, y1, x2, y2):
    """Convert corners (x1, y1, x2, y2) to format (x, y, w, h)."""
    x = x1
    y = y1
    w = x2 - x1
    h = y2 - y1
    return x, y, w, h

def process_json_files(directory , save_dir):
    """Process all JSON files in the specified directory and write detections to respective text files."""
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            # Define the output text file name based on the original JSON file but with a .txt extension
            output_file = os.path.splitext(filename)[0] + '.txt'
            output_file_path = os.path.join(save_dir, output_file)

            with open(file_path, 'r') as f_json, open(output_file_path, 'w') as f_out:
                data = json.load(f_json)
                # Extract detections from each JSON file
                for detection in data.get('detections', []):
                    cls_name = detection['cls_name']
                    conf = detection['conf']
                    bbox = detection['bbox']
                    x, y, w, h = convert_bbox(bbox['x1'], bbox['y1'], bbox['x2'], bbox['y2'])
                    # Write the formatted detection to the output file
                    f_out.write(f"{cls_name} {conf:.6f} {x:.2f} {y:.2f} {w:.2f} {h:.2f}\n")

# Set the directory containing the JSON files
directory_path = 'path/to/detection/jsons'
save_dir = "Object-Detection-Metrics/detections"
os.makedirs(save_dir, exist_ok=True)
process_json_files(directory_path, save_dir)
