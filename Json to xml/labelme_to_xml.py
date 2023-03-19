import json
import os

def labelme_to_xml(labelme_data):
    # Create the XML string
    xml = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    xml += '<annotation>\n'
    xml += '\t<folder>FireData</folder>\n'
    xml += '\t<filename>' + labelme_data['imagePath'].split('/')[-1] + '</filename>\n'
    xml += '\t<path>' + labelme_data['imagePath'] + '</path>\n'
    xml += '\t<source>\n'
    xml += '\t\t<database>Unknown</database>\n'
    xml += '\t</source>\n'
    xml += '\t<size>\n'
    xml += '\t\t<width>' + str(labelme_data['imageWidth']) + '</width>\n'
    xml += '\t\t<height>' + str(labelme_data['imageHeight']) + '</height>\n'
    xml += '\t\t<depth>3</depth>\n'
    xml += '\t</size>\n'
    xml += '\t<segmented>0</segmented>\n'

    # Create object elements for each labelme shape
    for shape in labelme_data['shapes']:
        xml += '\t<object>\n'
        xml += '\t\t<name>' + shape['label'] + '</name>\n'
        xml += '\t\t<pose>Unspecified</pose>\n'
        xml += '\t\t<truncated>0</truncated>\n'
        xml += '\t\t<difficult>0</difficult>\n'
        xml += '\t\t<bndbox>\n'
        points = shape['points']
        xml += '\t\t\t<xmin>' + str(int(min(point[0] for point in points))) + '</xmin>\n'
        xml += '\t\t\t<ymin>' + str(int(min(point[1] for point in points))) + '</ymin>\n'
        xml += '\t\t\t<xmax>' + str(int(max(point[0] for point in points))) + '</xmax>\n'
        xml += '\t\t\t<ymax>' + str(int(max(point[1] for point in points))) + '</ymax>\n'
        xml += '\t\t</bndbox>\n'
        xml += '\t</object>\n'

    xml += '</annotation>'

    # Return the XML string
    return xml

# Define input and output directories
input_directory = 'C:/Users/name/Fire data'
output_directory = 'C:/Users/name/Fire data'

# Create the new directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through each JSON file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.json'):
        # Read the JSON file
        with open(os.path.join(input_directory, filename), 'r') as f:
            labelme_data = json.load(f)

        # Convert the JSON data to Pascal VOC XML format
        xml_data = labelme_to_xml(labelme_data)

        # Write the XML data to a file in the output directory
        with open(os.path.join(output_directory, os.path.splitext(filename)[0] + '.xml'), 'w') as f:
            f.write(xml_data)
