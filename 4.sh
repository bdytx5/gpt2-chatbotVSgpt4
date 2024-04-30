#!/bin/bash

# Define the directory for the website files
dir="vr_sports_simulation_website"

# Create the directory if it doesn't exist
mkdir -p $dir

# Navigate into the directory
cd $dir

# Create an HTML file for the website
cat > index.html <<EOL
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VR Sports Simulation</title>
</head>
<body>
    <header>
        <h1>Welcome to VR Sports Simulation</h1>
        <p>Experience the future of sports!</p>
    </header>
    <section>
        <h2>About Us</h2>
        <p>VR Sports Simulation is a leading provider of virtual reality sports experiences, allowing users to immerse themselves in a variety of sports simulations. Whether you're training for the big leagues or just looking to have fun, our simulations offer an unparalleled level of realism and engagement.</p>
    </section>
    <section>
        <h2>Services</h2>
        <ul>
            <li>Custom Sports Simulations</li>
            <li>Training Programs for Athletes</li>
            <li>Interactive Sports Exhibitions</li>
        </ul>
    </section>
    <footer>
        <p>Contact us at info@vrsportssim.com</p>
    </footer>
</body>
</html>
EOL

# Open the website in the default browser
open index.html

