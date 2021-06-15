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
  - #### As a user I need:
    - user story.
        > :heavy_check_mark: Test.
## Testing Code
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