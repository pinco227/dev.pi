# {π} Dev.PI

**Dev.PI** is a Developer's Portfolio which also serves as a Milestone Project for the **Software Developer Diploma** programme of **Code Institute**.

## Table of Contents
  - [Demo](#demo)
  - [UX](#ux)
    - [Goals](#goals)
    - [User Needs](#users-needs)
    - [User Scenarios](#user-scenarios)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
      - [Wireframes](#initial-wireframes)
      - [Improvements](#improvements)
    - [Design Choices](#design-choices)
  - [Features](#features)
  - [Database](#database)
  - [Technologies used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Demo

### [Live website](https://dev-pi.herokuapp.com/)

[![Screenshot](https://github.com/pinco227/dev.pi/blob/main/docs/screenshot.jpg)](https://dev-pi.herokuapp.com/)

## UX

- ### Goals
  - The main goal is to get clients/contracts (job offers).
  - Expand online presence.
  - Present previous work (portfolio).
  - Present biography, skills, education, experience, links and CV.
  - Receive feedback/testimonials from clients/collaborators.
- ### Users Needs
  - Need to learn about the showcased developer.
  - Need of an up to date portfolio with previews and source code (where applicable).
  - Need of an up to date list of skills, education, experience.
  - Need to be able to download resume.
  - Need to be able to contact the developer if interested.
- ### User Scenarios
  - #### As a potential employer/recruiter I need:
    - To learn about the candidate's professional profile without having to click too many times and look too deep.
    - To be able to download the candidate's CV for print/file purposes.
    - To learn about the developer's current status and availability.
    - To be able to contact the candidate to further asses and discuss eventual contract/employment.
    - To see candidate's education, previous work experience and projects (including written code).
    - To find candidate's other relevant social profiles, for a deeper insight (linkedin, github).
    - To find more about the person behind the title, to understand how he got into software development, how passionate and motivated he is.
    - To find what other people say about the developer (testimonials).
  - #### As a potential collaborator I need:
    - To be able to explore developer's work, written code and skillset to understand if he is fit to my project idea.
    - To learn about the developer, personally, to see if he is compatible to work with.
    - To be able to contact the developer.
    - To connect with developer on other relevant social platforms.
  - #### As a user (of any kind) I need:
    - To easily understand the purpose of the website.
    - To easily navigate throughout the website on any device/platform.
    - To be able to write a testimonial
  - #### As the developer I need:
    - To be able to add, update and delete skills, education, work experience, portfolio projects and links.
    - To be able to update my current status, availability and contact information.
    - To be able to post, edit and delete personal blogs.
    - To be able to manage (approve, remove) user's testimonials.
    - To be able to update hero name, short bio, photo and CV.
    - To be able to update website's metadata and admin password.
- ### Structure
    The website is designed to be consistent, intuitive and learnable.
  - Interaction design
    - For predictability, the interface interacts with user actions as the user expects. The scroll/swipe actions respond with the normal behaviour and buttons acts instantly on press.
    - For consistency, the interface offers a subtle visual feedback to the user (on hover, focus and press of buttons and fields) which is similar throughout the application and helps the user to quickly learn the functionality.
  - Information architecture
    - The content is organised and prioritised by importance from top to bottom and left to right.
    - For consistency, the information is presented in the rule of 3 on large screens and individual on small screens.
    - The information is structured mostly in nested lists.
- ### Skeleton
  - ### Initial wireframes
    - Client Side:
      - Landing page [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/landing_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/landing_desktop.png)
      - Projects page [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/projects_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/projects_desktop.png)
      - Project details [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/project_details_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/project_details_desktop.png)
      - Blogs page [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/blog_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/blog_desktop.png)
      - Blog Post page [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/blog_post_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/blog_post_desktop.png)
      - Contact page [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/contact_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/contact_desktop.png)
    - Admin access:
      - Dashboard [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/dashboard_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/dashboard_desktop.png)
      - Get Items (list) [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/get_items_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/get_items_desktop.png) (universal wireframe for all items stored in database)
      - Create/Update (item) [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/create_update_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/create_update_desktop.png) (universal wireframe for all items stored in database)
      - Settings [mobile](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/settings_mobile.png) / [desktop](https://github.com/pinco227/dev.pi/blob/main/docs/wireframes/settings_desktop.png)
  - ### Improvements
    - #### **Client Side**:
      - **All pages**: Breadcrumbs between header and content
      - **Landing page**: Icons for education and experience items but no icon for testimonials.
      - **Blog Post page**: The post cover photo is displayed on the left.
      - **Contact page**: Profile Picture is displayed instead of person icon and is not hidden on mobile.
    - #### **Admin Panel**:
      - #### All pages:
        - The layout is completely separate and different from the client side, different navbar which only includes **App** and **Logout** buttons and the menu panel is now a full height sidebar, no footer.
        - On mobile, menu is expandable from the navbar and it covers the whole page.
        - A svg image on top right of every page (centred on mobile), representing the page's subject.
      - #### Dashboard:
        - Notifications panel is displayed in yellow and only if there are notifications.
        - Extra panel with quick links.
      - #### Get Items (list) page
        - Preview button for blogs and projects and no edit button for testimonials, skills and links.
      - #### Update (item) page and Settings page
        - There is a new panel for drag&drop photo upload on blog and project and edit page and on settings page, displayed beside the initial form.
- ### Design Choices 
  - #### Colours
    - The colour palette consists of different shades of blue inspired by the "Colours of Santorini".  
    ![Colour Palette](https://github.com/pinco227/dev.pi/blob/main/docs/palette.png)
    - According to [The Psychology of Color](https://www.toptal.com/designers/ux/color-in-ux), the chosen colours represent optimism, loyalty and reliability.
    ![Colour Psychology Wheel](https://github.com/pinco227/dev.pi/blob/main/docs/colour-wheel.jpg)  
    - The 60-30-10 Rule was also taken into consideration when building the project. The light shades which are used mostly for background are considered neutral and makes up to 60% of the palette. The dark shades are complementary and makes up to 30% while the accent colours completes the remaining 10% of the design. The landing page is an exception from this rule as it is divided into multiple sections and uses all colours to create contrast between these.
  - #### Typography
    There are three fonts used throughout the project. Two main fonts used for content and headings, both having a ```sans-serif``` typeface and fallback . These font-faces inspire a clean and modern aspect. The third font is a ```monospace``` typeface used for brand text (logo) only to make it look like a piece of code:
    - [Lato](https://fonts.google.com/specimen/Lato?query=lato) is used as a general font.
    - [Alegreya Sans](https://fonts.google.com/specimen/Alegreya+Sans?query=Alegreya+Sans) is used for h1, h2 and h3 headings.
    - [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro?query=Source+Code+Pro) is used for brand text and it has a ```monospace``` fallback.
  - #### Media
    The only media used on building this project are svg (inline html paths) section separators on the client side, svg minimalistic images on admin panel on top of every page and a ***"no-photo"*** image used as a fallback for any image issue. Any other media found on the app is added through the admin panel and is relevant to its container.
  - #### Iconography
    Icons are used throughout the project to help user understand more efficiently the meaning of the content. They are a very good asset to improve UX.

## Features
- ### Planned features
  - #### **Navigation Bar**
    - Allows users to navigate through the website. The navigation will be fixed to top and visible all the time. Links will be collapsed on small screens.
  - #### **Landing Page**
    - ***Hero*** featuring a title (dev's name), a short bio, current status and availability and two *Call-to-Action* buttons: **Download CV** and **Learn more**.
    - ***Skillset*** section where dev's skills will be presented as progress bars.
    - ***Education*** section.
    - ***Work Experience*** section.
    - ***Testimonials***.
  - #### **Projects Page**
    - Projects will be listed on a different page, as a detailed gallery, with quick access links and link to an individual project page for each.
  - #### **Blog**
    - Blogs will be presented on a different page, with further individual page for each post.
  - #### **Contact Page**
    - Contact details, social links and a contact form.
  - #### **Write Testimonial**
    - Individual page with a simple form to write testimonials, accessible to all users.
  - #### **Admin panel**
    - Hidden dashboard and buttons, only accessible when logged as admin.
- ### Extra Features
  - **Navigation** is hidden off-canvas on small screens and is opening full screen.
  - **Footer** is displayed on every page of the main app and it features a &copy; copyright message, a list of social links and two columns of app links, including the **Download CV** CTA and the **Write Testimonial** link.
  - #### **Landing Page**
    - **Hero** section extra features: Profile Picture, title (profession), social links and the CTA buttons act as follows:
      - ***Learn More*** opens a modal dialogue containing a long bio.
      - ***Download CV*** opens an auto-generated PDF attachment containing all the relevant information extracted from the database.
    - **Project** individual page features a photo gallery.
  - #### **Admin panel**
    - **Login Page** asks for user and password when trying to access any ```/admin``` url. While admin is logged in and until is logged out, the main app features quick links for each item/section to **Add new**, **Edit** and **Delete**. It also display a **Dashboard** and **Log out** buttons in both navbar and footer for quick access.
    - **Dashboard** page features a stand-out (yellow) **Notifications** panel for new (unapproved) testimonials, a **Quick Links** panel and a **Statistics** panel which shows count tiles for each item in database.
    - Full height collapsible (for small screen) **Sidebar Navigation**.
    - **Testimonials** page allows admin to approve/disapprove and delete testimonials.
    - **Blogs** and **Projects** shows a list of items and allows admin to access they're individual edit page, to delete any item on the list or to preview them on the main app. Also gives access to **[+ Add new]** item page and preview the list page on the app. **Add New** and **Edit existing** pages features a drag&drop multiple photo upload section. The first uploaded photo will be displayed as the main photo of the item. For ***Projects***, the rest of photos will be displayed as a gallery on they're individual page. For ***Blogs***, the rest of the photos can be used while writing/editing the post as inserted objects from the rich text editor field.
    - **Education** and **Experience** shows a list of items and allows admin to update they're order, access they're individual edit page and delete any of them from the database. Also gives access to **[+ Add new]** item page.
    - **Skills** and **Links** shows a list of items and allows admin to update they're data directly to the list, multiple items at once. It also allows admin to delete any of the items from database and gives access to **[+ Add new]** item page.
    - The **Settings** page features a form and a drag&drop single photo upload section where admin can update any information about the showcased developer or dynamic site data as META information.
    - **Log out** button which logs the admin out and deletes the session item.

## Database
  All the information in the database is only in relation with showcased developer. Therefore database used for this project is the document-based database **MongoDB** as a relational database is not needed.
  - ### Schema
    ![DB Schema](https://github.com/pinco227/dev.pi/blob/main/docs/db_schema.png)

## Technologies used
- Workspace
  * [Ubuntu20.04](https://ubuntu.com/) as Operating System
  * [Visual Studio Code](https://code.visualstudio.com/) as Integrated Development Environment
- Languages
  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/CSS)
  * [JS](https://en.wikipedia.org/wiki/JavaScript)
  * [Python](https://www.python.org/)
- Frameworks & Libraries
  * [Bootstrap5](https://getbootstrap.com/) is used for its great responsiveness, styling classes, icons and its javascript functionality.
  * [Font Awesome](https://fontawesome.com/) icons were used for writing the auto-generated CV.
  * [Google Fonts](https://fonts.google.com/) is used as the main font resource.
  * [GLightBox](https://biati-digital.github.io/glightbox/) is used for the lightbox photo gallery.
  * [TinyMCE](https://www.tiny.cloud/) is used for blog rich text editor.
  * [Flask](https://flask.palletsprojects.com/en/2.0.x/) is used as back-end framework.
  * Python modules:
    * [flask_breadcrumbs](https://flask-breadcrumbs.readthedocs.io/en/latest/): is used to generate breadcrumbs for routes.
    * [flask_mail](https://pythonhosted.org/Flask-Mail/) is used to send email from contact form.
    * [pymongo](https://pymongo.readthedocs.io/en/stable/) and [flask_pymongo](https://flask-pymongo.readthedocs.io/en/latest/) are used to connect the app to a MongoDB database.
    * [wtforms](https://wtforms.readthedocs.io/en/2.3.x/) and [flask_wtf](https://flask-wtf.readthedocs.io/en/0.15.x/) are used to generate secure forms with server side validation (inc. token validation).
    * [html5lib_truncation](https://github.com/tonyseek/html5lib-truncation) is used to truncate blogs html text in blogs list page while keeping html opening and closing tags.
    * [python-pdf (pydf)](https://github.com/tutorcruncher/pydf) is used to generate PDF file from html.
    * [secure.py](https://secure.readthedocs.io/en/latest/) is used to add security headers to http response.
- Version Control
  * [Git](https://git-scm.com/) as Version Control System.
  * [Github](https://www.github.com) for repository hosting.
  * [Commitizen](https://github.com/commitizen/cz-cli) for commit linting.
- Wireframes
  * [Balsamiq](https://balsamiq.com/) for creating [wireframes](#wireframes).
- Media
  * [Photopea](https://www.photopea.com/) online photo editor tool for creating the favicon and the no-photo image.
  * [Adobe Photoshop Express](https://photoshop.adobe.com/resize) for quick resizing and cropping images for improving performance.
  * [RealFaviconGenerator](https://realfavicongenerator.net/) for converting created favicon to all browser formats.
  * [Coolors](https://coolors.co/) for palette image generation.
  * [dbdiagram.io](https://dbdiagram.io/) for database diagram creation.
- Other
  * [SendGrid](https://sendgrid.com/) API for email sending.
  * [AWS S3](https://aws.amazon.com/s3/) API for file upload and storage.

## Testing
  ### [Click Here for Full Testing Process](https://github.com/pinco227/dev.pi/blob/main/TEST.md)
  ### Overview
  - #### Issues
    | Issue                                                                                                 | Fixed              |
    | ----------------------------------------------------------------------------------------------------- | ------------------ |
    | [Pylint(no-member) error](https://github.com/pinco227/dev.pi/blob/main/TEST.md#encountered-issues)    | :heavy_check_mark: |
    | [Image upload](https://github.com/pinco227/dev.pi/blob/main/TEST.md#encountered-issues)               | :heavy_check_mark: |
    | [Remove photo from database](https://github.com/pinco227/dev.pi/blob/main/TEST.md#encountered-issues) | :heavy_check_mark: |
  - #### Tests
    | Test                                                                                                                 | Result             |
    | -------------------------------------------------------------------------------------------------------------------- | ------------------ |
    | ***[User scenarios](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-user-stories)***                    | :heavy_check_mark: |
    | ***[Code](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-code)***                                      | :heavy_check_mark: |
    | ***[Functionality](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-functionality):*** links and buttons | :heavy_check_mark: |
    | ***[Functionality](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-functionality):*** form validation   | :heavy_check_mark: |
    | ***[Functionality](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-functionality):*** upload validation | :heavy_check_mark: |
    | ***[Functionality](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-functionality):*** CRUD              | :heavy_check_mark: |
    | ***[Functionality](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-functionality):*** contact           | :heavy_check_mark: |
    | ***[Functionality](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-functionality):*** errors            | :heavy_check_mark: |
    | ***[Compatibility](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-compatibility):*** Responsiveness    | :heavy_check_mark: |
    | ***[Compatibility](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-compatibility):*** System-cross      | :heavy_check_mark: |
    | ***[Compatibility](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-compatibility):*** Platform-cross    | :heavy_check_mark: |
    | ***[Compatibility](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-compatibility):*** Browser-cross     | :heavy_check_mark: |
    | ***[Performance](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-performance)***                        | :heavy_check_mark: |
    | ***[Accessibility](https://github.com/pinco227/dev.pi/blob/main/TEST.md#testing-accessibility)***                    | :heavy_check_mark: |
    | ***[HTML Validation](https://github.com/pinco227/dev.pi/blob/main/TEST.md#code-validation)***                        | :heavy_check_mark: |
    | ***[CSS Validation](https://github.com/pinco227/dev.pi/blob/main/TEST.md#code-validation)***                         | :heavy_check_mark: |
    | ***[JS Validation](https://github.com/pinco227/dev.pi/blob/main/TEST.md#code-validation)***                          | :heavy_check_mark: |
    | ***[Python Validation](https://github.com/pinco227/dev.pi/blob/main/TEST.md#code-validation)***                      | :heavy_check_mark: |
    | ***[Overflow](https://github.com/pinco227/dev.pi/blob/main/TEST.md#further-testing)***                               | :heavy_check_mark: |

## Deployment
- ### Forking the GitHub Repository
  By forking the GitHub Repository you make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository by using the following steps:
  1. Log in to GitHub and locate the [Dev.PI repository](https://github.com/pinco227/dev.pi).
  2. At the top right of the Repository just above the "Settings" Button on the menu, locate and click the "**Fork**" Button.
  3. You should now have a copy of the original repository in your GitHub account.
- ### Local Machine
  1. Log in to GitHub and locate the [Dev.PI repository](https://github.com/pinco227/dev.pi) (or the forked repo into your profile).
  2. At the top of the Repository just above the list of files, locate and click the "**Code**" dropdown.
  3. To clone the repository using HTTPS, under "**Clone**", make sure "**HTTPS**" is selected and copy the link.
  4. Open Git Bash.
  5. Change the current working directory to the location where you want the cloned directory to be made.
  6. Type ```git clone```, and then paste the URL you copied in Step 3.
      ```bash
      git clone https://github.com/pinco227/dev.pi.git
      ```
  7. Press Enter. Your local clone will be created.
      ```bash
      $ git clone https://github.com/pinco227/dev.pi.git
      Cloning into 'dev.pi'...
      remote: Enumerating objects: 408, done.
      remote: Counting objects: 100% (408/408), done.
      remote: Compressing objects: 100% (258/258), done.
      remote: Total 408 (delta 156), reused 368 (delta 116), pack-reused 0
      Receiving objects: 100% (408/408), 24.92 MiB | 15.71 MiB/s, done.
      Resolving deltas: 100% (156/156), done.
      ```
      > Click [Here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.
  8. Create accounts:
      - [MongoDB](https://www.mongodb.com/) account, project, cluster and database.
      - [AWS IAM](https://console.aws.amazon.com/iam/) User (retrieve access keys) and [AWS S3 bucket](https://s3.console.aws.amazon.com/s3).
      - [SendGrid](https://sendgrid.com/) API key or edit ```mail_settings``` in ```app.py``` for use of other mail server/provider.
      - [ReCaptcha](https://www.google.com/recaptcha/admin/): create site and retrieve keys.
  9.  Create `env.py` file and include the following code (note that the values should be replaced with your own credentials)
      ```python
      import os

      # App IP and PORT
      os.environ.setdefault("IP", "0.0.0.0")
      os.environ.setdefault("PORT", "5000")
      # Generate a secret key, use https://randomkeygen.com/
      os.environ.setdefault("SECRET_KEY", "<secret_key>")
      # Mongo DB credentials
      os.environ.setdefault("MONGO_URI", "<mongo_uri>")
      os.environ.setdefault("MONGO_DBNAME", "<db_name>")
      # Admin panel user and password
      os.environ.setdefault("ADMIN_USERNAME", "<username>")
      os.environ.setdefault("ADMIN_PASSWORD", "<password>")
      # AWS Keys
      os.environ.setdefault('AWS_ACCESS_KEY_ID', '<access_key>')
      os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<secret_key>')
      os.environ.setdefault('S3_BUCKET_NAME', '<bucket_name>')
      # Email credentials. See mail_settings in app.py for more email settings
      os.environ.setdefault("SENDGRID_API_KEY", "<api_key>")
      os.environ.setdefault("MAIL_DEFAULT_SENDER", "<sender_email>")
      # Recaptcha keys. Go to https://www.google.com/recaptcha/admin/create and create a new site
      os.environ.setdefault("RC_SITE_KEY", "<recaptcha_site_key>")
      os.environ.setdefault("RC_SECRET_KEY", "<recaptcha_secret_key>")
      ```
      > Make sure you add this file to **.gitignore** file so it will not be published.
  10. Install required `python` packages by running the following command into terminal:
      ```bash
      pip3 install -r requirements.txt
      ```
  11. Run app by typing the following into terminal:
      ```bash
      python3 app.py
      ```
  12. Browse app by accessing [0.0.0.0:5000](http://0.0.0.0:5000) into a browser. At this point, if configured right, the app will automatically build the database.
- ### Heroku
  1. Make sure the `requirements.txt` and `Procfile` are created. If not, type the followings into terminal:
      ```bash
      pip3 freeze --local > requirements.txt
      ```
      and
      ```bash
      echo web: python app.py > Procfile
      ```
  2. Commit and push changes to forked repository.
  3. Create a [Heroku](https://heroku.com) account and click **New** on top right of the dashboard to **Create a new app**.
  4. Within the newly created app go to **Settings** tab and press **Reveal Config Vars**. Here you can add the variables initially stored into local `env.py` file: IP, SECRET_KEY, MONGO_URI, MONGO_DBNAME, ADMIN_USERNAME, ADMIN_PASSWORD, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME, SENDGRID_API_KEY, MAIL_DEFAULT_SENDER, RC_SITE_KEY, RC_SECRET_KEY.
  5. Go to **Deploy** tab and under the **Deployment method** click on the **Github** icon.
  6. Right under this section, type the `dev.pi` and search for the forked repository into your GitHub account. Select the right repository and click **Connect**.
  7. Under the **Automatic deploys** section, click **Enable Automatic Deploys**. The deployment will be now automatic with every github `push` command.
  8. Under the **Manual deploy** section, click **Deploy Branch** for initial deploy.
  9. You can now browse the deployed app by clicking **Open app** button on top right of the dashboard.

## Credits
- ### Media
  - [XYZZY estudio web](https://codepen.io/xyzzyestudioweb) codepen user for [svg section separators](https://codepen.io/xyzzyestudioweb/pen/JgdKOR).
  - [Colorpalettes.net](https://colorpalettes.net/color-palette-3728/) for the color palette (#3728).
- ### Code
  - [CSS TRICKS](https://css-tricks.com/) as a general resource.
  - [Stack Overflow](https://stackoverflow.com/) as a general resource.
  - [w3schools](https://www.w3schools.com/) as a general resource.
  - [Hover.css](https://ianlunn.github.io/Hover/) for *Grow* and *Sweep to top* hover effects used in buttons navigation links.
  - [CSS Tricks user: Chris Coyier](https://css-tricks.com/author/chriscoyier/) for [Value Bubbles for Range Inputs](https://css-tricks.com/value-bubbles-for-range-inputs/) which was used on the **Skills** and **Add New Skill** page of the admin panel.
  - [Joseph Zimmerman](https://www.joezimjs.com/) for writing [How To Make A Drag-and-Drop File Uploader With Vanilla JavaScript](https://www.smashingmagazine.com/2018/01/drag-drop-file-uploader-vanilla-js/) which was adapted and used in admin panel for photo uploads.
  - [Gal Weizman's article](https://www.perimeterx.com/tech-blog/2019/beforeunload-and-unload-events/) about ```unload``` And ```beforeunload``` javascripts events for the ```sleep(delay)``` function which was used in admin panel when discarding a form that has uploaded images in order to get the files deleted before unload.
  - [GitHub Gist user: Mathew Byrne](https://gist.github.com/mathewbyrne) for the javascript ```slugify(text)``` function ([Gist](https://gist.github.com/mathewbyrne/1280286)) that was used in admin panel to generate slugs for blogs and projects.
  - [Bootsnipp user: devlopereswar](https://bootsnipp.com/devlopereswar) for the html responsive [email template snippet](https://bootsnipp.com/snippets/A2kpB).
  - [Bram.us](https://www.bram.us/) for [this article](https://www.bram.us/2020/11/04/preventing-double-form-submissions/) on how to prevent double form submission.
  - [This StackOverflow thread](https://stackoverflow.com/questions/15900485/correct-way-to-convert-size-in-bytes-to-kb-mb-gb-in-javascript) for ```formatBytes``` javascript function that takes a number of bytes and returns a readable size format (e.g.: **1Mb**).

## Acknowledgements
  - **My Mentor**: Nishant Kumar for continuous helpful feedback.
  - **Tutor** support at Code Institute for their support.
  - **Slack** Code Institute community for feedback.
  - **Peer student**: [Alexandru Valentin Grapa](https://github.com/alexandruvalentin) for helpful feedback along the coding progress and for help with testing.