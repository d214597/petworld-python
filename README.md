
***
Task Completion Report Context:

Steps Taken:

I created a .env file with all the necessary entries. APP_CONFIG__DB__URL is mandatory to start the project and apply initial migrations.
Ran the docker-compose-up command to start all containers.
I applied the latest migrations from the Alembic/versions folder using the Alembic upgrade head command.
Reviewed the APIs available for further development testing at localhost:8000/docs.
Logging Implementation:

The project was successfully set up locally and verified to run without errors.
Configured and implemented logging functionality that records every request to the console and a separate file named pet.log. The log data includes: Request URL Request method Status code Total time required to complete the request.
Additionally, implemented the same logging functionality using a decorator approach to improve code structure and conciseness.

>>>>>>> 7444c28 (Initial commit of petworld-python project)
