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

![Screenshot 2025-01-26 164348](https://github.com/user-attachments/assets/4eb7ed16-55d0-4b48-ae97-1c772938db69)
![Screenshot 2025-01-26 164446](https://github.com/user-attachments/assets/cc11811b-6a3b-43f7-87ec-a14517e72605)
![Screenshot 2025-01-26 173645](https://github.com/user-attachments/assets/e47310d3-5add-4666-b1d6-9fed090306ee)

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

[:arrow_up:](#top)
#### Delete Post
- User has to confirm deletion twice

![Screenshot 2025-01-26 181816](https://github.com/user-attachments/assets/9db59d35-5b08-48de-8e35-76c49ad48c67)
![Screenshot 2025-01-26 181859](https://github.com/user-attachments/assets/c3a73dee-79b4-4308-aa39-92b7179e723c)

