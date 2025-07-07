Imported Libraries:
pandas, ipaddress, matplotlib, os

Instructions to Run Script Locally:
- Ensure you've installed the following Python libraries: pandas, matplotlib, openpyxl
Also install these system dependencies (for Linux): build-essential, libfreetype6-dev, libpng-dev
- Place all project files in the same directory: subnet_analyzer.py , visualize.py , ip_data.xlsx
- If you're using Windows:
- Open the script in your IDE
- Modify the path parameters in the following sections:
- In the main function: ip = read_filedata('your_absolute_path/ip_data.xlsx', 'IP Address')
- In the export_data_csv function: data_after_process.to_csv('your_absolute_path/output/subnet_report.csv', index=False)
                                   os.makedirs('your_absolute_path/output', exist_ok=True)
- Linux users can skip this step.

- Run the script. You'll be greeted with an interactive CLI program.
  
- Important Note!!!!! Follow the function sequence correctly as they depend on each other.
- Choose 1: Read data from file (must be first)
- Choose 2: List CIDR notation of IPs and subnet masks
- Choose 3: List network addresses
- Choose 4: List broadcast addresses
- Choose 5: List number of usable hosts per network
- Choose 6: Group IPs by subnet (returns list of dictionaries)
- Choose 7: Export all data into a CSV file (saved in output directory)
- Choose 8: Generate a bar chart for host counts per subnet (saved in output directory)
- Choose 9: Terminate CLI program
Note: Do not enter any choices except those listed. Invalid inputs will raise the error:
"Invalid choice. Please select from 0 to 8."

Instructions to Run Script through Docker:
- Make sure Docker is installed.
- Test Docker with: sudo docker run hello-world
- Ensure the following files are in the same directory: subnet_analyzer.py , visualize.py , ip_data.xlsx , Dockerfile
- Build your image: sudo docker build -t image_name .
- Confirm image creation with: sudo docker images
- 
  Important note!!!!!!!!!!!! --> make sure to run the container in interactive mode by adding -it to running command or it will through an error #Our script is interactive cli [Dont Forget]
  Another important note!!!!! --> add option -v to run command to make bind mount between linked_dir on your local and dir on container to get copy of output files [export csv file-plot.png] we dont have ability to visualzie plot here so we just export files    in linked_dir (adjust it as you wish , empty dir preferable) from dir on container [/app/ouptut] which files generated in
- Run the container in interactive mode and bind your local output directory: sudo docker run -it -v /your/local/dir:/app/output --name container_name image_name
- This allows the container to save exported files in your local directory.
- Adjust /your/local/dir as needed. An empty folder is recommended.
- All container-generated files are located in /app/output

- Once inside the container, you'll see the same CLI program.
- Follow the same function sequence as in the local setup.
- After exiting the CLI, check container status: sudo docker ps -a
- If needed, stop container manually: sudo docker stop container_name
- Take a look on your local directory. You’ll find the exported CSV and bar chart image.
