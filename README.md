Instructions to run script locally:
(1) Make sure that you have already installed libraries: pandas , matplotlib ,openxyl and their dependencies (uild-essential,libfreetype6-dev,libpng-dev) for python
(2) Move all files in same directory subnet_analyzer.py , visualize.py , ip_data.xlsx 
(3) In case of windows user: open source code of script by IDE,change path parameter to your absolute path in main function (ip = read_filedata('path','IP Address')) ,
    export_data_csv function ( data_after_process.to_csv('path', index=False)   ,   os.makedirs('path/output', exist_ok=True) )
    -like that main funcion : ip = read_filedata('your_absolute_path/ip_data.xlsx','IP Address')
               export_data_csv function : data_after_process.to_csv('your_absolute_path/output/subnet_report.csv', index=False)
               export_data_csv function : os.makedirs('your_absolute_path/output', exist_ok=True)
   In case of linux user : ignore this step and move to the next one

(4) start running the script ,then you will find an interactive cli program 

Important Note!!!!!
(5) You should run program in specific sequence (functions depend on each other)
    choose 1 : To read the data from file      ##necessary for next steps
    then choose 2 : To get list of CIDR Notation of IPs and subnet masks    (depends on choice #1)
         choose 3 : To get list of network addresses of IPs and subnet masks    (depends on choice #1)
         choose 4 : To get list of broadcast  addresses of IPs and subnet masks    (depends on choice #1)
         choose 5 : To get list of number of usable hosts of each network    (depends on choice #1)
         choose 6 : To group IPs by subnets as list of dictionaries[key pairs]    (depends on choice #1)
         choose 7 : To export all previous data into csv file [called subnet_report.csv in output directory]   (depends on choices #1,2,3,4,5)
         choose 8 : To visualize the relation of number of hosts per subnet through bar chart and export the plot [in /output directory]  (depends on choices #1,5)
         choose 9 : To terminate the cli program
    Note:
    Dont enter choice except those which listed above , it will throw error exception message "Invalid choice. Please select from 0 to 8."



Instructions to run script through docker:
(1) Make sure that you have already installed Docker
(2) Test docker :sudo docker run hello-world     #It should return response
(3) Make sure you have the Dockerfile in same directory of subnet_analyzer.py, visualize.py, ip_data.xlsx

let's get started with docker
(4) build your image with docker file through command :sudo docker build -t image_name .   #(.) refers to location of Docker file that we have already move it to same dir
(5) check list of images to make sure it is created through command :sudo docker images

Important note!!!!!!!!!!!!
- make sure to run the container in interactive mode by adding -it to running command or it will through an error   #Our script is interactive cli [Dont Forget]
Another important note!!!!!
- add option -v to run command to make bind mount between linked_dir on your local and dir on container to get copy of output files [export csv file-plot.png]
  we dont have ability to visualzie plot here so we just export files in linked_dir (adjust it as you wish , empty dir preferable) 
  from dir on container [/app/ouptut] which files generated in 
(6) Run container from image through command :sudo docker run -it -v local_dir:/app/output --name container_name image_name

-Docker Container and script already run you will find an interactive cli program

(7) important Note!!!!!
You should run program in specific sequence (functions depend on each other)
    choose 1 : To read the data from file      ##necessary for next steps
    then choose 2 : To get list of CIDR Notation of IPs and subnet masks    (depends on choice #1)
         choose 3 : To get list of network addresses of IPs and subnet masks    (depends on choice #1)
         choose 4 : To get list of broadcast  addresses of IPs and subnet masks    (depends on choice #1)
         choose 5 : To get list of number of usable hosts of each network    (depends on choice #1)
         choose 6 : To group IPs by subnets as list of dictionaries[key pairs]    (depends on choice #1)
         choose 7 : To export all previous data into csv file [called subnet_report.csv in [/output directory]   (depends on choices #1,2,3,4,5)
         choose 8 : To export the bar chart plot [in /output directory]  (depends on choices #1,5)
         choose 9 : To terminate the cli program and container
    Note:
    Dont enter choice except those which listed above , it will throw error exception message "Invalid choice. Please select from 0 to 8."

(8) Check the statues of containers through command :sudo docker ps -a       #you will found that our container exited moments ago
(9) if not stop it manually through command : sudo docker stop [conainer_name or container_ID]
(10) Take a look on linked local directory which mounted with directory of container , you will find exported files [exported csv file and barchart plot]
