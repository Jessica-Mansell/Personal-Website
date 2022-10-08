# Verison 0.1
## Starting Ideas
- Blog-like
- Bird animation 
- Colors match Resume
	1. light pink: #dba4cb
	2. dark grey: #636363
	3. white
- About Me page
- Portfolio Examples:
	1. Mail App from Django class
	2. Python Adventure Game
	3. BirdLingo from CS50
- Links to:
	1. LinkedIn Profile
	2. GitHub Profile


## Overall idea:
Create a personal website which is also a blog in which I will cover topics I'm interested in as well as catalog my journey into software engineering. 

# Version 0.5 - New Update
## Goals: Turn to a single page responsive website with JavaScript and remove the user registration options so this will be just my own blog. 

## Description: Based on the "Mail" project in the Web Programming Class, I need to reduce the amount of template pages I have by turning the pages into views instead.

## Pages that can be converted to views and possible rework ideas:

### Templates in the blog itself
- Add_Category: Currently a button on the Add Post page will navigate to this page. This can be turned into a view box below the Add Post page instead.
- Add_Comment: This is now a link at the bottom of any article_details page. I would like this to be positioned under or beside the "Like" button and turned into a button which will then pop down with a comment box the user can type in.
- Delete_post: Navigates to a seperate page that says, "Are you sure you want to delete?" Maybe this can just be an alert or a pop down view which prompts the user.

### Templates in the members section
- Edit_Profile_Page: Keep as a drop-down option in the User/Member info dropdown but, also make into a view when on the User Profile page with a button that says "Edit Profile". 
- Edit_Profile: This is actually a Settings page for only the admin so, it can stay in case I decide to allow guest users in the future. This way I can easily shut-off access after guest user posts.
- Change_Password: Can be turned into a view which opens when user clicks change password button on their Edit_Profile/Settings page.
- 

