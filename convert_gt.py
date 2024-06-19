import os
import json

def convert_to_xywh(x1, y1, x2, y2):
    """Converts bounding box coordinates from (x1, y1, x2, y2) to (x, y, w, h) format."""
    x = x1
    y = y1
    w = x2 - x1
    h = y2 - y1
    return x, y, w, h

def process_ground_truth_files(ground_truth_dir, json_dir, save_dir):
    """Process all JSON ground truth files and convert bounding boxes to the specified format."""
    for filename in os.listdir(ground_truth_dir):
        if filename.endswith('.txt'):
            filename = filename.split(".")[0]
            file_path = os.path.join(json_dir, filename + ".json")
            with open(file_path) as f:
                data = json.load(f)
            
            # image_file = data['file_name']
            # image_path = os.path.join(images_dir, image_file)
            
            # # Ensure the image file exists to prevent errors
            # if not os.path.exists(image_path):
            #     print(f"Image file {image_path} not found, skipping.")
            #     continue

            # with Image.open(image_path) as img:
            #     image_width, image_height = img.size

            output_file = os.path.splitext(filename)[0] + '.txt'
            output_file_path = os.path.join(save_dir, output_file)

            with open(output_file_path, 'w') as f_out:
                for table in data['tables']:
                    coords = table['coordinates']
                    x, y, w, h = convert_to_xywh(coords['x1'], coords['y1'], coords['x2'], coords['y2'])
                    label = "Table"  # Assuming all are tables, adjust as necessary
                    f_out.write(f"{label} {x} {y} {w} {h}\n")

# Specify the directories containing the JSON files and images
ground_truth_dir = 'path/to/files/with/test/txt'
save_dir = "Object-Detection-Metrics/groundtruths2"
json_dir = "path/all/the/jsons"

os.makedirs(save_dir, exist_ok=True)
process_ground_truth_files(ground_truth_dir, json_dir, save_dir)
