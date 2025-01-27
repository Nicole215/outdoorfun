<a id="top"></a>
# Outdoorfun: A home for various outdoor events

![Screenshot 2025-01-26 131247](https://github.com/user-attachments/assets/0f1456dd-3fa2-476a-93ec-7a6db253b71c)

Outdoorfun is a website designed to help outdoor enthusiasts easily discover and explore events in the areas of hiking and mud runs. In today's world, finding an event can quickly become overwhelming—first, you struggle to locate a suitable event, then algorithms flood your social media feed with endless suggestions, making it hard to keep track.

This platform was created to simplify your search by providing a centralized and clutter-free overview of relevant events. Whether you're looking for your next adventure or just curious about what's happening nearby, Outdoorfun makes it easy to browse, filter, and find events that match your interests.

[Link to live website](https://outdoorfun-e7358f3cd44a.herokuapp.com/)

[:arrow_up:](#top)
# UX (User Experience)
The design and functionality of this website focus on providing a clear and intuitive experience for users looking to explore events. The UX principles are tailored to ensure simplicity, accessibility, and user satisfaction:

1. Target Audience
- Outdoor enthusiasts interested in hiking and mud run events.
- Individuals seeking a better overview of upcoming outdoor activities.
- Users who value a simple and clutter-free platform for event discovery.
2. User Goals
- Easily find events based on location, date, or type.
- Access detailed information about event organizers and their activities.
- Navigate the site without distractions or unnecessary complexity.

[:arrow_up:](#top)
# Design
## Color Choice
The design aims to evoke the natural and outdoor elements associated with hiking and mud runs:

![Screenshot 2025-01-24 215739](https://github.com/user-attachments/assets/0dc90274-1e77-46db-a54d-446ae884abf0)

- **Footer in green:** Represents grass at meeting points during events.
- **Main content in grayish brown:** Symbolizes the dust and mud encountered in outdoor adventures.
- **Header in blue:** Represents the sky, invoking a sense of openness and possibility.
- **Brand text in white:** Reflects the white clouds seen on a sunny day.

For text, buttons and links I used the **Grey Friends** color palette suggested by [ColorSpace](https://mycolor.space/?hex=%23D8D4D1&sub=1)

![Screenshot 2025-01-24 203008](https://github.com/user-attachments/assets/2457f25e-b7f9-42c1-a321-728435e9014f)

[:arrow_up:](#top)
## Wireframes
<details>

<summary>Home</summary>

![Home_view](https://github.com/user-attachments/assets/c3a86b01-ff64-4f46-822c-964d3c551815)

</details>

<details>

<summary>Organiser Details</summary>

![organiser_detail](https://github.com/user-attachments/assets/576f90bd-b1c8-4c0d-b2b7-8f8fbb69bddd)

</details>

<details>

<summary>FAQs</summary>

![faq_view](https://github.com/user-attachments/assets/7f76e9ae-830f-4747-8262-23912b1b2445)

</details>

<details>

<summary>Forum</summary>

![forum_view](https://github.com/user-attachments/assets/7019375a-201b-464b-b1c5-148b2e975ffd)

</details>

[:arrow_up:](#top)
# Features
## Existing Features

#### Navigation
- Navbar with nav links and a motivational brand text
- Different links visible for authenticated and unauthenticated users
- Collapsible burger menu with drop-down on small to medium screens

![Screenshot 2025-01-27 182754](https://github.com/user-attachments/assets/fa79a086-4d41-4600-a7e7-14fd9af4a423)
![Screenshot 2025-01-26 164446](https://github.com/user-attachments/assets/cc11811b-6a3b-43f7-87ec-a14517e72605)
![Screenshot 2025-01-26 173645](https://github.com/user-attachments/assets/e47310d3-5add-4666-b1d6-9fed090306ee)

[:arrow_up:](#top)
#### Logged in status
- If a user is logged in, this is displayed in the header together with the user name
- I have avoided pop-up messages as most users I have spoken to find them annoying or even distracting

#### Events List
- Paginated list view of all upcoming events in Europe, sorted by date
- Each card shows the organiser, date, town, country and event type
- Organiser Name serves as link to a detailed view of the organiser

![Screenshot 2025-01-26 173821](https://github.com/user-attachments/assets/c265c4f1-4f8e-4fbc-a6ff-ae851c428638)

#### Search bar
- Users can search the events list by city, country organiser and other criteria

[:arrow_up:](#top)
#### Organiser detailed view
- Organiser header shows name and logo, if available
- General Information about the organiser
- List of all events by selected organiser

![Screenshot 2025-01-26 174256](https://github.com/user-attachments/assets/1554aac4-1eae-4e5e-ac7a-0d41b7f7db21)

[:arrow_up:](#top)
#### FAQ
- Answers frequently asked questions
- Explains the purpose of the site for first-time users
- Explains the benefits of registering an account for first-time users

![Screenshot 2025-01-26 174605](https://github.com/user-attachments/assets/3ffc7656-9980-4253-bf44-2603a95b2d23)

[:arrow_up:](#top)
#### Contact Form
- Gives users the option of contacting the site administrator

![Screenshot 2025-01-26 174927](https://github.com/user-attachments/assets/8149ac11-7349-47c4-a721-d482c6a01adc)

[:arrow_up:](#top)
#### Register
- Allows user to create an account
- Fields include Username, Email (optional), Password and Password confirmation

![Screenshot 2025-01-26 175152](https://github.com/user-attachments/assets/6c8a0046-557a-40cb-b75e-39a369427277)

[:arrow_up:](#top)
#### Login
- Login form asking for username and password
- Includes a "Remember Me" optin box

![Screenshot 2025-01-26 175246](https://github.com/user-attachments/assets/50473852-de59-41ec-9077-2cb945ebad5c)

[:arrow_up:](#top)
#### Logout
- The user is asked to confirm the logout on a separate page

![Screenshot 2025-01-26 175413](https://github.com/user-attachments/assets/8dcb0f6b-c3ed-45a5-9581-79eeb8420a41)

[:arrow_up:](#top)
### Forum
A forum has been added to the website, allowing users to perform full CRUD (Create, Read, Update, Delete) operations. Users can create posts, comment on them, edit their own content, and delete posts or comments, showcasing the implementation of full CRUD functionality.

#### Post List
- A list of all previous forum entries with the name of the author and date of creation
- A button to create a new post is shown at the very top

![Screenshot 2025-01-26 180753](https://github.com/user-attachments/assets/ea27066e-03a3-4625-b65b-fda168da3b3b)

[:arrow_up:](#top)
#### Detailed Post View
- Shows the post and further editing options
- If user is author of the post, options to edit or delete the post are shown
- If logged in user is not author of the post, only option shown is 'Back to List'
- User can add a comment

![Screenshot 2025-01-26 181116](https://github.com/user-attachments/assets/513fd036-4da8-4ded-b9c6-1ffcb3391f9c)
![Screenshot 2025-01-26 181302](https://github.com/user-attachments/assets/c2ed9058-6f5d-4a68-8bc8-3765915aa57b)

[:arrow_up:](#top)
#### Create Post
- Form to create a post
- Both title and content have to be filled out

![Screenshot 2025-01-26 181415](https://github.com/user-attachments/assets/c2a509aa-8274-47f6-a1c8-15bfeebff4d0)

[:arrow_up:](#top)
#### Edit Post
- Fields are prefilled with original entry
- User can confirm edit or cancel
- After confirming the change, the user is taken back to their updated entry

[:arrow_up:](#top)
#### Delete Post
- User has to confirm deletion twice
- When deleting a post, all comments related to the post will be deleted, too

![Screenshot 2025-01-26 181816](https://github.com/user-attachments/assets/9db59d35-5b08-48de-8e35-76c49ad48c67)
![Screenshot 2025-01-26 181859](https://github.com/user-attachments/assets/c3a73dee-79b4-4308-aa39-92b7179e723c)

#### Add comment
- Logged in users can comment on Posts

![Screenshot 2025-01-27 100451](https://github.com/user-attachments/assets/cd3c6531-1174-4ffd-a385-5be6a5e0171c)
![Screenshot 2025-01-27 100507](https://github.com/user-attachments/assets/6d71ee2a-4023-4d91-bf19-357f255735f7)

[:arrow_up:](#top)
#### Edit and delete comment
- Only the user who wrote the comment, can edit or delete it
- Unlike posts, comments do not have to be confirmed twice when they are deleted, but once

![Screenshot 2025-01-27 100749](https://github.com/user-attachments/assets/61f552b9-d6b1-4baf-a317-cd16f06941ca)
![Screenshot 2025-01-27 101007](https://github.com/user-attachments/assets/ef599f59-bc08-4674-b0b9-abfb8abb1d7e)

[:arrow_up:](#top)
### Footer
- The footer includes icons for popular social media platforms.
- Links open in a separate tab

![Screenshot 2025-01-27 101450](https://github.com/user-attachments/assets/7df83b01-281c-48b1-a47b-231068cb57e7)

[:arrow_up:](#top)
## Possible Future Features
1. Links to all organisers
   - As this project is for educational purposes, I have refrained from including too many links to external websites. However, for the best user experience, it is appropriate to link to each organiser.
2. Event Details
   - The enthusiastic athlete can choose their distance at almost every event. For mud runs, the number of obstacles changes in addition to the distance. However, due to time constraints, I have decided to postpone these details until later.
3. Data input via the front end
   - With Django, it is possible to provide an input form via the front end, which can be used by trusted users or the organisers themselves to add events to the list, for example. This can be regulated via permissions.
4. Automatic deletion of past events
   - To keep the overview clean, you could set that events are automatically deleted if they are in the past.

[:arrow_up:](#top)
# Testing
## Validator Testing
### HTML [W3C validator](https://validator.w3.org/)
#### Home

![Screenshot 2025-01-26 111337](https://github.com/user-attachments/assets/c0cb64c7-5946-4d52-9906-04d251127552)

#### Organiser Detail View

![Screenshot 2025-01-26 111401](https://github.com/user-attachments/assets/c3529016-ad6f-4d19-bfd1-5cfb1d1aee2a)

#### FAQ

![Screenshot 2025-01-26 115738](https://github.com/user-attachments/assets/0583d3e2-7f95-43e0-bbc9-677d0ddfb89a)

#### Login

![Screenshot 2025-01-26 113004](https://github.com/user-attachments/assets/5c640c35-d63f-48fd-8c4c-bcb3ef204583)

#### Logout

![Screenshot 2025-01-26 112609](https://github.com/user-attachments/assets/e693418e-4b33-45aa-904e-7a93f863418f)

#### Forum

![Screenshot 2025-01-26 112118](https://github.com/user-attachments/assets/eace1974-0e66-4cb4-abdd-e0718ac6e4cc)

#### Forum Add Post

![Screenshot 2025-01-26 112140](https://github.com/user-attachments/assets/a9419100-6be5-4ec0-a57a-24083ce7667c)

#### Forum Post Detail

![Screenshot 2025-01-26 112238](https://github.com/user-attachments/assets/71a89491-6c6b-427c-ba65-2d1ad98a604e)

#### Forum Edit Post

![Screenshot 2025-01-26 130450](https://github.com/user-attachments/assets/dc9d3484-8743-43a7-8985-64dd156b54cf)

#### Forum Delete Post

![Screenshot 2025-01-26 130529](https://github.com/user-attachments/assets/18d472ca-62c3-4ec2-ad54-5873ae32ba4c)

#### Forum Add Comment

![Screenshot 2025-01-26 112349](https://github.com/user-attachments/assets/2bfd11a9-6154-410b-a0b0-942e97ced509)

#### Forum Edit Comment

![Screenshot 2025-01-26 130228](https://github.com/user-attachments/assets/89d3a3f2-2fc8-47c7-a99e-d0c7118141ed)

#### Forum Delete Comment

![Screenshot 2025-01-26 130309](https://github.com/user-attachments/assets/ae74721e-418a-480b-87e8-8e48db1fa603)

[:arrow_up:](#top)
### CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)

![Screenshot 2025-01-24 215819](https://github.com/user-attachments/assets/ce9949bc-1d54-4437-b182-c9d8de9750a0)

### Python [CI Python Linter](https://pep8ci.herokuapp.com/)
All Python code written by myself was checked via CI Python Linter. Errors coming up were line too long, trailing whitespace or missing newline at the end of file. All of such errors were corrected right away.

[:arrow_up:](#top)
### Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)
#### Desktop results

![Screenshot 2025-01-27 170046](https://github.com/user-attachments/assets/41933f42-999d-484c-b301-77860282fad3)

#### Mobile results

![Screenshot 2025-01-27 170127](https://github.com/user-attachments/assets/0abf0892-f465-4278-b72c-54c85abc068b)

[:arrow_up:](#top)
### Responsiveness
This page was created for larger screens. Thanks to the use of Bootstrap, the site is responsive. However, the organisers' logos had to be scaled down for small screens such as smartphones in order to retain the layout. This would have made the logo unrecognisable. On the other hand, the logo would have taken up too much space in its original size and distracted from the actual content. That's why I decided to do without the images in smartphone size and leave it at the Bootstrap settings with regard to the screen adjustments.

## Manual Testing
### Navigation
All navigation links can be found in navbar or on small to medium screens in the burger drop-down menu.

| Feature | Action | Expected Result |
| --- | --- | --- |
| Brand text | While not on homepage, click Brand text | User is redirected to homepage |
| Browse all | While not on homepage, click Browse all | User is redirected to homepage |
| FAQ | Click FAQ | User is directed to FAQ |
| Register | While not authenticated, click Register | User is directed to Sign up form |
| Login | While not authenticated, cick Login | User is directed to Login form |
| Logout | While authenticated, click Logout | User is directed to Lougout form |
| Forum | While authenticated, click Forum | User is directed to Forum Post List |

[:arrow_up:](#top)
### CRUD
The full CRUD functionality is only available for authenticated users in the forum.
#### Create
Write and submit a post to the forum or comment on a post (authenticated users only)
| Feature | Action | Expected Result |
| --- | --- | --- |
| Title field | Fill out title field (only available for posts) | The written text is displayed |
| Content field | Fill out content field | The written text is displayed |
| Submit | After completing your post, click submit | The user is taken to the post they have just written |
| Incomplete form | Leave one field empty and click submit | User remains on "Create" page and is prompted to complete missing fields |

[:arrow_up:](#top)
#### Read
Read submitted posts and comments.
| Feature | Action | Expected Result |
| --- | --- | --- |
| Post list | Scroll through all posts | User can see all posts |
| Post detail | Click on any post | User is directed to post detail view, where user could add a comment |
#### Update
Option to edit an entry or a comment. Only available for the respective author. (authenticated users only)
| Feature | Action | Expected Result |
| --- | --- | --- |
| User match | On post list, click a post submitted by a different user | Detail view does not show delete button, if user is not author |
| Edit-Btn | From post detail view, click edit button | Renders edit form with title (if post) and content field pre-populated by original post/comment |
| Update | Update text, then below text field, click Update | User is taken back to post detail view, showing updated post/comment |
| Cancel | Below form, click Cancel for post / Back to Post for comment | User is taken back to post detail view |

[:arrow_up:](#top)
#### Delete
Option to delete posts or comments. Only available for the respective author. (authenticated users only)
| Feature | Action | Expected Result |
| --- | --- | --- |
| User match | On post list, click a post submitted by a different user | Detail view does not show delete button, if user is not author |
| Delete-Btn | From post detail view, click Delete. Button is only visible after Login. | User is directed to delete page which prompts user to conform delete action. For posts, an additional pop-up prompts confirmation |
| Confirm Delete Post | On delete page, click Delete Post | User is taken back to post list |
| Confirm Delete Comment | On delete page, click Delete Comment | User is taken back to post |
| Cancel | On delete page, click Cancel | User is taken back to post |

[:arrow_up:](#top)
### Register
Account creation for unauthenticated users
| Feature | Action | Expected Result |
| --- | --- | --- |
| Sign Up form | Go to Register via nav link | Renders form input fields Username, Email (optional), Password, Password (confirm) |
| Submit | Fill in form fields, click Sign Up | Form closes itself, user is redirected to homepage and shown as logged in |
| Incomplete form | Leave one or more fields empty, click Sign Up. | User is prompted to fill out missing fields |

### Login
Signing into existing account (authenticated users only)
| Feature | Action | Expected Result |
| --- | --- | --- |
| Login form | Go to login form via link in navbar | Renders form input fields Username, Password, Remember me (checkbox) |
| Submit | Fill in form fields accordingly, click Sign In | User is redirected to homepage, shown as logged in in header |
| Incomplete form | Leave any field empty and click Sign In | User remains on Sign In form and is prompted to fill out missing fields |

[:arrow_up:](#top)
### Logout
Allows user to sign out of account (authenticated users only)
| Feature | Action | Expected Result |
| --- | --- | --- |
| Logout form | When authenticated, click on Logout in nav bar | User is directed to logout page, asking user to confirm logout |
| Sign Out | On Sign Out page, click Sign Out | User is redirected to homepage, navbar changes to unauthenticated user view |

[:arrow_up:](#top)
### Social Links
Links to social media sites located in footer (available to all users)
| Feature | Action | Expected Result |
| --- | --- | --- |
| Link Icons in Footer | Click on any of the social media icons | New tab opens with respective social media site |

# Fixed Bugs
The code worked well until implementing Cloudinary for media storage.
The first error message encountered was: "Organiser name cannot be null."
Since all organisers listed had names, I suspected the issue might be related to the images. To troubleshoot, I added a custom display_image method to the Django admin panel. This method checks for the presence of an image, and by ensuring the image field was correctly handled, the error was resolved.

![Screenshot 2025-01-27 213426](https://github.com/user-attachments/assets/20d8b928-a9a8-40b2-95a7-7dcabdcaf76a)

Next, the default image was no longer shown. I found a quick fix for this in Slack.

![Screenshot 2025-01-27 213539](https://github.com/user-attachments/assets/980284ee-1edc-4adc-935c-dee1e6cf63b9)

[:arrow_up:](#top)
#### Known error
Throughout the code I use Organisator instead of organiser. It wasn't until I spoke to my facilitator Kay at a weekly stand-up session that I realised I had used the German word. As the site is aimed at a predominantly German audience and I was planning to translate the site into German after the course anyway, I decided to leave this mistake. In conversation with Kay, I also realised that native English speakers are still able to understand the basic idea.

