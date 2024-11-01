"""
Matt Sowers
Module 08 Lab Assignment: Part B

This script picks a random number from 1-10 and then creates a html page that write Hello World! the number of times
the random number is and also displays an image located in the folder. .
"""
# import random
import random

# set random_number as random number from 1-10
random_number = random.randint(1, 10)

# setup html content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World!</title>
    <style>
        body {{
            background-color: #333;
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            text-align: center;
        }}
        h1 {{
            font-size: 3em;
            margin: 0.2em 0;
        }}
        img {{
            margin-top: 1em;
            width: 300px;
            height: auto;
        }}
    </style>
</head>
<body>
"""

# add Hello World! to html
for i in range(random_number):
    html_content += "<h1>Hello World!</h1>\n"

# add an external image
html_content += """
    <img src="image1.png" alt="A meme with: my program: *works perfectly*, me: *cleans up code*, also my program:  
    a picture of Pingu with his arms crossed saying 'well now I am not doing it'">
</body>
</html>
"""

# create and write html file
with open("hello_world.html", "w") as file:
    file.write(html_content)

# print that the html file was generated
print("HTML file 'hello_world.html' has been created")