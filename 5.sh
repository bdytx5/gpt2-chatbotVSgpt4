#!/bin/bash

# Define directory name and check if it exists
DIR="VRSportsSimCompany"
if [ -d "$DIR" ]; then
  echo "Directory $DIR already exists"
else
  mkdir $DIR
fi

cd $DIR

# Create HTML file
cat <<EOF >index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VR Sports Simulation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>VR Sports Simulation</h1>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <section id="about">
        <h2>About Us</h2>
        <p>Welcome to VR Sports Simulation, your number one source for immersive virtual reality sports experiences. Our company specializes in creating realistic sports simulations that allow you to play and feel as if you're on the field, court, or track.</p>
    </section>
    <section id="services">
        <h2>Services</h2>
        <p>We offer a variety of VR sports services, including but not limited to:</p>
        <ul>
            <li>Football Simulation</li>
            <li>Basketball Simulation</li>
            <li>Track and Field Events</li>
            <li>Customizable Player Stats and Teams</li>
        </ul>
    </section>
    <section id="contact">
        <h2>Contact Us</h2>
        <p>For any inquiries, please email us at: <a href="mailto:contact@vrsportssim.com">contact@vrsportssim.com</a></p>
    </section>
    <footer>
        <p>© 2024 VR Sports Simulation Company. All rights reserved.</p>
    </footer>
</body>
</html>
EOF

# Create CSS file
cat <<EOF >styles.css
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background: #f4f4f4;
    color: #333;
}
header, section, footer {
    margin: 20px;
    padding: 20px;
    background: #fff;
}
header {
    background: #0073e6;
    color: #fff;
}
nav ul {
    list-style: none;
    padding: 0;
}
nav ul li {
    display: inline;
    margin-right: 10px;
}
nav ul li a {
    color: #fff;
    text-decoration: none;
}
a {
    color: #0073e6;
}
footer {
    text-align: center;
    background: #222;
    color: #fff;
}
EOF

# Open the website in the default browser
if command -v xdg-open > /dev/null; then
    xdg-open index.html
elif command -v open > /dev/null; then
    open index.html
else
    echo "Could not detect the web browser to open the file automatically."
fi
