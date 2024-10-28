
***
Task Completion Report
Context:

This guide is intended for local setup and testing purposes only. Do not use any credentials you might find in files like docker-compose.yml in production.

Steps Taken:
1. Created a .env file with all the necessary entries. APP_CONFIG__DB__URL is mandatory to start the project and apply initial migrations.
2. Ran the docker-compose up command to start all containers.
3. Applied the latest migrations from the alembic/versions folder using the Alembic upgrade head command.
4. Reviewed the APIs available for further development testing at localhost:8000/docs.

Logging Implementation:
1. The project was successfully set up locally and verified to be running without errors.
2. Configured and implemented logging functionality that records every request to the console and a separate file named pet.log.
The log data includes:
Request URL
Request method
Status code
Total time required to complete the request

3.Additionally, implemented the same logging functionality using a decorator approach to improve code structure and conciseness.

>>>>>>> 7444c28 (Initial commit of petworld-python project)
