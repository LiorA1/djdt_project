#djdt_project

Use:
First time: "docker-compose up"  
Any sequential call: "docker-compose start"  

Note:  
1. See docker-compose.yml file for load data process.  
2. The server is in 8002 port.  
    First view is in: "http://localhost:8002/resumes/"  
        This is a reguler view.  
    Second view is in: "http://localhost:8002/resumes/list"  
        This view is low level cached.  
    
    No view is view-cached.  
