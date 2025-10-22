
# Create updated Hobbies page with new background color and menu order

hobbies_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hobbies & Interests - CV</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Times New Roman', Times, serif;
            background-color: #5293c9;
            color: #333;
            line-height: 1.6;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 50px;
            border-bottom: 3px solid #366e81;
            background-color: rgba(255, 255, 255, 0.95);
        }

        .name {
            font-size: 2.5em;
            font-weight: bold;
            color: #103250;
        }

        .photo-placeholder {
            width: 150px;
            height: 150px;
            border: 3px solid #366e81;
            border-radius: 50%;
            background-color: #f0f0f0;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #558a9b;
            font-size: 0.9em;
            text-align: center;
        }

        .hamburger {
            position: fixed;
            top: 30px;
            left: 30px;
            z-index: 1000;
            cursor: pointer;
            background-color: #366e81;
            padding: 10px;
            border-radius: 5px;
        }

        .hamburger div {
            width: 30px;
            height: 3px;
            background-color: white;
            margin: 6px 0;
            transition: 0.4s;
        }

        .side-menu {
            position: fixed;
            left: -300px;
            top: 0;
            width: 300px;
            height: 100%;
            background-color: #376475;
            padding: 80px 20px 20px 20px;
            transition: 0.4s;
            z-index: 999;
            box-shadow: 2px 0 10px rgba(0,0,0,0.1);
            overflow-y: auto;
        }

        .side-menu.active {
            left: 0;
        }

        .menu-section {
            margin-bottom: 30px;
        }

        .menu-section h3 {
            color: #ffffff;
            font-size: 1.2em;
            margin-bottom: 15px;
            border-bottom: 2px solid #558a9b;
            padding-bottom: 10px;
        }

        .menu-section a {
            display: block;
            color: #ffffff;
            text-decoration: none;
            padding: 12px 15px;
            margin: 5px 0;
            border-radius: 5px;
            transition: 0.3s;
        }

        .menu-section a:hover {
            background-color: #558a9b;
            padding-left: 25px;
        }

        .contact-info {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #558a9b;
        }

        .contact-item {
            color: #ffffff;
            padding: 8px 0;
            font-size: 0.95em;
            cursor: pointer;
            word-wrap: break-word;
        }

        .contact-item:hover {
            color: #558a9b;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 50px;
        }

        .section {
            margin-bottom: 50px;
            padding: 30px;
            background-color: rgba(255, 255, 255, 0.95);
            border-left: 5px solid #366e81;
            border-radius: 5px;
        }

        .section h2 {
            color: #103250;
            font-size: 2em;
            margin-bottom: 20px;
            border-bottom: 2px solid #558a9b;
            padding-bottom: 10px;
        }

        .section h3 {
            color: #376475;
            font-size: 1.5em;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .text-box {
            background-color: #ffffff;
            padding: 20px;
            border: 1px solid #558a9b;
            border-radius: 5px;
            margin-bottom: 20px;
            color: #333;
        }

        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.5);
            display: none;
            z-index: 998;
        }

        .overlay.active {
            display: block;
        }

        @media (max-width: 768px) {
            .header {
                flex-direction: column;
                text-align: center;
                padding: 20px;
            }

            .name {
                font-size: 1.8em;
                margin-bottom: 20px;
            }

            .container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="hamburger" onclick="toggleMenu()">
        <div></div>
        <div></div>
        <div></div>
    </div>

    <div class="side-menu" id="sideMenu">
        <div class="menu-section">
            <h3>Navigation</h3>
            <a href="index.html">Home</a>
            <a href="skills.html">Skills</a>
            <a href="projects.html">Projects & Certifications</a>
            <a href="volunteering.html">Volunteering</a>
            <a href="hobbies.html">Hobbies & Interests</a>
            <a href="your-cv-file.pdf" download>Download My CV</a>
        </div>
        
        <div class="contact-info">
            <h3>Contact</h3>
            <div class="contact-item" onclick="copyToClipboard('your.email@example.com')">
                📧 your.email@example.com
            </div>
            <div class="contact-item" onclick="copyToClipboard('+39 123 456 7890')">
                📱 +39 123 456 7890
            </div>
            <div class="contact-item" onclick="copyToClipboard('Your Address, City, Country')">
                📍 Your Address, City, Country
            </div>
            <div class="contact-item" onclick="copyToClipboard('linkedin.com/in/yourprofile')">
                💼 LinkedIn Profile
            </div>
        </div>
    </div>

    <div class="overlay" id="overlay" onclick="toggleMenu()"></div>

    <div class="header">
        <div class="name">Your Full Name</div>
        <div class="photo-placeholder">
            Your Photo Here
        </div>
    </div>

    <div class="container">
        <div class="section">
            <h2>Hobbies</h2>
            
            <div class="text-box">
                <h3>Hobby 1</h3>
                <p>
                    Describe this hobby in detail. Explain what you enjoy about it, 
                    how long you've been pursuing it, and any notable achievements or 
                    experiences related to it. Share how this hobby contributes to your 
                    personal development or work-life balance.
                </p>
            </div>

            <div class="text-box">
                <h3>Hobby 2</h3>
                <p>
                    Describe this hobby in detail. Explain what you enjoy about it, 
                    how long you've been pursuing it, and any notable achievements or 
                    experiences related to it. Share how this hobby contributes to your 
                    personal development or work-life balance.
                </p>
            </div>

            <div class="text-box">
                <h3>Hobby 3</h3>
                <p>
                    Describe this hobby in detail. Explain what you enjoy about it, 
                    how long you've been pursuing it, and any notable achievements or 
                    experiences related to it. Share how this hobby contributes to your 
                    personal development or work-life balance.
                </p>
            </div>
        </div>

        <div class="section">
            <h2>Interests</h2>
            
            <div class="text-box">
                <h3>Professional Interests</h3>
                <p>
                    Describe your professional interests and areas you're passionate about 
                    in your field. Include topics you're currently exploring, technologies 
                    or methodologies you're interested in learning, and how these interests 
                    align with your career goals.
                </p>
            </div>

            <div class="text-box">
                <h3>Personal Interests</h3>
                <p>
                    Share your personal interests beyond work. This could include cultural 
                    activities, sports, arts, travel, reading preferences, or any other 
                    areas that contribute to your well-rounded personality. Explain how 
                    these interests enrich your life and potentially complement your 
                    professional skills.
                </p>
            </div>

            <div class="text-box">
                <h3>Learning & Development</h3>
                <p>
                    Describe your commitment to continuous learning and personal development. 
                    Include areas you're currently studying, courses you're taking, or skills 
                    you're developing. Demonstrate your curiosity and dedication to growth 
                    both personally and professionally.
                </p>
            </div>
        </div>
    </div>

    <script>
        function toggleMenu() {
            const menu = document.getElementById('sideMenu');
            const overlay = document.getElementById('overlay');
            menu.classList.toggle('active');
            overlay.classList.toggle('active');
        }

        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                alert('Copied to clipboard: ' + text);
            }).catch(err => {
                console.error('Failed to copy: ', err);
            });
        }

        document.querySelectorAll('.side-menu a').forEach(link => {
            link.addEventListener('click', () => {
                toggleMenu();
            });
        });
    </script>
</body>
</html>'''

with open('hobbies.html', 'w', encoding='utf-8') as f:
    f.write(hobbies_html)

print("Updated hobbies.html created successfully!")
print("\n=== ALL UPDATED HTML FILES CREATED ===")
print("\nChanges applied:")
print("✓ Background color changed to #5293c9")
print("✓ Phone contact moved above address in menu")
print("✓ New 'Skills' page added (appears before Projects in menu)")
print("✓ Projects page: reduced to 1 project")
print("✓ Projects page: reduced to 2 certifications")
print("✓ Volunteering page: reduced to 1 experience")
print("\nFiles updated:")
print("1. index.html - Main page")
print("2. skills.html - NEW Skills page with 'Job Related' and 'Soft Skills' sections")
print("3. projects.html - 1 project, 2 certifications")
print("4. volunteering.html - 1 volunteer experience")
print("5. hobbies.html - Updated with new styling")
