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
    Through the process of building this app, testing was made at every step and there were many encountered issues and bugs along the way. Any issues that were quickly fixed were not worth mentioning. Therefore, these are the issues that has persisted and were a bit more time-consuming to fix:
    > - Pylint (python code linting/validator) `pylint(no-member)` error while programming using VSCode. This error was given for every class in `form_classes.py` file when trying to access `form.errors` in `app.py` file, due to the validator not being able to go that deep into every module inclusion:
        `Module 'SomeForm' has no 'errors' member`
    > - :heavy_check_mark: **FIXED**: Code was running with no issue while error was still showing. Fixed by creating `.pylintrc` file using
        `pylint --generate-rcfile .pylintrc` and modifying this line `generated-members=FlaskForm.*,Form.*` and adding `"python.linting.pylintArgs": ["--generated-members"]` to `settings.json` file. [CREDIT to this article](https://yann-leguilly.gitlab.io/post/2019-11-11-no-member-vs-code/).
    
    > - Image upload issue: Heroku server doesn't allow for filesystem writes and even if it seems that uploads are working, it is only temporary.
    > - :heavy_check_mark: **FIXED**: The whole internal upload process implementation was replaced with AWS S3 server upload and delete implementation and all photos urls were updated throughout the site to work with AWS urls. Database functionality was also updated to add/delete and read photos to/from an array type document.
- ### Issues found while using app's CRUD functionality with real data:
    > - Photo deletion on product/blog edit page is not fully functioning. The image is being deleted from AWS S3 server, but it is not removed from the database.
    > - :heavy_check_mark: **FIXED**: Fixed by passing the document id through the API request url to specify from which document the photo should be pulled from ```photos``` db array using mongoDB ```$pull``` operator.
- ### Issues found while testing:
    > - Issue found.
    > - :heavy_check_mark: **FIXED**: Issue fix.
## Testing user stories
  - #### As a potential employer/recruiter, I need:
    - To learn about the candidate's professional profile without having to click too many times and look too deep.
        > :heavy_check_mark: **Skills** and **Work Experience** sections are displayed on the landing page and can be accessed by scrolling down or by clicking once on the navigation menu corresponding item.
    - To be able to download the candidate's CV for print/file purposes.
        > :heavy_check_mark: There is a **Download CV** CTA button displayed on the landing page's hero section and another one displayed on the footer of every page.
    - To learn about the developer's current status and availability.
        > :heavy_check_mark: Status and availability (and other useful information) are displayed on the hero section of the landing page.
    - To be able to contact the candidate to further asses and discuss eventual contract/employment.
        > :heavy_check_mark: There is contact information and a contact form provided on the contact page. Also, social links are displayed on the landing page's hero section and on the footer of every page.
    - To see candidate's education, previous work experience and projects (including written code).
        > :heavy_check_mark: **Education** and **Work Experience** sections are displayed on the landing page and can be accessed from any page through the top navigation and footer links. There is also a **Portfolio** page, easily accessible from the navigation provided, that lists all the projects, each with an individual page with details and links to live app and source code.
    - To find candidate's other relevant social profiles, for a deeper insight (linkedin, github).
        > :heavy_check_mark: Social links are provided on the hero section of the landing page and on the footer of every page.
    - To find more about the person behind the title, to understand how he got into software development, how passionate and motivated he is.
        > :heavy_check_mark: There is a short bio displayed on the hero of the landing page and a longer bio accessible by pressing the **Learn More** CTA button. There is also a **Blog** page which lists developer's personal blog posts.
    - To find what other people say about the developer (testimonials).
        > :heavy_check_mark: There is a **Testimonials** section displayed on the landing page, that can be accessible from any page using provided navigation.
  - #### As a potential collaborator, I need:
    - To be able to explore developer's work, written code and skill set to understand if he is fit to my project idea.
        > :heavy_check_mark: **Skills** are displayed on the landing page, and can be accessed from any page using provided navigation. Developer's work is presented as a **Portfolio** with detailed **Projects**, including source code.
    - To learn about the developer, personally, to see if he is compatible to work with.
        > :heavy_check_mark: Developer's social profiles are displayed as social links. User can also browse through developer's personal blog.
    - To be able to contact the developer.
        > :heavy_check_mark: The contact details and a functional contact form can be found on the **Contact** page.
    - To connect with developer on other relevant social platforms.
        > :heavy_check_mark: User can access social platforms through the provided social links.
  - #### As a user (of any kind), I need:
    - To easily understand the purpose of the website.
        > :heavy_check_mark: First thing that can be seen on the landing page, is the **Hero** section, which presents a profile picture, a name, a title and a short bio, and part of the **Skills** section. These make the purpose obvious, promoting a professional profile.
    - To easily navigate throughout the website on any device/platform.
        > :heavy_check_mark: Top navigation bar and footer links are displayed on every page. On mobile, navigation is hidden under a *burger* button.
    - To be able to write a testimonial.
        > :heavy_check_mark: There is a **Write a testimonial** form, where users can submit they're thoughts, subject to approval. This form can be accessed from any page using the button on the footer.
  - #### As the developer, I need:
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
   - ### Testing links and buttons
        > #### Header (every page except dashboard) :heavy_check_mark:
        > - top navigation fully functional including the brand title.
        > - mobile navigation toggle "burger" working as expecting, opening the off-canvas navigation.

        > #### Landing Page :heavy_check_mark:
        > - clicking on profile picture triggers the lightbox and displays it full screen.
        > - CTA buttons are fully functional, and they run as expected. **Learn More** button opens the modal and **Download CV** calls the pdf route that gives the user the file as attachment, not as page.
        > - Social links are functioning properly, opening the link in a new tab/window.
        > - When logged as admin, **Dashboard** and **Log out** buttons on the navigation, works as expected. Every "plus" and "pen" button for add and edit, works as expected, sending the user to relevant section of the dashboard.

        > #### Portfolio :heavy_check_mark:
        > - Clicking on any project photo, title or **Details** button opens the project page, as expected.
        > - Clicking on dynamically generated **Source** and **Demo** (where applicable) buttons, opens the given link in a new tab/window, as expected.
        > - When logged as admin, "plus" and "pen" buttons on top, for add and edit, works as expected, sending user to **Add new project**, respectively **Projects list** in admin panel. Every "pen" and "trash" button for every project, works as expected, sending user to **Edit project** section, respectively asks user for delete confirmation, and deletes the selected project.

        > #### Project page :heavy_check_mark:
        > - Clicking on the main photo triggers the lightbox and opens the image full screen.
        > - Clicking on dynamically generated **Source** and **Demo** (where applicable) buttons, opens the given link in a new tab/window, as expected.
        > - Clicking on dynamically generated **Gallery** (where applicable, more than 1 photo) button, scrolls the page down to **Gallery** section, as expected.
        > - **Gallery**: clicking on any photo triggers the lightbox and opens the clicked image in fullscreen, without leaving the website and allowing the user to navigate through the rest of the photos, by clicking right and left arrows. "**X**" button closes the lightbox.
        > - **Go back** buttons, both on top and bottom, sends the user back to the **Portfolio** page, as expected.
        > - When logged as admin, "pen" and "trash" buttons on top, for edit and delete opened project, works as expected, sending user to **Edit project** section of admin panel, respectively **Projects list** in admin panel. Every "pen" and "trash" button for every project, works as expected, sending user to **Edit project** section, respectively asks user for delete confirmation, and deletes the opened project.

        > #### Blogs :heavy_check_mark:
        > - Clicking on "**Read More ...**" button of every blog post, opens the blog post page, as expected.
        > - When logged as admin, "plus" and "pen" buttons on top, for add and edit, works as expected, sending user to **Add new blog**, respectively **Blogs list** in admin panel. Every "pen" and "trash" button for every post, works as expected, sending user to **Edit Blog Post** section, respectively asks user for delete confirmation, and deletes the selected post.

        > #### Blog post page :heavy_check_mark:
        > - Clicking on the main photo triggers the lightbox and opens the image full screen.
        > - **Go back** buttons, both on top and bottom, sends user back to **Blogs** page, as expected.
        > - When logged as admin, "pen" and "trash" buttons on top, for edit and delete opened post, works as expected, sending the user to **Edit blog post** section of admin panel, respectively asks user for delete confirmation, and deletes the selected post.

        > #### Contact page :heavy_check_mark:
        > - **Send** button submits the form.
        > - When logged as admin, "pen" button on **Contact Info** section, works as expected, sending user to **Settings** section of admin panel.

        > #### Write testimonial page :heavy_check_mark:
        > - **Submit** button submits the form.

        > #### Breadcrumbs :heavy_check_mark:
        > - On every page, except the landing page, breadcrumbs are displayed on top. Clicking of every item of the breadcrumb, works as expected, directing the user to the page described by the link.

        > #### Footer (every page except dashboard) :heavy_check_mark:
        > - Social links are functioning properly, opening the link in a new tab/window.
        > - navigation links are fully functional, each acting as expecting.
        > - When logged as admin, **Dashboard** and **Log out** links are displayed and works as expected. "Pen" and "plus" buttons for edit and add social links, works as expected, sending user to relevant section of the dashboard.

        > #### Admin panel :heavy_check_mark:
        > - Every link on the top nav and side nav, works as expected, sending the user to relevant section.
        > - Quick links on the dashboard are functioning as expected, sending the user each to it's described destination.
        > - **View** button of the notification panel (when there are unapproved testimonials), works as expected, sending the user to **Testimonials** page.
        > - On every section (except **Dashboard**, **Testimonials** and **Settings**) of the admin panel, "plus" button work as expected, sending user to **Add new item** of that section.
        > - On **Blogs** and **Projects** sections, the "eye" buttons, the top one and for each item, works as expected, sending the user to the relevant view page of the main app.
        > - On **Testimonials**, **Skills**, **Education**, **Experience** and **Links** sections, the **Update** button, on both top and bottom, acts as expected, updating the list after modifications have been made.
        > - On every section (except **Dashboard** and **Settings**), the "trash" button for every item, works as expected, asking user for confirmation and finally deleting selected item.
        > On **Blogs**, **Education**, **Experience** and **Projects** sections, the "pen" button for every item, works as expected, sending the user to edit page of the selected item.
        > On the **Settings** page, the **Update** button on the bottom of the form, works as expected, updating the settings with the values on the form.
        > On **Photo**/**Photos** sections of **Settings**, **Add new project**, **Add new blog**, **Edit project** and **Edit blog** pages, clicking on, or dropping files into ***Drag&Drop area***, acts as expected, opening device's file selection tool, respectively uploads dropped files. Clicking on "trash" button of the uploaded images, acts as expected, asking user to confirm and finally removing selected picture. Clicking on the picture itself, triggers the lightbox and opens the image full-screen.
        > - On every **Add new item** and **Edit item** pages, the blue button on the bottom submits the form, while the red button cancels the operation, sending the user back to the list of items page, as expected.

   - ### Testing form validation
        > :heavy_check_mark: **Contact** form: the form was tested for validation by trying to submit first with no data and then by filling the fields one by one. Result as expected, all fields asked for input. The email field asks for email format with `@`. Recaptcha works as expected and server returns an error message if Recaptcha is not checked. Using the Chrome's DevTools, I have removed the ```required``` from every field and resubmitted the form, the server-side validation works, returning error messages for every required field. Also, server-side validation checks email field against a regex string.

        > :heavy_check_mark: **Write testimonial** form: was tested following the same procedure as the contact form. Results are as expected.

        > :heavy_check_mark: **Admin panel**: The admin panel functionality is mostly built on add and edit forms. Every form was tested against client-side and server-side validation, and results are satisfying.
   - ### Testing image upload validation
        > :heavy_check_mark: **File size**: image upload was tested against file size by trying to upload a bigger than 1Mb file. The website returns a toast message saying that file is too big.

        > :heavy_check_mark: **File type**: image upload was tested against file type by trying to upload a non-image file. The website returns a toast message saying that file type is not allowed.
   - ### Testing CRUD functionality
        > :heavy_check_mark: **Create**: Create functionality was tested with real data for real world application, by adding items in admin panel and inserting testimonials from the designated page. Results are satisfying. Image upload during creation process, works as expected. Rich text editors, in projects and blogs creation state, are fully functional, including inserting uploaded images. No issues found.

        > :heavy_check_mark: **Read**: Read functionality was tested with real data for real world application, by verifying that created data is displayed correctly and in the correct section. No issues found.

        > :heavy_check_mark: **Update**: Update functionality was tested with real data for real world application, by updating items in admin panel. Results are satisfying. Images can be updated by adding more images using the provided section, and any uploaded new images can be used to be inserted in the rich text editors (where applicable). No issues found.

        > :heavy_check_mark: **Delete**: Delete functionality was tested by deleting items, both from admin panel lists and from quick links in the main app. Images can be deleted and removed from database using the provided section, by clicking the "trash" button attached to every image. Errors were reported and fixed. No issues found.
   - ### Testing contact functionality
        > :heavy_check_mark: Contact functionality was tested by sending sample emails using the provided form. Email was sent to the email address provided in the settings section. Email was received successfully.
   - ### Testing for errors
        > :heavy_check_mark: Full app browsing and functionality was tested with browser's console open. Console is clear of errors.

        > :heavy_check_mark: Python console with debug mode on is clear of errors.

## Testing Compatibility
   - ### Responsiveness
        > Using DevTools and different device sizes such as mobile and tablet, the website was tested for any possible screen size combination and orientation. No issues found. **Site is size compatible** :heavy_check_mark:.
   - ### OS test
        > #### Desktop
        > The website was tested on Ubuntu 20.04, Windows 7 and Windows 10 systems. Further tests were made using [LambdaTest](https://www.lambdatest.com/), for MacOS Mojave. Result as expected, **desktop system-cross compatible** :heavy_check_mark:.

        > #### Mobile
        > The website was tested on Android 6, Android 9, Android 10 and iOS 14 systems. Further tests were made using [LambdaTest](https://www.lambdatest.com/), for iOS on iPad Pro. Result as expected, **mobile system-cross compatible** :heavy_check_mark:.
   - ### Devices test
        > The website was tested on ASUS 17" notebook, ACER 17" notebook, Huawei P30 PRO, Huawei P20 PRO, Huawei P10, iPhone 11, Samsung Galaxy Note10, Samsung Galaxy A7, Samsung Galaxy TabS6, Lenovo Yoga Tab. Further device tests were made using [LambdaTest](https://www.lambdatest.com/), for iPad Pro (11 inch) and MacOS. The result is consistent, website is **platform-cross compatible** :heavy_check_mark:.
   - ### Browser test
        > The website was tested on Google Chrome, Firefox, Safari, Edge, Samsung Internet, Opera, Vivaldi and Yandex. This website is NOT designed to be compatible with IE. Browsers versions were all up to date. Results were consistent. Conclusion: the website is **browser-cross compatible** :heavy_check_mark:.
## Testing Performance
Performance has been tested using Chrome's **Lighthouse** tool for both desktop and mobile. Mobile tests were made using **remote device** connection and an actual mobile phone. Results are as follows:

> :heavy_check_mark: Landing Page:
>
>   ![LightHouse Performance Result for Landing page](https://github.com/pinco227/dev.pi/blob/main/docs/landing-perf.png)  

> :heavy_check_mark: Portfolio page (with over 30 photos displayed):
>
>   ![LightHouse Performance Result for Portfolio page](https://github.com/pinco227/dev.pi/blob/main/docs/portfolio-perf.png)

> :heavy_check_mark: Admin panel -> Projects page:
> 
>   ![LightHouse Performance Result for Admin panel - Projects page](https://github.com/pinco227/dev.pi/blob/main/docs/admin-projects-perf.png)  

## Testing Accessibility
The accessibility was tested using [a11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/). Results are as follows:
> :heavy_check_mark: Landing Page: There were 6 problems detected on the landing page, 4 of these problems are due to the fact that the validator doesn't see the actual background colour of the work experience cards and education cards, these being gradient backgrounds, while the other 2 problems are design choices, so they are accepted. 

> :heavy_check_mark: Any other page of the main app: The only problems found are the cards/badges with gradient background, where the validator cannot read the actual value, the design choices (testimonials and project gallery section titles, and breadcrumbs which are not supposed to stand out) and the buttons with ```btn-accent``` class, where the problem is solved by having a dark shadow around the text, but it is not read by the validator.
## Code Validation
  - ### HTML :heavy_check_mark:
    > Html was tested and validated with [W3C Validator](https://validator.w3.org/). Code has been adjusted. Final results are as follows:
    > - No errors on any page of the main app. There were few warnings found on the **Blogs** page, about empty headings, generated by the html truncate function for the blog body.
    > - For admin panel, html has been tested by manual input of the source code for every page. No errors found. Same warnings were found on the blogs list page, generated by the html truncate function.
  - ### CSS :heavy_check_mark:
    > Custom CSS was validated with [W3C CSS](https://jigsaw.w3.org/css-validator/). Code has been adjusted, and the results are as follows:
    > - The only errors found are ```Invalid RGB function``` caused by the use of css variables inside rgb functions. These functions are rendering correctly on every test, therefore, the errors are acceptable and can be ignored. The only warnings are about the vendor prefixes, which are acceptable and can be ignored.
  - ### JavaScript :heavy_check_mark:
    > Javascript has been validated during building process by **VSCode** extension **[ESLint](https://eslint.org/)**. **No errors or issues** :heavy_check_mark:.
  - ### Python :heavy_check_mark:
    > Python has been validated during building process by **VSCode** integrated extensions **[Pylint](https://www.pylint.org/)** and **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)**, which are in compliance with PEP8 style guide. **No errors or issues**.
## Further Testing
  - ### Overflow :heavy_check_mark:
    > Every page was tested for overflow by using the [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) chrome extension to highlight the elements margins. **No issues found**.

  - ### Spelling :heavy_check_mark:
    > English grammar & spelling throughout the website was checked using [LanguageTool](https://languagetool.org/#plugins) chrome extension. The results are satisfying.

  - ### Mobile Friendly :heavy_check_mark:
    > According to [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?id=blMQX7ozm7UxRGhyXEvhVA), page is mobile friendly.
    >
    > ![Mobile-Friendly](https://github.com/pinco227/dev.pi/blob/main/docs/mobile-friendly.png)  