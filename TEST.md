# Testing

## Table of Contents
- [Encountered Issues](#encountered-issues)
- [Testing User Stories](#testing-user-stories)
- [Testing Code](#testing-code)
- [Testing Functionality](#testing-functionality)
- [Testing Compatibility](#testing-compatibility)
- [Testing Performance](#testing-performance)
- [Testing Accessibility](#testing-accessibility)
- [Code Validation](#code-validation)
- [Further Testing](#further-testing)
## Encountered Issues
- ### Issues found during the building process:
    Through the proccess of building this app, testing was made at every step and there were many encountered issues and bugs along the way. Any issues that were quickly fixed were not worth mentioning. Therefore these are the issues that has persisted and were a bit more time consuming to fix:
    > - Pylint (python code linting/validator) `pylint(no-member)` error while programming using VSCode. This error was given for every class in `form_classes.py` file when trying to access `form.errors` in `app.py` file, due to the validator not being able to go that deep into every module inclusion:
        `Module 'SomeForm' has no 'errors' member`
    > - :heavy_check_mark: **FIXED**: Code was running with no issue while error was still showing. Fixed by creating `.pylintrc` file using
        `pylint --generate-rcfile .pylintrc` and modifying this line `generated-members=FlaskForm.*,Form.*` and adding `"python.linting.pylintArgs": ["--generated-members"]` to `settings.json` file. [CREDIT to this article](https://yann-leguilly.gitlab.io/post/2019-11-11-no-member-vs-code/).
    
    > - Image upload issue: Heroku server doesn't allow for filesystem writes and even if it seems that uploads are working, it is only temporary.
    > - :heavy_check_mark: **FIXED**: The whole internal upload proccess implementation was replaced with AWS S3 server upload and delete implementation and all photos urls were updated throughout the site to work with aws urls. Database functionality was also updated to add/delete and read photos to/from an array type document.
- ### Issues found while using app's CRUD functionality with real data:
    > - Photo deletion on product/blog edit page is not fully functioning. The image is being deleted from AWS S3 server but it is not removed from the database.
    > - :heavy_check_mark: **FIXED**: Fixed by passing the document id through the API request url to specify from which document the photo should pe pulled from ```photos``` db array using mongoDB ```$pull``` operator.
- ### Issues found while testing:
    > - Issue found.
    > - :heavy_check_mark: **FIXED**: Issue fix.
## Testing user stories
  - #### As a potential employer/recruiter I need:
    - To learn about the candidate's professional profile without having to click too many times and look too deep.
        > :heavy_check_mark: **Skills** and **Work Experience** sections are displayed on the landing page and can be accessed by scrolling down or by clicking once on the navigation menu corresponding item.
    - To be able to download the candidate's CV for print/file purposes.
        > :heavy_check_mark: There is a **Download CV** CTA button displayed on the landing page's hero section and another one displayed on the footer of every page.
    - To learn about the developer's current status and availability.
        > :heavy_check_mark: Status and availability (and other useful information) are displayed on the hero section of the landing page.
    - To be able to contact the candidate to further asses and discuss eventual contract/employment.
        > :heavy_check_mark: There is contact information and a contact form provided on the contact page. Also social links are displayed on the landing page's hero section and on the footer of every page.
    - To see candidate's education, previous work experience and projects (including written code).
        > :heavy_check_mark: **Education** and **Work Experience** sections are displayed on the landing page and can be accessed from any page through the top navigation and footer links. There is also a **Portfolio** page, easily accessible from the navigation provided, that lists all the projects, each with an individual page with details and links to live app and source code.
    - To find candidate's other relevant social profiles, for a deeper insight (linkedin, github).
        > :heavy_check_mark: Social links are provided on the hero section of the landing page and on the footer of every page.
    - To find more about the person behind the title, to understand how he got into software development, how passionate and motivated he is.
        > :heavy_check_mark: There is a short bio displayed on the hero of the landing page and a longer bio accessible by pressing **Learn More** CTA button. There is also a **Blog** page which lists developer's personal blog posts.
    - To find what other people say about the developer (testimonials).
        > :heavy_check_mark: There is a **Testimonials** section displayed on the landing page, that can be accessible from any page using provided navigation.
  - #### As a potential collaborator I need:
    - To be able to explore developer's work, written code and skillset to understand if he is fit to my project idea.
        > :heavy_check_mark: **Skills** are displayed on the landing page, and can be accessed from any page using provided navigation. Developer's work is presented as a **Portfolio** with detailed **Projects**, including source code.
    - To learn about the developer, personally, to see if he is compatible to work with.
        > :heavy_check_mark: Developer's social profiles are displayed as social links. User can also browse through developer's personal blog.
    - To be able to contact the developer.
        > :heavy_check_mark: The contact details and a functional contact form can be found on **Contact** page.
    - To connect with developer on other relevant social platforms.
        > :heavy_check_mark: User can access social platforms through the provided social links.
  - #### As a user (of any kind) I need:
    - To easily understand the purpose of the website.
        > :heavy_check_mark: First thing that can be seen on the landing page, is the **Hero** section, which presents a profile picture, a name, a title and a short bio, and part of the **Skills** section. These make the purpose obvious, promoting a professional profile.
    - To easily navigate throughout the website on any device/platform.
        > :heavy_check_mark: Top navigation bar and footer links are displayed on every page. On mobile, navigation is hidden under a *burger* button.
    - To be able to write a testimonial.
        > :heavy_check_mark: There is a **Write a testimonial** form, where users can submit they're thoughts, subject to aproval. This form can be accessed from any page using the button on the footer.
  - #### As the developer I need:
    - To be able to add, update and delete skills, education, work experience, portfolio projects and links.
        > :heavy_check_mark: There is an **Admin Panel** accessible only by the developer (with user and password), which presents full **CRUD** functionality for every item in the database. Furthermore, once logged in, the admin can see add/edit/delete buttons displayed on every section of the main app for quick access, and quick **Dashboard** and **Log out** buttons displayed on top and footer navigation.
    - To be able to update my current status, availability and contact information.
        > :heavy_check_mark: This can be done accessing the **Settings** page of the admin panel, or, once logged in, by clicking the edit button of the relevant section.
    - To be able to post, edit and delete personal blogs.
        > :heavy_check_mark: There is full **CRUD** functionality for blogs in the admin panel. There are also quick access buttons (add/edit/delete) displayed on blogs page and beside each blog post, once logged in.
    - To be able to manage (approve, remove) user's testimonials.
        > :heavy_check_mark: When there are new/unapproved testimonials, a notification will be displayed on the dashboard. There is also a **Testimonials** page in the admin panel, where testimonials statuses can be changed, and testimonials can be deleted. This section can be accessed through the quick access button displayed on the app, once admin is logged in.
    - To be able to update hero name, short bio, photo and CV.
        > :heavy_check_mark: Same as status, availability and contact details, this can be done accessing the **Settings** page of the admin panel, or, once logged in, by clicking the edit button of the relevant section.
    - To be able to update website's metadata and admin password.
        > :heavy_check_mark: Website's metadata, as **Title**, **Description** and **Keywords** can be edited in the **Settings** Page of the admin panel. The access password for admin panel can only be changed by the developer, server-side, by changing the values of the environmental variables.
## Testing Code
> :heavy_check_mark: Every javascript method was tested for the expected outcome by using the app, in console by using `console.log()` or by manually calling the function. 
> :heavy_check_mark: Every python function and route was tested for the expected outcome by using the app, by accessing the route, in python console, while debug mode was set to on, by using `print()` and by watching for the correct response. 
## Testing Functionality
## Testing Compatibility
   - ### Responsiveness
   - ### OS test
   - ### Devices test
   - ### Browser test
## Testing Performance
## Testing Accessibility
## Code Validation
  - ### HTML
  - ### CSS
  - ### JavaScript
  - ### Python
## Further Testing