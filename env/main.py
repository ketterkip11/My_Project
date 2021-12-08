import os

os.environ['DATABASE']='universities'
os.environ['USER']='postgres'
os.environ['PASSWORD']='postgres'
os.environ['HOST']='127.0.0.1'
os.environ['PORT']='5432'

DATABASE = os.getenv('DATABASE')
USER =os.getenv('USER')
PASSWORD =os.getenv('PASSWORD')
HOST =os.getenv('HOST')
PORT =os.getenv('PORT')




# DATABASE=universities
# USER=postgres
# PASSWORD="postgres"
# HOST=127.0.0.1
# PORT=5432

# FOO = os.getenv('FOO') # None
# BAR = os.environ.get('BAR') # None
# BAZ = os.environ['BAZ'] # KeyError: key does not exist.


# print(os.environ.get('USER'))

# Import os module
# import os
#
# # Iterate loop to read and print all environment variables
# print("The keys and values of all environment variables:")
# for key in os.environ:
#     print(key, '=>', os.environ[key])
#
# # Print the value of the particular environment variable
# print("The value of HOME is: ", os.environ['HOME'])
#
#

# Import os module
# import os
# # Import sys module
# import sys
#
# while True:
#     # Take the name of the environment variable
#     key_value = input("Enter the key of the environment variable:")
#
#     # Check the taken variable is set or not
#     try:
#         if os.environ[key_value]:
#             print("The value of", key_value, " is ", os.environ[key_value])
#     # Raise error if the variable is not set
#     except KeyError:
#         print(key_value, 'environment variable is not set.')
#         # Terminate from the script
#         sys.exit(1)


# Import os module
# import os
#
# # Checking the value of the environment variable
# if os.environ.get('DEBUG') == 'True':
#     print('Debug mode is on')
# else:
#     print('Debug mode is off')


# Import os module
# import os
#
# # Set the value DEBUG variable
# os.environ.setdefault('DEBUG', 'True')
#
# # Checking the value of the environment variable
# if os.environ.get('DEBUG') == 'True':
#     print('Debug mode is on')
# else:
#     print('Debug mode is off')