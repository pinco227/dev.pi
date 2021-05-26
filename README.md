# {π} Dev.PI

**Dev.PI** is a Developer's Portfolio which also serves as a Milestone Project for the **Software Developer Diploma** programme of **Code Institute**.

## Table of Contents
  - [Demo](#demo)
  - [UX](#ux)
    - [Goals](#goals)
    - [User Needs](#users-needs)
    - [User Stories](#user-stories)
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
  - [Aknowledgements](#aknowledgements)

## Demo

### [Live website](https://dev-pi.herokuapp.com/)

(( Website screenshots here ))

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
    - For predictability, the interface interacts with user actions as the user expetcs. The scroll/swipe actions respond with the normal behaviour and buttons acts instantly on press.
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
      - #### All pages:
        - Breadcrumbs between header and content
      - #### Landing page
        - Icons for education and experience items but no icon for testimonials.
      - #### Blog Post page
        - The post cover photo is displayed on the left.
      - #### Contact page
        - Profile Picture is displayed instead of person icon and is not hidden on mobile.
    - #### **Admin Panel**:
      - #### All pages:
        - The layout is completely separate and different from the client side, different navbar which only includes **App** and **Logout** buttons and the menu panel is now a full height sidebar, no footer.
        - On mobile, menu is expandable from the navbar and it covers the whole page.
        - A svg image on top right of every page (centered on mobile), representing the page's subject.
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
  - #### Iconography

## Features
- ### Initial features
  - #### **Navigation Bar**
    - Allows users to navigate through the website. The navigation will be fixed to top and visible all the time. Links will be collapsed on small screens.
  - #### **Landing Page**
    - ***Hero*** featuring a title (dev's name), a short bio, current status and availability and two *Call-to-Action* buttons: **Download CV** and **Learn more**.
    - ***Skillset*** section where dev's skills will be presented as progress bars.
    - ***Education*** section.
    - ***Work Experience*** section.
    - ***Tetimonials***.
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

## Database
  All the information in the database is only in relation with showcased developer. Therefore database used for this project is the document-based database **MongoDB** as a relational database is not needed.
  - ### Schema
    ![DB Schema](https://github.com/pinco227/dev.pi/blob/main/docs/db_schema.png)

## Technologies used
- Workspace
  * [Ubuntu20.04](https://ubuntu.com/) as Operating System
  * [Visual Studio Code](https://code.visualstudio.com/) as Integrated Development Environment
- Languages
- Frameworks & Libraries
- Version Control
- Wireframes
  * [Balsamiq](https://balsamiq.com/) for creating [wireframes](#wireframes).
- Media
- Other

## Testing
  ### [Click Here for Full Testing Process](https://github.com/pinco227/dev.pi/blob/main/TEST.md)
  ### Overview
  - #### Issues
    | Issue                                                                                              | Fixed              |
    | -------------------------------------------------------------------------------------------------- | ------------------ |
    | [Pylint(no-member) error](https://github.com/pinco227/dev.pi/blob/main/TEST.md#encountered-issues) | :heavy_check_mark: |
  - #### Tests
    | Test                               | Result             |
    | ---------------------------------- | ------------------ |
    | ***[Link to test on TEST.md](#)*** | :heavy_check_mark: |

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
  7. Create a [MongoDB](https://www.mongodb.com/) account, project, cluster and database.
  8. Create `env.py` file and include the following code (note that the values should be replaced with your own db credentials)
      ```python
      import os

      os.environ.setdefault("IP", "0.0.0.0")
      os.environ.setdefault("PORT", "5000")
      os.environ.setdefault("SECRET_KEY", "<secret_key>")
      os.environ.setdefault("MONGO_URI", "<mongo_uri>")
      os.environ.setdefault("MONGO_DBNAME", "<db_name>")
      ```
      > Make sure you add this file to **.gitignore** file so it will not be published.
  9. Install required `python` packages by running the following command into terminal:
      ```bash
      pip3 install -r requirements.txt
      ```
  10. Run app bu typing the following into terminal:
      ```bash
      python3 app.py
      ```
  11. Browse app by accessing [0.0.0.0:5000](http://0.0.0.0:5000) into a browser.
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
  4. Within the newly created app go to **Settings** tab and press **Reveal Config Vars**. Here you can add the variables initially stored into local `env.py` file: IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME.
  5. Go to **Deploy** tab and under the **Deployment method** click on the **Github** icon.
  6. Right under this section, type the `dev.pi` and search for the forked repository into your GitHub account. Select the right repository and click **Connect**.
  7. Under the **Automatic deploys** section, click **Enable Automatic Deploys**. The deployment will be now automatic with every github `push` command.
  8. Under the **Manual deploy** section, click **Deploy Branch** for initial deploy.
  9. You can now browse the deployed app by clicking **Open app** button on top right of the dashboard.

## Credits
- ### Content
  - [Colorpalettes.net](https://colorpalettes.net/color-palette-3728/) for the color palette (#3728).
  - [Coolors](https://coolors.co/) for palette image generation.
- ### Media
- ### Code

## Aknowledgements